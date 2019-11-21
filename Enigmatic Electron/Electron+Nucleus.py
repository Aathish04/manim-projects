from manimlib.imports import *
#Note that manim internally runs update source functions multiple times in order to render the update. This means any internal variables
#are reset every frame. Therefore, all position and angle and similar variables that must remain unreset between updates must remain outside the function.
# t_offset = 0
initposE1=0
initposE2=0.1
initposE3=0.3
class OrbitAnimation(Scene):
    def construct(self):
        
        nucleus= Dot(color = BLUE).center()

        path1 = Ellipse(color=WHITE,stroke_width=1,center=Dot(color=BLUE),width=3,height=0.5);path1.rotate(PI/4)
        
        # path2 = Ellipse(color=WHITE,stroke_width=1,center=Dot(color=BLUE),width=3,height=0.5);path2.rotate(3*PI/4)
        # path3 = Ellipse(color=WHITE,stroke_width=1,center=Dot(color=BLUE),width=2.7,height=0.5);path3.rotate(PI/2)

        electron1 = Dot(color=YELLOW)

        # electron2 = Dot(color=YELLOW)
        # electron3 = Dot(color=YELLOW)

        H_atom=VGroup(nucleus,path1,electron1) # H_atom=VGroup(nucleus,path1,path2,path3,electron1,electron2,electron3)
        
        def update_electron1(electron1, dt):
            global initposE1
            rate = dt
            electron1.move_to(path1.point_from_proportion(((initposE1 + rate))%1))
            initposE1 += rate*2
        
        # def update_electron2(electron2, dt):
        #     global initposE2
        #     rate = -dt
        #     electron2.move_to(path2.point_from_proportion(((initposE2 + rate))%1))
        #     initposE2 += rate*2
        
        # def update_electron3(electron3, dt):
        #     global initposE3
        #     rate = -dt
        #     electron3.move_to(path3.point_from_proportion(((initposE3 + rate))%1))
        #     initposE3 += rate*2

        #H_atom.rotate(PI/4)
        electron1.add_updater(update_electron1)
        # electron2.add_updater(update_electron2)
        # electron3.add_updater(update_electron3)

        self.add(H_atom)
        self.wait(9)