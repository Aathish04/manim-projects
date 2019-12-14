from manimlib.imports import *
from random import randrange
#Note that manim internally runs update source functions multiple times in order to render the update. This means any internal variables
#are reset every frame. Therefore, all position and angle and similar variables that must remain unreset between updates must remain outside the function.
# t_offset = 0

class RutherfordsModel(Scene):
    initposEl=0    
    def construct(self):
        
        nucleus= Dot(color = BLUE).center()

        orbit = Circle(color=WHITE,stroke_width=1,center=nucleus)
        
        electron = Dot(color=YELLOW)

        H_atom=VGroup(electron,nucleus,orbit) # Manim adds onto screen in the order in which it reads. Adds electron first, nucleus second, and orbit third.
        
        def update_electron(electron, dt):
            global initposEl
            rate = dt
            electron.move_to(orbit.point_from_proportion(((initposEl + rate))%1)) #point_from_proportion takes a value from -1,1 specifying direction to move in with sign and how much to move by with value
            initposEl += rate*2

        self.play(GrowFromCenter(H_atom))
        electron.add_updater(update_electron)
        self.wait(9)

class ThomsonsModel(SpecialThreeDScene):
        
    def get_surface(self, surface,shade_color,opacity=0.2):
        result = surface.copy()
        result.set_fill(shade_color, opacity=opacity)
        result.set_stroke(WHITE, width=0.5, opacity=opacity)
        return result

    def construct(self):
        electronlist=[]
        for i in range(0,20):
            electron=self.get_surface(Sphere(radius=0.08),shade_color=YELLOW,opacity=1)
            electron.move_to([(randrange(-14,14,1))/10,(randrange(-14,14,1))/10,(randrange(-14,14,1))/10])
            electronlist.append(electron)
        
        positivecloud = self.get_surface(surface = self.get_sphere(),shade_color=BLUE)
        positivecloud.set_stroke(width=0)
        axes = self.get_axes()
        
        atom=VGroup(*electronlist,positivecloud)

        self.add(positivecloud,axes)
        for electron in electronlist:
            self.add(electron)
        
        self.move_camera(
            **self.default_angled_camera_position,
            run_time=2,
        )