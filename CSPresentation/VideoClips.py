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
        self.clear()
    
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
        
        SoWhatIsIt=Text("So what is it?",font="Geneva").move_to(QualitiesTable[0].get_center())
        
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

        self.clear()


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
        self.play(Uncreate(HowDoWebsitesTrack))

        self.clear()
    
    def IPTracking(self):
        
        Tracking=Text("Tracking",font="Geneva",color=REP_GREEN).to_edge(UP)
        self.add(Tracking)


        IPAddressTracing=Text("IP Address Tracing",font="Geneva").next_to(Tracking,DOWN)
        IPDef1=Text("Your IP Address is essentially the",font="Geneva")
        IPDef2=Text("address of your computer on the Internet.",font="Geneva").next_to(IPDef1,DOWN)
        IPDef=VGroup(IPDef1,IPDef2).scale(0.5).next_to(IPAddressTracing,DOWN)

        IPsLinked1=Text("Your local IP address is linked to that of",font="Geneva",color=DARK_GRAY)
        IPsLinked2=Text("other devices on the same local network.",font="Geneva",color=DARK_GRAY).next_to(IPsLinked1,DOWN)
        IPsLinked=VGroup(IPsLinked1,IPsLinked2).move_to(IPDef.get_center())
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
        
        class GlobalIPUpdaters():
            def Updater1(self):
                IP1.set_value(np.random.randint(100,223))

            def Updater2(self):
                IP2.set_value(np.random.randint(100,255))

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
        OthersCanAttack=VGroup(OthersCanAttack1,OthersCanAttack2).scale(0.5).move_to(IPsLinked.get_center())

        self.play(ReplacementTransform(IPsLinked,OthersCanAttack))

        self.play(Tools.wait_while_updating(2))

        self.play(FadeOutAndShiftDown(IP),Uncreate(IP4Brace),Uncreate(YourIP),Uncreate(YourSharedSubnet),Uncreate(RestOfIPBrace),Uncreate(OthersCanAttack))

        self.wait(1)

        IP1.clear_updaters()
        IP2.clear_updaters()
        IP3.clear_updaters()
        IP4.clear_updaters()

        self.remove(IP,IP4Brace,YourIP,YourSharedSubnet,RestOfIPBrace,OthersCanAttack) #Mandatory cleanup. ;)

        IP1.add_updater(GlobalIPUpdaters.Updater1)
        IP2.add_updater(GlobalIPUpdaters.Updater2)
        IP3.add_updater(GlobalIPUpdaters.Updater3)
        IP4.add_updater(GlobalIPUpdaters.Updater4)
        IP.set_color(WHITE)

        IP4Brace=Brace(IP4,DOWN,color=BLUE)
        RouterPart=Text("for your router",font="Geneva",color=BLUE).next_to(IP4Brace,DOWN).scale(0.3)
        
        RestOfIPBrace=Brace(VGroup(IP1,IP2,IP3),UP,color=REP_GREEN)

        ISPSpecific=Text("from ISP, for everyone",font="Geneva",color=REP_GREEN).scale(0.3).next_to(RestOfIPBrace,UP)

        FromGlobalIP=Text("From your Global IP address,",font="Geneva")
        CanGetLocation=Text("a website can get your rough physical location.",font="Geneva",color=RED).next_to(FromGlobalIP,DOWN)

        LocationFromIP=VGroup(FromGlobalIP,CanGetLocation).scale(0.5).next_to(IPAddressTracing,DOWN)
        
        
        
        
        self.play(Write(LocationFromIP),run_time=2)

        self.play(FadeInFromDown(IP))
        self.play(FadeInFromDown(VGroup(IP4Brace,RouterPart)),FadeToColor(IP4,BLUE))

        self.play(Tools.wait_while_updating(1))

        self.play(Write(VGroup(RestOfIPBrace,ISPSpecific)),FadeToColor(VGroup(IP1,IPSep1,IP2,IPSep2,IP3,IPSep3),REP_GREEN))

        self.play(Tools.wait_while_updating(0.5))


        WorldMap=ImageMobject("/Users/aathishs/Desktop/WorldMap.png").scale(2).shift(2.5*RIGHT+1.8*DOWN)
        TracerDot=SmallDot(color=RED).move_to(WorldMap.get_center())
        self.play(VGroup(IP,IP4Brace,RouterPart,RestOfIPBrace,ISPSpecific).shift,3*LEFT)
        
        self.play(FadeInFromDown(WorldMap))
        self.play(FadeIn(TracerDot))

        self.play(ApplyMethod(
                TracerDot.shift, (RIGHT*1.23),
                path_func = path_along_arc(-TAU/2)
            ))

        self.play(Tools.wait_while_updating(2))
        
        self.play(Uncreate(TracerDot))
        
        self.play(FadeOutAndShiftDown(WorldMap))
        
        self.play(Uncreate(RestOfIPBrace),
        Uncreate(ISPSpecific),
        Uncreate(IP4Brace),
        Uncreate(RouterPart),
        Uncreate(IP)
        )

        self.play(Uncreate(LocationFromIP))


        CookieTracking=Text("Cookies and Scripts",font="Geneva").next_to(Tracking,DOWN)
        DummyCookie=Text("Cookies and Cream",font="Geneva").next_to(Tracking,DOWN)
        
        self.play(ReplacementTransform(IPAddressTracing,DummyCookie))
        self.wait(0.5)
        self.play(ReplacementTransform(DummyCookie,CookieTracking))
        self.wait(1)

        self.clear()

    def CookiesAndScripts(self):
        Tracking=Text("Tracking",font="Geneva",color=REP_GREEN).to_edge(UP)
        self.add(Tracking)

        CookieTracking=Text("Cookies and Scripts",font="Geneva").next_to(Tracking,DOWN)
        self.add(CookieTracking)

        CookieDef1=Text("A cookie is a small text file on your computer that stores",font="Geneva").next_to(CookieTracking,DOWN)
        CookieDef2=Text("some data about your behaviour online and/or on a website.",font="Geneva").next_to(CookieDef1,DOWN)

        CookieDef=VGroup(CookieDef1,CookieDef2).scale(0.4)

        self.play(Write(CookieDef),run_time=2)

        self.wait(1)

        CookiesGood=Text("Cookies are really useful to keep your preferences on a website.",font="Geneva").scale(0.4)

        CookiesBad=Text("But they can also be used by cybercriminals to get personal info.",font="Geneva",color=RED).scale(0.4)

        self.play(ReplacementTransform(CookieDef,CookiesGood))
        self.wait(2)
        self.play(ReplacementTransform(CookiesGood,CookiesBad))

        self.wait(2)

        CookiesDict={
            Text("Cookie Types:",font="Geneva",color=REP_GREEN):[Text("First Party",color=BLUE,font="Geneva"),Text("Third party",font="Geneva",color=RED),Text("SuperCookies",font="Geneva",color=PURPLE)]
        }

        CookiesTable=Table.get_table(CookiesDict).scale(0.5)

        CookiesTable.move_to(ORIGIN)
        CookiesTable.shift(DOWN)

        self.play(ReplacementTransform(CookiesBad,CookiesTable))

        self.wait(2)

        FirstParty=CookiesTable[1].deepcopy()

        self.add(FirstParty)

        

        self.play(
        FadeOut(CookiesTable),
        FirstParty.set_color,REP_GREEN,
        FirstParty.scale,1.5,
        FirstParty.next_to,CookieTracking,DOWN
        )

        FirstPartyDef1=Text("These are cookies that the websites you visit",font="Geneva").next_to(FirstParty,DOWN)
        FirstPartyDef2=Text("use to store your login details and preferences.",font="Geneva").next_to(FirstPartyDef1,DOWN)

        FirstPartyDef=VGroup(FirstPartyDef1,FirstPartyDef2).scale(0.5)

        self.play(Write(FirstPartyDef),run_time=2)

        self.wait(1.5)

        self.play(Uncreate(FirstPartyDef))

        ThirdParty=Text("Third party",font="Geneva",color=RED).scale(0.75).move_to(FirstParty.get_center())
        
        self.play(ReplacementTransform(FirstParty,ThirdParty))

        ThirdPartyDef1=Text("These are cookies that websites use to",font="Geneva").next_to(ThirdParty,DOWN)
        ThirdPartyDef2=Text("record your web activity.",font="Geneva",color=RED).next_to(ThirdPartyDef1,DOWN)

        ThirdPartyDef=VGroup(ThirdPartyDef1,ThirdPartyDef2).scale(0.5)

        self.play(Write(ThirdPartyDef))

        UsetoAdvert1=Text("They can use this info to annoyingly advertise",font="Geneva",color=RED) 
        
        UsetoAdvert2=Text("products that may interest you.",font="Geneva",color=RED).next_to(UsetoAdvert1,DOWN)

        UsetoAdvert=VGroup(UsetoAdvert1,UsetoAdvert2).next_to(ThirdParty,DOWN).scale(0.5)
        
        self.play(ReplacementTransform(ThirdPartyDef,UsetoAdvert))

        self.wait(1)

        self.play(Uncreate(UsetoAdvert))

        SuperCookies=Text("SuperCookies",font="Geneva",color=PURPLE).scale(0.75).move_to(ThirdParty.get_center())

        self.play(ReplacementTransform(ThirdParty,SuperCookies))

        LikeNormalCookies=Text("These are very similar to normal cookies.",font="Geneva").scale(0.5).next_to(SuperCookies,DOWN)

        CanRepairSelves=Text("But, they can repair themselves if deleted.",font="Geneva",color=RED).scale(0.5).move_to(LikeNormalCookies.get_center())

        UsedforBoth=Text("They can be used for both bad and good.",font="Geneva").scale(0.5).move_to(CanRepairSelves.get_center())

        MustBeCareful=Text("So it is best to constantly be aware of them.",font="Geneva",color=BLUE_E).scale(0.5).move_to(UsedforBoth.get_center())

        self.play(Write(LikeNormalCookies))
        self.wait(2)
        self.play(ReplacementTransform(LikeNormalCookies,CanRepairSelves))
        self.wait(2)
        self.play(ReplacementTransform(CanRepairSelves,UsedforBoth))
        self.wait(2)
        self.play(ReplacementTransform(UsedforBoth,MustBeCareful))
        self.wait(2)

        self.play(Uncreate(MustBeCareful),Uncreate(SuperCookies))
        HTTPReferrer=Text("HTTP Referrers",font="Geneva").next_to(Tracking,DOWN)

        self.play(ReplacementTransform(CookieTracking, HTTPReferrer))

        
        self.clear()

    def HTTPReferrers(self):
        Tracking=Text("Tracking",font="Geneva",color=REP_GREEN).to_edge(UP)
        self.add(Tracking)

        HTTPReferrer=Text("HTTP Referrers",font="Geneva").next_to(Tracking,DOWN)
        self.add(HTTPReferrer)

        ReallySimple=Text("These are really simple.",font="Geneva").next_to(HTTPReferrer,DOWN).scale(0.5)

        TellNextPage1=Text("Essentially, when you click a link to another page,",font="Geneva").next_to(HTTPReferrer,DOWN)
        TellNextPage2=Text("the page you were on, tells the new page about you.",font="Geneva").next_to(TellNextPage1,DOWN)
        TellNextPage=VGroup(TellNextPage1,TellNextPage2).scale(0.5)

        self.play(Write(ReallySimple))

        self.wait(2)
        self.play(ReplacementTransform(ReallySimple,TellNextPage))

        Page1=ImageMobject("/Users/aathishs/Desktop/WebsiteIcon1.png").next_to(TellNextPage,DOWN*2).shift(LEFT*3)
        Page2=ImageMobject("/Users/aathishs/Desktop/WebsiteIcon2.png").next_to(TellNextPage,DOWN*2).shift(RIGHT*3)
        self.play(FadeIn(Page1),FadeIn(Page2))

        HeyHeWants=Text("Hey, this guy wants to see you.",font="American Typewriter",color=LIGHT_GREY).scale(0.375).next_to(Page1,UP*0.3)
        HisIPIs=Text("His IP is 74.125.24.101",font="American Typewriter",color=LIGHT_GREY).next_to(Page1,DOWN).scale(0.375)

        Cool=Text("Cool. Thanks!",font="Baskerville",color=LIGHT_GREY).scale(0.5).next_to(Page2,DOWN)

        self.play(Write(HeyHeWants))
        self.play(Write(HisIPIs))
        self.play(Write(Cool))

        self.wait(1)
        self.play(FadeOut(HeyHeWants),FadeOut(HisIPIs),FadeOut(Cool))
        self.play(FadeOut(Page1),FadeOut(Page2))
        self.play(Uncreate(TellNextPage))

        UserAgent=Text("User Agents",font="Geneva").next_to(Tracking,DOWN)

        self.play(ReplacementTransform(HTTPReferrer,UserAgent))

        self.wait(1)

        self.clear()
        
    def UserAgents(self):
        Tracking=Text("Tracking",font="Geneva",color=REP_GREEN).to_edge(UP)
        self.add(Tracking)

        UserAgent=Text("User Agents",font="Geneva").next_to(Tracking,DOWN)
        self.add(UserAgent)
        QuiteSimple=Text("This one is quite simple.",font="Geneva").scale(0.5).next_to(UserAgent,DOWN)
        
        UADef1=Text("A 'User Agent' is sent by your browser to the",font="Geneva").next_to(UserAgent,DOWN)
        UADef2=Text("sites you visit with info on your OS and browser.",font="Geneva").next_to(UADef1,DOWN)
        UADef=VGroup(UADef1,UADef2).scale(0.5)

        self.play(Write(QuiteSimple))
        self.play(ReplacementTransform(QuiteSimple,UADef))

        self.wait(2)
        
        self.play(Uncreate(UADef))


        HowToCircumvent=Text("So how do you circumvent all this stalking?",font="Geneva").scale(0.6).next_to(UserAgent,DOWN)
        
        self.play(ReplacementTransform(UserAgent,HowToCircumvent))
        self.wait(3)
        PrivateBrowsing=Text("Private Browsing",font="Geneva",color=REP_GREEN).scale(1.3).to_edge(UP)

        self.play(ReplacementTransform(Tracking,PrivateBrowsing),Uncreate(HowToCircumvent))

        self.clear()
    
    def construct(self):
        self.LeadIntoTracking()
        self.IPTracking()
        self.CookiesAndScripts()
        self.HTTPReferrers()
        self.UserAgents()

