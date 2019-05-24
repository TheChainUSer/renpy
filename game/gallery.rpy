###############GALLERY##################
init python:

    g = Gallery()
    g.transition = dissolve

    g.locked_button = "locked.png" 

    g.button("e1c1v1") 
    g.condition("persistent.unlock_e1c1v1") 
    g.image("cg/gallery/images/e1c1v1.png")  
    g.image("cg/gallery/images/e1c1v2.png")  
    g.image("cg/gallery/images/e1c1v3.png") 

    g.button("e1c1v2") 
    g.condition("persistent.unlock_e1c1v2") 

    g.button("e1c1v3") 
    g.condition("persistent.unlock_e1c1v3") 

    g.button("e1girls") 
    g.condition("persistent.unlock_girls") 
    g.image("cg/gallery/images/girls_cg.png")  

    g.button("promo") 
    g.image("cg/promo.png")  

    g.button("e1c2v1") 
    g.condition("persistent.unlock_e1c2v1") 
    g.image("cg/gallery/images/e1c2v2.png")  
    g.image("cg/gallery/images/e1c2v1.png")  

    g.button("e1c2v2") 
    g.condition("persistent.unlock_e1c2v2") 

    g.button("e1c3v1") 
    g.condition("persistent.unlock_e1c3v1") 
    g.image("cg/gallery/images/e1c3v1.png")  
    g.image("cg/gallery/images/e1c3v2.png")  

    g.button("e1c3v2") 
    g.condition("persistent.unlock_e1c3v2") 

    g.button("e1c4v1") 
    g.condition("persistent.unlock_e1c4v1") 
    g.image("cg/gallery/images/e1c4v1.png")  
    g.image("cg/gallery/images/e1c4v2.png")  
    g.image("cg/gallery/images/e1c4v3.png") 

    g.button("e1c4v2") 
    g.condition("persistent.unlock_e1c4v2") 

    g.button("e1c4v3") ## DAMN YOU V3
    g.condition("persistent.unlock_e1c4v3") 

    g.button("e1g1") 
    g.image("Chie00chan")

    g.button("e1g2") 
    g.image("Sayuui")

    g.button("e1g3") 
    g.image("oekkim")

    g.button("e1g4") 
    g.image("MGCoco")

    g.button("e1g5") 
    g.image("Jae")

    g.button("e1g6") 
    g.image("NPGLogo")

#For main menu

screen gallerye1p1():
    zorder 100
    tag menu
    modal True
    $ achievement.grant("Entrance Fee")
    imagemap:
        idle "gui/gallery_idle.png"
        hover "gui/gallery_hover.png"
        ground "gui/gallery_ground.png"
        selected_idle "gui/gallery_selected.png"
        selected_hover "gui/gallery_selected.png"
        hotspot (613, 246, 207, 52) action ShowMenu("gallerye1p1")
        hotspot (854, 246, 228, 52)action ShowMenu("galleryguest1")
    grid 3 2:

        xfill False
        yfill False
        add g.make_button("promo", "cg/gallery/thumb/promothumb.png", xpos=692, ypos=447)
        add g.make_button("e1c1v1", "cg/gallery/thumb/e1c1v1_thumb.png", xpos=707, ypos=447)
        add g.make_button("e1girls", "cg/gallery/thumb/girlsthumb.png", xpos=722, ypos=447)
        add g.make_button("e1c2v1", "cg/gallery/thumb/e1c2v1_thumb.png", xpos=692, ypos=461)
        add g.make_button("e1c3v1", "cg/gallery/thumb/e1c3v1_thumb.png", xpos=707, ypos=461)
        add g.make_button("e1c4v1", "cg/gallery/thumb/e1c4v1_thumb.png", xpos=722, ypos=461)

    use navigationmm
## Weee pages for the guest art thanks people you rule
screen galleryguest1():
    zorder 100
    tag menu
    modal True
    $ achievement.grant("Love Our Parks")
    imagemap:
        idle "gui/gallery_idle.png"
        hover "gui/gallery_hover.png"
        ground "gui/gallery_ground.png"
        selected_idle "gui/gallery_selected.png"
        selected_hover "gui/gallery_selected.png"
        hotspot (613, 246, 207, 52) action ShowMenu("gallerye1p1")
        hotspot (854, 246, 228, 52)action ShowMenu("galleryguest1")

    grid 3 2:

        xfill False
        yfill False

        add g.make_button("e1g1", "cg/gallery/guest/thumb/e1g1_thumb.png", xpos=692, ypos=447)
        add g.make_button("e1g2", "cg/gallery/guest/thumb/e1g2_thumb.png", xpos=707, ypos=447)
        add g.make_button("e1g3", "cg/gallery/guest/thumb/e1g3_thumb.png", xpos=722, ypos=447)
        add g.make_button("e1g4", "cg/gallery/guest/thumb/e1g4_thumb.png", xpos=692, ypos=461)
        add g.make_button("e1g5", "cg/gallery/guest/thumb/e1g5_thumb.png", xpos=707, ypos=461)
        add g.make_button("e1g6", "locked.png", xpos=722, ypos=461)        
        # The screen is responsible for returning to the main menu. It could also
        # navigate to other gallery screens.
    use navigationmm

init-1:
    image Chie00chan = Fixed(Image("images/cg/gallery/guest/Zion_by_Chie00chan.png", xalign=0.5, yalign=0.1), 
    Text("{a=https://twitter.com/Chie00chan}@Chie00chan", xalign=0.0, yalign=0.1))

    image Sayuui = Fixed(Image("images/cg/gallery/guest/national_park_girls_game_size.png", xalign=0.5, yalign=0.1), 
    Text("{a=https://twitter.com/Sayuui}@Sayuui", xalign=0.0, yalign=0.1))

    image oekkim = Fixed(Image("images/cg/gallery/guest/GB42Np2.png", xalign=0.5, yalign=0.1), 
    Text("{a=https://www.pixiv.net/member.php?id=123246}@Oekkim", xalign=0.0, yalign=0.1))

    image MGCoco= Fixed(Image("images/cg/gallery/guest/mgcoco.png", xalign=0.5, yalign=0.1), 
    Text("{a=https://twitter.com/mgcoco_art}@MGCoco", xalign=0.0, yalign=0.1))

    image Jae= Fixed(Image("images/cg/gallery/guest/wowmeow.png", xalign=0.5, yalign=0.1), 
    Text("{a=https://twitter.com/umujacha}@umujacha", xalign=0.0, yalign=0.1))

    image NPGLogo= Fixed(Image("images/title credits npg.png", xalign=0.5, yalign=0.1))