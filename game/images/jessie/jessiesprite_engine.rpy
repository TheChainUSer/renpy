image jessie_hat_night = ConditionSwitch(
    "night_tint == True", AlphaMask(Solid("#1d006144"), "images/jessie/jessie_hat.png"),
    "night_tint == False", Null(width=896, height=1895),
    "True", Null(width=896, height=1895))

image jessie hat curious = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_hat.png",
    (0, 0), "images/jessie/jessie_face_curious.png",
    (0, 0), "jessie_hat_night"
    )

image jessie hat ditzy = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_hat.png",
    (0, 0), "images/jessie/jessie_face_ditzy.png",
    (0, 0), "jessie_hat_night"
    )

image jessie hat happy = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_hat.png",
    (0, 0), "images/jessie/jessie_face_happy.png",
    (0, 0), "jessie_hat_night"
    )

image jessie hat laugh = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_hat.png",
    (0, 0), "images/jessie/jessie_face_laugh.png",
    (0, 0), "jessie_hat_night"
    )

image jessie hat neutral = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_hat.png",
    (0, 0), "images/jessie/jessie_face_neutral.png",
    (0, 0), "jessie_hat_night"
    )

image jessie hat pout = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_hat.png",
    (0, 0), "images/jessie/jessie_face_pout.png",
    (0, 0), "jessie_hat_night"
    )

image jessie hat sad = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_hat.png",
    (0, 0), "images/jessie/jessie_face_sad.png",
    (0, 0), "jessie_hat_night"
    )

image jessie hat serious = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_hat.png",
    (0, 0), "images/jessie/jessie_face_serious.png",
    (0, 0), "jessie_hat_night"
    )

image jessie hat smug = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_hat.png",
    (0, 0), "images/jessie/jessie_face_smug.png",
    (0, 0), "jessie_hat_night"
    )

image jessie hat stress = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_hat.png",
    (0, 0), "images/jessie/jessie_face_stress.png",
    (0, 0), "jessie_hat_night"
    )

image jessie hat yell = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_hat.png",
    (0, 0), "images/jessie/jessie_face_yell.png",
    (0, 0), "jessie_hat_night"
    )

image jessie_nohat_night = ConditionSwitch(
    "night_tint == True", AlphaMask(Solid("#1d006144"), "images/jessie/jessie_nohat.png"),
    "night_tint == False", Null(width=896, height=1895),
    "True", Null(width=896, height=1895))

image jessie nohat curious = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_nohat.png",
    (0, 0), "images/jessie/jessie_face_curious.png",
    (0, 0), "jessie_nohat_night"
    )

image jessie nohat ditzy = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_nohat.png",
    (0, 0), "images/jessie/jessie_face_ditzy.png",
    (0, 0), "jessie_nohat_night"
    )

image jessie nohat happy = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_nohat.png",
    (0, 0), "images/jessie/jessie_face_happy.png",
    (0, 0), "jessie_nohat_night"
    )

image jessie nohat laugh = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_behindback_base.png",
    (0, 0), "images/jessie/jessie_face_laugh.png",
    (0, 0), "jessie_nohat_night"
    )

image jessie nohat neutral = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_nohat.png",
    (0, 0), "images/jessie/jessie_face_neutral.png",
    (0, 0), "jessie_nohat_night"
    )

image jessie nohat pout = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_nohat.png",
    (0, 0), "images/jessie/jessie_face_pout.png",
    (0, 0), "jessie_nohat_night"
    )

image jessie nohat sad = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_behindback_base.png",
    (0, 0), "images/jessie/jessie_face_sad.png",
    (0, 0), "jessie_nohat_night"
    )

image jessie nohat serious = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_behindback_base.png",
    (0, 0), "images/jessie/jessie_face_serious.png",
    (0, 0), "jessie_nohat_night"
    )

image jessie nohat smug = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_nohat.png",
    (0, 0), "images/jessie/jessie_face_smug.png",
    (0, 0), "jessie_nohat_night"
    )

image jessie nohat stress = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_behindback_base.png",
    (0, 0), "images/jessie/jessie_face_stress.png",
    (0, 0), "jessie_nohat_night"
    )

image jessie nohat yell = LiveComposite(
    (896, 1895),
    (0, 0), "images/jessie/jessie_nohat.png",
    (0, 0), "images/jessie/jessie_face_yell.png",
    (0, 0), "jessie_nohat_night"
    )

##POCKET JESSIE ITS LIKE A NUT YOU CAN PLAY WITH OUTSIDE

image jessie pocket curious = LiveComposite(
    (563, 349),
    (0, 0), "images/jessie/jessie cut in curious.png"
    )

image jessie pocket ditzy = LiveComposite(
    (563, 349),
    (0, 0), "images/jessie/jessie cut in ditzy.png"
    )
image jessie pocket happy = LiveComposite(
    (563, 349),
    (0, 0), "images/jessie/jessie cut in happy.png"
    )
image jessie pocket laugh = LiveComposite(
    (563, 349),
    (0, 0), "images/jessie/jessie cut in laugh.png"
    )
image jessie pocket neutral = LiveComposite(
    (563, 349),
    (0, 0), "images/jessie/jessie cut in neutral.png"
    )
image jessie pocket pout = LiveComposite(
    (563, 349),
    (0, 0), "images/jessie/jessie cut in pout.png"
    )
image jessie pocket sad = LiveComposite(
    (563, 349),
    (0, 0), "images/jessie/jessie cut in sad.png"
    )
image jessie pocket serious = LiveComposite(
    (563, 349),
    (0, 0), "images/jessie/jessie cut in serious.png"
    )
image jessie pocket smug = LiveComposite(
    (563, 349),
    (0, 0), "images/jessie/jessie cut in smug.png"
    )
image jessie pocket stressed = LiveComposite(
    (563, 349),
    (0, 0), "images/jessie/jessie cut in stressed.png"
    )
image jessie pocket yell = LiveComposite(
    (563, 349),
    (0, 0), "images/jessie/jessie cut in yell.png"
    )
