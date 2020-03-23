#phi changes camera "along z axis"
#theta rotates camera?
import random
from manimlib.imports import *
from sanim.anim_tools.tables import *
class Tools():
    def spherical_to_cartesian(pol_ang,azim_ang,radius=1): #This function converts given spherical coordinates (theta, phi and radius) to cartesian coordinates.
        return np.array((radius*np.sin(pol_ang) * np.cos(azim_ang),
                            radius*np.sin(pol_ang) * np.sin(azim_ang),
                            radius*np.cos(pol_ang))
                            )
    def get_surface(surface,shade_color,stroke_width=0.5,opacity=0.3):
        result = surface.copy()
        result.set_fill(shade_color, opacity=opacity)
        result.set_stroke(WHITE, width=stroke_width, opacity=opacity)
        return result
    
    def flatten(inlist):
        outlist=[]
        for element in inlist:
            for sub_element in element:
                outlist.append(sub_element)
        return outlist
    
    def wait_while_updating(duration=1):
        return Animation(Mobject(), run_time=duration)

class StoichiometricLaws(ZoomedScene):
    def IntroduceLaws(self):
        LawsOf=Text("The Laws of",font="Futura",stroke_width=0).scale(1)
        Stoichiometry=Text("Stoichiometry",font="Geneva",stroke_width=0).scale(1).next_to(LawsOf,DOWN)
        LawsOfStoichiometry=VGroup(LawsOf,Stoichiometry).move_to(ORIGIN) 
        
        StoichioBrace=Brace(Stoichiometry[0:8],DOWN,color=REP_GREEN)
        MetryBrace=Brace(Stoichiometry[8:13],DOWN,color=BLUE,buff=0)
        
        stoicheionGreek=Text("στοιχεῖον",font="Geneva",stroke_width=0).scale(0.5).next_to(StoichioBrace,DOWN)
        stoicheionEnglish=Text("stoicheion",font="Geneva",stroke_width=0,slant=ITALIC).scale(0.3).next_to(stoicheionGreek,DOWN)
        element=Text("(element)",font="Geneva",stroke_width=0,slant=ITALIC).scale(0.25).next_to(stoicheionEnglish,DOWN)
        
        metronGreek=Text("μέτρον",font="Geneva",stroke_width=0).scale(0.5).next_to(MetryBrace,DOWN)
        metronEnglish=Text("metron",font="Geneva",stroke_width=0,slant=ITALIC).scale(0.3).next_to(metronGreek,DOWN)
        measure=Text("(measure)",font="Geneva",stroke_width=0,slant=ITALIC).scale(0.25).next_to(metronEnglish,DOWN)
        
        Everything=VGroup(LawsOfStoichiometry,StoichioBrace,MetryBrace,stoicheionGreek,stoicheionEnglish,element,metronGreek,metronEnglish,measure).move_to(ORIGIN)
        
        self.play(Write(LawsOfStoichiometry))
        self.wait(1)
        
        self.play(
            Stoichiometry[0:8].set_color,(REP_GREEN),
            Write(StoichioBrace),
            run_time=1
            )

        self.play(Write(stoicheionGreek),run_time=1)
        self.play(Write(stoicheionEnglish),Write(element),run_time=1)
        
        self.play(
            Stoichiometry[8:13].set_color,(BLUE),
            Write(MetryBrace),
            run_time=1
            )
        
        self.play(Write(metronGreek),run_time=1)
        self.play(Write(metronEnglish),Write(measure),run_time=1
            )
        self.wait(2)


        self.play(Uncreate(Everything),run_time=2)
        self.clear()
    
    def ConservationOfMass(self):
        LavoisierPhoto=ImageMobject("/Users/aathishs/AtomThroughAgesImages/Lavoisier.png").scale(2)
        Date=Text("1743-1794",font="Geneva",stroke_width=0,slant=ITALIC).scale(0.5).next_to(LavoisierPhoto,DOWN)
        
        self.play(FadeInFromDown(LavoisierPhoto))
        self.play(Write(Date))
        
        self.wait(7)
        
        LCMTitle=Text("The Law Of Conservation of Mass",font="Futura",stroke_width=0).to_edge(UP).scale(0.5)
        
        self.play(FadeOutAndShiftDown(LavoisierPhoto),ReplacementTransform(Date,LCMTitle))
        self.wait(2)
        
        System=RegularPolygon(n=9,color=GREEN,fill_color=RED,fill_opacity=0.1).scale(2).round_corners()

        self.play(ShowCreation(System))
        
        InParticles=VGroup()
        
        for i in range(0,15):
            particle=Dot(
                color=[GREEN,REP_GREEN,DARK_BLUE,GOLD_A,PINK,LIGHT_PINK,TEAL_A,LIGHT_BROWN,DARK_GREY,PURPLE_A,GREEN_B,BLUE_D,MAROON_E,WHITE,GREY_BROWN][i]
                )
            InParticles.add(particle)
        
        
        class IPUs:
            def IPU0(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[0].move_to(ORIGIN)
                else:
                    InParticles[0].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
            def IPU1(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[1].move_to(ORIGIN)
                else:
                    InParticles[1].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
            def IPU2(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[2].move_to(ORIGIN)
                else:
                    InParticles[2].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
            def IPU3(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[3].move_to(ORIGIN)
                else:
                    InParticles[3].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
            def IPU4(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[4].move_to(ORIGIN)
                else:
                    InParticles[4].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
            def IPU5(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[5].move_to(ORIGIN)
                else:
                    InParticles[5].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
            def IPU6(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[6].move_to(ORIGIN)
                else:
                    InParticles[6].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
            def IPU7(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[7].move_to(ORIGIN)
                else:
                    InParticles[7].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
            def IPU8(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[8].move_to(ORIGIN)
                else:
                    InParticles[8].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
            def IPU9(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[9].move_to(ORIGIN)
                else:
                    InParticles[9].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
            def IPU10(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[10].move_to(ORIGIN)
                else:
                    InParticles[10].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
            def IPU11(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[11].move_to(ORIGIN)
                else:
                    InParticles[11].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
            def IPU12(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[12].move_to(ORIGIN)
                else:
                    InParticles[12].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
            def IPU13(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[13].move_to(ORIGIN)
                else:
                    InParticles[13].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
            def IPU14(obj):
                coord=obj.get_center()
                c_x=coord[0];c_y=coord[1]
                dist_from_origin=np.sqrt((c_x**2)+(c_y**2))
                if dist_from_origin>=1.75:
                    InParticles[14].move_to(ORIGIN)
                else:
                    InParticles[14].shift(
                        random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR])*0.05
                    )
                
        InParticles[0].add_updater(IPUs.IPU0)
        InParticles[1].add_updater(IPUs.IPU1)
        InParticles[2].add_updater(IPUs.IPU2)
        InParticles[3].add_updater(IPUs.IPU3)
        InParticles[4].add_updater(IPUs.IPU4)
        InParticles[5].add_updater(IPUs.IPU5)
        InParticles[6].add_updater(IPUs.IPU6)
        InParticles[7].add_updater(IPUs.IPU7)
        InParticles[8].add_updater(IPUs.IPU8)
        InParticles[9].add_updater(IPUs.IPU9)
        InParticles[10].add_updater(IPUs.IPU10)
        InParticles[11].add_updater(IPUs.IPU11)
        InParticles[12].add_updater(IPUs.IPU12)
        InParticles[13].add_updater(IPUs.IPU13)
        InParticles[14].add_updater(IPUs.IPU14)

        self.add(InParticles)

        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame
        frame.add_updater(lambda m:m.move_to(InParticles[0].get_center()))
        zoomed_display.scale(0.5)
        self.activate_zooming(animate=True)

        Mass=Text("Mass=1 unit",font="Futura",stroke_width=0).scale(0.25).next_to(zoomed_display,DOWN).shift(LEFT)
        Volume=Text("Volume = 1 unit",font="Futura",stroke_width=0).scale(0.25).next_to(zoomed_display,DOWN).shift(RIGHT)

        self.play(Write(Mass),Write(Volume))

        self.play(Tools.wait_while_updating(2))   

        TemperatureMonitor=VGroup(Text("Temperature: 25 °C",font="serif",stroke_width=0)).scale(0.5).to_corner(UP+LEFT)
        self.play(Uncreate(LCMTitle),Write(TemperatureMonitor))
        
        self.play(Tools.wait_while_updating(7))  
        
        FirstLaw=TexMobject("U=Q+W").next_to(System,DOWN)
        self.play(Write(FirstLaw))
        self.play(Tools.wait_while_updating(2))
        self.play(Uncreate(FirstLaw))

        OutParticles=VGroup(
            Dot(color=GREEN),Dot(color=BLUE),Dot(color=RED),
            Dot(color=GRAY),Dot(color=PURPLE_A),Dot(color=DARK_BLUE),
            Dot(color=TEAL_A),Dot(color=BLUE_D),Dot(color=WHITE),
            Dot(color=TEAL_B),Dot(color=DARKER_GREY),Dot(color=GREY_BROWN),
        )

        PathofParticleRIGHT=FunctionGraph(lambda x:np.abs((x-2)*3),x_max=5,x_min=-3).rotate(270*DEGREES, about_point=(2,0,0))
        PathofParticleLEFT=FunctionGraph(lambda x:np.abs((x+2)*3),x_max=5,x_min=-5).rotate(90*DEGREES, about_point=(-2,0,0))
        PathofParticleUP=FunctionGraph(lambda x:np.abs((x)*3),x_max=5,x_min=-3).shift(UP*2)
        PathofParticleDOWN=FunctionGraph(lambda x:-np.abs((x)*3),x_max=5,x_min=-3).shift(DOWN*2)

        self.play(
            LaggedStart(

                MoveAlongPath(OutParticles[0],PathofParticleRIGHT,run_time=5),
                MoveAlongPath(OutParticles[4],PathofParticleRIGHT,run_time=5),
                MoveAlongPath(OutParticles[8],PathofParticleRIGHT,run_time=5),
            ),
            LaggedStart(
                MoveAlongPath(OutParticles[5],PathofParticleLEFT,run_time=5),
                MoveAlongPath(OutParticles[9],PathofParticleLEFT,run_time=5),
                MoveAlongPath(OutParticles[1],PathofParticleLEFT,run_time=5),
            ),
            LaggedStart(
                MoveAlongPath(OutParticles[2],PathofParticleUP,run_time=5),
                MoveAlongPath(OutParticles[6],PathofParticleUP,run_time=5),
                MoveAlongPath(OutParticles[10],PathofParticleUP,run_time=5),
            ),
            LaggedStart(
                MoveAlongPath(OutParticles[3],PathofParticleDOWN,run_time=5),
                MoveAlongPath(OutParticles[7],PathofParticleDOWN,run_time=5),
                MoveAlongPath(OutParticles[11],PathofParticleDOWN,run_time=5),
            )
        )

        self.play(Uncreate(OutParticles),Uncreate(zoomed_display),Uncreate(zoomed_display_frame),Uncreate(frame))
        self.play(Uncreate(InParticles))
        self.play(Uncreate(System),Uncreate(TemperatureMonitor),Uncreate(Mass),Uncreate(Volume))

        self.zoom_activated = False#This stops the 
        self.camera.image_mobjects_from_cameras = []#ImageMobject buffer from being filled. Essentially deactivates zooming. Add a function that does this?
        self.wait(3)

        BeforeSystem=Square(color=GREEN,fill_color=RED,fill_opacity=0.1).scale(1.5).round_corners().shift(LEFT*3)
        
        AfterSystem=Square(color=RED,fill_color=GREEN,fill_opacity=0.1).scale(1.5).round_corners().shift(RIGHT*3)

        Reactants=VGroup(
            Dot(color=BLUE).shift(UP),
            Dot(color=GREEN).shift(DOWN),
            Dot(color=RED).shift(RIGHT),
            Dot(color=WHITE).shift(LEFT),
            Dot(color=LIGHT_GRAY).shift(UL),
            Dot(color=PINK).shift(DL),
            Dot(color=PURPLE_A).shift(UR),
            Dot(color=YELLOW).shift(DR),)
        
        Products=Reactants.copy()
        
        def arrange_in_circle(inputs):
            total_angle=2*PI
            angle_diff_per_particle=total_angle/len(inputs)
            for i in range(len(inputs)):
                particle=inputs[i]
                particle.move_to((3,0,0))
                particle.shift(UP)
                particle.rotate(angle_diff_per_particle*i,about_point=(3,0,0))
        Reactants.move_to(BeforeSystem.get_center())
        
        arrange_in_circle(Products)
        
        Reactants.add_updater(lambda m: m.move_to(BeforeSystem.get_center()))
        Products.add_updater(lambda m: m.move_to(AfterSystem.get_center()))
        
        RSLabel=Text("Reactants",font="Futura",color=GREEN,stroke_width=0).scale(0.5).add_updater(lambda m: m.next_to(BeforeSystem,UP))
        PSLabel=Text("Products",font="Futura",color=RED,stroke_width=0).scale(0.5).add_updater(lambda m: m.next_to(AfterSystem,UP))
        
        BScaleTop=Line(BeforeSystem.get_center()-(2,1.8,0),BeforeSystem.get_center()-(-2,1.8,0))
        AScaleTop=Line(AfterSystem.get_center()-(2,1.8,0),AfterSystem.get_center()-(-2,1.8,0))
        BScaleConnect=Line(BScaleTop.get_center(),BScaleTop.get_center()-(0,1,0))
        AScaleConnect=Line(AScaleTop.get_center(),AScaleTop.get_center()-(0,1,0))
        ABConnect=Line(BScaleConnect.get_end(),AScaleConnect.get_end())
        Fulcrum=Triangle().move_to(ABConnect.get_center()).scale(0.5).shift(DOWN*0.5)
        Scale=VGroup(BScaleTop,AScaleTop,BScaleConnect,AScaleConnect,ABConnect,Fulcrum)
        
        BScaleTop.add_updater(lambda m: m.put_start_and_end_on(BeforeSystem.get_center()-(2,1.8,0),BeforeSystem.get_center()-(-2,1.8,0)))
        AScaleTop.add_updater(lambda m: m.put_start_and_end_on(AfterSystem.get_center()-(2,1.8,0),AfterSystem.get_center()-(-2,1.8,0)))
        AScaleConnect.add_updater(lambda m: m.put_start_and_end_on(AScaleTop.get_center(),AScaleTop.get_center()-(0,1,0)))
        BScaleConnect.add_updater(lambda m: m.put_start_and_end_on(BScaleTop.get_center(),BScaleTop.get_center()-(0,1,0)))
        ABConnect.add_updater(lambda m: m.put_start_and_end_on(BScaleConnect.get_end(),AScaleConnect.get_end()))

        self.play(ShowCreation(BeforeSystem),ShowCreation(AfterSystem))
        self.play(ShowCreation(Reactants),ShowCreation(Products),Write(RSLabel),Write(PSLabel))
        self.play(Write(Scale))
        self.wait(1)
        self.play(BeforeSystem.shift,DOWN,AfterSystem.shift,UP)
        self.wait(0.5)
        self.play(BeforeSystem.shift,UP*2,AfterSystem.shift,DOWN*2)
        self.wait(0.5)
        self.play(BeforeSystem.shift,DOWN,AfterSystem.shift,UP)
        self.wait(1)
        self.play(Uncreate(Scale),FadeOut(Reactants),FadeOut(Products))
        
        Reactants.clear_updaters()
        Products.clear_updaters()
        BScaleTop.clear_updaters()
        AScaleTop.clear_updaters()
        BScaleConnect.clear_updaters()
        AScaleConnect.clear_updaters()
        ABConnect.clear_updaters()

        Reactants=VGroup(
            Dot(color=BLUE).shift(UP),
            Dot(color=GREEN).shift(DOWN),
            Dot(color=RED).shift(RIGHT),
            Dot(color=WHITE).shift(LEFT),
            Dot(color=LIGHT_GRAY).shift(UL),
            Dot(color=PINK).shift(DL),
            Dot(color=PURPLE_A).shift(UR),
            Dot(color=YELLOW).shift(DR),
        )
        Products=Reactants.copy()
        
        def arrange_in_circle(inputs):
            total_angle=2*PI
            angle_diff_per_particle=total_angle/len(inputs)
            for i in range(len(inputs)):
                particle=inputs[i]
                particle.move_to((3,0,0))
                particle.shift(UP)
                particle.rotate(angle_diff_per_particle*i,about_point=(3,0,0))
        Reactants.move_to(BeforeSystem.get_center())
        
        arrange_in_circle(Products)

        ReactionArrow=Arrow(BeforeSystem.get_center()+(1.4,0,0),AfterSystem.get_center()-(1.5,0,0))
        
        self.play(Write(ReactionArrow),Write(Reactants))
        
        self.wait(1)
        
        self.play(Uncreate(Reactants))
        
        self.play(Write(Products))

        crossout=VGroup(
            Line(BeforeSystem.get_corner(UP+LEFT),AfterSystem.get_corner(DOWN+RIGHT),color=RED,stroke_width=5),
            Line(BeforeSystem.get_corner(DOWN+LEFT),AfterSystem.get_corner(UP+RIGHT),color=RED,stroke_width=5)
        )
        
        self.play(Write(crossout))
        self.play(Uncreate(crossout),Uncreate(Products))
        
        Reactants=VGroup(
            Dot(color=BLUE).shift(UP),
            Dot(color=GREEN).shift(DOWN),
            Dot(color=RED).shift(RIGHT),
            Dot(color=WHITE).shift(LEFT),
            Dot(color=LIGHT_GRAY).shift(UL),
            Dot(color=PINK).shift(DL),
            Dot(color=PURPLE_A).shift(UR),
            Dot(color=YELLOW).shift(DR),
        )
        Products=Reactants.copy()
        def arrange_in_circle(inputs):
            total_angle=2*PI
            angle_diff_per_particle=total_angle/len(inputs)
            for i in range(len(inputs)):
                particle=inputs[i]
                particle.move_to((3,0,0))
                particle.shift(UP)
                particle.rotate(angle_diff_per_particle*i,about_point=(3,0,0))
                Reactants.move_to(BeforeSystem.get_center())
        arrange_in_circle(Products)
        
        self.play(Write(Reactants))

        self.wait(1)
        self.play(ReplacementTransform(Reactants.copy(),Products),
        Reactants.set_color,GRAY)
        self.wait(1)
        self.play(FadeOut(Reactants),Uncreate(Products),Uncreate(ReactionArrow),Uncreate(Reactants.copy()))
        self.play(Uncreate(BeforeSystem),Uncreate(AfterSystem),Uncreate(RSLabel),Uncreate(PSLabel))
        self.clear()
    
    def DefiniteProportions(self):
        LDPTitle=Text("The Law of Definite Proportions",font="Futura",stroke_width=0).scale(0.5)
        self.play(Write(LDPTitle))
        self.wait(2)
        self.play(LDPTitle.to_edge,UP)
        ProustPortrait=ImageMobject("/Users/aathishs/AtomThroughAgesImages/Proust.png").scale(2)
        Date1=Text("1754-1826",font="Geneva",stroke_width=0).scale(0.5).next_to(ProustPortrait,DOWN)
        self.play(FadeInFromDown(ProustPortrait))
        self.play(Write(Date1))
        self.wait(0.5)
        self.play(FadeOutAndShiftDown(ProustPortrait),Uncreate(Date1))
        
        E1=Square(color=REP_GREEN,fill_color=REP_GREEN,fill_opacity=1).to_edge(LEFT)
        E2=Square(color=BLUE,fill_color=BLUE,fill_opacity=1).to_edge(LEFT).shift(2.5*RIGHT)
        PLUS0=TexMobject("+").move_to(VGroup(E1,E2).get_center())
        P1=Rectangle(color="#28CEC4",fill_color="#28CEC4",fill_opacity=1).to_edge(RIGHT)
        Arrow0=Arrow(E2,P1).shift(DOWN)
        
        
        
        self.play(Write(VGroup(E1,E2,PLUS0,P1,Arrow0)))

        self.wait(1)
        for i in range(3):
            self.play(
                E1.scale,0.75,
                E2.scale,0.75,
            )
            self.play(
                P1.scale,0.75
            )
        
        self.play(
            FadeOut(E1),FadeOut(E2),FadeOut(P1),FadeOut(PLUS0),FadeOut(Arrow0)
        )

        self.wait(2)

        ThreeFe=VGroup(
            Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5), 
            Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5).shift(RIGHT*1.1),
            Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5).shift(LEFT*1.1)
            ).shift(LEFT*5)
        
        
        TwoO2=VGroup(
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25), 
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(RIGHT*0.5),
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(RIGHT*1.1), 
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(RIGHT*1.6),
            ).rotate(90*DEGREES).next_to(ThreeFe,RIGHT,buff=1)
        
        Fe3O4=Rectangle(colour=WHITE,fill_color=BLACK,fill_opacity=1,height=1,width=1.5).shift(RIGHT*0.5)

        PLUS1=TexMobject("+").move_to(VGroup(ThreeFe[1],TwoO2).get_center()).shift(RIGHT*0.25)
        arrow1=Arrow(TwoO2.get_center()+RIGHT*0.1,Fe3O4.get_center()+LEFT*0.6)
        
        R1=VGroup(ThreeFe,PLUS1,TwoO2,arrow1,Fe3O4).move_to(ORIGIN)
        
        FourFe=VGroup(
            Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5), 
            Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5).shift(RIGHT*1.1),
            Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5).shift(DOWN*1.1),
            Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5).shift(RIGHT*1.1).shift(DOWN*1.1),
            ).shift(LEFT*5)
        ThreeO2=VGroup(
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25), 
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(RIGHT*0.5),

            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(UP*0.6),
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(UP*0.6).shift(RIGHT*0.5),

            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(DOWN*0.6),
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(DOWN*0.6).shift(RIGHT*0.5),

            ).rotate(90*DEGREES).next_to(FourFe,RIGHT,buff=1)
        TwoFe2O3=VGroup(
            Rectangle(colour=WHITE,fill_color=MAROON_E,fill_opacity=1,height=1,width=1.5),
            Rectangle(colour=WHITE,fill_color=MAROON_E,fill_opacity=1,height=1,width=1.5).shift(LEFT*1.5)).shift((RIGHT)*5).shift(DOWN*0.5)
        PLUS2=TexMobject("+").move_to(VGroup(FourFe,ThreeO2).get_center()).shift(RIGHT*0.13)
        arrow2=Arrow(ThreeO2.get_center()+ RIGHT,(TwoFe2O3.get_center()+LEFT*1.5))
        
        R2=VGroup(FourFe,PLUS2,ThreeO2,arrow2,TwoFe2O3).move_to(ORIGIN).shift(DOWN)
        
        self.play(Write(R1),run_time=2)
        self.wait(2)
        self.play(R1.shift,UP*1.9)
        self.play(Write(R2),run_time=2)
        self.wait(2)
        self.play(Uncreate(VGroup(R2,R1)),run_time=2)
        self.wait(2)
        
        
        Compounds=Text("Compounds",font="Futura",color=REP_GREEN,stroke_width=0).scale(0.5)
        CDef=Text("""A compound is a substance:
        made up of two or more different elements,
        in definite proportions,
        joined together by bonds.""",font="Futura",stroke_width=0).scale(0.5)
        
        self.play(Write(Compounds))
        self.wait(1)
        self.play(Compounds.next_to,LDPTitle,DOWN)
        self.play(Write(CDef),run_time=8)
        self.play(CDef[59:78].set_color,(REP_GREEN))
        self.wait(3)
        self.play(FadeOut(CDef))
        Reverse=VGroup(Text("The Law of Definite Proportions",font="Futura",stroke_width=0).scale(0.5),TexMobject(r"\Updownarrow"),Text("Compounds",font="Futura",color=WHITE,stroke_width=0).scale(0.5))
        Reverse[0].shift(DOWN)
        Reverse[2].shift(UP)
        self.play(
            ReplacementTransform(LDPTitle.copy(),Reverse[0]),
            ReplacementTransform(Compounds.copy(),Reverse[2]),
            Write(Reverse[1])
        )
        self.wait(3)
        self.play(Uncreate(Reverse))
        LDPDef=Text("""For a given compound:
        the elements that are in it are 
        always present in a fixed ratio, 
        no matter where the elements came from 
        or how they bonded.""",font="Futura",stroke_width=0).scale(0.5).shift(DOWN)
        
        self.play(Write(LDPDef),run_time=4)
        self.wait(3)
        self.play(Uncreate(LDPDef))
        
        self.play(Compounds.shift,2.2*RIGHT)
        NonStoichiometric=Text("Non-Stoichiometric",font="Futura",color=RED,stroke_width=0).scale(0.5).next_to(Compounds,LEFT).shift(UP*0.05)
        self.play(Write(NonStoichiometric))
        
        NaClStruct=ImageMobject("/Users/aathishs/AtomThroughAgesImages/NaClWustite.png").scale(2).shift(DOWN)
        self.play(FadeIn(NaClStruct))
        Below=TextMobject("(This is actually Sodium Chloride, but the structures are pretty similar)").scale(0.5).next_to(NaClStruct,DOWN)
        self.play(Write(Below))
        self.wait(5)
        self.play(Uncreate(Below))
        self.play(FadeOut(NaClStruct))
        self.play(Uncreate(NonStoichiometric),Uncreate(Compounds),Uncreate(LDPTitle))

    def MultipleProportions(self):
        LMPTitle=Text("The Law of Multiple Proportions",font="Futura",stroke_width=0).scale(0.5)
        self.play(Write(LMPTitle))
        self.wait(3)
        self.play(LMPTitle.to_edge,UP,LMPTitle.set_color,REP_GREEN)
        DaltonPortrait=ImageMobject("/Users/aathishs/AtomThroughAgesImages/Dalton.png").scale(2.9)
        Date3=TextMobject("1766-1844").next_to(DaltonPortrait,DOWN)
        self.play(FadeInFrom(DaltonPortrait,UP),Write(Date3))
        self.wait(3)
        self.play(FadeOutAndShiftDown(DaltonPortrait),Uncreate(Date3))

        ThreeFe=VGroup(
            Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5), 
            Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5).shift(RIGHT*1.1),
            Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5).shift(LEFT*1.1)
            ).shift(LEFT*5)
        
        
        TwoO2=VGroup(
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25), 
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(RIGHT*0.5),
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(RIGHT*1.1), 
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(RIGHT*1.6),
            ).rotate(90*DEGREES).next_to(ThreeFe,RIGHT,buff=1)
        
        Fe3O4=Rectangle(colour=WHITE,fill_color=BLACK,fill_opacity=1,height=1,width=1.5).shift(RIGHT*0.5)

        PLUS1=TexMobject("+").move_to(VGroup(ThreeFe[1],TwoO2).get_center()).shift(RIGHT*0.25)
        arrow1=Arrow(TwoO2.get_center()+RIGHT*0.1,Fe3O4.get_center()+LEFT*0.6)
        
        R1=VGroup(ThreeFe,PLUS1,TwoO2,arrow1,Fe3O4).move_to(ORIGIN)
        
        FourFe=VGroup(
            Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5), 
            Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5).shift(RIGHT*1.1),
            Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5).shift(DOWN*1.1),
            Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5).shift(RIGHT*1.1).shift(DOWN*1.1),
            ).shift(LEFT*5)
        ThreeO2=VGroup(
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25), 
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(RIGHT*0.5),

            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(UP*0.6),
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(UP*0.6).shift(RIGHT*0.5),

            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(DOWN*0.6),
            Square(color=WHITE,fill_color=BLUE,fill_opacity=1).scale(0.25).shift(DOWN*0.6).shift(RIGHT*0.5),

            ).rotate(90*DEGREES).next_to(FourFe,RIGHT,buff=1)
        TwoFe2O3=VGroup(
            Rectangle(colour=WHITE,fill_color=MAROON_E,fill_opacity=1,height=1,width=1.5),
            Rectangle(colour=WHITE,fill_color=MAROON_E,fill_opacity=1,height=1,width=1.5).shift(LEFT*1.5)).shift((RIGHT)*5).shift(DOWN*0.5)
        PLUS2=TexMobject("+").move_to(VGroup(FourFe,ThreeO2).get_center()).shift(RIGHT*0.13)
        arrow2=Arrow(ThreeO2.get_center()+ RIGHT,(TwoFe2O3.get_center()+LEFT*1.5))
        
        R2=VGroup(FourFe,PLUS2,ThreeO2,arrow2,TwoFe2O3).move_to(ORIGIN).shift(DOWN)

        OneFe1=Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5).move_to(ThreeFe[0].get_center()).shift(UP*1.8)
        OneFe2=Square(color=MAROON_A,fill_color=MAROON_A,fill_opacity=1).scale(0.5).move_to(FourFe.get_center())

        One0=TextMobject("1g",color=BLACK).add_updater(lambda m: m.move_to(OneFe1.get_center()))
        One1=TextMobject("1g",color=BLACK).add_updater(lambda m: m.move_to(OneFe2.get_center()))
        
        Oxygen42981=Rectangle(color=BLUE,fill_color=BLUE,fill_opacity=1,width=0.25,height=0.25*0.42981).move_to(TwoO2.get_center()).shift(UP*1.8).shift(LEFT*0.5)
        Oxygen38206=Rectangle(color=BLUE,fill_color=BLUE,fill_opacity=1,width=0.25,height=0.25*0.38206).move_to(ThreeO2.get_center())

        self.play(Write(R1),run_time=2)
        self.wait(1)
        self.play(R1.shift,UP*1.8)
        self.play(Write(R2),run_time=2)
        self.wait(2)
        self.play(
            ReplacementTransform(ThreeFe,OneFe1),
            ReplacementTransform(FourFe,OneFe2),
            PLUS1.shift,LEFT*0.3,
            PLUS2.shift,LEFT*0.25,
        )
        self.play(
        Write(One0),Write(One1),
        ReplacementTransform(TwoO2,Oxygen42981),
        ReplacementTransform(ThreeO2,Oxygen38206),
        PLUS1.shift,LEFT*0.5,
        PLUS2.shift,RIGHT*0.5,
        )
        self.play(
            TwoFe2O3.scale,0.5693,
            Fe3O4.scale,0.6,
        )

        R1.remove(TwoO2)
        R1.remove(ThreeFe)
        R2.remove(ThreeO2)
        R2.remove(FourFe)
        R1.add(Oxygen42981)
        R2.add(Oxygen38206)
        R1.add(OneFe1)
        R2.add(OneFe2)
        R2.add(One1)
        R1.add(One0)
        self.remove(TwoO2)
        self.remove(ThreeO2)

        R1OBrace=Brace(Oxygen42981,DOWN).add_updater(lambda m:m.next_to(Oxygen42981,DOWN))
        R2OBrace=Brace(Oxygen38206,DOWN).add_updater(lambda m:m.next_to(Oxygen38206,DOWN))

        R1OText=TextMobject("0.42981g").scale(0.5).add_updater(lambda m:m.next_to(R1OBrace,DOWN))
        R2OText=TextMobject("0.38206g").scale(0.5).add_updater(lambda m:m.next_to(R2OBrace,DOWN))


        self.play(Write(R1OBrace),Write(R1OText),Write(R2OBrace),Write(R2OText))

        
        self.play(R2.shift,UP)

        self.wait(1)

        GramFrac=VGroup(DecimalNumber(0.42981,num_decimal_places=5))
        GramFrac.add(DecimalNumber(0.38206,num_decimal_places=5).next_to(GramFrac[0],DOWN))
        GramFrac.add(
            Line(
                GramFrac[0].get_corner(LEFT+DOWN)+LEFT*0.2,
                GramFrac[0].get_corner(RIGHT+DOWN)+RIGHT*0.2,
                ).shift(DOWN*0.1)
            )
        GramFrac.to_edge(DOWN)
        self.play(
            ReplacementTransform(R1OText.copy(),GramFrac[0]),
            ReplacementTransform(R2OText.copy(),GramFrac[1]),
            Write(GramFrac[2])
        )
        
        self.wait(1)

        Approx=TexMobject(r"\approx").add_updater(lambda m: m.next_to(GramFrac,RIGHT))
        GramFrac2=VGroup(DecimalNumber(0.42975,num_decimal_places=5))
        GramFrac2.add(DecimalNumber(0.38200,num_decimal_places=5).next_to(GramFrac2[0],DOWN))
        GramFrac2.add(
            Line(
                GramFrac2[0].get_corner(LEFT+DOWN)+LEFT*0.2,
                GramFrac2[0].get_corner(RIGHT+DOWN)+RIGHT*0.2,
                ).shift(DOWN*0.1)
            )
        GramFrac2.add_updater(lambda m: m.next_to(Approx,RIGHT))
        self.play(
            GramFrac.shift,3*LEFT,
            Write(Approx),
            Write(GramFrac2)
            )
        
        GramFracFinal=VGroup(DecimalNumber(9))
        GramFracFinal.add(DecimalNumber(8).next_to(GramFracFinal[0],DOWN))
        GramFracFinal.add(
            Line(
                GramFracFinal[0].get_corner(LEFT+DOWN)+LEFT*0.2,
                GramFracFinal[0].get_corner(RIGHT+DOWN)+RIGHT*0.2,
                ).shift(DOWN*0.1)
            )
        Equals=TexMobject(r"=").add_updater(lambda m: m.next_to(GramFrac2,RIGHT))
        GramFracFinal.next_to(Equals,RIGHT)
        SmallWholeNumBrace=Brace(GramFracFinal,RIGHT,color=BLUE)
        SmallWholeNumText=Text("our\nsmol\nwhole\nnumbers",font="Futura",stroke_width=0).scale(0.25).next_to(SmallWholeNumBrace,RIGHT)
        self.play(
            Write(Equals),
            Write(GramFracFinal)
        )
        self.play(
            Write(SmallWholeNumBrace),
            Write(SmallWholeNumText)
        )
        
        self.wait(3)
        self.play(Uncreate(
            VGroup(
                *self.get_mobjects()[1:]
            )
        ))
        DWNTableDict={
            Text("Doesn't Like:",color=RED,font="Futura",stroke_width=0):[
                Text("Non-Stoichiometric Compounds (e.g FeO)",font="Futura",color=BLUE,stroke_width=0),
                Text("Large, Complex Compounds (e.g large Hydrocarbons)",font="Futura",stroke_width=0),
            ]
        }
        DoesntWorkWith=Table(DWNTableDict,line_color=RED).scale(0.5).move_to(ORIGIN)
        self.wait(1)
        self.play(Write(DoesntWorkWith))
        self.wait(2)
        self.play(Uncreate(DoesntWorkWith))
        Undecane=SVGMobject("/Users/aathishs/AtomThroughAgesImages/Undecane.svg").next_to(LMPTitle,DOWN)
        Decane=SVGMobject("/Users/aathishs/AtomThroughAgesImages/Decane.svg").next_to(Undecane,DOWN)
        DHydro=VGroup(*Decane.submobjects[38:53])
        DHydro.add(*Decane.submobjects[54:56])
        DHydro.add(*Decane.submobjects[57:59])
        DHydro.add(*Decane.submobjects[60:63])
        
        UHydro=VGroup(*Undecane.submobjects[41:56])
        UHydro.add(*Undecane.submobjects[57:59])
        UHydro.add(*Undecane.submobjects[60:62])
        UHydro.add(*Undecane.submobjects[63:65])
        UHydro.add(*Undecane.submobjects[66:69])

        DecaneBrace=Brace(Decane,LEFT)
        DecaneBraceText=TexMobject("Decane").rotate(90*DEGREES).next_to(DecaneBrace,LEFT)
        UndecaneBrace=Brace(Undecane,LEFT)
        UndecaneBraceText=TexMobject("Undecane").rotate(90*DEGREES).next_to(UndecaneBrace,LEFT)

        self.play(Write(Decane),Write(Undecane),Write(VGroup(DecaneBrace,DecaneBraceText,UndecaneBrace,UndecaneBraceText)))
        self.wait(1)
        GramFrac=VGroup(TexMobject("121"))
        GramFrac.add(TexMobject("120").next_to(GramFrac[0],DOWN))

        GramFrac.add(
            Line(
                GramFrac[0].get_corner(LEFT+DOWN)+LEFT*0.2,
                GramFrac[0].get_corner(RIGHT+DOWN)+RIGHT*0.2,
                ).shift(DOWN*0.1)
            )
        GramFrac.to_edge(DOWN)

        self.play(
            ReplacementTransform(DHydro.copy(),GramFrac[0]),
        )
        self.play(
            ReplacementTransform(UHydro.copy(),GramFrac[1]),
            Write(GramFrac[2])
        )
        
        NotSmallWholeNumBrace=Brace(GramFrac,RIGHT,color=RED)
        NotSmallWholeNumText=Text("not\nsmol\nwhole\nnumbers :(",font="Futura",stroke_width=0,color=RED).scale(0.25).next_to(NotSmallWholeNumBrace,RIGHT)
        self.play(Write(NotSmallWholeNumBrace))
        self.play(Write(NotSmallWholeNumText))
        self.wait(8)
        self.play(Uncreate(
            VGroup(
                *self.get_mobjects()
            )
        ))
        self.clear()
    def construct(self):
        self.IntroduceLaws()
        self.ConservationOfMass()
        self.DefiniteProportions()
        self.MultipleProportions()

class DaltonsModel(SpecialThreeDScene):
    def Make_Atom(self,color,radius):
        atom=Tools.get_surface(self.get_sphere(color=color,radius=radius),shade_color=color,opacity=0.5)
        atom.set_stroke(width=0)
        atom.set_fill(color=color)
        always_rotate(atom)
        return atom

    def construct(self):
        self.set_camera_orientation(**self.default_angled_camera_position)
        
        H_atom=self.Make_Atom(color=WHITE,radius=1)
        Fe_atom=self.Make_Atom(color=MAROON_A,radius=2.4)
        

        Fe_atom.shift(RIGHT*1.6)
        atoms=VGroup(Fe_atom,H_atom)
        self.play(GrowFromCenter(H_atom))
        self.play(H_atom.shift,LEFT*2)

        self.play(GrowFromCenter(Fe_atom))
        self.play(Fe_atom.shift,RIGHT*2)

        self.play(atoms.move_to, ORIGIN)
        self.wait(1)
        self.clear()

class ThomsonsModel(SpecialThreeDScene):
    
    def Make_Atom(self):
        
        #Uncomment the first of the 4 code blocks below, 
        # and the 3rd one if you want random locations for the electrons
        # or the 4th one, if you want organised location, but only for single shell.
        
        # electronlist=[] #This holds the electrons.
        # electron_count=100 #Change this to change the amount of electrons.electronlist=[] #This holds the electrons.

        # def get_random_electron_coordinates(inner_radius):
        #     pol_ang= np.random.uniform(0, 2*PI)
        #     azi_ang= np.random.uniform(0, 2*PI)
        #     return Tools.spherical_to_cartesian(pol_ang,azi_ang,inner_radius)

        # # The following code generates random electron postions, but only if used in conjucntion with get_random_electron_coordinates().
        # # Uncomment them both, and comment out the other electron generation functions to enable randomization.
        # for i in range(0,electron_count):
        #     electron=Tools.get_surface(Sphere(radius=0.08),shade_color=YELLOW,opacity=1)
        #     electron_position=get_random_electron_coordinates(1)
        #     electron.move_to(electron_position)
        #     electronlist.append(electron)

        # for electron_coordinate in get_electron_coordinates_list(electron_count): #for each electron coordinate in get_electron_coordinates where the radius of the inner circle is 1 and electron_count electrons are needed:
        #     electron=Tools.get_surface(Sphere(radius=0.08),shade_color=YELLOW,opacity=1)
        #     electron.move_to(electron_coordinate)
        #     electronlist.append(electron)
        
        def get_electron_coordinates_list(electron_count):
            #Special Edge Case for 2 Electrons.
            if electron_count==1: #Edge case for Hydrogen. DO NOT RUN if shell is greater than 1
                print("1 point generated")
                return([[0,0,0]])
            elif electron_count==2: #Edge case for 2 electrons.
                print("2 points generated")
                return([[0,0,1],[0,0,-1]])
            else:
                #Algorithm used was mostly  taken from https://www.cmu.edu/biolphys/deserno/pdf/sphere_equi.pdf . Explanations in code added by me.
                
                #For some reason unbeknownst to me, this algorithm's output varies HIGHLY depending on radius. If the radius is lesser than one, it creates way more electrons than requested.
                #If the radius is more than one, this creates not enough electrons. ;( As a result, I've had to force this to use only radius one, and change the apparent radius later on, by scaling the model up.
                
                inner_radius=1
                
                electron_coordinate_list=[]
                inner_area=4*(PI*inner_radius**2)
                area_per_electron=inner_area/electron_count
                pseudo_length_per_electron=np.sqrt(area_per_electron) #This is the side length of a square where the area of it is the area per electron on the sphere.
                #Now, we need to get a value of angular space, such that angular space between electrons on latitude and longitude per electron is equal
                #As a first step to obtaining this, we must make another value holding a whole number approximation of the ratio between PI and the pseudo_length. This will give the number of 
                #possible latitudes.

                possible_count_of_lats=np.round(PI/pseudo_length_per_electron)
                
                approx_length_per_electron_lat=PI/possible_count_of_lats #This is the length between electrons on a latitude
                approx_length_per_electron_long=area_per_electron/approx_length_per_electron_lat #This is the length between electrons on a longitude

                for electron_num_lat in range(int(possible_count_of_lats.item())): #The int(somenumpyvalue.item()) is used because Python cannot iterate over a numpy integer and it must be converted to normal int.
                    pol_ang=PI*(electron_num_lat+0.5)/possible_count_of_lats #The original algorithm recommended pol_ang=PI*(electron_num_lat+0.5)/possible_count_of_lats. The 0.5 appears to be added in order to get a larger number of coordinates.
                    #not sure if removing the 0.5 affects results. It didnt do so drastically, so what gives? Anyway, this gets the polar angle as PI*(latitudenumber)/totalnumberoflatitudes.
                    
                    possible_count_of_longs=np.round(2*PI*np.sin(pol_ang)/approx_length_per_electron_long)
                    
                    for electron_num_long in range(int(possible_count_of_longs.item())):
                        
                        azim_ang=(2*PI)*(electron_num_long)/possible_count_of_longs #This gets the azimuthal angle as 2PI*longitudenumber/totalnumberoflongitudes
                        
                        electron_coordinate=Tools.spherical_to_cartesian(pol_ang, azim_ang,inner_radius) #Converts the recieved spherical coordinates to cartesian so Manim can easily handle them.
                        electron_coordinate_list.append(electron_coordinate) #Add this coordinate to the electron_coordinate_list
                
                        #print("Got coordinates: ",electron_coordinate) #Print the coordinate recieved.
                
                print(len(electron_coordinate_list)," points generated.") #Print the amount of electrons will exist. Comment these two lines out if you don't need the data.
                return electron_coordinate_list 
        
        
        shell_config={ #gives info about each shell and electrons inside.
            "shell_1":{"radius":1.0,"electron_count":4,"colour":YELLOW_C},
            "shell_2":{"radius":1.5,"electron_count":4,"colour":YELLOW_B}
        }
        electron_dict={} #This holds all the electrons in the format {"shell_n":electron}
        
        for shell in shell_config:
            electron_dict[shell]=[]
            tempVGroup=VGroup()
            if shell_config[shell]["electron_count"]==0:
                continue
            else:
                for electron_coordinate in get_electron_coordinates_list(shell_config[shell]["electron_count"]): #for each electron coordinate in get_electron_coordinates where the radius of the inner circle is 1 and electron_count electrons are needed:
                    electron=Tools.get_surface(Sphere(radius=0.08),shade_color=shell_config[shell]["colour"],opacity=1)
                    electron.move_to(electron_coordinate)
                    electron_dict[shell].append(electron)
            tempVGroup=VGroup(*electron_dict[shell])
            tempVGroup.space_out_submobjects(shell_config[str(shell)]["radius"])

        #print(electron_dict)
        
        positivecloud = Tools.get_surface(surface = self.get_sphere(radius=2),shade_color=DARK_BLUE)
        positivecloud.set_stroke(width=0)
        axes = self.get_axes()

        allElectrons=Tools.flatten(list(electron_dict.values()))

        # atom=VGroup(*electron_dict["shell_1"],*electron_dict["shell_2"],positivecloud)
        atom=VGroup(*allElectrons,positivecloud)
        
        # atomaxes=VGroup(atom,axes)
        
        # always_rotate(atomaxes,rate=0.15,about_point=(0,0,0))
        
        always_rotate(atom,rate=0.15)
        return atom

    def construct(self):
        atom=self.Make_Atom()
        self.play(GrowFromCenter(atom))
        
        self.move_camera(
            **self.default_angled_camera_position,
            run_time=1,
        )
        # self.begin_ambient_camera_rotation(0.15) #I dont need this since im using always_rotate()
        self.wait(8)
    
class RutherfordsModel(SpecialThreeDScene):
    def Make_Atom(self,ATOMIC_NUMBER=3):
        nucleus=VGroup()
        atom=VGroup()
        
        def make_nucleus(ATOMIC_NUMBER=ATOMIC_NUMBER):
            for n in range(ATOMIC_NUMBER):
                DIRECTION=[LEFT,RIGHT,UP,DOWN,OUT,IN,UL,UR][np.random.randint(0,8)]
                proton=Tools.get_surface(Sphere(radius=0.1),shade_color=BLUE,opacity=1)
                proton.shift(DIRECTION*0.1)

                neutron=Tools.get_surface(Sphere(radius=0.1),shade_color=DARK_GREY,opacity=1)
                DIRECTION=[LEFT,RIGHT,UP,DOWN,OUT,IN,UL,UR][np.random.randint(0,8)]
                neutron.shift(DIRECTION*0.15)
                nucleus.add(proton,neutron)
            return nucleus
        
        nucleus=make_nucleus(ATOMIC_NUMBER)
        atom.add(nucleus)


        electron_count=ATOMIC_NUMBER
        angle_between_orbits=PI/electron_count
        electrons=VGroup()

        for n in range(electron_count):
            orbit=Circle(radius=1)
            orbit.rotate(angle_between_orbits*n,axis=Y_AXIS)
            atom.add(orbit)
        # always_rotate(atom,rate=-20*DEGREES)
        self.add(atom)


    def construct(self):
        # self.begin_ambient_camera_rotation(0.15) #I dont need this since im using always_rotate()
        # print(**self.default_angled_camera_position)
        # quit()
        # self.Make_Atom(ATOMIC_NUMBER=5)

        self.add(Cube())
        
        self.move_camera(
            theta= 20 * DEGREES,
            phi=20*DEGREES,
            run_time=1,
        )
        self.wait(2)

