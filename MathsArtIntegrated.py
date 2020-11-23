from manim import *

class Angle(VMobject):
    # Credit to @cigar666
    CONFIG = {
        'radius': 1,
        'color': RED,
        'opacity': 0.4,
        'stroke_width': 5,
        'below_180': True,
    }

    def __init__(self, A, O, B, **kwargs):

        VMobject.__init__(self, **kwargs)
        OA, OB = A-O, B-O
        if self.below_180:
            theta = np.angle(complex(*OA[:2])/complex(*OB[:2])) # angle of OB to OA
        else:
            theta = TAU + np.angle(complex(*OA[:2])/complex(*OB[:2]))
        self.add(Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius,
                     stroke_width=self.stroke_width,color=self.color, arc_center=O))


class Hill(GraphScene):
    def draw_hill_and_axes(self):
        self.axes_color = BLACK
        self.include_tip = True
        self.x_min = -0.25
        self.x_max = 1.1
        self.x_axis_config={"unit_size": 10,"tick_frequency" : 0.05}
        self.y_min = -0.25
        self.y_max = 1.1
        self.y_axis_config={"tick_frequency" : 0.05,"unit_size": 5}
        self.x_axis_visibility = False
        self.y_axis_visibility = False
        self.setup_axes(animate = False)

        self.hill_outline = self.get_graph(double_smooth, x_min = 0, x_max=1.1, color=LIGHT_BROWN,stroke_width=2*DEFAULT_STROKE_WIDTH)
        
        self.play(Write(self.hill_outline))
        self.hill_fill = self.get_area(self.hill_outline,t_min = 0, t_max = 1.1,dx_scaling=0.5, area_color=DARK_BROWN)
        self.play(Write(self.hill_fill))
        
        self.wait(1)
        
        self.axes.set_stroke(opacity=1,color=BLACK)
        self.y_axis_label_mob.set_color(BLACK)
        self.x_axis_label_mob.set_color(BLACK).shift(DOWN+LEFT)
        
        self.play(Write(self.axes))
        self.wait(1)

    def construct(self):
        self.draw_hill_and_axes()

        LandPoint1 = Dot(color=BLACK).move_to(self.input_to_graph_point(0.4,self.hill_outline))
        LandPoint2= Dot(color=BLUE).move_to(self.input_to_graph_point(0.85,self.hill_outline))
        AirPoint = Dot(color = GREEN).move_to(LandPoint1.get_center()[0]*LEFT+LandPoint2.get_center()[1]*UP)

        KnownHeight = BraceBetweenPoints(
            LandPoint1.get_center(),
            [LandPoint1.get_x(),-2.5,0],RIGHT,color = BLACK,buff=0).scale(0.95)
        KHLabel =  Tex(r"Known Height ($H$)",color=BLACK).scale(0.5).rotate(90*DEGREES).next_to(KnownHeight)
        
        
        self.play(Write(VGroup(KnownHeight,KHLabel)))

        self.play(Write(LandPoint1))
        self.play(Write(LandPoint2))
        Point_U_H = Tex(r"Point of unknown height ($h$)",color=BLACK).scale(0.4).next_to(LandPoint2,DOWN,buff=0.1).shift(RIGHT*(1.2))
        self.play(Write(Point_U_H))

        LineP1P2 = Line(LandPoint1,LandPoint2,color=BLACK)
        self.play(Write(LineP1P2))

        LTex = Tex(r"Length ($l$)",color=BLACK).scale(0.75).rotate(LineP1P2.get_angle()).move_to(LineP1P2.get_center()).shift(DR*0.2)
        self.play(Write(LTex))
        
        LineP2A = DashedLine(LandPoint2,AirPoint,color=BLACK)
        self.play(Write(LineP2A))
        
        self.play(Write(AirPoint))

        LineP1A = DashedLine(AirPoint,LandPoint1,color=BLACK)
        self.play(Write(LineP1A))

        LP1_LP2Angle = Angle(
            LandPoint2.get_center(),
            LandPoint1.get_center(),
            LandPoint1.get_center()+(RIGHT),
            color=BLACK, radius=0.5)

        LP2_LP1Angle = Angle(
            AirPoint.get_center(),
            LandPoint2.get_center(),
            LineP1P2.get_center(),
            color=BLACK, radius=0.5)
    
        self.play(Write(LP1_LP2Angle))
        self.play(Write(LP2_LP1Angle))
        P2Theta = MathTex(r"\theta",color=BLACK).scale(0.6).next_to(LP2_LP1Angle,DL).shift(UP*0.32)
        P1Theta = MathTex(r"\theta",color=BLACK).scale(0.6).next_to(LP1_LP2Angle,UR).shift(DOWN*0.3)

        self.play(Write(P1Theta))
        self.play(Write(P2Theta))

        lsintheta = MathTex(r"l sin(\theta)",color=BLACK).rotate(90*DEGREES).scale(0.75).next_to(LineP1A,LEFT)
        self.play(Write(lsintheta[0][1:]))
        self.play(Transform(LTex[0][-2].copy(),lsintheta[0][0]))

        totalheightbrace = BraceBetweenPoints(
            AirPoint.get_center(),
            [LandPoint1.get_x(),-2.5,0],
            LEFT,color = BLACK,buff=0).scale(0.95
            )
        totalheightbracelabel = MathTex(r"H + l sin(\theta)",color = BLACK).rotate(90*DEGREES).next_to(totalheightbrace,LEFT)
        totalheightindicator = VGroup(totalheightbrace,totalheightbracelabel).shift(LEFT)
        self.play(Write(totalheightbrace))
        self.play(Transform(KHLabel[0][-2].copy(),totalheightbracelabel[0][0]))
        self.play(Write(totalheightbracelabel[0][1]))
        self.play(Transform(lsintheta.copy(),totalheightbracelabel[0][2:]))

        conclusion = MathTex(r"\therefore h =  H + l sin(\theta)",color = BLACK)
        conclusion.to_edge(UP)

        self.play(Write(conclusion[0][0]))
        self.play(Transform(Point_U_H[0][-2].copy(),conclusion[0][1]))
        self.play(Write(conclusion[0][2]))
        self.play(Transform(totalheightbracelabel.copy(),conclusion[0][3:]))

class HillWithTemple(GraphScene):
    def draw_hill_and_axes(self):
        self.axes_color = BLACK
        self.include_tip = True
        self.x_min = -0.25
        self.x_max = 1.1
        self.x_axis_config={"unit_size": 10,"tick_frequency" : 0.05}
        self.y_min = -0.25
        self.y_max = 1.1
        self.y_axis_config={"tick_frequency" : 0.05,"unit_size": 5}
        self.x_axis_visibility = False
        self.y_axis_visibility = False
        self.setup_axes(animate = False)

        self.hill_outline = self.get_graph(double_smooth, x_min = 0, x_max=1.1, color=LIGHT_BROWN,stroke_width=2.3*DEFAULT_STROKE_WIDTH)
        
        self.play(Write(self.hill_outline))
        self.hill_fill = self.get_area(self.hill_outline,t_min = 0, t_max = 1.1,dx_scaling=0.5, area_color=DARK_BROWN)
        self.play(Write(self.hill_fill))
        temple = SVGMobject("/Users/aathishs/Python/ManimEnv/manim-projects/assets/Temple.svg",fill_color=LIGHT_GREY,stroke_width=0)
        temple.set_width(1.5, stretch=True)
        temple.set_height(1.5, stretch=True)
        print(self.coords_to_point(1,1))
        temple.move_to(self.coords_to_point(1,1.2)).shift(DOWN*0.2+RIGHT*0.25)
        self.play(Write(temple))
        
        self.wait(1)
        
        self.axes.set_stroke(opacity=1,color=BLACK)
        self.y_axis_label_mob.set_color(BLACK)
        self.x_axis_label_mob.set_color(BLACK).shift(DOWN+LEFT)
        
        self.play(Write(self.axes))
        self.wait(1)

    def construct(self):
        self.draw_hill_and_axes()

        LandPoint1 = Dot(color=BLACK).move_to(self.input_to_graph_point(0.4,self.hill_outline))
        LandPoint2= Dot(color=BLUE).move_to(self.input_to_graph_point(0.85,self.hill_outline))
        AirPoint = Dot(color = GREEN).move_to(LandPoint1.get_center()[0]*LEFT+LandPoint2.get_center()[1]*UP)

        KnownHeight = BraceBetweenPoints(
            LandPoint1.get_center(),
            [LandPoint1.get_x(),-2.5,0],RIGHT,color = BLACK,buff=0).scale(0.95)
        KHLabel =  Tex(r"Known Height ($H$)",color=BLACK).scale(0.5).rotate(90*DEGREES).next_to(KnownHeight)
        
        
        self.play(Write(VGroup(KnownHeight,KHLabel)))

        self.play(Write(LandPoint1))
        self.play(Write(LandPoint2))
        Point_U_H = Tex(r"Point of unknown height ($h$)",color=BLACK).scale(0.4).next_to(LandPoint2,DOWN,buff=0.1).shift(RIGHT*(1.2))
        self.play(Write(Point_U_H))

        LineP1P2 = Line(LandPoint1,LandPoint2,color=BLACK)
        self.play(Write(LineP1P2))

        LTex = Tex(r"Length ($l$)",color=BLACK).scale(0.75).rotate(LineP1P2.get_angle()).move_to(LineP1P2.get_center()).shift(DR*0.2)
        self.play(Write(LTex))
        
        LineP2A = DashedLine(LandPoint2,AirPoint,color=BLACK)
        self.play(Write(LineP2A))
        
        self.play(Write(AirPoint))

        LineP1A = DashedLine(AirPoint,LandPoint1,color=BLACK)
        self.play(Write(LineP1A))

        LP1_LP2Angle = Angle(
            LandPoint2.get_center(),
            LandPoint1.get_center(),
            LandPoint1.get_center()+(RIGHT),
            color=BLACK, radius=0.5)

        LP2_LP1Angle = Angle(
            AirPoint.get_center(),
            LandPoint2.get_center(),
            LineP1P2.get_center(),
            color=BLACK, radius=0.5)
    
        self.play(Write(LP1_LP2Angle))
        self.play(Write(LP2_LP1Angle))
        P2Theta = MathTex(r"\theta",color=BLACK).scale(0.6).next_to(LP2_LP1Angle,DL).shift(UP*0.32)
        P1Theta = MathTex(r"\theta",color=BLACK).scale(0.6).next_to(LP1_LP2Angle,UR).shift(DOWN*0.3)

        self.play(Write(P1Theta))
        self.play(Write(P2Theta))

        lsintheta = MathTex(r"l sin(\theta)",color=BLACK).rotate(90*DEGREES).scale(0.75).next_to(LineP1A,LEFT)
        self.play(Write(lsintheta[0][1:]))
        self.play(Transform(LTex[0][-2].copy(),lsintheta[0][0]))

        totalheightbrace = BraceBetweenPoints(
            AirPoint.get_center(),
            [LandPoint1.get_x(),-2.5,0],
            LEFT,color = BLACK,buff=0).scale(0.95
            )
        totalheightbracelabel = MathTex(r"H + l sin(\theta)",color = BLACK).rotate(90*DEGREES).next_to(totalheightbrace,LEFT)
        totalheightindicator = VGroup(totalheightbrace,totalheightbracelabel).shift(LEFT)
        self.play(Write(totalheightbrace))
        self.play(Transform(KHLabel[0][-2].copy(),totalheightbracelabel[0][0]))
        self.play(Write(totalheightbracelabel[0][1]))
        self.play(Transform(lsintheta.copy(),totalheightbracelabel[0][2:]))

        conclusion = MathTex(r"\therefore h =  H + l sin(\theta)",color = BLACK)
        conclusion.to_edge(UP)

        self.play(Write(conclusion[0][0]))
        self.play(Transform(Point_U_H[0][-2].copy(),conclusion[0][1]))
        self.play(Write(conclusion[0][2]))
        self.play(Transform(totalheightbracelabel.copy(),conclusion[0][3:]))
