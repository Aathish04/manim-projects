from manim import *


class StringToSpherical(ThreeDScene):
    def construct(self):

        title = (
            Tex("String Harmonics lead elegantly to Spherical Harmonics.")
            .scale(0.75)
            .to_corner(UL)
        )

        axes = Axes(x_axis_config={"include_tip": False})
        self.add(axes[0])

        t = ValueTracker()  # Timekeeper

        x_min = ValueTracker(axes.x_axis_config["x_min"])
        x_max = ValueTracker(axes.x_axis_config["x_max"])

        A = 1 / 2  # Maximum amplitude of standing wave. Arbitrary.

        l = 3  # Wavelength of standing wave. Arbitrary.

        f = 0.5  # Frequency of standing wave in hertz. Arbitrary.

        w = 2 * PI * f  # Angular frequency of standing wave.

        def twodwavefunction(x, t):
            return 2 * A * np.sin(2 * PI * x / l) * np.cos(w * t)

        wave = always_redraw(
            lambda: axes.get_graph(
                lambda x: twodwavefunction(x, t.get_value()),
                x_min=x_min.get_value(),
                x_max=x_max.get_value(),
            )
        )

        nodes = VGroup(
            *[
                Dot(RIGHT * i, color=RED)
                for i in np.arange(
                    int(x_min.get_value()) + 1,
                    int(x_max.get_value()),
                    step=l / 2,
                )
            ]  # A node occurs every l/2 interval
        )

        indication_rect = (
            Rectangle(color=GREEN, width=VGroup(nodes[5:7]).width - 0.15, height=2.2)
            .move_to(nodes[5:7].get_center())
            .shift(LEFT * l / 4)
        )

        considertex = (
            Tex(
                r"Consider the standing wave with one node\\and antinodes at either end."
            )
            .scale(0.75)
            .next_to(indication_rect, DOWN)
        )

        self.add(wave)

        t_val = 4
        self.play(
            AnimationGroup(
                t.animate(run_time=t_val, rate_func=linear).increment_value(t_val),
                Write(nodes, lag_ratio=1),
                lag_ratio=0.5,
            ),
            Write(title, run_time=4),
        )

        t_val = 8
        self.play(
            t.animate(run_time=t_val, rate_func=linear).increment_value(t_val),
            AnimationGroup(
                Write(considertex, run_time=3),
                AnimationGroup(  # Focus only on part of graph with one node and antinodes at either end.
                    FadeInFromLarge(indication_rect, 5),
                    x_min.animate().set_value(indication_rect.get_left()[0]),
                    x_max.animate().set_value(indication_rect.get_right()[0]),
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

        self.play(
            FadeOutAndShift(title, UP),
            Write(axes[1]),
            FadeOutAndShift(indication_rect, DOWN),
            ReplacementTransform(considertex, andbendtex),
            Transform(wave, Arc(start_angle=PI / 2, angle=-PI)),
            nodes[5].animate().shift(LEFT * 0.5),
        )
