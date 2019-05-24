label creditse01:
    $ credits_speed = 137 #scrolling speed in seconds
    $ achievement.grant("National Park Girls")
    show creditsbg onlayer middle with dissolve
    hide creditsblock onlayer background
    hide NPGCreditse1Card onlayer middle
    show cred at Move((0.5, 8.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom") onlayer middle:
        alpha 0.0
        linear 1.0 alpha 1.0
    with Pause(credits_speed)
    hide cred onlayer middle
    hide creditsbg onlayer middle with fade
    hide screen unskip_text
    jump fireside1

init python:
    credits = ('DIRECTOR', 'Syon Santeria'), ('CHARACTER ARTIST', 'Satchely'), ('CHARACTER DESIGN', 'Moorina'), ('CHIBIS AND ADDITIONAL ART', 'Umujacha'), ('BACKGROUNDS', 'Badriel'), ('ADDITIONAL BACKGROUNDS', 'TripleDistress'), ('USER INTERFACE', 'TopHat '), ('BETA UI', 'Potouto'), ('MUSIC', 'Sarah "Esselfortium" Mancuso'), ('WRITER', 'Syon Santeria'), ('EDITOR', 'Max Jeffery Sher'), ('PROGRAMMER', 'Kari Tuberville'), ('PRODUCTION ASSISTANT', 'Josh Kaplan'), ('SOUND ENGINEER', 'Lisa Reimold'), ('CASTING', 'Yin Yang Voices'), ('CASTING CONSULTANT', 'John Wesley Go'), ('', 'CAST'), ('Eve Aadams', 'Natalie Van Sistine'), ('Yosemite', 'Rachael Messer'), ('Yellowstone', 'Jill Harris'), ('Zion, Dumbass Camper Girl, Dumbass Camper Girl 2', 'Lisa Reimold'), ('Jessie Hayvers', 'Daisy Guevara'), ('Ernie, Dumbass Camper, Dumbass Camper 2', 'Freddie Heinz'), ('Pup', 'Syon Santeria'), ('', ''), ('', '"Broken Wings"'), ('Vocals', 'Lisa Reimold'), ('Composition', 'Sarah "Esselfortium" Mancuso'), ('Lyrics', 'Syon Santeria'), ('ENGINE', 'Ren’py 7.1.1'), ('Special Thanks', 'The rangers and employees of the National Park Service'), ('Special Thanks', 'Alice in Dissonance for the 3D Camera '), ('Special Thanks', 'Kevin Turner'), ('Special Thanks', 'TJ "Vogue" Huckabee'), ('All sound effects were obtained via http://freesound.org/ under the Creative Commons 0 license. ', ''), ('This is a work of fiction. Names, characters, places and incidents either are products of the author’s imagination or are used fictitiously. Any resemblance to actual events or locales or persons, living or dead, is entirely coincidental.', ''), ('Studio Coattails is not associated with the National Park Service or the Department of the Interior. National Park Girls is not an accurate example of the runnings of the National Park Service or the Department of the Interior.', ''), ('Publisher', 'Sekai Project'), ('Developer', 'Studio Coattails')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    
##I just want it on the record that Eve's last name isn't misspelled and yes we are aware of it.

init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, font="VarelaRound-Regular.ttf", text_align=0.5, color="#ecd9b1")
    image NPGCreditse1Card = "gui/npgcreditscarde1.png"
    image creditsblock = "gui/creditsblock.png"
    image creditsbg = "gui/creditsbg.png"