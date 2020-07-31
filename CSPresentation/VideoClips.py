#This script should run stably on commit af65c9d5d4ecbcffc5e569508053d56d1f7e86eb of the version of manim at 3b1b/manim, master.
# Use commit 46c285e9427fb3e6f240a76e7904f0b056c20814 of Aathish04/Sanim on the manim-3b1b branch.
from manimlib.imports import *
from sanim.anim_tools.tables import *
REP_GREEN="#00C099"
class Tools():
    def wait_while_updating(duration=1):
        return Animation(Mobject(), run_time=duration)

    def get_surface(surface,shade_color,opacity=0.3):
        result = surface.copy()
        result.set_fill(shade_color, opacity=opacity)
        result.set_stroke(WHITE, width=0.5, opacity=opacity)
        return result

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
        self.wait(1.5)
        self.play(GrowFromPoint(CommApps,SpinningGlobe.get_center()))
        self.wait(1.5)
        self.play(GrowFromPoint(Ecomm,SpinningGlobe.get_center()))
        self.wait(2)

        self.play(ShrinkToCenter(BeforeCyberSafety),run_time=1.5)
        self.remove(BeforeCyberSafety)
        self.wait(1)
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

        QualitiesTable=Table(tabledict=Qualities).scale(0.5)
        QualitiesTable.move_to((0,-1,0))

        SoWhatIsIt=Text("So what is it?",font="Geneva").move_to(QualitiesTable[0].get_center())

        self.play(Write(SoWhatIsIt))
        self.wait(1)

        self.play(ReplacementTransform(SoWhatIsIt,QualitiesTable[0]))
        self.play(Write(QualitiesTable[4]))
        self.wait(1)
        self.play(Write(QualitiesTable[1]))
        self.wait(1)
        self.play(Write(QualitiesTable[2]))
        self.wait(1)
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
            PointsToNote:[Text("Anonymity",font="Geneva"),
            Text("Tracking",font="Geneva"),
            Text("Privacy",font="Geneva"),
            Text("Cybersafety",font="Geneva")]
        }

        PointsTable=Table(tabledict=PointsDict).scale(0.5)
        PointsTable.move_to((0,-1,0))
        self.play(Write(PointsTable[0]),Write(PointsTable[5]))
        self.wait(1)
        self.play(Write(PointsTable[1]))
        self.wait(1)
        self.play(Write(PointsTable[2]))
        self.wait(1)
        self.play(Write(PointsTable[3]))
        self.wait(1)
        self.play(Write(PointsTable[4]))
        self.wait(1)

        Anonymity=PointsTable[1].deepcopy()
        self.add(Anonymity)
        self.remove(PointsTable[1])

        self.play(FadeOut(WebBrowsing),FadeOut(PointsTable))
        self.remove(WebBrowsing,PointsTable)


        self.play(
        Anonymity.set_color,REP_GREEN,
        Anonymity.scale,1.5,
        Anonymity.to_edge,UP,
        )
        AnonyMask=SVGMobject("/Users/aathishs/Desktop/Mask.svg").next_to(Anonymity).scale(0.6)
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
            IDTheft:[Text("Type of Fraud",color=RED,font="Arial Black"),
            Text("Impersonation",color=RED,font="Arial Black"),
            Text("Stealing Private Info",color=RED,font="Arial Black")]
        }

        IDTheftTable=Table(tabledict=IDTDetails)

        IDTheftTable.scale(0.5)
        IDTheftTable.move_to((0,-1,0))

        self.play(Write(IDTheftTable[0]))
        self.wait(1)
        WhatIsit=Text("What is it?",font="Geneva").move_to(IDTheftTable[0].get_center())
        self.play(Transform((IDTheftTable[0]),WhatIsit),rate_func=there_and_back_with_pause,run_time=3)

        self.play(Write(IDTheftTable[1]))
        self.wait(1)
        self.play(Write(IDTheftTable[2]))
        self.wait(1)
        self.play(Write(IDTheftTable[3]))
        self.wait(1)
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
        self.wait(2)
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

        self.wait(2)

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

        self.play(FadeOutAndShiftDown(IP),
        Uncreate(IP4Brace),
        Uncreate(YourIP),
        Uncreate(YourSharedSubnet),
        Uncreate(RestOfIPBrace),
        Uncreate(OthersCanAttack))

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
        TracerArc=ArcBetweenPoints(TracerDot.get_center(), TracerDot.get_center()+RIGHT*1.23, color=RED,angle=-TAU/2)
        self.play(VGroup(IP,IP4Brace,RouterPart,RestOfIPBrace,ISPSpecific).shift,3*LEFT)

        self.play(FadeInFromDown(WorldMap))
        self.play(FadeIn(TracerDot))

        self.play(

            ApplyMethod(
                TracerDot.shift, (RIGHT*1.23),
                path_func = path_along_arc(-TAU/2)
                ),
                Write(TracerArc)
            )

        self.play(Tools.wait_while_updating(2))

        self.play(Uncreate(TracerDot),Uncreate(TracerArc))

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
        self.wait(1)
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

        self.wait(3)

        CookiesGood=Text("Cookies are really useful to keep your preferences on a website.",font="Geneva").scale(0.4)

        CookiesBad=Text("But they can also be used by cybercriminals to get personal info.",font="Geneva",color=RED).scale(0.4)

        self.play(ReplacementTransform(CookieDef,CookiesGood))
        self.wait(2)
        self.play(ReplacementTransform(CookiesGood,CookiesBad))

        self.wait(2)

        CookiesDict={
            Text("Cookie Types:",font="Geneva",color=REP_GREEN):[Text("First Party",color=BLUE,font="Geneva"),
            Text("Third party",font="Geneva",color=RED),
            Text("SuperCookies",font="Geneva",color=PURPLE)]
        }

        CookiesTable=Table(tabledict=CookiesDict).scale(0.5)

        CookiesTable.move_to(ORIGIN)
        CookiesTable.shift(DOWN)

        self.play(ReplacementTransform(CookiesBad,CookiesTable))

        self.wait(2)

        FirstParty=CookiesTable[1].deepcopy()

        self.add(FirstParty)
        self.remove(CookiesTable[1])

        self.play(FadeOut(CookiesTable))
        self.play(
        FirstParty.set_color,REP_GREEN,
        FirstParty.scale,1.5,
        FirstParty.next_to,CookieTracking,DOWN
        )

        FirstPartyDef1=Text("These are cookies that the websites you visit",font="Geneva").next_to(FirstParty,DOWN)
        FirstPartyDef2=Text("use to store your login details and preferences.",font="Geneva").next_to(FirstPartyDef1,DOWN)

        FirstPartyDef=VGroup(FirstPartyDef1,FirstPartyDef2).scale(0.5)

        self.play(Write(FirstPartyDef),run_time=2)

        self.wait(2)

        self.play(Uncreate(FirstPartyDef))

        ThirdParty=Text("Third party",font="Geneva",color=RED).scale(0.75).move_to(FirstParty.get_center())

        self.play(ReplacementTransform(FirstParty,ThirdParty))

        ThirdPartyDef1=Text("These are cookies that websites use to",font="Geneva").next_to(ThirdParty,DOWN)
        ThirdPartyDef2=Text("record your web activity.",font="Geneva",color=RED).next_to(ThirdPartyDef1,DOWN)

        ThirdPartyDef=VGroup(ThirdPartyDef1,ThirdPartyDef2).scale(0.5)

        self.play(Write(ThirdPartyDef),run_time=2)

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
        PrivateBrowsing=Text("Private and Anonymous Browsing",font="Geneva",color=REP_GREEN).scale(0.85).to_edge(UP)

        self.play(ReplacementTransform(Tracking,PrivateBrowsing),Uncreate(HowToCircumvent))

        self.clear()

    def construct(self):
        self.LeadIntoTracking()
        self.IPTracking()
        self.CookiesAndScripts()
        self.HTTPReferrers()
        self.UserAgents()

class PrivateAndAnonymousBrowsing(Scene):
    def DefinePrivateAnonBrowsing(self):

        PrivateAndAnonBrowsing=Text("Private and Anonymous Browsing",font="Geneva",color=REP_GREEN).scale(0.85).to_edge(UP)
        self.add(PrivateAndAnonBrowsing)
        self.wait(1)

        AnonBrowsing=Text("Anonymous Browsing",font="Geneva",color=REP_GREEN).scale(0.85).to_edge(UP)
        self.play(ReplacementTransform(PrivateAndAnonBrowsing,AnonBrowsing))

        WhatTheyDo1=Text("Anonymous Browsers allow users to view ",font="Geneva").scale(0.5).next_to(PrivateAndAnonBrowsing,DOWN)
        WhatTheyDo2=Text("websites without revealing their information.",font="Geneva").scale(0.5).next_to(WhatTheyDo1,DOWN)
        WhatTheyDo=VGroup(WhatTheyDo1,WhatTheyDo2)

        UsedBy=Text("It's often used by whistleblowers and journalists. ",font="Geneva").scale(0.5).move_to(WhatTheyDo.get_center())

        self.play(Write(WhatTheyDo))
        self.wait(2)
        self.play(ReplacementTransform(WhatTheyDo,UsedBy))
        self.wait(2)

        AnotherType=Text("Another type of browsing is called Private Browsing. ",font="Geneva").scale(0.5).move_to(UsedBy.get_center())
        self.play(ReplacementTransform(UsedBy,AnotherType))

        PrivateBrowsing=Text("Private Browsing",font="Geneva",color=REP_GREEN).scale(0.85).to_edge(UP)

        self.play(ReplacementTransform(AnonBrowsing,PrivateBrowsing))

        PrivDef=Text("Private browsers don't store cookies and browsing history.",font="Geneva").scale(0.5).move_to(AnotherType.get_center())

        PrivTypesDict={
            Text("Some types of private browsing are:",font="Geneva",color=REP_GREEN).scale(1.5):[Text("Incognito Browsing",font="Geneva"),Text("Proxy Based Browsing",font="Geneva"),Text("VPN Based Browsing",font="Geneva")]
            }

        PrivTypesTable=Table(tabledict=PrivTypesDict).scale(0.5)

        PrivTypesTable.move_to(ORIGIN)

        self.play(ReplacementTransform(AnotherType,PrivDef))

        self.wait(2)
        self.play(ReplacementTransform(PrivDef,PrivTypesTable[0]))
        self.play(Write(PrivTypesTable[1:]))

        self.wait(1)

        IncognitoBrowsing=PrivTypesTable[1].deepcopy()

        self.add(IncognitoBrowsing)
        self.remove(PrivTypesTable[1])

        self.play(
        FadeOut(PrivTypesTable),
        IncognitoBrowsing.set_color,LIGHT_GREY,
        IncognitoBrowsing.scale,1.25,
        IncognitoBrowsing.next_to,PrivateBrowsing,DOWN
        )

        DoNotStore=Text("These browsers don't record your activity.",font="Geneva").scale(0.5).next_to(IncognitoBrowsing,DOWN)
        FoundAsSetting=Text("Most modern browsers show this as an option in settings.",font="Geneva").scale(0.5).next_to(DoNotStore,DOWN)
        AlsoUseDuck=Text("There are also some privacy oriented browsers like DuckDuckGo.",font="Geneva").scale(0.4).next_to(FoundAsSetting,DOWN)

        self.play(Write(DoNotStore))
        self.wait(1)
        self.play(Write(FoundAsSetting))
        self.wait(2)
        self.play(Write(AlsoUseDuck))

        DuckLogo=ImageMobject("/Users/aathishs/Desktop/Duckduckgo.png").scale(1.5).shift(DOWN*2)

        self.play(FadeInFromDown(DuckLogo))
        self.wait(1)
        self.play(FadeOutAndShiftDown(DuckLogo))
        self.play(Uncreate(AlsoUseDuck))
        self.play(Uncreate(FoundAsSetting),Uncreate(DoNotStore))
        self.play(ReplacementTransform(IncognitoBrowsing,Text("Proxied Browsing",color=LIGHT_GREY,font="Geneva").scale(0.75).next_to(PrivateBrowsing,DOWN)))
        self.wait(1)
        self.clear()

    def ProxiedBrowsing(self):
        PrivateBrowsing=Text("Private Browsing",font="Geneva",color=REP_GREEN).scale(0.85).to_edge(UP)
        ProxiedBrowsing= Text("Proxied Browsing",color=LIGHT_GREY,font="Geneva").scale(0.75).next_to(PrivateBrowsing,DOWN)

        self.add(PrivateBrowsing)
        self.add(ProxiedBrowsing)

        ProxyDef1=Text("A proxy acts as a mediator between your",font="Geneva").next_to(ProxiedBrowsing,DOWN)
        ProxyDef2=Text("computer and the site you want to visit.",font="Geneva").next_to(ProxyDef1,DOWN)

        ProxyDef=VGroup(ProxyDef1,ProxyDef2).scale(0.5)

        GetsOtherIP=Text("The website you visit only gets info",font="Geneva").next_to(ProxiedBrowsing,DOWN)
        AndNotYours=Text("about the proxy site and not yours!",font="Geneva").next_to(GetsOtherIP,DOWN)
        GetsOtherIPAndNotYours=VGroup(GetsOtherIP,AndNotYours).scale(0.5)

        self.play(Write(ProxyDef),run_time=2)

        self.wait(2)

        self.play(ReplacementTransform(ProxyDef,GetsOtherIPAndNotYours))

        HomePC=ImageMobject("/Users/aathishs/Desktop/HomePC.png")
        ProxyServer=ImageMobject("/Users/aathishs/Desktop/ProxyServer.png")
        Website=ImageMobject("/Users/aathishs/Desktop/WebsiteIcon1.png")

        HomePC.to_edge(DOWN).shift(LEFT*5)
        ProxyServer.to_edge(DOWN)
        Website.to_edge(DOWN).shift(RIGHT*5)

        self.play(FadeInFromDown(HomePC))
        self.play(FadeInFromDown(Website))

        FirstBeginLoc=HomePC.get_center()+(HomePC.get_width()/2+0.1,0,0)
        FirstEndLoc=ProxyServer.get_center()-(ProxyServer.get_width()/2+0.1,0,0)

        FirstArrow=Arrow(start=FirstBeginLoc,end=FirstEndLoc,color=WHITE)

        SecondBeginloc=ProxyServer.get_center()+(ProxyServer.get_width()/2+0.1,0,0)
        SecondEndLoc=Website.get_center()-(Website.get_width()/2+0.1,0,0)

        SecondArrow=Arrow(start=SecondBeginloc,end=SecondEndLoc,color=LIGHT_GREY)

        ThirdArrow=Arrow(start=SecondEndLoc,end=SecondBeginloc,color=LIGHT_GREY)

        FourthArrow=Arrow(start=FirstEndLoc,end=FirstBeginLoc,color=WHITE)

        ZeroethArrow=Arrow(start=FirstBeginLoc,end=SecondEndLoc,color=RED)
        ZeroPointOnethArrow=Arrow(start=SecondEndLoc,end=FirstBeginLoc,color=RED)
        YourInfo=Text("Your Information",font="Geneva",color=RED).scale(0.4).next_to(ZeroethArrow,UP)
        self.play(ShowCreation(ZeroethArrow))
        self.play(Write(YourInfo))
        self.play(Uncreate(ZeroethArrow),Uncreate(YourInfo))
        self.play(ShowCreation(ZeroPointOnethArrow))
        self.wait(1)
        self.play(Uncreate(ZeroPointOnethArrow))


        self.play(FadeIn(ProxyServer))
        YourInfo2=Text("Your Info",font="Geneva",color=BLUE).scale(0.4).next_to(FirstArrow,UP)
        self.play(ShowCreation(FirstArrow))
        self.play(Write(YourInfo2))

        self.play(Uncreate(FirstArrow),Uncreate(YourInfo2))

        ProxyInfo=Text("Proxy's Info",font="Geneva",color=RED).scale(0.4).next_to(SecondArrow,UP)
        self.play(ShowCreation(SecondArrow))
        self.play(Write(ProxyInfo))

        self.play(Uncreate(SecondArrow),Uncreate(ProxyInfo))
        self.play(ShowCreation(ThirdArrow))
        self.play(Uncreate(ThirdArrow))
        self.play(ShowCreation(FourthArrow))
        self.wait(1)

        self.play(Uncreate(FourthArrow))

        self.play(FadeOutAndShiftDown(Website))
        self.play(FadeOut(ProxyServer))
        self.play(FadeOutAndShiftDown(HomePC))

        self.play(Uncreate(GetsOtherIPAndNotYours))

        self.play(ReplacementTransform(ProxiedBrowsing,Text("Virtual Private Networks",color=LIGHT_GREY,font="Geneva").scale(0.75).next_to(PrivateBrowsing,DOWN)))

        self.clear()

    def VPNs(self):
        PrivateBrowsing=Text("Private Browsing",font="Geneva",color=REP_GREEN).scale(0.85).to_edge(UP)
        VPN= Text("Virtual Private Networks",color=LIGHT_GREY,font="Geneva").scale(0.75).next_to(PrivateBrowsing,DOWN)
        self.add(PrivateBrowsing)
        self.add(VPN)

        LikeProxy=Text("These work very much like Proxies.",font="Geneva").scale(0.5).next_to(VPN,DOWN)
        RouteThroughOwnNetwork=Text("However,they route your data through an entire private network",font="Geneva").scale(0.4).next_to(VPN,DOWN)
        BeforeSending=Text("before it reaches the site, and do it once more before it reaches you.",font="Geneva").scale(0.4).next_to(RouteThroughOwnNetwork,DOWN)
        RouteThroughOwnNetworkBeforeSending=VGroup(RouteThroughOwnNetwork,BeforeSending)

        self.play(Write(LikeProxy))
        self.wait(1)
        self.play(ReplacementTransform(LikeProxy,RouteThroughOwnNetworkBeforeSending))

        VPNDiagram=ImageMobject("/Users/aathishs/Desktop/VPN.png").scale(2).shift(DOWN*2)
        self.play(FadeInFromDown(VPNDiagram))
        self.wait(1)
        VPNsAtHome=Text("Now, you can even set up your own VPN's at home!",font="Geneva").scale(0.5).next_to(VPN,DOWN)
        self.play(ReplacementTransform(RouteThroughOwnNetworkBeforeSending,VPNsAtHome))

        self.play(FadeOutAndShiftDown(VPNDiagram))
        self.play(Uncreate(VPNsAtHome))
        self.play(Uncreate(VPN))
        self.play(Uncreate(PrivateBrowsing))
        self.clear()

    def construct(self):
        self.DefinePrivateAnonBrowsing()
        self.ProxiedBrowsing()
        self.VPNs()

class CommonCybercrime(Scene):

    def WhatIsCyberCrime(self):
        WhatIsCC=Text("What is CyberCrime?",font="Geneva",color=REP_GREEN).to_edge(UP)
        self.add(WhatIsCC)

        CCDef1=Text("Cybercrime is any criminal offense that uses e-communication",font="Geneva")
        CCDef2=Text("such as the Internet or uses an electronic device, like a computer.",font="Geneva").next_to(CCDef1,DOWN)

        CCDef=VGroup(CCDef1,CCDef2).scale(0.4).move_to(ORIGIN)

        CyberCrimeDict={
            Text("The Most Common CyberCrimes are:",color=REP_GREEN,font="Geneva"):[
                Text("CyberBullying and Trolling",color="#C30000",font= "Geneva"),
                Text("Cyber Stalking",color="#C30000",font="Geneva"),
            ]
        }

        CyberCrimeTable=Table(tabledict=CyberCrimeDict).scale(0.5).move_to(ORIGIN)

        self.play(Write(WhatIsCC))
        self.wait(1)
        self.play(Write(CCDef),run_time=3)
        self.wait(3)
        self.play(Uncreate(CCDef))

        self.play(ReplacementTransform(WhatIsCC,CyberCrimeTable[0]),Write(CyberCrimeTable[3]))

        self.play(Write(CyberCrimeTable[1:3]))
        self.wait(3)
        self.clear()

    def CyberBullying(self):
        CyberCrimeDict={
            Text("The Most Common CyberCrimes are:",color=REP_GREEN,font="Geneva"):[
                Text("CyberBullying and Trolling",color="#C30000",font= "Geneva"),
                Text("Cyber Stalking",color="#C30000",font="Geneva"),
            ]
        }

        CyberCrimeTable=Table(tabledict=CyberCrimeDict).scale(0.5).move_to(ORIGIN)

        self.add(CyberCrimeTable)
        self.wait(2)
        CyberBullyTroll=CyberCrimeTable[1].deepcopy()
        self.add(CyberBullyTroll)
        self.remove(CyberCrimeTable[1])

        self.play(FadeOut(CyberCrimeTable),
        FadeToColor(CyberBullyTroll,REP_GREEN),
        CyberBullyTroll.to_edge,UP,
        CyberBullyTroll.scale,1.5,
        )

        CyberTrollDef1=Text("A Cyber Troll is someone who purposely posts sarcastic",color=RED,font= "Geneva").next_to(CyberBullyTroll,DOWN)
        CyberTrollDef2=Text("sarcastic or insulting comments to target someone online.",color=RED,font= "Geneva").next_to(CyberTrollDef1,DOWN)
        CyberTrollDef=VGroup(CyberTrollDef1,CyberTrollDef2).scale(0.5)

        TrollMsg=Text("Such a comment is also called 'Troll'.",color=RED,font= "Geneva").scale(0.5).move_to(CyberTrollDef.get_center())

        TrollImage=ImageMobject("/Users/aathishs/Desktop/TrollFace.png").next_to(CyberTrollDef,DOWN)


        CyberBullyDef=Text("Harassing or defaming someone using modern tech is called cyberbullying.",color=RED,font= "Geneva").scale(0.36).move_to(TrollMsg.get_center())

        CBasCrime=Text("It is a criminal offence and can even count as assault.",color=RED,font= "Geneva").scale(0.4).next_to(CyberTrollDef,DOWN)

        self.play(Write(CyberTrollDef),FadeIn(TrollImage),run_time=2,
        )

        self.wait(2)

        self.play(ReplacementTransform(CyberTrollDef,TrollMsg))

        self.wait(2)

        self.play(FadeOutAndShiftDown(TrollImage),ReplacementTransform(TrollMsg,CyberBullyDef))
        self.wait(2)
        self.play(Write(CBasCrime))

        self.wait(3)

        CyberStalking=Text("Cyber Stalking",color="#C30000",font="Geneva").to_edge(UP)

        self.play(Uncreate(CBasCrime),Uncreate(CyberBullyDef),ReplacementTransform(CyberBullyTroll,CyberStalking))
        self.clear()

    def CyberStalking(self):
        CyberStalking=Text("Cyber Stalking",color="#C30000",font="Geneva").to_edge(UP)
        self.add(CyberStalking)

        CStalking1=Text("Cyberstalking is the repeated use of electronic",font="Geneva").next_to(CyberStalking,DOWN)
        CStalking2=Text("communications to harass or frighten someone.",font="Geneva").next_to(CStalking1,DOWN)

        CStalking=VGroup(CStalking1,CStalking2).scale(0.5)

        VictimsKnown=Text("Usually, the stalker knows the victim personally.",font="Geneva").scale(0.5).next_to(CStalking,DOWN)
        AnonymityImportant=Text("They hide behind the anonymity provided by the Net.",font="Geneva").scale(0.5).next_to(CStalking,DOWN)

        StalkingDict={
            Text("They Do Things Like:",font="Impact"):[
            Text("Posting the victims info Online.",font="Geneva"),
            Text("Masquerade as the Victim on obscene websites.",font="Geneva"),
            Text("Allow people from bad backgrounds to access Victim's info.",font="Geneva"),
            Text("Add Victim to Mailing list of obscene websites.",font="Geneva"),
            Text("Threaten the Victim directly or indirectly.",font="Geneva")
            ]
        }

        StalkingTable=Table(tabledict=StalkingDict,line_color=RED).scale(0.4).move_to(ORIGIN)

        self.play(Write(CStalking))
        self.wait(1)
        self.play(Write(VictimsKnown))
        self.wait(2)
        self.play(ReplacementTransform(VictimsKnown,AnonymityImportant))
        self.wait(2)
        self.play(ReplacementTransform(AnonymityImportant,StalkingTable[0]),Write(StalkingTable[6]),FadeOut(CStalking))
        self.play(Write(StalkingTable[1:6]))
        self.wait(5)

        self.play(FadeOutAndShiftDown(StalkingTable),ReplacementTransform(CyberStalking,Text("Rumour Spreading",color="#C30000",font="Geneva").to_edge(UP)))
        self.clear()
    def RumourSpreading(self):
        RumourSpreadingH=Text("Rumour Spreading",color="#C30000",font="Geneva").to_edge(UP)
        self.add(RumourSpreadingH)
        FakeInfo=Text("Often, people post fake info behind fake accounts.",font="Geneva").scale(0.5).next_to(RumourSpreadingH,DOWN)

        Tension=Text("This could lead to tensions between communities and even riots.",font="Geneva").scale(0.4).next_to(FakeInfo,DOWN)
        Punishable=Text("Spreading such rumors is illegal and a punishable offence.",font="Geneva").scale(0.5).next_to(Tension,DOWN)
        JailTime1=Text("As per Information Technology Act, the deed could land you",font="Geneva").scale(0.4).next_to(Tension,DOWN)
        JailTime2=Text("upto 3 years of jail and a fine.",font="Geneva").scale(0.4).next_to(JailTime1,DOWN)
        JailTime=VGroup(JailTime1,JailTime2)

        self.play(Write(FakeInfo))
        self.wait(1)
        self.play(Write(Tension))
        self.wait(1)
        self.play(Write(Punishable))
        self.wait(1)
        self.play(ReplacementTransform(Punishable,JailTime))
        self.wait(2)
        self.play(Uncreate(JailTime))
        self.play(Uncreate(Tension),Uncreate(FakeInfo))
        self.play(Uncreate(RumourSpreadingH))

        self.clear()

    def ReportingCyberCrime(self):
        Report=Text("Reporting CyberCrime",font="Geneva",color=REP_GREEN).to_edge(UP)
        self.play(Write(Report))
        Firstly=Text("One must first report it to their Guardian/school staff.",font="Geneva").scale(0.4).next_to(Report,DOWN)
        Then=Text("Then, one may report it like any 'non-cyber' crime:",font="Geneva").scale(0.4).next_to(Firstly,DOWN)

        ReportingDict={
            Text("To report a CyberCrime",font="Impact",color=REP_GREEN):[
            Text("Approach Local Police.",font="Geneva"),
            Text("File E-FIRs.",font="Geneva"),
            Text("Contact the CyberSecurity Cell of your state's police.",font="Geneva"),
            ]
        }

        ReportingTable=Table(tabledict=ReportingDict,line_color=LIGHT_GRAY).scale(0.5).move_to(ORIGIN)

        self.play(Write(Firstly))
        self.wait(1)
        self.play(Write(Then))
        self.wait(2)
        self.play(ReplacementTransform(Then,ReportingTable))
        self.wait(5)
        self.play(FadeOutAndShiftDown(ReportingTable))

        self.play(Uncreate(Firstly))
        self.play(Uncreate(Report))

        GoodTips=Text("Now, for some general tips on staying safe online...",font="Geneva",color=BLUE).scale(0.5)

        self.play(Write(GoodTips))
        self.wait(1)
        self.play(Uncreate(GoodTips))

    def construct(self):
        self.WhatIsCyberCrime()
        self.CyberBullying()
        self.CyberStalking()
        self.RumourSpreading()
        self.ReportingCyberCrime()

class SafePracticesAgainstCyberCrime(Scene):

    def All(self):

        SafePracDict={
            Text("Some good practices to be safe are:",color=REP_GREEN,font="Geneva"):[
                Text("Using firewalls.",color=RED,font= "Geneva"),
                Text("Controlling your browser to avoid tracking.",color=WHITE,font="Geneva"),
                Text("Browsing Privately",color=LIGHT_GREY,font="Geneva"),
                Text("Using Common Sense. ;)",color=BLUE,font="Geneva"),
                Text("Ensuring secure connections.",color=GREEN,font="Geneva"),
                Text("Not responding to scam/spam emails.",color=LIGHT_GREY,font="Geneva"),
                Text("Transmiting sensitive data securely.",color=BLUE,font="Geneva"),
                Text("Avoiding Public Computers.",color=RED,font="Geneva"),]
        }

        SafePracTable=Table(tabledict=SafePracDict).scale(0.5).move_to(ORIGIN)

        Wall=ImageMobject("/Users/aathishs/Desktop/FireWall.png").scale(0.6).next_to(SafePracTable[1],RIGHT)
        Browsers=ImageMobject("/Users/aathishs/Desktop/Browsers.png").scale(0.3).next_to(SafePracTable[2],RIGHT)
        Incognito=ImageMobject("/Users/aathishs/Desktop/Incognito.png").scale(0.5).next_to(SafePracTable[3],RIGHT)
        Lock=ImageMobject("/Users/aathishs/Desktop/Lock.png").scale(0.5).next_to(SafePracTable[5],RIGHT)
        HomePC=ImageMobject("/Users/aathishs/Desktop/HomePC.png").scale(0.5).next_to(SafePracTable[8],RIGHT)

        self.play(Write(SafePracTable[0]),Write(SafePracTable[9]))
        self.wait(1)
        self.play(Write(SafePracTable[1]),FadeIn(Wall))
        self.wait(1)
        self.play(Write(SafePracTable[2]),FadeIn(Browsers))
        self.wait(1)
        self.play(Write(SafePracTable[3]),FadeIn(Incognito))
        self.wait(1)
        self.play(Write(SafePracTable[4]))
        self.wait(5)
        self.play(Write(SafePracTable[5]),FadeIn(Lock))
        self.wait(1)
        self.play(Write(SafePracTable[6]))
        self.wait(1)
        self.play(Write(SafePracTable[7]))
        self.wait(1)
        self.play(Write(SafePracTable[8]),FadeIn(HomePC))

        self.play(FadeOutAndShiftDown(SafePracTable),
        FadeOut(Wall),
        FadeOut(Browsers),
        FadeOut(Incognito),
        FadeOut(Lock),
        FadeOut(HomePC),
        Write(Text("Stay Safe, and Have Fun!",font="Geneva",color=REP_GREEN).move_to(ORIGIN)))

    def construct(self):
        self.All()