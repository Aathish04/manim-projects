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

    def polar_to_cartesian(self,pol_ang,azim_ang,radius):
        return np.array((radius*np.sin(pol_ang) * np.cos(azim_ang),
                            radius*np.sin(pol_ang) * np.sin(azim_ang),
                            radius*np.cos(pol_ang)))
    
    def get_surface(self, surface,shade_color,opacity=0.3):
        result = surface.copy()
        result.set_fill(shade_color, opacity=opacity)
        result.set_stroke(WHITE, width=0.5, opacity=opacity)
        return result

    def Make_Atom(self):
            
        def get_electron_coordinates(inner_radius):
            pol_ang= np.random.uniform(0, 2*PI)
            azi_ang= np.random.uniform(0, 2*PI)
            return self.polar_to_cartesian(pol_ang,azi_ang,inner_radius)   
        
        electronlist=[]
        electron_count=100

        while electron_count>0:
            electron=self.get_surface(Sphere(radius=0.08),shade_color=YELLOW,opacity=1)
            
            # electron_position=[ps_x,ps_y,ps_z]
            electron_position=get_electron_coordinates(1)
            DistFromOrigin=1
            
            if DistFromOrigin<2:
                electron.move_to(electron_position)
                electronlist.append(electron)
                electron_count-=1
            else:
                continue
        
        positivecloud = self.get_surface(surface = self.get_sphere(radius=2.4),shade_color=DARK_BLUE)
        positivecloud.set_stroke(width=0)
        axes = self.get_axes()
        
        atom=VGroup(*electronlist,positivecloud)

        self.add(atom,axes)

    def construct(self):
        self.Make_Atom()
        
        self.move_camera(
            **self.default_angled_camera_position,
            run_time=2,
        )
        self.begin_ambient_camera_rotation()
        self.wait(8)