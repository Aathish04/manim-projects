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

    def spherical_to_cartesian(self,pol_ang,azim_ang,radius): #This function converts given spherical coordinates (theta, phi and radius) to cartesian coordinates.
        return np.array((radius*np.sin(pol_ang) * np.cos(azim_ang),
                            radius*np.sin(pol_ang) * np.sin(azim_ang),
                            radius*np.cos(pol_ang))
                            )

    def get_surface(self, surface,shade_color,opacity=0.3):
        result = surface.copy()
        result.set_fill(shade_color, opacity=opacity)
        result.set_stroke(WHITE, width=0.5, opacity=opacity)
        return result

    def Make_Atom(self):

        # def get_random_electron_coordinates(inner_radius):
        #     pol_ang= np.random.uniform(0, 2*PI)
        #     azi_ang= np.random.uniform(0, 2*PI)
        #     return self.spherical_to_cartesian(pol_ang,azi_ang,inner_radius)   

        def get_electron_coordinates_list(inner_radius,electron_count):
            #Algorithm used was mostly  taken from https://www.cmu.edu/biolphys/deserno/pdf/sphere_equi.pdf . Explanations in code added by me.
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
                    
                    electron_coordinate=self.spherical_to_cartesian(pol_ang, azim_ang,inner_radius) #Converts the recieved spherical coordinates to cartesian so Manim can easily handle them.
                    electron_coordinate_list.append(electron_coordinate) #Add this coordinate to the electron_coordinate_list
            
                    print("Got coordinates: ",electron_coordinate) #Print the coordinate recieved.
            print(len(electron_coordinate_list)," points generated.") #Print the amount of electrons will exist. Comment these two lines out if you don't need the data.
            
            return electron_coordinate_list 
        
        electronlist=[] #This holds the electrons.
        electron_count=100 #Change this to change the amount of electrons.
        
        # The following code generates random electron postions, but only if used in conjucntion with get_random_electron_coordinates().
        # Uncomment them both, and comment out the for-loop immediately above this to enable randomization
        # for i in range(0,electron_count):
        #     electron=self.get_surface(Sphere(radius=0.08),shade_color=YELLOW,opacity=1)
        #     electron_position=get_random_electron_coordinates(1)
        #     electron.move_to(electron_position)
        #     electronlist.append(electron)
        
        
        for electron_coordinate in get_electron_coordinates_list(1,electron_count): #for each electron coordinate in get_electron_coordinates where the radius of the inner circle is 1 and electron_count electrons are needed:
            electron=self.get_surface(Sphere(radius=0.08),shade_color=YELLOW,opacity=1)
            electron.move_to(electron_coordinate)
            electronlist.append(electron)


        positivecloud = self.get_surface(surface = self.get_sphere(radius=2),shade_color=DARK_BLUE)
        positivecloud.set_stroke(width=0)
        axes = self.get_axes()
        
        atom=VGroup(*electronlist,positivecloud)
        atomaxes=VGroup(atom,axes)
        self.add(atomaxes)

    def construct(self):
        self.Make_Atom()
        
        self.move_camera(
            **self.default_angled_camera_position,
            run_time=2,
        )
        self.begin_ambient_camera_rotation()
        self.wait(8)