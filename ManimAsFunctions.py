from manim import *

class ManimAsFunctions(GraphScene):
    def MCurve(self):
        LeftMCurve = ParametricFunction(
            lambda t : RIGHT*(0.9*np.cos(t)-1.8) + UP*(3*np.sin(t)+3),
            t_min=-PI/2,t_max=np.arcsin(-0.5/3)).set_color(GREEN)

        MiddleMCurve = ParametricFunction(
            lambda t : RIGHT*(np.cos(t)) + UP*(np.sqrt(1.5)*np.sin(t)+3),
            t_min=-PI + np.arccos(np.sqrt(1.25/1.5)),
            t_max=-np.arccos(np.sqrt(1.25/1.5))).set_color(GREEN)

        RightMCurve = ParametricFunction(
            lambda t : RIGHT*(0.9*np.cos(t)+1.8) + UP*(3*np.sin(t)+3),
            t_min=np.arcsin(-2.125/3),t_max=-PI+np.arcsin(0.5/3)).set_color(GRAY)
        return VGroup(LeftMCurve,MiddleMCurve,RightMCurve)

    def aCurve(self):
        aCircle=ParametricFunction(
            lambda t :RIGHT*(0.875*np.cos(t)+3.325)+UP*(0.875*np.sin(t)+0.875),
            t_min=-PI,t_max=PI).set_color(BLUE)
        aTail= ParametricFunction(
            lambda t: RIGHT*(0.9*np.cos(t)+4.86) + UP*(3*np.sin(t)+3),
            t_min=-PI+np.arcsin(1.3/3),
            t_max=-PI/2+np.arcsin(1.3/3)).set_color(GREEN)
        return VGroup(aCircle,aTail)

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
        ).set_color(GREEN)
        return VGroup(nline,nCurve)

    def iLine(self):
        iline = ParametricFunction(
            lambda t: UP*t + RIGHT*(np.arcsin(1.3/3)+4.86+1.8),
            t_min=0,t_max=1.75
        ).set_color(BLUE)
        idot = Dot().move_to(iline).shift(UP*1.755).set_color(RED)
        return VGroup(iline,idot)

    def mCurve(self):
        mcurve = ParametricFunction(
            lambda t: RIGHT*t + UP*(1.75*(np.cos(2*t)**2)),
            t_min=7.10818814,t_max=7.10818814+PI).set_color(GREEN)
        return mcurve

    def construct(self):
        ManimCurves = VGroup(
            self.MCurve(),
            self.aCurve(),
            self.nCurve(),
            self.iLine(),
            self.mCurve()
            )
        ManimCurves.set_x(0)
        self.play(Write(ManimCurves))