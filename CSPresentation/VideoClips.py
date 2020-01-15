from manimlib.imports import *
from sanim.anim_tools.tables import *
class Tools():
    def wait_while_updating(duration=1):
        return Animation(Mobject(), run_time=duration)
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

        WikipediaLogo=ImageMobject("/Users/aathishs/Desktop/WikipediaLogo.png").scale(1)
        CommApps=ImageMobject("/Users/aathishs/Desktop/CommApps.png").scale(0.5)
        Ecomm=ImageMobject("/Users/aathishs/Desktop/Ecommerce.jpg").scale(0.75)
        
        WikipediaLogo.move_to(SpinningGlobe.get_center()+2*RIGHT+UP)
        CommApps.move_to(SpinningGlobe.get_center()+2*LEFT+UP)
        Ecomm.move_to(SpinningGlobe.get_center()+2*DOWN)
        BeforeCyberSafety=Group(WikipediaLogo,CommApps,Ecomm,InternetIsEverywhere,SpinningGlobe)
        self.play(GrowFromPoint(WikipediaLogo,SpinningGlobe.get_center()))
        self.wait(1)
        self.play(GrowFromPoint(CommApps,SpinningGlobe.get_center()))
        self.wait(1)
        self.play(GrowFromPoint(Ecomm,SpinningGlobe.get_center()))
        self.wait(1)
        
        self.play(ShrinkToCenter(BeforeCyberSafety),run_time=1.5)
        self.remove(BeforeCyberSafety)
        self.wait(0.5)
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

        MainQualities=Text("Cybersafety is the practice of utilising the internet:",font="Geneva")
        
        Qualities={
            MainQualities:[Text("Safely",font="Geneva"),Text("Responsibly",font="Geneva"),Text("Securely",font="Geneva")]
        }
        
        QualitiesTable=Table.get_table(Qualities).scale(0.5)
        QualitiesTable.move_to((0,-1,0))
        
        SoWhatIsIt=Text("So what is it?",font=Geneva).move_to(QualitiesTable[0].get_center())
        
        self.play(Write(SoWhatIsIt))
        self.wait(0.5)

        self.play(ReplacementTransform(SoWhatIsIt,QualitiesTable[0]))
        self.play(Write(QualitiesTable[4]))
        self.wait(0.5)
        self.play(Write(QualitiesTable[1]))
        self.wait(0.5)
        self.play(Write(QualitiesTable[2]))
        self.wait(0.5)
        self.play(Write(QualitiesTable[3]))
        
        self.wait(1)
        Everything=Group(CYBERSAFETY,QualitiesTable,MainQualities,SoWhatIsIt)
        self.play(ShrinkToCenter(Everything))
        self.remove(Everything)
        self.wait(1)
        
        NetsMostPrevalent=Text("Let's talk about securing the net's most prevalent use...",font="Geneva").scale(0.5)
        
        self.play(Write(NetsMostPrevalent))
        self.wait(1)
        self.play(ReplacementTransform(NetsMostPrevalent,Text("Web Browsing",font="Geneva").scale(2)))

        self.remove(NetsMostPrevalent)


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
        PointsToNote=Text("Points To Be Covered:",font="Geneva",color=REP_GREEN).scale(1.5)
        PointsDict={
            PointsToNote:[Text("Anonymity",font="Geneva"),Text("Tracking",font="Geneva"),Text("Privacy",font="Geneva"),Text("Cybercrime",font="Geneva")]
        }

        PointsTable=Table.get_table(PointsDict).scale(0.5)
        PointsTable.move_to((0,-1,0))
        self.play(Write(PointsTable[0]),Write(PointsTable[5]))
        self.wait(0.5)
        self.play(Write(PointsTable[1]))
        self.wait(0.5)
        self.play(Write(PointsTable[2]))
        self.wait(0.5)
        self.play(Write(PointsTable[3]))
        self.wait(0.5)
        self.play(Write(PointsTable[4]))
        self.wait(0.5)
        
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


        Why=Text("Why be anonymous?",font="Geneva")
        self.play(Write(Why))
        self.play(Why.scale,0.5)
        self.play(Why.to_edge,LEFT,
        Why.shift,2*UP)
        self.wait(1)
        IDTheft=Text("Identity Theft",font="Impact").scale(1.5)
        IDTDetails={
            IDTheft:[Text("Fraud",color=RED,font="Arial Black"),Text("Impersonation",color=RED,font="Arial Black"),Text("Steal Private Info",color=RED,font="Arial Black")]
        }

        IDTheftTable=Table.get_table(IDTDetails)

        IDTheftTable.scale(0.5)
        IDTheftTable.move_to((0,-1,0))

        self.play(Write(IDTheftTable[0]))
        self.wait(0.5)
        self.play(Transform((IDTheftTable[0]),Text("What is it?",font="Geneva")),rate_func=there_and_back_with_pause,run_time=3)

        self.play(Write(IDTheftTable[1]))
        self.wait(0.5)
        self.play(Write(IDTheftTable[2]))
        self.wait(0.5)
        self.play(Write(IDTheftTable[3]))
        self.wait(0.5)
        self.play(Write(IDTheftTable[4]))

        NotSolution=Group(IDTheftTable,Why,IDTheft)
        
        HowToPrevent=Text("So, how do we prevent this?",color=BLUE,font="Geneva").scale(0.5)
        
        self.play(FadeOut(NotSolution))
        self.play(FadeIn(HowToPrevent))
        self.remove(NotSolution)
        self.play(HowToPrevent.shift,UP*2)

        PrivateBrowsing=Text("Private Browsing",font="Geneva",color=GREY)

        self.play(Write(PrivateBrowsing))
        self.play(Uncreate(HowToPrevent))
        self.remove(HowToPrevent)

        self.play(PrivateBrowsing.shift,2*UP)
        self.wait(1.5)
        HowDoWebsitesTrack=Text("How do Websites Track You?",font="Geneva",color=GREY).scale(0.75)
        HowDoWebsitesTrack.move_to(PrivateBrowsing.get_center())
        self.play(ReplacementTransform(PrivateBrowsing,HowDoWebsitesTrack))


        Tracking=Text("Tracking",font="Geneva",color=REP_GREEN)
        Tracking.to_edge(UP)
        self.play(ReplacementTransform(VGroup(Anonymity,AnonyMask),Tracking))

        self.remove(Tracking,HowDoWebsitesTrack,Anonymity,AnonyMask)
    
    def IPTracking(self):
        
        Tracking=Text("Tracking",font="Geneva",color=REP_GREEN)
        Tracking.to_edge(UP)
        self.add(Tracking)

        HowDoWebsitesTrack=Text("How do Websites Track You?",font="Geneva",color=GREY).scale(0.75)
        HowDoWebsitesTrack.move_to((0,2,0))
        self.add(HowDoWebsitesTrack)


        IPAddressTracing=Text("IP Address Tracing",font="Geneva").next_to(HowDoWebsitesTrack,DOWN)
        IPDef1=Text("Your IP Address is essentially the",font="Geneva")
        IPDef2=Text("address of your computer on the Internet.",font="Geneva").next_to(IPDef1,DOWN)
        IPDef=VGroup(IPDef1,IPDef2).scale(0.5)

        IPsLinked1=Text("Your local IP address is linked to that of",font="Geneva",color=DARK_GRAY)
        IPsLinked2=Text("other devices on the same local network.",font="Geneva",color=DARK_GRAY).next_to(IPsLinked1,DOWN)
        IPsLinked=VGroup(IPsLinked1,IPsLinked2)
        IPsLinked.scale(0.5)
        
        class LocalIPUpdaters():
            def Updater1(self):
                IP1.set_value(192)

            def Updater2(self):
                IP2.set_value(168)

            def Updater3(self):
                IP3.set_value(np.random.randint(100,255))

            def Updater4(self):
                IP4.set_value(np.random.randint(100,255))

        IP1=Integer()
        IP2=Integer()
        IP2.move_to(IP1.get_center()+((IP1.get_width()/2)+IP2.get_width()/2,0,0)+RIGHT/1.25)
        IP3=Integer()
        IP3.move_to(IP2.get_center()+((IP2.get_width()/2)+IP3.get_width()/2,0,0)+RIGHT/1.25)
        IP4=Integer()
        IP4.move_to(IP3.get_center()+((IP3.get_width()/2)+IP4.get_width()/2,0,0)+RIGHT/1.25)
        
        IPNums=VGroup(IP1,IP2,IP3,IP4).next_to(IPDef,DOWN)

        IP1.add_updater(LocalIPUpdaters.Updater1)
        IP2.add_updater(LocalIPUpdaters.Updater2)
        IP3.add_updater(LocalIPUpdaters.Updater3)
        IP4.add_updater(LocalIPUpdaters.Updater4)
        IPSep1=SmallDot(color=WHITE).move_to(IP1.get_center()+((IP1.get_width()/2)+0.1,-(IP1.get_height()/2)+0.05,0))
        IPSep2=SmallDot(color=WHITE).move_to(IP2.get_center()+((IP2.get_width()/2)+0.1,-(IP2.get_height()/2)+0.05,0))
        IPSep3=SmallDot(color=WHITE).move_to(IP3.get_center()+((IP3.get_width()/2)+0.1,-(IP3.get_height()/2)+0.05,0))

        IP=VGroup(IPNums,IPSep1,IPSep2,IPSep3)
        IP.shift(DOWN)
        self.play(Write(IPAddressTracing))
        self.play(Write(IPDef),run_time=2)
        
        self.wait(1.5)
        
        self.play(ReplacementTransform(IPDef,IPsLinked))
        
        self.play(Write(IP))
        

        self.play(Tools.wait_while_updating(1))
        
        IP4Brace=Brace(IP4,DOWN,color=BLUE)
        
        YourIP=Text("the IP part unique to you",color=BLUE,font="Geneva").scale(0.3).next_to(IP4Brace,DOWN)
        
        self.play(Tools.wait_while_updating(1))
        
        IP4.clear_updaters()
        self.play(Write(YourIP),FadeToColor(IP4,BLUE),ShowCreation(IP4Brace))
        self.play(Tools.wait_while_updating(1))

        RestOfIPBrace=Brace(VGroup(IP1,IP2,IP3,IPSep1,IPSep2,IPSep3),UP,color=REP_GREEN)
        YourSharedSubnet=Text("your local network",font="Geneva",color=REP_GREEN).scale(0.3).next_to(RestOfIPBrace,UP)
        
        self.play(FadeToColor(VGroup(IP1,IP2,IP3,IPSep1,IPSep2,IPSep3),REP_GREEN),
        ShowCreation(RestOfIPBrace),
        Write(YourSharedSubnet)
        )
        self.play(Tools.wait_while_updating(2))
        OthersCanAttack1=Text("Others on the same (local) network",font="Geneva",color=RED)
        OthersCanAttack2=Text("could attack you.",font="Geneva",color=RED).next_to(OthersCanAttack1,DOWN)
        OthersCanAttack=VGroup(OthersCanAttack1,OthersCanAttack2).scale(0.5)

        self.play(ReplacementTransform(IPsLinked,OthersCanAttack))

        self.play(Tools.wait_while_updating(2))

        self.play(Uncreate(IP),Uncreate(IP4Brace),Uncreate(YourIP),Uncreate(YourSharedSubnet),Uncreate(RestOfIPBrace),Uncreate(OthersCanAttack))

        self.wait(1)

        self.remove(IP,IP4Brace,YourIP,YourSharedSubnet,RestOfIPBrace,OthersCanAttack)

        
    def construct(self):
        self.LeadIntoTracking()
        self.IPTracking()

