from manimlib.imports import *
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
    CONFIG = {
        "R_color": YELLOW,
        "space_out_factor": 1.15,
    }

    def construct(self):
        self.showPlumPudding()

    def showPlumPudding(self):
        
        PlumPudding = Sphere(radius=1.5,stroke_width=0.5,stroke_color=BLACK)
        PlumPudding.set_fill(REP_GREEN, opacity=0.5)
        PlumPudding.add_updater(lambda s, dt: s.rotate(0.1 * dt, axis=OUT))
        
        pieces = PlumPudding.deepcopy()
            
        pieces.space_out_submobjects(1.5)
        pieces.shift(OUT)
        pieces.set_color(REP_GREEN)



        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-90 * DEGREES,
        )

        self.play(
            ShowCreation(PlumPudding,run_time=1.5),
        )
        #Comment the below play statement to avoid expanding the sphere sectors.
        self.play(
            Transform(
                PlumPudding, pieces,
                rate_func=there_and_back_with_pause,
                run_time=2
            )
        )
        self.play(LaggedStartMap(
            UpdateFromAlphaFunc, PlumPudding,
            lambda mob: (mob, lambda m, a: m.set_fill(
                color=interpolate_color(REP_GREEN, YELLOW,a),
                opacity=interpolate(0.5, 1, a)
            )),
            rate_func=there_and_back,
            lag_ratio=0.1,
            run_time=4
        ))