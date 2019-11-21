from manimlib.imports import *
class Open(Scene):
    def construct(self):
        eq1=TextMobject("KKT")
        eq1.shift(2*UP)
        eq2=TextMobject("Shubhamastu")
        eq2.shift(2*DOWN)

        self.play(Write(eq1))
        self.play(Write(eq2))

class OpeningQuote(Scene):
    CONFIG = {
        "quote": ["I saw in a dream a table where all the elements fell into place as required.", "Awakening,", "I immediately wrote it down on a piece of paper."],
        "quote_arg_separator": " ",
        "highlighted_quote_terms": {"Awakening,": REP_GREEN,},
        "author": "Dimitri Ivanovich Mendeleev",
        "fade_in_kwargs": {
            "lag_ratio": 0.5,
            "rate_func": linear,
            "run_time": 12,
        },
        "text_size": "\\Large",
        "use_quotation_marks": True,
        "top_buff": 1.0,
        "author_buff": 1.0,
    }


    def construct(self):
        self.quote = self.get_quote()
        self.author = self.get_author(self.quote)

        self.play(FadeIn(self.quote, **self.fade_in_kwargs))
        self.wait(1)
        self.play(Write(self.author, run_time=3))
        self.wait()

    def get_quote(self, max_width=FRAME_WIDTH - 1):
        text_mobject_kwargs = {
            "alignment": "",
            "arg_separator": self.quote_arg_separator,
        }
        if isinstance(self.quote, str):
            if self.use_quotation_marks:
                quote = TextMobject("``%s''" %
                                    self.quote.strip(), **text_mobject_kwargs)
            else:
                quote = TextMobject("%s" %
                                    self.quote.strip(), **text_mobject_kwargs)
        else:
            if self.use_quotation_marks:
                words = [self.text_size + " ``"] + list(self.quote) + ["''"]
            else:
                words = [self.text_size] + list(self.quote)
            quote = TextMobject(*words, **text_mobject_kwargs)
            # TODO, make less hacky
            if self.quote_arg_separator == " ":
                quote[0].shift(0.2 * RIGHT)
                quote[-1].shift(0.2 * LEFT)
        for term, color in self.highlighted_quote_terms.items():
            print(self.highlighted_quote_terms)
            quote.set_color_by_tex(term, color)
        quote.to_edge(UP, buff=self.top_buff)
        if quote.get_width() > max_width:
            quote.set_width(max_width)
        return quote

    def get_author(self, quote):
        author = TextMobject(self.text_size + " --" + self.author)
        author.next_to(quote, DOWN, buff=self.author_buff)
        author.set_color(REP_GREEN)
        return author


