screen episode1select():
    tag menu
    add "gui/episode/episodes.png"
    add "gui/episode/ep1.png"
    use navigationmm
    imagemap:
        alpha False
        idle "gui/episodes_idle.png"
        hover "gui/episodes_hover.png"
        ground "gui/episodes_ground.png"
        selected_idle "gui/episodes_idle.png"
        selected_hover "gui/episodes_hover.png"
        hotspot (1260, 814, 160, 97) action Hide("menu", dissolve)
        hotspot (962, 828, 271, 79) action Start("scripte01s01")
        hotspot (781, 475, 98, 152) action ShowMenu("episode5select")
        hotspot (1497, 482, 94, 137) action ShowMenu("episode2select")


screen episode2select():
    tag menu
    add "gui/episode/episodes.png"
    add "gui/episode/ep2.png"
    use navigationmm

    imagemap:
        idle "gui/episodes_idle.png"
        hover "gui/episodes_hover.png"
        ground "gui/episodes_ground.png"
        selected_idle "gui/episodes_idle.png"
        selected_hover "gui/episodes_hover.png"
        hotspot (1260, 814, 160, 97) action Hide("menu", dissolve)
        hotspot (781, 475, 98, 152) action ShowMenu("episode1select")
        hotspot (1497, 482, 94, 137) action ShowMenu("episode3select")

screen episode3select():
    tag menu
    add "gui/episode/episodes.png"
    add "gui/episode/ep3.png"
    use navigationmm
    imagemap:
        idle "gui/episodes_idle.png"
        hover "gui/episodes_hover.png"
        ground "gui/episodes_ground.png"
        selected_idle "gui/episodes_idle.png"
        selected_hover "gui/episodes_hover.png"
        hotspot (1260, 814, 160, 97) action Hide("menu", dissolve)
        hotspot (781, 475, 98, 152) action ShowMenu("episode2select")
        hotspot (1497, 482, 94, 137) action ShowMenu("episode4select")

                
screen episode4select():
    tag menu
    add "gui/episode/episodes.png"
    add "gui/episode/ep4.png"
    use navigationmm
    imagemap:
        idle "gui/episodes_idle.png"
        hover "gui/episodes_hover.png"
        ground "gui/episodes_ground.png"
        selected_idle "gui/episodes_idle.png"
        selected_hover "gui/episodes_hover.png"
        hotspot (1260, 814, 160, 97) action Hide("menu", dissolve)
        hotspot (781, 475, 98, 152) action ShowMenu("episode3select")
        hotspot (1497, 482, 94, 137) action ShowMenu("episode5select")

screen episode5select():
    tag menu
    add "gui/episode/episodes.png"
    add "gui/episode/ep5.png"
    use navigationmm
    imagemap:
        idle "gui/episodes_idle.png"
        hover "gui/episodes_hover.png"
        ground "gui/episodes_ground.png"
        selected_idle "gui/episodes_idle.png"
        selected_hover "gui/episodes_hover.png"
        hotspot (1260, 814, 160, 97) action Hide("menu", dissolve)
        hotspot (781, 475, 98, 152) action ShowMenu("episode4select")
        hotspot (1497, 482, 94, 137) action ShowMenu("episode1select")

        