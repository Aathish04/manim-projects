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
    def get_surface(surface,shade_color,opacity=0.3):
        result = surface.copy()
        result.set_fill(shade_color, opacity=opacity)
        result.set_stroke(WHITE, width=0.5, opacity=opacity)
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
        self.play(GrowFromPoint(zoomed_display,InParticles[0].get_center()))
        self.activate_zooming()

        Mass=Text("Mass=1 unit",font="Futura",stroke_width=0).scale(0.25).next_to(zoomed_display,DOWN).shift(LEFT)
        Volume=Text("Volume = 1 unit",font="Futura",stroke_width=0).scale(0.25).next_to(zoomed_display,DOWN).shift(RIGHT)

        self.play(Write(Mass),Write(Volume))

        self.play(Tools.wait_while_updating(2))   

        TemperatureMonitor=VGroup(Text("Temperature: 25 °C",font="serif",stroke_width=0)).scale(0.5).to_corner(UP+LEFT)
        self.play(Uncreate(LCMTitle),Write(TemperatureMonitor))
        
        self.play(Tools.wait_while_updating(6))  
        
        FirstLaw=TexMobject("U=Q+W").next_to(System,DOWN)
        self.play(Write(FirstLaw))
        self.play(Tools.wait_while_updating(0.5))
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
        self.clear()

        self.wait(1)

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
    
    def construct(self):
        self.IntroduceLaws()
        self.ConservationOfMass()


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

