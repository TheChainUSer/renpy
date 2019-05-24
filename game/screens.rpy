################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)



style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)




################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"
    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label



style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.8

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos



## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    imagemap:
        idle "gui/navigation_idle.png"
        hover "gui/navigation_hover.png"
        ground "gui/navigation_ground.png"
        selected_idle "gui/navigation_idle.png"
        selected_hover "gui/navigation_hover.png"
        ##Nav
        hotspot (0, 230, 555, 108) at h_smooth(0,0.6,0,0) action Hide("menu", dissolve)
        hotspot (0, 362, 555, 108) at h_smooth(0,0.6,0,0) action ShowMenu("load")
        hotspot (0, 488, 555, 108) at h_smooth(0,0.6,0,0) action ShowMenu("preferences")
        hotspot (0, 613, 556, 109) at h_smooth(0,0.6,0,0) action ShowMenu("save2")
        hotspot (0, 740, 555, 108) at h_smooth(0,0.6,0,0) action MainMenu("main_menu")
        hotspot (0, 905, 555, 108) at h_smooth(0,0.6,0,0) action Quit('quit')

screen navigationmm():
    imagemap:
        idle "gui/mmnav_idle.png"
        hover "gui/mmnav_hover.png"
        ground "gui/navigation_ground.png"
        selected_idle "gui/mmnav_idle.png"
        selected_hover "gui/mmnav_hover.png"

        hotspot (0, 230, 555, 108) at h_smooth(0,0.6,0,0) action Hide("menu", dissolve)
        hotspot (0, 362, 555, 108) at h_smooth(0,0.6,0,0) action ShowMenu("load")
        hotspot (0, 488, 555, 108) at h_smooth(0,0.6,0,0) action ShowMenu("preferencesmm")
        hotspot (0, 613, 556, 109) at h_smooth(0,0.6,0,0) action ShowMenu("episode1select")
        hotspot (0, 740, 555, 108) at h_smooth(0,0.6,0,0) action ShowMenu("gallerye1p1")
        hotspot (0, 905, 555, 108) at h_smooth(0,0.6,0,0) action Quit('quit'), Hide("menu", dissolve)

init -1:
    transform h_smooth(p=0, t=.5, x=0, y=0): ##transform with horizontal hover
        alpha .0 xoffset x yoffset y 
        pause p
        easein t  alpha 1.0 xoffset 0 yoffset 0
        on replaced:
            easeout t alpha 0
        on hide:
            easeout t alpha 0
        on hover:
            easein .2 xoffset 15
        on idle:
            easeout .2 xoffset 0
        on selected_idle:
            easeout .2 xoffset 0
        on selected_hover:
            easein .2 xoffset 15
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag mainmenu
    style_prefix "main_menu"
    add "intro_animation"
    add gui.main_menu_background
    imagemap:
        idle "gui/mainmenu_idle.png"
        hover "gui/mainmenu_idle.png"
        ground "gui/mainmenu_idle.png"
        selected_idle "gui/mainmenu_idle.png"
        selected_hover "gui/mainmenu_idle.png"
        alpha True
        hotspot (0, 230, 555, 108) at h_smooth(0,0.6,0,0) action Start('start')
        hotspot (0, 362, 555, 108) at h_smooth(0,0.6,0,0) action ShowMenu("load")
        hotspot (0, 488, 555, 108) at h_smooth(0,0.6,0,0) action ShowMenu("preferencesmm")
        hotspot (0, 613, 556, 109) at h_smooth(0,0.6,0,0) action ShowMenu("episode1select")
        hotspot (0, 740, 555, 108) at h_smooth(0,0.6,0,0) action ShowMenu("gallerye1p1")
        hotspot (0, 905, 555, 108) at h_smooth(0,0.6,0,0) action Quit('quit')

init -2:

    style main_menu_hotspot:
        hover_sound "sfx/bigsteppy.mp3"
        activate_sound "sfx/pageturn.mp3"

    style hotspot:
        hover_sound "sfx/bigsteppy.mp3"
        activate_sound "sfx/pageturn.mp3"

label splashscreen():
    scene black
    pause 1.0
    play music "music/NPG_Insert_F_Instrumental.mp3"
    show sky2 with fade
    show coattailslogo_for_npg with dissolve
    pause 1.5
    hide coattailslogo_for_npg with dissolve
    show sekailogoblack with dissolve
    pause 1.5
    hide sekailogoblack with dissolve
    return
## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.


screen game_menu(title):
    use say
    default x = -1
    default y = -1
    if x == -1 and y == -1:
        $ x,y = renpy.get_mouse_pos()
    modal True
    imagemap:
        pos (x, y) anchor (0.5, 0.5)
        idle "gui/radial_idle.png"
        hover "gui/radial_hover.png"
        hotspot (106, 4, 84, 79) action Skip(fast=True, confirm=False)
        hotspot (216, 61, 84, 83) action Preference("auto-forward", "toggle")
        hotspot (214, 168, 86, 94) action MainMenu()
        hotspot (109, 231, 83, 86) action ShowMenu("preferences")
        hotspot (0, 160, 90, 98) action ShowMenu("load")
        hotspot (0, 56, 88, 90) action ShowMenu("save2")

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.


screen quick_menu():
    zorder 100
    default x = -1
    default y = -1
    if x == -1 and y == -1:
        $ x,y = renpy.get_mouse_pos()
        $ x,y = max( 252, min( config.screen_width - 252, x) ), max( 252, min( config.screen_height - 252, y) )    
    modal True
    imagemap:
        pos (x, y) anchor (0.5, 0.5)
        idle "gui/radial_idle.png"
        hover "gui/radial_hover.png"
        hotspot (181, 7, 139, 143) action Skip() alternate Skip(fast=True, confirm=True)
        hotspot (341, 98, 139, 143) action Hide("quick_menu"), Preference("auto-forward", "toggle")
        hotspot (341, 264, 139, 143) action MainMenu("main_menu")
        hotspot (181, 355, 139, 143) action ShowMenu("preferences")
        hotspot (23, 264, 139, 143) action ShowMenu("load")
        hotspot (23, 98, 139, 143) action ShowMenu("save2")

## Episode Select screen
## Pick what episode you wanna play woo groovy


## Gallery
## You can stare at pictures of Yellowstone all day, the true way to win the game



## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html
## save https://## www.renpy.org/doc/html/screen_special.html#load
screen save:
    use quick_menu

screen save2:
    tag menu
    use file_slots(_("Save"))
    add gui.save_screen_background
    use navigation
screen load:
    tag menu
    use file_slots(_("Load"))
    add gui.load_screen_background
    if main_menu:
        use navigationmm
    else:
        use navigation
screen load_save_slot:


    add FileScreenshot(number) xpos 3 ypos 2
    
    key "save_delete" action FileDelete(number)
    
init -2 python:
    
    config.thumbnail_width = 320
    config.thumbnail_height = 180

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    imagemap:
        idle "gui/saveload_idle.png"
        hover "gui/saveload_hover.png"
        selected_idle "gui/saveload_hover.png"
        selected_hover "gui/saveload_hover.png"
        ground "gui/saveload_ground.png"
        alpha False 
        ##Pages
        hotspot (603, 243, 48, 63) clicked FilePage("quick") #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (661, 243, 48, 63) clicked FilePage("auto") #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (719, 243, 48, 63) clicked FilePage(1) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (777, 243, 48, 63) clicked FilePage(2) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (835, 243, 48, 63) clicked FilePage(3)
        hotspot (893, 243, 48, 63) clicked FilePage(4)
        hotspot (951, 243, 48, 63) clicked FilePage(5)
        ##Slots
        hotspot (622, 417, 320, 180) clicked FileAction(1):
            use load_save_slot(number=1) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (1024, 417, 320, 180) clicked FileAction(2):
            use load_save_slot(number=2) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (1426, 417, 320, 180) clicked FileAction(3):
            use load_save_slot(number=3)
        hotspot (622, 733, 320, 180) clicked FileAction(4):
            use load_save_slot(number=4)
        hotspot (1024, 733, 320, 180) clicked FileAction(5):
            use load_save_slot(number=5)    
        hotspot (1426, 733, 320, 180) clicked FileAction(6):
            use load_save_slot(number=6)
style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Keymap screen
screen keymap_screen():
    key "game_menu" action toggle
    key "p" action ShowMenu('preferences')
    key "s" action Screenshot()

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    tag menu
    add gui.settings_screen_background
    use navigation
    imagemap:   
        idle "gui/settings_screen_idle.png"
        hover "gui/settings_screen_idle.png"
        selected_idle "gui/settings_screen_selected.png" 
        selected_hover "gui/settings_screen_selected.png"
        ground "gui/settings_screen_ground.png"

        alpha False
        
        hotspot (726, 308, 129, 26) action Preference("display", "fullscreen")
        hotspot (726, 352, 129, 26) action Preference("display", 0.666666666666666666666666666667)
        hotspot (726, 509, 129, 26) action Preference("rollback side", "right") 
        hotspot (726, 553, 129, 26) action Preference("rollback side", "left") 
        hotspot (726, 596, 129, 26) action Preference("rollback side", "disable")
        hotspot (726, 761, 149, 26) action Preference("skip", "toggle")

        bar pos (1215, 298) value Preference("music volume") style "pref_slider"
        bar pos (1215, 432) value Preference("sound volume") style "pref_slider"
        bar pos (1215, 566) value Preference("text speed") style "pref_slider"
        bar pos (1215, 700) value Preference("auto-forward time") style "pref_slider"
        bar pos (1215, 834) value Preference("voice volume") style "pref_slider"

screen preferencesmm():
    tag menu
    add gui.settings_screen_background
    use navigationmm
    imagemap:   
        idle "gui/settings_screen_idle.png"
        hover "gui/settings_screen_idle.png"
        selected_idle "gui/settings_screen_selected.png" 
        selected_hover "gui/settings_screen_selected.png"
        ground "gui/settings_screen_ground.png"

        alpha False
        
        hotspot (726, 308, 129, 26) action Preference("display", "fullscreen")
        hotspot (726, 352, 129, 26) action Preference("display", 0.666666666666666666666666666667)
        hotspot (726, 509, 129, 26) action Preference("rollback side", "right") 
        hotspot (726, 553, 129, 26) action Preference("rollback side", "left") 
        hotspot (726, 596, 129, 26) action Preference("rollback side", "disable")
        hotspot (726, 761, 149, 26) action Preference("skip", "toggle")

        bar pos (1215, 298) value Preference("music volume") style "pref_slider"
        bar pos (1215, 432) value Preference("sound volume") style "pref_slider"
        bar pos (1215, 566) value Preference("text speed") style "pref_slider"
        bar pos (1215, 700) value Preference("auto-forward time") style "pref_slider"
        bar pos (1215, 834) value Preference("voice volume") style "pref_slider"
init -2 python:
    style.pref_slider.left_bar = "gui/full2.png"
    style.pref_slider.right_bar = "gui/empty2.png"

    style.pref_slider.xmaximum = 355
    style.pref_slider.ymaximum = 52
    style.pref_slider.thumb_offset = 0
    style.pref_slider.thumb_shadow = None

## No soup for you screen ######
## Cause timing the credits song is hard
screen unskip_text():
    #Dismiss keys
    key "K_RETURN" action Hide("nonexistent_screen")
    key "K_KP_ENTER" action Hide("nonexistent_screen")
    key "K_SPACE" action Hide("nonexistent_screen")
    
    key "mousedown_4" action Hide("nonexistent_screen")
    key "K_PAGEUP" action Hide("nonexistent_screen")
    key "mousedown_5" action Hide("nonexistent_screen")
    key "K_PAGEDOWN" action Hide("nonexistent_screen")
    
    key "mouseup_3" action Hide("nonexistent_screen")
    key "mouseup_1" action Hide("nonexistent_screen")

    key "K_ESCAPE" action Return("smth")

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

#I have no clue what I'm doing!
#It's okay buddy, I don't either.

screen help():

    tag menu

    default device = "keyboard"



screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True
    style_prefix "confirm"
    add "gui/npg_yesno.png"

    if message == layout.QUIT:
        imagemap:
            add "gui/yesno_exit.png"
            idle "gui/yesno_idle.png"
            hover "gui/yesno_hover.png"
            alpha True
            hotspot (723, 561, 232, 89) action yes_action
            hotspot (978, 561, 232, 89) action no_action
    ## Right-click and escape answer "no".
        key "game_menu" action no_action
    elif message == layout.DELETE_SAVE:
        imagemap:
            add "gui/yesno_delete.png"
            idle "gui/yesno_idle.png"
            hover "gui/yesno_hover.png"
            alpha False
            hotspot (723, 561, 232, 89) action yes_action
            hotspot (978, 561, 232, 89) action no_action
    elif message == layout.MAIN_MENU:
        imagemap:
            add "gui/yesno_title.png"
            idle "gui/yesno_idle.png"
            hover "gui/yesno_hover.png"
            alpha False
            hotspot (723, 561, 232, 89) action yes_action
            hotspot (978, 561, 232, 89) action no_action
    elif message == layout.OVERWRITE_SAVE:
        imagemap:
            add "gui/yesno_overwrite.png"
            idle "gui/yesno_idle.png"
            hover "gui/yesno_hover.png"
            alpha False
            hotspot (723, 561, 232, 89) action yes_action
            hotspot (978, 561, 232, 89) action no_action
    elif message == layout.LOADING:
        imagemap:
            add "gui/yesno_load.png"
            idle "gui/yesno_idle.png"
            hover "gui/yesno_hover.png"
            alpha False
            hotspot (723, 561, 232, 89) action yes_action
            hotspot (978, 561, 232, 89) action no_action

## Auto indicator
screen indicator():
    zorder 9999
    if _rollback:
        if _preferences.afm_enable:
            add "auto_image" at indicator
            add "chibiyose" at indicator
        if config.skipping == "slow":
            add "skip_image" at indicator
            add "chibieve" at indicator

        if config.skipping == "fast":
            add "skip_image" at indicator
            add "chibieve" at indicator

init python:
    config.skip_indicator = None
    config.overlay_screens.append("indicator")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator


screen skip_indicator():
    text _("") size 50 xpos 15 ypos 12 at indicator

init -1:
    image chibieve:
        "gui/eebu.png"
        xpos 310
        ypos 5
        block:
            yoffset 0
            ease 0.5 yoffset 2
            ease 0.5 yoffset 0
            repeat
    image chibiyose:
        "gui/yosie.png"
        xpos 310
        ypos 5
        block:
            yoffset 0
            ease 0.5 yoffset 2
            ease 0.5 yoffset 0
            repeat
    image skip_image:
        "gui/skipmode.png"
        xpos 0
        ypos 15

    image auto_image:
        "gui/automode.png"
        xpos 0
        ypos 15

    transform indicator:
        on show:
            alpha 0.0
            ease 0.5 alpha 1.0
        on hide:
            ease 0.5 alpha 0.0

## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"



## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None



