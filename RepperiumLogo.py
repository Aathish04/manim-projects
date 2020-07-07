from manim import *
REP_GREEN="#00C099"
class LogoAdd(Scene):
    def construct(self):

        background=Rectangle(height=5, width=5, fill_color=REP_GREEN,fill_opacity=1,stroke_color=REP_GREEN)

        Re=Text("Rp",font="Futura",size=3.6)

        FaradaysConst=Text("F",font="Alys Script Bold", size=1.1,stroke_width=0)
        FaradaysConst.move_to((0,2,0))

        AvogadrosNumN=Text("N",font="Snell Roundhand", size=0.92, stroke_width=1)
        AvogadrosNumN.move_to((-0.5,-1.8,0))

        AvogadrosNumA=Text("A",font="Snell Roundhand",size=0.7,stroke_width=1)
        AvogadrosNumA.move_to((-0.25,-2.2,0))

        AvogadrosNum=VGroup(AvogadrosNumN,AvogadrosNumA)

        logo=VGroup(background,Re,FaradaysConst,AvogadrosNum)
        logo.scale(0.5)

        self.play(ShowCreation(background,run_time = 1))
        self.play(Write(Re,run_time = 1))
        self.play(Write(FaradaysConst,run_time = 0.5))
        self.play(Write(AvogadrosNumN,run_time = 0.25))
        self.play(Write(AvogadrosNumA,run_time = 0.25))
        self.wait(0.5)

class LogoRemove(Scene):
    def construct(self):

        background=Rectangle(height=5, width=5, fill_color=REP_GREEN,fill_opacity=1,stroke_color=REP_GREEN)

        Re=Text("Rp",font="Futura",size=3.6)

        FaradaysConst=Text("F",font="Alys Script Bold", size=1.1,stroke_width=0)
        FaradaysConst.move_to((0,2,0))

        AvogadrosNumN=Text("N",font="Snell Roundhand", size=0.92,stroke_width=1)
        AvogadrosNumN.move_to((-0.5,-1.8,0))

        AvogadrosNumA=Text("A",font="Snell Roundhand",size=0.7,stroke_width=1)
        AvogadrosNumA.move_to((-0.25,-2.2,0))

        AvogadrosNum=VGroup(AvogadrosNumN,AvogadrosNumA)

        logo=VGroup(background,Re,FaradaysConst,AvogadrosNum)
        logo.scale(0.5)

        self.add(background)
        self.add(Re)
        self.add(FaradaysConst)
        self.add(AvogadrosNumN)
        self.add(AvogadrosNumA)

        self.play(Uncreate(AvogadrosNumA,run_time = 0.25))
        self.play(Uncreate(AvogadrosNumN,run_time = 0.25))
        self.play(Uncreate(FaradaysConst,run_time = 0.5))
        self.play(Uncreate(Re,run_time = 1))
        self.play(Uncreate(background,run_time = 1))
        self.wait(0.5)

class LogoBoth(Scene):
    def construct(self):

        background=Rectangle(height=5, width=5, fill_color=REP_GREEN,fill_opacity=1,stroke_color=REP_GREEN)

        Re=Text("Rp",font="Futura",size=3.6)

        FaradaysConst=Text("F",font="Alys Script Bold", size=1.1,stroke_width=0)
        FaradaysConst.move_to((0,2,0))

        AvogadrosNumN=Text("N",font="Snell Roundhand", size=0.92, stroke_width=1)
        AvogadrosNumN.move_to((-0.5,-1.8,0))

        AvogadrosNumA=Text("A",font="Snell Roundhand",size=0.7,stroke_width=1)
        AvogadrosNumA.move_to((-0.25,-2.2,0))

        AvogadrosNum=VGroup(AvogadrosNumN,AvogadrosNumA)

        logo=VGroup(background,Re,FaradaysConst,AvogadrosNum)
        logo.scale(0.5)

        self.play(ShowCreation(background,run_time = 1))
        self.play(Write(Re,run_time = 1))
        self.play(Write(FaradaysConst,run_time = 0.5))
        self.play(Write(AvogadrosNumN,run_time = 0.25))
        self.play(Write(AvogadrosNumA,run_time = 0.25))
        self.wait(0.5)

        self.play(Uncreate(AvogadrosNumA,run_time = 0.25))
        self.play(Uncreate(AvogadrosNumN,run_time = 0.25))
        self.play(Uncreate(FaradaysConst,run_time = 0.5))
        self.play(Uncreate(Re,run_time = 0.5))
        self.play(Uncreate(background,run_time = 0.5))
        self.wait(0.5)

