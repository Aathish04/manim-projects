from manimlib.imports import *
from random import randrange
#Note that manim internally runs update source functions multiple times in order to render the update. This means any internal variables
#are reset every frame. Therefore, all position and angle and similar variables that must remain unreset between updates must remain outside the function.
# t_offset = 0
initposEl=0
class RutherfordsModel(Scene):
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
        
    def get_surface(self, surface,shade_color,opacity=0.3):
        result = surface.copy()
        result.set_fill(shade_color, opacity=opacity)
        result.set_stroke(WHITE, width=0.5, opacity=opacity)
        return result

    def construct(self):
        electronlist=[]
        ENum=100

        while ENum>0:
            rad=randrange(8,30,3)/100
            electron=self.get_surface(Sphere(radius=rad),shade_color=YELLOW,opacity=1)
            ps_x=randrange(-20,20,1)/10
            ps_y=randrange(-20,20,1)/10
            ps_z=randrange(-20,20,1)/10
            DistFromOrigin=np.sqrt((ps_x**2)+(ps_y**2)+(ps_z**2))
            if DistFromOrigin<2:
                electron.move_to([ps_x,ps_y,ps_z])
                electronlist.append(electron)
                ENum-=1
            else:
                continue
        
        positivecloud = self.get_surface(surface = self.get_sphere(radius=2.4),shade_color=DARK_BLUE)
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
        self.begin_ambient_camera_rotation()
        self.wait(8)