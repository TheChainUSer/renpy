# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Characters
init:
    define narrator =  Character(ctc="ctc_blink", ctc_position="fixed")
    define Journal = Character(' ', kind=nvl, color="#c8ffc8")
    define Eve = Character("Ева",color="#c2d5bc", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define Yosemite = Character("Йосемити",color="#c4d5e0", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define Yellowstone = Character("Йеллоустон",color="#edeab7", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define Zion = Character("Зайон",color="#eec995", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define Pup = Character("Щенок",color="#ecd9b1", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define Jessie = Character("Джесси",color="f9dcf7", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define Scanner = Character("Рация",color="#ecd9b1", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define M1 = Character("???",color="#ecd9b1", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define DCamper = Character("Тупой турист",color="#ecd9b1", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define DCamper2 = Character("Тупой турист 2",color="#ecd9b1", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define DCamperG = Character("Тупой турист 3",color="#ecd9b1", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define DCamperG2 = Character("Тупой турист 4",color="#ecd9b1", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define WalkieTalkie = Character("Walkie-Talkie",color="#ecd9b1", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define GShadow= Character("Призрачная тень",color="#ecd9b1", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define SGhost= Character("Простынный призрак",color="#ecd9b1", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")
    define YellowstoneZion = Character("Йеллоустон + Зайон",color="#ecd9b1", who_font="mr_OzHandicraft_BTG.otf", ctc="ctc_blink", ctc_position="fixed")

#Code Stuff
    define fds = Dissolve(.5)
    define fds2 = Dissolve(.2)
    style say_label:
        outlines [ (absolute(3), "#718266", absolute(0), absolute(0)) ]
    image ctc_blink = Animation("gui/ctc1.png", 0.4, "gui/ctc2.png", 0.4, xpos=1.0, ypos=1.0, xanchor=1.0, yanchor=1.0)
    define ironspy_flash = Fade(.25, 0, .75, color="#ED1C24")
## Yeahhhh that's a good ass TUNE
    define audio.anchors= "<loop 12.706 to 139.021>music/Anchors.mp3"
    define audio.bitter= "<loop 29.445 to 146.996>music/Bitter Coffee.mp3"
    define audio.bursting= "<loop 15.645 to 115.645>music/Bursting Forth.mp3"
    define audio.fever= "<loop 31.365 to 114.844>music/Cabin Fever.mp3"
    define audio.devastation= "<loop 14.856 to 088.702>music/Devastation.mp3"
    define audio.mariposa= "<loop 9.255 to 101.563>music/Mariposa Hymn.mp3"
    define audio.memories= "<loop 13.385 to 113.385>music/Memories of Yosemite.mp3"
    define audio.north= "<loop 31.365 to 125.279>music/North Guardian Angel.mp3"
    define audio.trails= "<loop 10.130 to 105.104>music/Trails.mp3"
#Image Defining Stuff
    image bobross = "backgrounds/bobross.png" ##Rest in peace, Bob Ross joke. I'll always remember you.
    image intro_animation:
        contains:
            "gui/someday.png" ###
        contains:
            pause 0.2
            Movie(channel="bg_anim1", play="gui/introanimation.mpg", size=(1500,1080), xpos=420)
            alpha 1.0
            pause 4.0
            linear 0.5 alpha 0
        contains:
            "sky2.png"
            alpha 1.0
            pause 1.1
            linear 0.3 alpha 0.0

    image bg_black = Solid("#000")
    image ohboythankyoupytom = Movie(channel="bg_anim1", play="gui/introanimation.mpg")
    image staticshockwasacoolshow = Movie(channel="mydadblockedthewbsoiwouldntturnintoalesbianbutitdidntwork", play="images/static_2.ogv")

    default night_tint = False
    default fire_tint = False

init python:
    config.gl_resize=False
label start:
       stop music fadeout 1.8
       jump scripte01s01
