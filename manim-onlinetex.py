import requests
import urllib
import base64

from manim import config, logger
from manim.utils.tex_file_writing import generate_tex_file


def tex_to_svg_file_online(
    expression, environment=None, tex_template=None, host="latex4technics"
):
    """Takes a tex expression and returns the path to the svg file of the compiled tex
    after compiling it via an online Rendering service.

    Parameters
    ----------
    expression : :class:`str`
        String containing the TeX expression to be rendered, e.g. ``\\sqrt{2}`` or ``foo``
    environment : Optional[:class:`str`], optional
        The string containing the environment in which the expression should be typeset, e.g. ``align*``
    tex_template : Optional[:class:`~.TexTemplate`], optional
        Template class used to typesetting. If not set, use default template set via `config["tex_template"]`
    host : Optional[:class:`str`], optional
        Service through which the TeX should be rendered. Can be any one of {'latex4technics', 'quicklatex'}

    Returns
    -------
    :class:`str`
        Path to generated SVG file.
    """
    if tex_template is None:
        tex_template = config["tex_template"]
    tex_file = generate_tex_file(expression, environment, tex_template)

    hosturl = (
        "https://www.quicklatex.com/latex3.f"
        if host == "quicklatex"
        else "https://www.latex4technics.com/compileLatex"
    )

    if host == "latex4technics":
        params = {
            "content": tex_template.get_texcode_for_expression_in_env(
                expression, environment
            ),
            "compile_mode": "full",
            "crop": True,
            "format": "svg",
            "resolution": 100,
        }
        payload = params
    elif host == "quicklatex":
        begin, end = tex_template._texcode_for_environment(environment)
        params = {
            "formula": f"{begin}\n{expression}\n{end}",
            "preamble": tex_template.preamble,
            # "mode": 0,
            "out": 2,
        }
        payload = urllib.parse.urlencode(
            params, quote_via=urllib.parse.quote
        )  # This is so requests doesn't use plus signs instead of spaces like it usually does.
    logger.debug(f'Rendering "{expression}" via {host}...')
    response = requests.post(hosturl, data=payload)

    if host == "latex4technics":
        responsedict = response.json()
        if responsedict["error"] == True:
            if responsedict["content"].find("! LaTeX Error") > -1:
                relevant_error_start = responsedict["content"].find("! LaTeX Error")
                error = responsedict["content"][relevant_error_start:]
            else:
                error = responsedict["content"]
            logger.error(error)
        else:
            svgtext = base64.b64decode(responsedict["content"]).decode("utf-8")

    elif host == "quicklatex":
        if not response.text.startswith("0"):
            error = "\n".join(
                response.text.split("\r\n")[2:]
            )  # First 2 lines are API error code and error image URL resp.
            logger.error(error)
        else:
            svgurl = response.text.split("\n")[-1].split(" ")[0].replace("png", "svg")
            svgtext = requests.get(svgurl, headers={"Accept-Encoding": "identity"}).text
    svgfilepath = tex_file.replace("tex", "svg")
    with open(svgfilepath, "w") as svgfile:
        svgfile.write(svgtext)
    logger.debug(f'SVG of "{expression}" written to {svgfilepath}')
    return svgfilepath


if __name__ == "__main__":
    expression = "This is TEX."
    environment = "center"
    print(tex_to_svg_file_online(expression, environment, host="quicklatex"))


