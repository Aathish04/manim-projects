from manimlib.imports import *
from sanim.anim_tools.tables import *
class Tools():
    def spherical_to_cartesian(pol_ang,azim_ang,radius=1): #This function converts given spherical coordinates (theta, phi and radius) to cartesian coordinates.
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

class Intro(SpecialThreeDScene):
    def InternetNow(self):
        InternetIs=Text("The Internet is",color=WHITE,font="Impact")
        Everywhere=Text("EVERYWHERE!",color=REP_GREEN,font="Impact").next_to(InternetIs,DOWN)
        InternetIsEverywhere=VGroup(InternetIs,Everywhere)
        CYBERSAFETY=Text("CYBERSAFETY",color=REP_GREEN,font="Geneva")
        CYBERSAFETY.scale(2)
        self.play(Write(InternetIsEverywhere))
        self.play(
            InternetIsEverywhere.scale,0.75,
            InternetIsEverywhere.to_edge,UP
        )

        SpinningGlobe=Tools.get_surface(Sphere(),shade_color=WHITE,opacity=1)
        SpinningGlobe.set_stroke(BLUE,width=5)
        SpinningGlobe.rotate(about_point=SpinningGlobe.get_center(),axis=X_AXIS,angle=90*DEGREES)

        self.play(ShowCreation(SpinningGlobe))
        
        always_rotate(SpinningGlobe,about_point=SpinningGlobe.get_center(),axis=-Y_AXIS)
        
        self.wait(1)

        EmailLogo=ImageMobject("/Users/aathishs/Desktop/EmailLogo.png").scale(0.75)
        CommApps=ImageMobject("/Users/aathishs/Desktop/CommApps.png").scale(0.5)
        Ecomm=ImageMobject("/Users/aathishs/Desktop/Ecommerce.jpg").scale(0.75)
        
        EmailLogo.move_to(SpinningGlobe.get_center()+2*RIGHT+UP)
        CommApps.move_to(SpinningGlobe.get_center()+2*LEFT+UP)
        Ecomm.move_to(SpinningGlobe.get_center()+2*DOWN)
        BeforeCyberSafety=Group(EmailLogo,CommApps,Ecomm,InternetIsEverywhere,SpinningGlobe)
        self.play(GrowFromPoint(EmailLogo,SpinningGlobe.get_center()))
        self.play(GrowFromPoint(CommApps,SpinningGlobe.get_center()))
        self.play(GrowFromPoint(Ecomm,SpinningGlobe.get_center()))
        
        self.play(ShrinkToCenter(BeforeCyberSafety))
        self.remove(BeforeCyberSafety)
        self.play(Write(CYBERSAFETY))
        
        self.wait(2)
    
    def construct(self):
        self.InternetNow()

class WhatIsCyberSafety(Scene):
    def Define(self):

        CYBERSAFETY=Text("CYBERSAFETY",color=REP_GREEN,font="Geneva")
        CYBERSAFETY.scale(2)
        self.add(CYBERSAFETY)
        self.play(CYBERSAFETY.to_edge,UP)

        SoWhatIsIt=Text("So what is it?")

        Qualities={
            SoWhatIsIt:[Text("Safe Usage",font="Geneva"),Text("Responsible Usage",font="Geneva"),Text("Ensure Security",font="Geneva")]
        }
        QualitiesTable=Table.get_table(Qualities).scale(0.5)
        QualitiesTable.move_to((0,-1,0))

        self.play(Write(QualitiesTable[0]))
        self.play(Write(QualitiesTable[4]))
        self.wait(0.5)
        self.play(Write(QualitiesTable[1]))
        self.wait(0.5)
        self.play(Write(QualitiesTable[2]))
        self.wait(0.5)
        self.play(Write(QualitiesTable[3]))
        
        self.wait(1)
        Everything=Group(CYBERSAFETY,QualitiesTable)
        self.play(ShrinkToCenter(Everything))

        self.play(Write(Text("Web Browsing",font="Geneva").scale(2)))

    def construct(self):
        self.Define()

class WebBrowsing(Scene):
    def LeadIntoTracking(self):
        WebBrowsing=Text("Web Browsing",font="Geneva").scale(2)
        self.add(WebBrowsing)

        self.play(
            WebBrowsing.scale,0.75,
            WebBrowsing.to_edge,UP
        )
        PointsToNote=Text("Points To Note:",font="Geneva",color=REP_GREEN).scale(1.5)
        PointsDict={
            PointsToNote:[Text("Anonymity",font="Geneva"),Text("Tracking",font="Geneva"),Text("Privacy",font="Geneva"),Text("Cybercrime",font="Geneva")]
        }

        PointsTable=Table.get_table(PointsDict).scale(0.5)
        PointsTable.move_to((0,-1,0))
        self.play(Write(PointsTable[0]),Write(PointsTable[5]))
        self.wait(0.5)
        self.play(Write(PointsTable[1]))
        self.wait(0.25)
        self.play(Write(PointsTable[2]))
        self.wait(0.25)
        self.play(Write(PointsTable[3]))
        self.wait(0.25)
        self.play(Write(PointsTable[4]))
        self.wait(0.25)
        
        Anonymity=PointsTable[1].deepcopy()
        self.add(Anonymity)

        self.play(FadeOut(WebBrowsing),FadeOut(PointsTable))
        self.remove(WebBrowsing,PointsTable)


        self.play(
        Anonymity.set_color,REP_GREEN,
        Anonymity.scale,1.5,
        Anonymity.to_edge,UP,
        )
        AnonyMask=SVGMobject("/Users/aathishs/Desktop/Mask.svg").next_to(Anonymity).scale(0.7)
        self.play(ShowCreation(AnonyMask))

        self.wait(1)


        Why=Text("Why be anonymous?")
        self.play(Write(Why))
        self.play(Why.scale,0.5)
        self.play(Why.to_edge,LEFT,
        Why.shift,2*UP)

        IDTheft=Text("Identity Theft",font="Impact").scale(1.5)
        IDTDetails={
            IDTheft:[Text("Fraud",color=RED,font="Arial Black"),Text("Impersonation",color=RED,font="Arial Black"),Text("Steal Private Info",color=RED,font="Arial Black")]
        }

        IDTheftTable=Table.get_table(IDTDetails)

        IDTheftTable.scale(0.5)
        IDTheftTable.move_to((0,-1,0))

        self.play(Write(IDTheftTable[0]))

        self.play(Write(IDTheftTable[1]))
        self.play(Write(IDTheftTable[2]))
        self.play(Write(IDTheftTable[3]))
        self.play(Write(IDTheftTable[4]))

        NotSolution=Group(IDTheftTable,Why,IDTheft)
        
        HowToPrevent=Text("So, how do we prevent this?",color=BLUE,font="Geneva").scale(0.5)
        
        self.play(FadeOut(NotSolution))
        self.play(FadeIn(HowToPrevent))
        self.remove(NotSolution)
        self.play(HowToPrevent.shift,UP*2)

        PrivateBrowsing=Text("Private Browsing",color=GREY)

        self.play(Write(PrivateBrowsing))
        self.play(Uncreate(HowToPrevent))
        self.remove(HowToPrevent)

        self.play(PrivateBrowsing.shift,2*UP)
        
        HowDoWebsitesTrack=Text("How do Websites Track You?",font="Geneva",color=GREY).scale(0.75)
        HowDoWebsitesTrack.move_to(PrivateBrowsing.get_center())
        self.play(ReplacementTransform(PrivateBrowsing,HowDoWebsitesTrack))


        Tracking=Text("Tracking",color=REP_GREEN)
        Tracking.to_edge(UP)
        self.play(ReplacementTransform(VGroup(Anonymity,AnonyMask),Tracking))

        self.remove(VGroup(HowDoWebsitesTrack,Anonymity,AnonyMask,Tracking))
    
    def Tracking(self):
        HowDoWebsitesTrack=Text("How do Websites Track You?",font="Geneva",color=GREY).scale(0.75)
        HowDoWebsitesTrack.move_to((0,2,0))
        self.add(HowDoWebsitesTrack)
        Tracking=Text("Tracking",color=REP_GREEN)
        Tracking.to_edge(UP)
        self.add(Tracking)


        IPAddressHeading=Text("IP Address Tracing").next_to(HowDoWebsitesTrack,DOWN)
        WhatIsIP1=Text("Your IP Address is essentially the")
        WhatIsIP2=Text("address of your computer on the Internet.").next_to(WhatIsIP1,DOWN)
        WhatIsIP=VGroup(WhatIsIP1,WhatIsIP2).scale(0.5)

        IPsLinked=Text("Your IP address is linked to that of other devices on the same network.",color=DARK_GRAY)
        IPsLinked.scale(0.4)
        IPsGeo=Text("Your IP can be used to get your rough location.",color=DARK_GRAY).next_to(IPsLinked,DOWN)
        IPsGeo.scale(0.5)

        
        self.play(Write(IPAddressHeading))
        self.play(Write(WhatIsIP))
        self.wait(0.5)
        self.play(ReplacementTransform(WhatIsIP,VGroup(IPsLinked,IPsGeo)))
        
        self.wait(1)
    def construct(self):
        self.LeadIntoTracking()
        self.Tracking()

