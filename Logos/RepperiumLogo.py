from manim import *

REP_GREEN = "#00C099"


class LogoAdd(Scene):

    textcolor = BLACK

    background = Rectangle(
        height=5, width=5, fill_color=REP_GREEN, stroke_color=REP_GREEN, fill_opacity=1
    ).move_to(ORIGIN)

    Rp = Text("Rp", font="Futura", size=3.6, color=textcolor)

    ChargeConst = (
        MathTex("q_e", stroke_width=1, color=textcolor)
        .scale(1.75)
        .next_to(Rp, UP * 1.1)
    )

    AvogadrosNum = (
        MathTex("N_A", stroke_width=1, color=textcolor).scale(1.75).next_to(Rp, DOWN)
    )

    logo = VGroup(background, Rp, ChargeConst, AvogadrosNum).scale(0.5)

    def construct(self):
        self.play(ShowCreation(self.background, run_time=1))
        self.play(Write(self.Rp, run_time=1))
        self.play(Write(self.ChargeConst, run_time=0.5))
        self.play(Write(self.AvogadrosNum, run_time=0.25))
        self.wait(0.5)


class LogoRemove(LogoAdd):
    def construct(self):
        self.add(self.background)
        self.add(self.Rp)
        self.add(self.ChargeConst)
        self.add(self.AvogadrosNum)

        self.play(Uncreate(self.AvogadrosNum, run_time=0.5))
        self.play(Uncreate(self.ChargeConst, run_time=0.5))
        self.play(Uncreate(self.Rp, run_time=1))
        self.play(Uncreate(self.background, run_time=1))
        self.wait(0.5)


class LogoBoth(LogoAdd):
    def construct(self):
        LogoAdd.construct(self)
        LogoRemove.construct(self)
