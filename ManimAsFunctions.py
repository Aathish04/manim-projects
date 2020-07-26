from manim import *

class ManimAsFunctions(GraphScene):
    def MCurve(self):
        LeftMCurve = ParametricFunction(
            lambda t : RIGHT*(0.9*np.cos(t)-1.8) + UP*(3*np.sin(t)+3),
            t_min=-PI/2,t_max=np.arcsin(-0.5/3))

        MiddleMCurve = ParametricFunction(
            lambda t : RIGHT*(np.cos(t)) + UP*(np.sqrt(1.5)*np.sin(t)+3),
            t_min=-PI + np.arccos(np.sqrt(1.25/1.5)),
            t_max=-np.arccos(np.sqrt(1.25/1.5)))

        RightMCurve = ParametricFunction(
            lambda t : RIGHT*(0.9*np.cos(t)+1.8) + UP*(3*np.sin(t)+3),
            t_min=np.arcsin(-2.125/3),t_max=-PI+np.arcsin(0.5/3))
        return VGroup(LeftMCurve,MiddleMCurve,RightMCurve).set_color(GREEN)

    def aCurve(self):
        aCircle=ParametricFunction(
            lambda t :RIGHT*(0.875*np.cos(t)+3.325)+UP*(0.875*np.sin(t)+0.875),
            t_min=-PI,t_max=PI)
        aTail= ParametricFunction(
            lambda t: RIGHT*(0.9*np.cos(t)+4.86) + UP*(3*np.sin(t)+3),
            t_min=-PI+np.arcsin(1.3/3),
            t_max=-PI/2+np.arcsin(1.3/3))
        return VGroup(aCircle,aTail).set_color(BLUE)

    def nCurve(self):
        nline=ParametricFunction(
            lambda t: UP*t + RIGHT*(np.cos(-np.pi/2+np.arcsin(1.3/3))+4.86),
            t_min=0,
            t_max=1.75
        ).set_color(ORANGE)
        nCurve =  ParametricFunction(
            lambda t: RIGHT*(0.75*np.cos(t)+(np.arcsin(1.3/3)+4.86)+0.75) + UP*(1.8*np.sin(t)),
            t_min=0,
            t_max=PI
        ).set_color(ORANGE)
        return VGroup(nline,nCurve)

    def iLine(self):
        iline = ParametricFunction(
            lambda t: UP*t + RIGHT*(np.arcsin(1.3/3)+4.86+1.8),
            t_min=0,t_max=1.75
        ).set_color(RED)
        idot = Dot().move_to(iline).shift(UP*1.755).set_color(RED)
        return VGroup(iline,idot)

    def mCurve(self):
        mcurve = ParametricFunction(
            lambda t: RIGHT*t + UP*(1.75*(np.cos(2*t)**2)),
            t_min=7.10818814,t_max=7.10818814+PI).set_color(GREEN)
        return mcurve

    def construct(self):
        ManimCurves = VDict()
        ManimCurves["MCurve"]=self.MCurve()
        ManimCurves["aCurve"]=self.aCurve()
        ManimCurves["nCurve"]=self.nCurve()
        ManimCurves["iLine"]=self.iLine()
        ManimCurves["mCurve"]=self.mCurve()
        ManimCurves.set_x(0).set_stroke(width=10)

        x_axis = NumberLine(
            x_min=0,
            x_max=ManimCurves.get_width(),
            unit_size=1,
            numbers_with_elongated_ticks=range(0,13,3),
            color=WHITE,
            include_tip=True,
            add_start=True,
            add_end=True,
        ).move_to(ORIGIN)

        y_axis = NumberLine(
            x_min=0,
            x_max=ManimCurves.get_height(),
            unit_size=1,
            leftmost_tick=self.y_bottom_tick,
            numbers_with_elongated_ticks=range(0,4),
            color=WHITE,
            include_tip=True,
            add_start=True,
            add_end=True
        )
        y_axis.shift(ManimCurves.get_corner(LEFT+DOWN) - y_axis.number_to_point(0))
        y_axis.rotate(PI / 2, about_point=y_axis.number_to_point(0))

        axes= VGroup(x_axis,y_axis)
        axesandgraph = VGroup(axes,ManimCurves).shift(DOWN)
        self.play(Write(axes))
        for m in ManimCurves:
            self.play(Write(m),run_time=0.5)
