from manimlib.imports import *
class Open(Scene):
    def construct(self):
        eq1=TextMobject("KKT")
        eq1.shift(2*UP)
        eq2=TextMobject("Shubhamastu")
        eq2.shift(2*DOWN)

        self.play(Write(eq1))
        self.play(Write(eq2))
