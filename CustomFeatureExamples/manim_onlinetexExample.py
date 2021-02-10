from manim import *
from manim_onlinetex import * # Always import manim_onlinetex AFTER you import everything from manim.

class Test(Scene):
    def construct(self):
        t = Tex("Hello World!")
        self.play(Write(t))
        self.wait(1)