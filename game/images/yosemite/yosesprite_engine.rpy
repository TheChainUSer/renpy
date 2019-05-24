image yosemite_back_night = ConditionSwitch(
    "night_tint == True", AlphaMask(Solid("#1d006144"), "images/yosemite/yosemite_behindback_base.png"),
    "night_tint == False", Null(width=1107, height=1895),
    "True", Null(width=1107, height=1895))

image yosemite back annoyed = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_behindback_base.png",
    (0, 0), "images/yosemite/yosemite_face_annoyed.png",
    (0, 0), "yosemite_back_night"
    )

image yosemite back blush = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_behindback_base.png",
    (0, 0), "images/yosemite/yosemite_face_blush.png",
    (0, 0), "yosemite_back_night"
    )

image yosemite back bored = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_behindback_base.png",
    (0, 0), "images/yosemite/yosemite_face_bored.png",
    (0, 0), "yosemite_back_night"
    )

image yosemite back cringe = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_behindback_base.png",
    (0, 0), "images/yosemite/yosemite_face_cringe.png",
    (0, 0), "yosemite_back_night"
    )

image yosemite back crying = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_behindback_base.png",
    (0, 0), "images/yosemite/yosemite_face_crying.png",
    (0, 0), "yosemite_back_night"
    )

image yosemite back curious = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_behindback_base.png",
    (0, 0), "images/yosemite/yosemite_face_curious.png",
    (0, 0), "yosemite_back_night"
    )

image yosemite back frustrated = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_behindback_base.png",
    (0, 0), "images/yosemite/yosemite_face_frustrated.png",
    (0, 0), "yosemite_back_night"
    )

image yosemite back happy = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_behindback_base.png",
    (0, 0), "images/yosemite/yosemite_face_happy.png",
    (0, 0), "yosemite_back_night"
    )

image yosemite back nervous = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_behindback_base.png",
    (0, 0), "images/yosemite/yosemite_face_nervous.png",
    (0, 0), "yosemite_back_night"
    )

image yosemite back neutral = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_behindback_base.png",
    (0, 0), "images/yosemite/yosemite_face_neutral.png",
    (0, 0), "yosemite_back_night"
    )

image yosemite back smallsmile = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_behindback_base.png",
    (0, 0), "images/yosemite/yosemite_face_smallsmile.png",
    (0, 0), "yosemite_back_night"
    )

image yosemite back smug = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_behindback_base.png",
    (0, 0), "images/yosemite/yosemite_face_smug.png",
    (0, 0), "yosemite_back_night"
    )

image yosemite back yelling = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_behindback_base.png",
    (0, 0), "images/yosemite/yosemite_face_yelling.png",
    (0, 0), "yosemite_back_night"
    )


image yosemite_chin_night = ConditionSwitch(
    "night_tint == True", AlphaMask(Solid("#1d006144"), "images/yosemite/yosemite_chintouch_base.png"),
    "night_tint == False", Null(width=1107, height=1895),
    "True", Null(width=1107, height=1895))

image yosemite chin annoyed = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_chintouch_base.png",
    (0, 0), "images/yosemite/yosemite_face_annoyed.png",
    (0, 0), "yosemite_chin_night"
    )

image yosemite chin blush = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_chintouch_base.png",
    (0, 0), "images/yosemite/yosemite_face_blush.png",
    (0, 0), "yosemite_chin_night"
    )

image yosemite chin bored = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_chintouch_base.png",
    (0, 0), "images/yosemite/yosemite_face_bored.png",
    (0, 0), "yosemite_chin_night"
    )

image yosemite chin cringe = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_chintouch_base.png",
    (0, 0), "images/yosemite/yosemite_face_cringe.png",
    (0, 0), "yosemite_chin_night"
    )

image yosemite chin crying = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_chintouch_base.png",
    (0, 0), "images/yosemite/yosemite_face_crying.png",
    (0, 0), "yosemite_chin_night"
    )

image yosemite chin curious = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_chintouch_base.png",
    (0, 0), "images/yosemite/yosemite_face_curious.png",
    (0, 0), "yosemite_chin_night"
    )

image yosemite chin frustrated = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_chintouch_base.png",
    (0, 0), "images/yosemite/yosemite_face_frustrated.png",
    (0, 0), "yosemite_chin_night"
    )

image yosemite chin happy = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_chintouch_base.png",
    (0, 0), "images/yosemite/yosemite_face_happy.png",
    (0, 0), "yosemite_chin_night"
    )

image yosemite chin nervous = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_chintouch_base.png",
    (0, 0), "images/yosemite/yosemite_face_nervous.png",
    (0, 0), "yosemite_chin_night"
    )

image yosemite chin neutral = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_chintouch_base.png",
    (0, 0), "images/yosemite/yosemite_face_neutral.png",
    (0, 0), "yosemite_chin_night"
    )

image yosemite chin smallsmile = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_chintouch_base.png",
    (0, 0), "images/yosemite/yosemite_face_smallsmile.png",
    (0, 0), "yosemite_chin_night"
    )

image yosemite chin smug = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_chintouch_base.png",
    (0, 0), "images/yosemite/yosemite_face_smug.png",
    (0, 0), "yosemite_chin_night"
    )

image yosemite chin yelling = LiveComposite(
    (1107, 1895),
    (0, 0), "images/yosemite/yosemite_chintouch_base.png",
    (0, 0), "images/yosemite/yosemite_face_yelling.png",
    (0, 0), "yosemite_chin_night"
    )

