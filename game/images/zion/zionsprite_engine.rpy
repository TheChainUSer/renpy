image zion_arms_night = ConditionSwitch(
    "night_tint == True", AlphaMask(Solid("#1d006144"), "images/zion/zion_armsside_base.png"),
    "night_tint == False", Null(width=969, height=1895),
    "True", Null(width=969, height=1895))

image zion_arms_fire = ConditionSwitch(
    "fire_tint == True", AlphaMask(Solid("#61100044"), "images/zion/zion_armsside_base.png"),
    "fire_tint == False", Null(width=969, height=1895),
    "True", Null(width=969, height=1895))

image zion arms curious = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_armsside_base.png",
    (0, 0), "images/zion/zion_face_curious.png",
    (0, 0), "zion_arms_night",
    (0, 0), "zion_arms_fire"
    )

image zion arms default = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_armsside_base.png",
    (0, 0), "images/zion/zion_face_default.png",
    (0, 0), "zion_arms_night",
    (0, 0), "zion_arms_fire"
    )

image zion arms flat = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_armsside_base.png",
    (0, 0), "images/zion/zion_face_flat.png",
    (0, 0), "zion_arms_night",
    (0, 0), "zion_arms_fire"
    )

image zion arms happy = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_armsside_base.png",
    (0, 0), "images/zion/zion_face_happy.png",
    (0, 0), "zion_arms_night",
    (0, 0), "zion_arms_fire"
    )

image zion arms hardcry = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_armsside_base.png",
    (0, 0), "images/zion/zion_face_hardcry.png",
    (0, 0), "zion_arms_night",
    (0, 0), "zion_arms_fire"
    )

image zion arms laugh = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_armsside_base.png",
    (0, 0), "images/zion/zion_face_laugh.png",
    (0, 0), "zion_arms_night",
    (0, 0), "zion_arms_fire"
    )

image zion arms nervous = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_armsside_base.png",
    (0, 0), "images/zion/zion_face_nervous.png",
    (0, 0), "zion_arms_night",
    (0, 0), "zion_arms_fire"
    )

image zion arms sad = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_armsside_base.png",
    (0, 0), "images/zion/zion_face_sad.png",
    (0, 0), "zion_arms_night",
    (0, 0), "zion_arms_fire"
    )

image zion arms shock = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_armsside_base.png",
    (0, 0), "images/zion/zion_face_shock.png",
    (0, 0), "zion_arms_night",
    (0, 0), "zion_arms_fire"
    )

image zion arms softcry = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_armsside_base.png",
    (0, 0), "images/zion/zion_face_softcry.png",
    (0, 0), "zion_arms_night",
    (0, 0), "zion_arms_fire"
        )

image zion arms softsmile = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_armsside_base.png",
    (0, 0), "images/zion/zion_face_softsmile.png",
    (0, 0), "zion_arms_night",
    (0, 0), "zion_arms_fire"
    )

image zion_hands_night = ConditionSwitch(
    "night_tint == True", AlphaMask(Solid("#1d006144"), "images/zion/zion_handtouch_base.png"),
    "night_tint == False", Null(width=969, height=1895),
    "True", Null(width=969, height=1895))

image zion_hands_fire = ConditionSwitch(
    "fire_tint == True", AlphaMask(Solid("#61100044"), "images/zion/zion_handtouch_base.png"),
    "fire_tint == False", Null(width=969, height=1895),
    "True", Null(width=969, height=1895))

image zion hands curious = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_handtouch_base.png",
    (0, 0), "images/zion/zion_face_curious.png",
    (0, 0), "zion_hands_night",
    (0, 0), "zion_hands_fire"
    )

image zion hands default = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_handtouch_base.png",
    (0, 0), "images/zion/zion_face_default.png",
    (0, 0), "zion_hands_night",
    (0, 0), "zion_hands_fire"
    )

image zion hands flat = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_handtouch_base.png",
    (0, 0), "images/zion/zion_face_flat.png",
    (0, 0), "zion_hands_night",
    (0, 0), "zion_hands_fire"
    )

image zion hands happy = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_handtouch_base.png",
    (0, 0), "images/zion/zion_face_happy.png",
    (0, 0), "zion_hands_night",
    (0, 0), "zion_hands_fire"
    )

image zion hands hardcry = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_handtouch_base.png",
    (0, 0), "images/zion/zion_face_hardcry.png",
    (0, 0), "zion_hands_night",
    (0, 0), "zion_hands_fire"
    )

image zion hands laugh = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_handtouch_base.png",
    (0, 0), "images/zion/zion_face_laugh.png",
    (0, 0), "zion_hands_night",
    (0, 0), "zion_hands_fire"
    )

image zion hands nervous = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_handtouch_base.png",
    (0, 0), "images/zion/zion_face_nervous.png",
    (0, 0), "zion_hands_night",
    (0, 0), "zion_hands_fire"
    )

image zion hands sad = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_handtouch_base.png",
    (0, 0), "images/zion/zion_face_sad.png",
    (0, 0), "zion_hands_night",
    (0, 0), "zion_hands_fire"
    )

image zion hands shock = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_handtouch_base.png",
    (0, 0), "images/zion/zion_face_shock.png",
    (0, 0), "zion_hands_night"
    )

image zion hands softcry = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_handtouch_base.png",
    (0, 0), "images/zion/zion_face_softcry.png",
    (0, 0), "zion_hands_night",
    (0, 0), "zion_hands_fire"
    )

image zion hands softsmile = LiveComposite(
    (969, 1895),
    (0, 0), "images/zion/zion_handtouch_base.png",
    (0, 0), "images/zion/zion_face_softsmile.png",
    (0, 0), "zion_hands_night",
    (0, 0), "zion_hands_fire"
    )

image zionchibi nervous = LiveComposite(
    (900, 1220),
    (0, 0), "images/zion/zion_chibi.png",
    (0, 0), "images/zion/zion_chibi_nervous.png"
    )

image zionchibi normal = LiveComposite(
    (900, 1220),
    (0, 0), "images/zion/zion_chibi.png",
    (0, 0), "images/zion/zion_chibi_normal.png"
    )

image zionchibi sad = LiveComposite(
    (900, 1220),
    (0, 0), "images/zion/zion_chibi.png",
    (0, 0), "images/zion/zion_chibi_sad.png"
    )

image zionchibi sigh = LiveComposite(
    (900, 1220),
    (0, 0), "images/zion/zion_chibi.png",
    (0, 0), "images/zion/zion_chibi_sigh.png"
    )

image zionchibi smile = LiveComposite(
    (900, 1220),
    (0, 0), "images/zion/zion_chibi.png",
    (0, 0), "images/zion/zion_chibi_smile.png"
    )

