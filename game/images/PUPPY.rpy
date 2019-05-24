image pup_neutral_night = ConditionSwitch(
    "night_tint == True", AlphaMask(Solid("#1d006144"), "images/coyote.png"),
    "night_tint == False", Null(width=563, height=386),
    "True", Null(width=563, height=386))

image pup_tilt_night = ConditionSwitch(
    "night_tint == True", AlphaMask(Solid("#1d006144"), "images/coyote_confused.png"),
    "night_tint == False", Null(width=563, height=386),
    "True", Null(width=563, height=386))

image pup_bark_night = ConditionSwitch(
    "night_tint == True", AlphaMask(Solid("#1d006144"), "images/coyote_angry.png"),
    "night_tint == False", Null(width=563, height=386),
    "True", Null(width=563, height=386))

image coyote neutral = LiveComposite(
    (563, 386),
    (0, 0), "images/coyote.png",
    (0, 0), "pup_neutral_night"
    )

image coyote tilt = LiveComposite(
    (563, 386),
    (0, 0), "images/coyote_confused.png",
    (0, 0), "pup_tilt_night"
    )

image coyote bark = LiveComposite(
    (563, 386),
    (0, 0), "images/coyote_angry.png",
    (0, 0), "pup_bark_night"
    )