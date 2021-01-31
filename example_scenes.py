##信号的时域、频域和相位观察(signal showed in time domain,frequency domain and phase domain
##借用了3b1b 的库manim
#!/usr/bin/env python

from manimlib.imports import *

# python -m manim example_scenes.py ShowSignal -pl


class ShowSignal(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes().shift(LEFT*(-TAU))
        wall = ParametricSurface(
            lambda u, v: np.array([
                6.2,
                u,
                v
            ]))
        self.set_camera_orientation(phi=80 * DEGREES,theta=50*DEGREES)
        self.play(ShowCreation(axes))
        self.play(FadeInFromLarge(wall))
        #self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(1)
        #self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES, run_time=3)


        curve = ParametricFunction(
            lambda u: np.array([
                -u,
                0,
                1*np.cos(9*u)+1.8*np.cos(3*u)+0.6*np.cos(1.5*u+PI/3)+0.2*np.sin(6*u)
            ]), color=RED, t_min=-TAU, t_max=2*TAU,
        )
        fun = TextMobject('y=1.0cos(9x)+1.8cos(3x)+0.6cos(1.5x+60°)+0.2sin(6x)').set_color(RED).scale(0.8).move_to(2*LEFT+3.0*UP)
        cur1=curve.copy()
        cur2 = curve.copy()
        cur3 = curve.copy()
        cur4 = curve.copy()
        self.play(ShowCreation(curve),run_time=2)
        self.add_fixed_in_frame_mobjects(fun)
        self.play(FadeInFromLarge(fun), run_time=1)
        self.wait(0.8)
        #self.play(FadeOut(fun),run_time=1)
        #self.play(Transform(fun),run_time=2)
        self.wait(0.8)

        curve1 = ParametricFunction(
            lambda u: np.array([
                -u,
                6 * np.ones_like(u),
                1.0 * np.cos(9 * u)
            ]), color=GREY, t_min=-TAU, t_max= TAU,
        )
        fun1 = TextMobject('y=1.0cos(9x)').set_color(GREY).scale(1.5).move_to(3.5 * LEFT + 3 * UP)
        #self.play(ShowCreation(curve1), run_time=5)
        self.play(Indicate(curve))
        self.play(Transform(cur1, curve1), run_time=2)
        self.add_fixed_in_frame_mobjects(fun1)
        self.play(Transform(fun,fun1), run_time=1)
        self.wait(0.8)
        self.play(FadeOut(fun), run_time=2)


        curve2 = ParametricFunction(
            lambda u: np.array([
                -u,
                2 * np.ones_like(u),
                1.8 * np.cos(3*u)
            ]), color=GREEN, t_min=-TAU, t_max= TAU,
        )
        self.play(Indicate(curve))
        self.play(Transform(cur2, curve2))
        fun2 = TextMobject('y=1.8cos(3x)').set_color(GREEN).scale(1.5).move_to(3.5 * LEFT + 3 * UP)
        #self.play(ShowCreation(curve2), run_time=5)
        self.add_fixed_in_frame_mobjects(fun2)
        self.play(Transform(fun1,fun2), run_time=1)
        self.wait(0.8)
        self.play(FadeOut(fun1), run_time=2)


        curve3 = ParametricFunction(
            lambda u: np.array([
                -u,
                1 * np.ones_like(u),
                0.6 * np.cos(1.5* u+PI/3)
            ]), color=BLUE, t_min=-TAU, t_max= TAU,
        )
        self.play(Indicate(curve))
        self.play(Transform(cur3, curve3), run_time=2)
        fun3 = TextMobject('y=0.6cos(1.5x+60°)').set_color(BLUE).scale(1.5).move_to(3.5 * LEFT + 3 * UP)
        # self.play(ShowCreation(curve1), run_time=5)
        self.add_fixed_in_frame_mobjects(fun3)
        self.play(Transform(fun2,fun3), run_time=1)
        self.wait(0.8)
        self.play(FadeOut(fun2))

        curve4 = ParametricFunction(
            lambda u: np.array([
                -u,
                4 * np.ones_like(u),
                0.2 * np.sin(6 * u)
            ]), color=PURPLE, t_min=-TAU, t_max= TAU,
        )
        self.play(Indicate(curve))
        fun4 = TextMobject('y=0.2cos(6x)').set_color(PURPLE).scale(1.5).move_to(3.5 * LEFT + 3 * UP)
        # self.play(ShowCreation(curve1), run_time=5)
        self.play(Transform(cur4, curve4), run_time=2)
        self.add_fixed_in_frame_mobjects(fun4)
        self.play(Transform(fun3,fun4), run_time=1)
        self.wait(0.8)
        self.play(FadeOut(fun3))
        self.play(FadeOut(fun4))
        # self.play(Transform(curve11,fun1),run_time=2)
        wall.set_opacity(0)
        self.wait(1)


        wh=VGroup(axes,curve,curve1,curve2,curve3,curve4,cur1,cur2,cur3,cur4)
        self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES, run_time=3)
        self.wait(1)
        self.play(wh.scale,0.8,wh.shift,DOWN*6+IN*2)



        ##从频域上观察
        self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES, run_time=3)
        axes1 = ThreeDAxes()
        self.play(FadeInFromLarge(axes1))
        self.wait(1)

        xl = TextMobject('f/Hz').move_to([6.5, -0.3, 0])
        self.add_fixed_in_frame_mobjects(xl)
        self.play(Write(xl))
        yl = TextMobject('A').move_to([0.5, 3.3, 0])
        self.add_fixed_in_frame_mobjects(yl)
        self.play(Write(yl))
        self.wait(1)


        line1 = ParametricFunction(
            lambda u: np.array([
                0,
                6,
                u
            ]), color=GREY, t_min=0, t_max=1,
        )
        self.play(Transform(curve1,line1))
        line2 = ParametricFunction(
            lambda u: np.array([
                0,
                2,
                1.8*u
            ]), color=GREEN, t_min=0, t_max=1,
        )
        self.play(Transform(curve2, line2))
        line3 = ParametricFunction(
            lambda u: np.array([
                4/9*PI*u,
                1,
                0.6*u
            ]), color=BLUE, t_min=0, t_max=1,
        )
        self.play(Transform(curve3, line3))
        line4 = ParametricFunction(
            lambda u: np.array([
                PI/2*u,
                4,
                0.2*u
            ]), color=PURPLE, t_min=0, t_max=1,
        )
        self.play(Transform(curve4, line4))
        self.wait(1)


        x1 = TextMobject('1.5').move_to([1, -0.3, 0])
        self.add_fixed_in_frame_mobjects(x1)
        self.play(Write(x1))
        x2 = TextMobject('3').move_to([2, -0.3, 0])
        self.add_fixed_in_frame_mobjects(x2)
        self.play(Write(x2))
        x3 = TextMobject('6').move_to([4, -0.3, 0])
        self.add_fixed_in_frame_mobjects(x3)
        self.play(Write(x3))
        x4 = TextMobject('9').move_to([6, -0.3, 0])
        self.add_fixed_in_frame_mobjects(x4)
        self.play(Write(x4))
        y1 = TextMobject('1.5').move_to([-0.5, 0.2, 0])
        self.add_fixed_in_frame_mobjects(y1)
        self.play(Write(y1))
        y2 = TextMobject('3').move_to([-0.5, 0.6, 0])
        self.add_fixed_in_frame_mobjects(y2)
        self.play(Write(y2))
        y3 = TextMobject('6').move_to([-0.5, 1, 0])
        self.add_fixed_in_frame_mobjects(y3)
        self.play(Write(y3))
        y4 = TextMobject('9').move_to([-0.5, 1.8, 0])
        self.add_fixed_in_frame_mobjects(y4)
        self.play(Write(y4))

        self.move_camera(phi=0)
        self.play(FadeOut(yl))
        yl1 = TextMobject('phase').move_to([0.5, 3.3, 0])
        self.add_fixed_in_frame_mobjects(yl1)
        self.play(FadeInFromLarge(yl1))
        self.remove(y1)
        self.remove(y2)
        self.remove(y3)
        self.remove(y4)
        self.wait(2)
        y1=TextMobject('4/9pai').move_to([1,-4/9*PI,0])
        y2=TextMobject('1/2pai').move_to([4,-1/2*PI,0])

        self.add_fixed_in_frame_mobjects(y1)
        self.add_fixed_in_frame_mobjects(y2)
        self.wait(5)










#python -m manim example_scenes.py t -pl
class t(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        self.set_camera_orientation(phi=90 * DEGREES,theta=0*DEGREES)
        self.play(ShowCreation(axes))
        #self.begin_ambient_camera_rotation(rate=0.1)
        #self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES, run_time=3)

        dot3 = Dot().move_to([1, 0, 0]).set_color(RED)
        dot2 = Dot().move_to([2, 0, 0]).set_color(RED)
        self.add_fixed_in_frame_mobjects(dot3)
        self.add_fixed_in_frame_mobjects(dot2)
        dot4 = Dot().move_to([4, 0, 0]).set_color(RED)
        self.add_fixed_in_frame_mobjects(dot4)
        dot1 = Dot().move_to([6, 0, 0]).set_color(RED)
        self.add_fixed_in_frame_mobjects(dot1)
        d3 = Dot().move_to([1, 0.6, 4 / 9 * PI]).set_color(GREEN)
        self.add_fixed_in_frame_mobjects(d3)
        d2 = Dot().move_to([2, 1.8, 0]).set_color(GREEN)
        self.add_fixed_in_frame_mobjects(d2)
        d4 = Dot().move_to([4, 0.2, PI / 2]).set_color(GREEN)
        self.add_fixed_in_frame_mobjects(d4)
        d1 = Dot().move_to([6, 1, 0]).set_color(GREEN)
        self.add_fixed_in_frame_mobjects(d1)

        line1 = Line(dot1, d1)

        self.add_fixed_orientation_mobjects(line1)
        self.play(FadeIn(line1))
        line2 = Line(dot2, d2)

        self.add_fixed_in_frame_mobjects(line2)
        self.play(FadeIn(line2))
        line3 = Line(dot3, d3)

        self.add_fixed_in_frame_mobjects(line3)
        self.play(FadeIn(line3))
        line4 = Line(dot4, d4)

        self.add_fixed_in_frame_mobjects(line4)
        self.play(FadeIn(line4))

        self.add_fixed_orientation_mobjects(line1)




        self.move_camera(phi=0*DEGREES)
        self.wait(4)






