from manimlib.imports import *
from sanim.anim_tools.tables import *
class Tables(Scene):
    def construct(self):
        
        tabledict={
            TextMobject("TextMobject Input"):[TextMobject("Must"),TextMobject("add"),TextMobject("element"),TextMobject("retrieval.")],
            TexMobject("TexMobject Input"):[TexMobject(r"e^{\iota\pi}+1 = 0"),TexMobject(r"Tex: \alpha\theta\epsilon")],
            Text("Text input",font="Lucida Grande"):[Text("Text",font="Alys Script Bold"),Text("is"),Text("Supported")],
            "Raw String Input":["Defaults","to","TextMobject."]

        }

        table=Table.get_table(tabledict,line_color=BLUE,raw_string_color=GREY)
        table.move_to((0,0,0))
        self.play(Write(table.scale(0.5)),run_time=2)

        self.wait(1)
