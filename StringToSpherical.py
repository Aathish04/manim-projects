# Until https://github.com/ManimCommunity/manim/pull/1469 is merged,
# use manim from https://github.com/Aathish04/manim/tree/add_bezier_utils

from manim import *


class StringToSpherical(ThreeDScene):

    A = 1 / 2  # Maximum amplitude of travelling wave.
    # Arbitrary, but set here so the max amplitude of the standing wave is 1.

    l = 3  # Wavelength of standing wave. Arbitrary.

    f = 0.5  # Frequency of standing wave in hertz. Arbitrary.

    w = 2 * PI * f  # Angular frequency of standing wave.

    clock = ValueTracker()

    def anchor_and_handle_func(self, anchors_obj, anchor_func, **kwargs):
        anchors = anchors_obj.get_anchors()

        anchorpairs = np.split(anchors, len(anchors) / 2)
        outanchor1 = []
        outhandle1 = []
        outhandle2 = []
        outanchor2 = []
        for anchorpair in anchorpairs:
            for i, anchor in enumerate(anchorpair):
                outanchor = outanchor1 if i == 0 else outanchor2
                outanchor.append(anchor_func(anchors_obj, anchor, **kwargs))
            handles = get_smooth_cubic_bezier_handle_points(
                (outanchor1[-1], outanchor2[-1])
            )
            outhandle1.append(handles[0])
            outhandle2.append(handles[1])

        return outanchor1, outhandle1, outhandle2, outanchor2

    def twodwavefunction(self, x, t):
        return 2 * self.A * np.sin(2 * PI * x / self.l) * np.cos(self.w * t)

    def arcwavepointsfunction(self, anchorobj, anchor, t_range):
        p = anchorobj.proportion_from_point(anchor)
        t_min = t_range[0].get_value()
        t_max = t_range[1].get_value()
        x_val = t_min + (p * (t_max - t_min))
        scale_factor = 0.5 * (self.twodwavefunction(x_val, self.clock.get_value()))
        return anchor * (1 + scale_factor)

    def threedwavepointsfunction(self, u, v, t_range):
        p = u / (PI - 10e-6)

        t_min = t_range[0].get_value()
        t_max = t_range[1].get_value()
        x_val = t_min + (p * (t_max - t_min))
        scale_factor = 0.5 * (self.twodwavefunction(x_val, self.clock.get_value()))

        vect = np.array(
            [
                np.cos(v) * np.sin(u),
                np.cos(u),
                np.sin(v) * np.sin(u),
            ]
        )

        return vect * (1 + scale_factor)

    def intro_till_first_sphere(self):

        title = (
            Tex("String Harmonics lead elegantly to Spherical Harmonics.")
            .scale(0.75)
            .to_corner(UL)
        )

        axes = Axes(x_axis_config={"include_tip": False}, x_length=14, y_length=8)
        self.add(axes[0])

        t_range = [ValueTracker(axes.x_range[0]), ValueTracker(axes.x_range[1])]

        wave = always_redraw(
            lambda: axes.get_graph(
                lambda x: self.twodwavefunction(x, self.clock.get_value()),
                t_range=[t_range[0].get_value(), t_range[1].get_value()],
            )
        )

        nodes = VGroup(
            *[
                Dot(RIGHT * i, color=RED)
                for i in np.arange(
                    int(t_range[0].get_value()) + 1,
                    int(t_range[1].get_value()),
                    step=self.l / 2,
                )
            ]  # A node occurs every l/2 interval
        )

        indication_rect = (
            Rectangle(color=GREEN, width=VGroup(nodes[5:7]).width - 0.15, height=2.2)
            .move_to(nodes[5:7].get_center())
            .shift(LEFT * self.l / 4)
        )

        considertex = (
            Tex(
                r"Consider the standing wave with one node\\and antinodes at either end."
            )
            .scale(0.75)
            .next_to(indication_rect, DOWN)
        )

        self.add(wave)

        clock_incr = 4
        self.play(
            AnimationGroup(
                self.clock.animate(
                    run_time=clock_incr, rate_func=linear
                ).increment_value(clock_incr),
                Write(nodes, lag_ratio=1),
                lag_ratio=0.5,
            ),
            Write(title, run_time=4),
        )

        clock_incr = 8
        self.play(
            self.clock.animate(run_time=clock_incr, rate_func=linear).increment_value(
                clock_incr
            ),
            AnimationGroup(
                Write(considertex, run_time=3),
                AnimationGroup(  # Focus only on part of graph with one node and antinodes at either end.
                    FadeInFromLarge(indication_rect, 5),
                    t_range[0].animate().set_value(indication_rect.get_left()[0]),
                    t_range[1].animate().set_value(indication_rect.get_right()[0]),
                    FadeOut(VGroup(nodes[:5] + nodes[6:])),
                ),
                lag_ratio=1,
            ),
        )

        andbendtex = (
            Tex(r"And bend it into a semicircle.")
            .scale(0.75)
            .move_to(considertex)
            .shift(RIGHT * 1.25)
        )

        semicircle = always_redraw(
            lambda: VMobject()
            .set_anchors_and_handles(
                *self.anchor_and_handle_func(
                    Arc(start_angle=PI / 2, angle=-PI),
                    self.arcwavepointsfunction,
                    t_range=t_range,
                )
            )
            .make_smooth()
        )

        self.play(
            FadeOutAndShift(title, UP),
            Write(axes[1]),
            FadeOutAndShift(indication_rect, DOWN),
            ReplacementTransform(considertex, andbendtex),
            ReplacementTransform(wave, semicircle),
            nodes[5].animate().shift(LEFT * 0.5),
        )
        nodedot3d = Dot3D(nodes[5].get_center(), color=RED)

        clock_incr = 4
        self.move_camera(
            phi=-45 * DEGREES,
            theta=-135 * DEGREES,
            gamma=-55 * DEGREES,
            added_anims=[
                self.clock.animate(
                    run_time=clock_incr, rate_func=linear
                ).increment_value(clock_incr),
                ReplacementTransform(nodes[5], nodedot3d),
            ],
        )
        nodes = VGroup(*nodes[:5], nodedot3d, *nodes[6:])

        v_max_tracker = ValueTracker()

        threedwaveform = always_redraw(
            lambda: ParametricSurface(
                func=lambda u, v: self.threedwavepointsfunction(u, v, t_range=t_range),
                u_min=10e-6,
                u_max=PI - 10e-6,
                v_min=0,
                v_max=v_max_tracker.get_value(),
                checkerboard_colors=[None, None],
                fill_color=WHITE,
                fill_opacity=1,
            )
        )

        axes.add(
            axes.create_axis(
                (-4, 4, 1),
                axis_config={},
                length=8,
            ).rotate_about_zero(-PI / 2, UP)
        )

        androtatetex = (
            Tex(r"Now, spin that semicircle about its axis.")
            .scale(0.7)
            .to_corner(UR)
            .shift(LEFT * 0.3)
        )
        nodecircle = Circle(color=RED).reverse_direction().rotate(-PI / 2, RIGHT)

        self.add(threedwaveform)
        self.play(
            v_max_tracker.animate().set_value(2 * PI),
            Write(axes[2]),
            FadeOut(semicircle),
            Write(androtatetex, run_time=1),
            FadeOutAndShift(andbendtex, DOWN),
            Create(nodecircle, run_time=1),
            ShrinkToCenter(nodes[5]),
        )
        nodes = VGroup(*nodes[:5], nodecircle, *nodes[6:])

        clock_incr = 4
        self.play(
            self.clock.animate(run_time=clock_incr, rate_func=linear).increment_value(
                clock_incr
            ),
        )

    def construct(self):
        self.intro_till_first_sphere()
