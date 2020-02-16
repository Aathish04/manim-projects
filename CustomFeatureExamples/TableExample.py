from manimlib.imports import *
from sanim.anim_tools.tables import *
class Tables(Scene):
    def construct(self):
        
        tabledict={
            TextMobject("TextMobject Input"):[TextMobject("Must"),TextMobject("add"),TextMobject("element"),TextMobject("retrieval.")],
            TexMobject("TexMobject Input"):[TexMobject(r"e^{\iota\pi}+1 = 0"),TexMobject(r"Tex: \alpha\theta\epsilon")],
            Text("Text input",font="Lucida Grande"):[Text("Text",font="Alys Script Bold"),Text("is",font="serif"),Text("Supported",font="serif")],
            "Raw String Input":["Defaults","to","TextMobject."]
        }

        table=Table(tabledict=tabledict,line_color=GRAY,raw_string_color=BLUE)

        table.move_to((0,0,0))
        table.scale(0.5)
        self.play(Write(table),run_time=2)

        table.add_record(TextMobject("Text").scale(0.5),1)
        self.wait(1)
