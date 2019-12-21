from manimlib.imports import *

class Tools():
    def spherical_to_cartesian(pol_ang,azim_ang,radius): #This function converts given spherical coordinates (theta, phi and radius) to cartesian coordinates.
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

class RutherfordsModel(SpecialThreeDScene):
    def construct(self):
        
        nucleus= Sphere(color = BLUE,radius=0.08,).center()

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
        atomaxes=VGroup(atom,axes)
        self.add(atomaxes)

    def construct(self):
        self.Make_Atom()
        
        self.move_camera(
            **self.default_angled_camera_position,
            run_time=2,
        )
        self.begin_ambient_camera_rotation(0.15)
        self.wait(8)

# class SceneTransform(Scene):
    