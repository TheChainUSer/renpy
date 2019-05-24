init:
    image cg_1 = "images/cg/cg_1.png"
    image title credits_1 = "images/title credits coattails.png"
    image title credits_2 = "images/title credits sekai.png"
    image title credits_3 = "images/title credits npg.png"
    image landscape_tile = Composite(
        (6288, 1440),
        (0, 0), "images/cg/cg1/landscape.jpg",
        (3144, 0), "images/cg/cg1/landscape.jpg")
    image landscape:
        "landscape_tile"
        xpos 2.16
        block:
            xoffset 0
            linear 4.0 xoffset -3144
            repeat
    image random_dustcloud:
        choice (0.33):
            "images/cg/cg1/dustcloud.png"
            alpha 0.0
            xoffset 2500
            zoom 2.0
            yoffset 1000
            parallel:
                linear 0.8 alpha 0.2
                linear 2.0 alpha 0.0
            parallel:
                linear 2.0 xoffset -1920
            parallel:
                ease 2.0 yoffset 0
                ease 3.0 yoffset 1000
        choice (0.66):
            Null()
        pause 5.0
        repeat

label scripte01s01:
#Scene 01

stop music fadeout 0.5
play ambient "ambience/car ambience with dispatch radio.ogg"

show black onlayer forward with dissolve
pause 2.0
show title credits_1 onlayer forward with dissolve
pause 3.0
hide title credits_1 onlayer forward with dissolve
show black onlayer forward with dissolve
pause 2.0
play sound "sfx/jammed car window.ogg"
show title credits_2 onlayer forward with dissolve
pause 3.0
hide title credits_2 onlayer forward with dissolve
show black onlayer forward with dissolve
pause 2.0
play sound "sfx/jammed car window.ogg"
play music audio.mariposa

show title credits_3 onlayer forward with dissolve
pause 5.0
play sound "sfx/jammed car window.ogg"
hide title credits_3 onlayer forward with dissolve
show black onlayer forward:
 zoom 2.5
with dissolve
show landscape onlayer background
$ camera_reset()

$all_moves(camera_check_points={u'y': [(-2366, 0, u'linear')], u'z': [(-450, 0, u'linear')]})
$all_moves(camera_check_points={u'y': [(-2366, 0, None), (-2250, 1.2, u'ease'), (-2366, 2.2, u'ease')], u'x': [(-156, 0, u'ease'), (100, 5, u'ease'), (-156, 10, u'ease')]}, y_loop=True, x_loop=True)
show landscape onlayer background
show cg1j happy onlayer background
show cg1e flat onlayer middle
show random_dustcloud onlayer forward
hide black onlayer forward with dissolve

window show

voice "scripte01s01_25be1cc4"
Jessie "Извини, дорогая. Оно застряло. Ниже уже не опустится."

Eve "Так ли это…"

play sound "sfx/jammed car window.ogg"
"Я нажимаю на переключатель. Грохот врывается в машину вместе с тугим, стремительным ветром и заполняет её."

play sound "sfx/car window up.ogg"
"Я тяну переключатель вверх. Окно поднимается с мягким скрипом."

play sound "sfx/car window down jam.ogg"
"Я ещё раз жму на переключатель. Мягкий скрип. Окно останавливается на полпути вниз. Грохот."
show cg1j laugh onlayer background with dissolve

voice "scripte01s01_f30614f5"
Jessie "Ага! С этим окном на самом деле забавная история."

"Джесси виновато смеётся и пожимает плечами."

voice "scripte01s01_b4f40355"
Jessie "Но... я её уже позабыла."
play sound "sfx/car bump.ogg"
show cg1e annoyed onlayer middle with vpunch
#PYUNPYUN bump
"Мы наезжаем на ухаб на дороге. Машина подпрыгивает, и я ударяюсь плечом об дверь. Бросаю взгляд в боковое зеркало, когда мы проезжаем ухаб."

Eve "У каждой проблемы в этом парке есть своя история. А историй здесь много."
show cg1j happy onlayer background with dissolve

Jessie "Парк обходится тем, что имеет, Ева. Мы изворотливы в этом плане."
show cg1e jerkface onlayer middle with dissolve

"Я закатила глаза. Джесси вроде ободряюще ухмыляется, но её отражение в дурацком сломанном окне показывает совсем другое. Например, реки кофе и переутомление длиною в десять лет."

"Я даже могу разглядеть пару морщинок, поселившихся на её весёлом круглом лицо. Но я не посмею заикнуться об этом. Я люблю пошутить, но желания умирать у меня нет. Пока что."
show cg1e flat onlayer middle with dissolve

"Йосемитский национальный парк в это время года представляет собой смесь зелёного и белого. Место, где зимний снег все ещё пятнает вершины каменно-серых гор и сливается с ожившими весенними деревьями."

"Я закрываю глаза и подставляю лицо свистящему ветру. И на секунду снова чувствую себя маленькой девочкой. Вот я еду на заднем сиденье папиного пикапа. Мы мчимся по перевалу Тиога в поисках новой, неизведанной тропы."
show cg1e annoyed onlayer middle with dissolve
#PYUNPYUN van

"Но как только я вспоминаю запах сладкого, свежего воздуха, мимо нас проносится фургон, оставляя за собой след ядовитых газов. Воспоминания были нагло прерваны."

"Затяжной выхлоп напоминает серое небо. И я должна задаться вопросом - если грозовая туча покажется, но дождь не пойдёт, она пустая или водой всё же заполнена?"
show cg1e jerkface onlayer middle with dissolve

"Из радиоприёмника доносится треск помех."

Scanner "Ситуация в Уавоне была урегулирована. Приём."

"Джесси снимает рацию с приборной панели, держа одну руку на руле, и переключается на свой командирский голос."
show cg1j laugh onlayer background with dissolve

Jessie "10-4. Опиши мне детали."

Scanner "А.. Особых деталей и нет. 10-56. Белый мужчина, около 50 лет."

Scanner "Он весь шатался, когда я приехал. Перестал стрелять, как только увидел меня. Похоже, он стрелял по бутылкам."
show cg1e annoyed onlayer middle with dissolve

show cg1j annoyed onlayer background with dissolve

"Я ухмыляюсь. Даже не пытаюсь скрыть это. Джесси бросает на меня прищуренный взгляд."

Scanner "Никаких препирательств с его стороны. Но и без алкотестера было видно, что он бухой. Сейчас он под стражей."
show cg1e jerkface onlayer middle with dissolve

"Джесси глубоко вздыхает, и я почти вижу, как мешки показываются из-под её глаз."
show cg1j laugh onlayer background with dissolve

Jessie "Это всего лишь бумажная работа…"
show cg1j happy onlayer background with dissolve

Jessie "Ладно. Спасибо, Эрни. Я буду довольно поздно, так что можешь съесть йогурт в холодильнике, пока будешь заполнять отчёт."

Scanner "Подожди. Ты всё ещё с дикобразом?"
show cg1e annoyed onlayer middle with dissolve

"Мои зубы заскрипели, а плечи напряглись."

Scanner "Скажи подруге, что мы уже скучаем по её темпераменту! Надеемся, что у отдыхающих в Туалэми хорошие стоматологи!"
show cg1e jerkface onlayer middle with dissolve

"Я протягиваю руку и вырываю рацию у Джесси."

Eve "Закрой рот, Эрнандес! Или {i}твоей{/i} жирной задницы понадобится стоматолог и--"
show cg1j annoyed onlayer background with dissolve

"Джесси отбирает у меня рацию, а Эрни хихикает."

Jessie "Просто положи отчёт на мой стол к завтрашнему дню! Конец связи!"
show cg1e annoyed onlayer middle with dissolve

"Я всё ещё пытаюсь схватить рацию, но Джесси швыряет её обратно на приборную панель. Застонав, я скрещиваю руки на груди и смотрю в окно злобным взглядом."
show cg1j happy onlayer background with dissolve

Jessie "Блин. Ты знаешь, что они просто пытаются самоутвердиться за твой счёт. Почему ты всегда клюёшь на их наживку?"
show cg1e jerkface onlayer middle with dissolve

Eve "Потому, что если бы их всех действительно заботила их работа, они бы тоже разозлились."
show cg1e flat onlayer middle with dissolve

Eve "Не то чтобы это было важно…"

"Я уже не уверена, что {i}меня{/i} что-либо заботит."
show cg1j laugh onlayer background with dissolve

Jessie "Так не с каждым, Ева. Здесь ещё есть люди, которым не всё равно."
show cg1e jerkface onlayer middle with dissolve
voice "scripte01s01_b2ccf54a"
Eve "Кто, например? Туристы? Потому что я могу показать тебе камни и деревья, которые один 'художник' посчитал идеальным холстом."
show cg1e annoyed onlayer middle with dissolve

"Я подавляю желание сплюнуть."

Eve "Такие вещи не исправишь за одну ночь."
show cg1j annoyed onlayer background with dissolve

"Тень падает на пронзительный взгляд Джесси."

Jessie "Так же как и его сломанную челюсть. Или твоё отстранение."
show cg1e flat onlayer middle with dissolve

"Я откидываюсь на своё сиденье."

"Чувство стыда или сожаления полностью отсутствует. Всё, что есть - это грызущая пустота, которая змеёй заползла в мою грудь и поселилась там."
show cg1j happy onlayer background with dissolve

"Джесси смягчается. Нежное выражение лица с нотками жалости."

Jessie "Что с тобой случилось? Ты была таким милым кадетом."
show cg1e jerkface onlayer middle with dissolve

Eve "Что? Я уже не милашка?"

"Я хлопаю ресницами, затем закатываю глаза."

"Обычно из-за таких разговоров увольняют людей {i}любой{/i} профессии. И втайне я на это надеюсь."
show cg1j laugh onlayer background with dissolve

Jessie "Всё дело в твоём отношении. Я помню времена, когда ты была энергичной и решительной."
show cg1e annoyed onlayer middle with dissolve

"Она толкает меня."
show cg1j happy onlayer background with dissolve

Jessie "Стань такой снова!"
show cg1e jerkface onlayer middle with dissolve

Eve "Они выбили это из меня."

"Джесси на мгновение хмурится. Затем сжимает руль и натягивает на лицо улыбку. Ямочки на её щеках похожи на тугие барабаны."

stop ambient fadeout 5.0
show cg1j laugh onlayer background with dissolve

Jessie "Тогда давай посмотрим, сможем ли мы запихнуть это обратно!"

play ambient "ambience/car ambience.ogg" fadein 1.5
show cg1e flat onlayer middle with dissolve

Eve "Путем перевода?"
show cg1j laugh onlayer background with dissolve

Jessie "Путём смены обстановки!"
show cg1j happy onlayer background with dissolve

Jessie "Ты полюбишь Луга! В это время года немного прохладно, но ты сможешь уютно укутаться в хижине, которая, кстати, будет в твоём {i}полном{/i} распоряжении."
show cg1j laugh onlayer background with dissolve

Jessie "Можешь поблагодарить за это рейнджера Смита и его пристрастие к джину."
show cg1e annoyed onlayer middle with dissolve

Eve "А туристы на кемпинге?"
show cg1j happy onlayer background with dissolve

"Джесси прикусывает губу. Бросает взгляд через дорогу."
show cg1e jerkface onlayer middle with dissolve

voice "scripte01s01_bf360f67"
Eve "Не думай, что ты самая умная. Когда я была маленькой, мы каждое лето ездили в Туалэми. И я знаю, что там есть кемпинг."
show cg1j happy onlayer background with dissolve

"Она испускает тяжёлый вздох и сдаётся."

Jessie "Сейчас здесь в основном скалолазы и пешие туристы, поскольку дороги только что открылись. Но я уверена, что они нагрянут, как только потеплеет."

Jessie "Я жду, что ты будешь делать свою работу."
show cg1e annoyed onlayer middle with dissolve

Eve "Отлично. Теперь я ещё и няня."
show cg1j annoyed onlayer background with dissolve

Jessie "Помни, на что ты подписалась."
show cg1e jerkface onlayer middle with dissolve

voice "scripte01s01_a2e68c31"
Eve "Поверь мне. Я помню. По крайней мере, помнила до того, как поняла, что этот парк - всего лишь помойка для туристов."
show cg1j happy onlayer background with dissolve
voice "scripte01s01_ab2314ca"
Jessie "Вот почему существует Служба национальных парков. Нам не под силу защитить каждый квадратный дюйм земли, но с большей её частью иы можем справиться."

"Я усмехаюсь."
show cg1e flat onlayer middle with dissolve

Eve "Если бы. Большинство людей считают парки платными дорогами. Они платят, чтобы приехать и уйти в запой на нескольких дней."
show cg1e jerkface onlayer middle with dissolve
voice "scripte01s01_c1d6a8c1"
Eve "Они будут сидеть вокруг костра и говорить о том, насколько они ‘{i}связаны с природой{/i}’. И, может быть, даже напишут стихи об этом."
show cg1e annoyed onlayer middle with dissolve

Eve "А потом оставят огонь тлеть, забудут собрать мусор и свалят."
show cg1j annoyed onlayer background with dissolve

"Джесси съёживается и громко сглатывает. Она глядит на меня этим неловким взглядом, как на уродца, на которого не хочется смотреть, но глаз отвести сложно."

"Но правда {i}именно{/i} уродлива. Так что ладно, пусть."
show cg1j laugh onlayer background with dissolve

"Она натягивает ещё одну из своих улыбок."

Jessie "Ну, именно поэтому мы--"
show cg1e flat onlayer middle with dissolve

Eve "‘{i}Именно поэтому мы здесь,’{/i} правильно? Это наша работа. Обеспечение соблюдения закона о защите земель."
show cg1e jerkface onlayer middle with dissolve

voice "scripte01s01_19f1fa95"
Eve "Но для кого мы защищаем эту землю?"
show cg1j annoyed onlayer background with dissolve

"Я смотрю на Джесси безразличным взглядом, ожидая ответа, которого, я знаю, никогда не будет."

"Точно так же она косится на меня, а треск радио нарушает тишину."
show cg1e flat onlayer middle with dissolve

Eve "Для тех же людей, которые её разрушают."

"Я откидываюсь на спинку сиденья и смотрю в окно."
show cg1e annoyed onlayer middle with dissolve

Eve "И где справедливость в такой работе..."

"Солнце пробивается сквозь прорезь в облаках, но вскоре серое море поглощает его."

"Джесси ничего не говорит. Я слышу, как её кулак сжимает резиновую рукоятку руля. А после наступает тишина."
window hide
$ persistent.unlock_e1c1v1 = True
$ persistent.unlock_e1c1v2 = True
$ persistent.unlock_e1c1v3 = True
$ achievement.grant("Rot")

show black  onlayer forward:
    subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 2.01 rotate None
with fade
hide cg1e annoyed onlayer middle
hide cg1j annoyed onlayer background
hide landscape onlayer background
hide random_dustcloud onlayer forward
"Мы проезжаем поляну, и лес, который преследовал нас до сих пор, заканчивается. Вдали я замечаю гладкую каменную вершину Купола Лемберта."

"Когда я была ещё ребёнком, мы туда иногда забирались. И когда мы достигали вершины, я всегда чувствовала, что ко мне приходит осознание. Всё казалось таким маленьким, а мысли были такими ясными."

"И мне интересно: если бы я стояла там сейчас, почувствовала бы то же самое?"

stop ambient fadeout 3.0

"Важно ли то, что я делаю? Важно ли защищать эту землю и сохранять её достоинство?"

"А если нет, что тогда вообще важно?"
window hide

jump scripte01s02
