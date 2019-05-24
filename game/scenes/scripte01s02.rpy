init:
    $ flash = Fade(.25, 0, .75, color="#fff")


label scripte01s02:
#Scene 2


play ambient "ambience/car ambience.ogg" fadein 1.5
stop music fadeout 1.5

window show

"К тому времени, как мы проезжаем мимо семей с палатками и шезлонгами, небо становится тёмно-серым. Осколки кроваво-оранжевого и красного цветов светятся из открытых небесных карманов."
stop ambient fadeout 3.0
"Заворачиваем влево и едем по короткому, проторённому пути. Шины хрустят грязью и гравием, затем останавливаются."
play sound "sfx/ignition turning off with keys.ogg"
play ambient "ambience/outside daytime ambience.ogg"

"Джесси поворачивает ключ зажигания. Машина заглухает, становится слышно щебетание птиц."

Jessie "Вот мы и на месте."
$ camera_reset()
$ layer_move("background", 1700)
hide black onlayer forward with dissolve
scene black onlayer background with dissolve:
    zoom 0.70
    xalign 0.1
    yalign 0.2
$ layer_move("background", 1700)
scene cabinoutdoor_dusk onlayer background:
    zoom 1.2
    xalign 0.2
    yalign 0.2
$ layer_move("background", 1700)
show eve rangerhat hair bored onlayer middle:
    xpos 0.5
    ypos 1.45
    xanchor 0.5
    yanchor 1.0

with dissolve

play sound "sfx/car door closing.ogg"
play music audio.anchors

"Я выхожу из машины и вытаскиваю свои вещи из багажника."

"Потянувшись, я обвожу взглядом хижину."

$camera_move(6000, 0, 0, 0, duration=10, warper='ease')
show eve transparency hair bored onlayer middle:
    ease 7.0 alpha 0.30 additive -0.75
    ease 10.0 xpos 0.50 ypos 1.45 xanchor 0.5 yanchor 1.0

"Это скромное здание, охраняемое множеством деревьев, которые устремляются далеко в небо и нависают над остроконечной крышей."

"Почти каждый дюйм хижины построен из одного вида отшлифованной древесины. Очень гладкая. У древесной коры должно быть больше текстуры."

scene cabinoutdoor_dusk onlayer background:
    zoom 1.2
    xalign 0.2
    yalign 0.2
$ camera_reset()
$ layer_move("background", 1700)
show eve rangerhat hair bored onlayer middle:
    xpos 0.3 ypos 1.45 xanchor 0.5 yanchor 1.0 alpha 1.0 additive 0.0
show jessie hat happy onlayer middle:
    xpos 0.7 ypos 1.5 xanchor 0.5 yanchor 1.0
with flash

Jessie "Не слишком маленькая для тебя?"

"Джесси подходит ко мне, крутя ключи на пальце."

"Я оглядываюсь через плечо. За густым рядом деревьев можно увидеть соседний лагерь туристов. Через листву изредка проглядывают палатки."
show eve rangerhat scratch deepthink onlayer middle with dissolve:
Eve "Не. Идеально."

play sound "sfx/cabin porch creak.ogg"
"Деревянный пол скрипит под нашими сапогами, когда мы поднимаемся по ступенькам."
show jessie hat neutral onlayer middle with dissolve
voice "scripte01s02_c8932cdc"
Jessie "Рядом есть ещё одна станция, но они в основном занимаются скучными бюрократическими делами. Они тебя трогать не будут, но тебе, возможно, придётся подменять их на выдаче разрешений, если они выйдут на обед или ещё куда-нибудь."
show eve rangerhat scratch annoyed onlayer middle with dissolve:

Eve "А у меня есть выбор?"
show jessie hat smug onlayer middle with dissolve:

Jessie "Боюсь, что нет, дорогая."

"Её мелодичный голос и пружинистая походка сбивают меня с ног."
show jessie hat ditzy onlayer middle with dissolve:

Jessie "Зная тебя, ты бы заставляла прыгать в озеро, прежде чем выдавать разрешение на ловлю рыбы."

"Да, она меня хорошо знает."

stop ambient fadeout 1.5
play sound "sfx/cabin door open.ogg"
scene cabininside_day1 onlayer background
$ camera_reset()
$ layer_move("background", 1860)
$camera_move(1832, 0, 407, 0, duration=0)
hide eve onlayer middle
hide jessie onlayer middle
with fade
$camera_move(-1822, 0, 407, 0, duration=7, warper='ease')

play ambient "ambience/cabin daytime room tone.ogg"
"Джесси открывает дверь, и мои ноздри атакует затхлый запах сырого дерева."

Jessie "О, уютно!"

"Джесси включает свет и отступает в сторону."
voice "scripte01s02_a831912a"
Eve "Очень точное описание."

"Улыбка на моём лице выдаёт сарказм."

"Мне это напоминает диораму в обувной коробке. Всё пространство используется, и все вещи именно там, где должны быть. От пухлой кровати, угнездившейся в углу, до камина, сложенного из кирпичей, в центре стены."

"Даже телевизора нет. Только кресло-качалка, обитый кожей диван и кофейный столик."

scene cabininside_day1 onlayer background
$ camera_reset()
$ layer_move("background", 1860)
show eve rangerhat hair bored onlayer middle:
    xpos 0.7 ypos 1.45 xanchor 0.5 yanchor 1.0  alpha 1.0 additive 0.0
show jessie hat happy onlayer middle:
    xpos 0.3 ypos 1.5 xanchor 0.5 yanchor 1.0
with fade


"Джесси скользит пальцем по столу, затем осматривает его прищуренным взглядом."

show jessie hat curious onlayer middle with dissolve

Jessie "Хм. Не так пыльно, как я думала."
show eve rangerhat scratch deepthink onlayer middle with dissolve

Eve "Может, рейнджер Смит и 'Виндекс' прибухнуть любил?"

show eve ranger scratch deepthink onlayer middle with dissolve:

"Я бросаю сумки и запускаю шляпу на диван. Однако она не долетает и падает на пол."
show jessie hat serious onlayer middle with dissolve:

Jessie "Разве что он пробирался сюда недавно…"

$camera_move(0, 0, 200, 0, duration=3, warper='ease')
show jessie hat serious onlayer middle:
    ease 2.0 xpos -0.21 ypos 1.5 xanchor 0.5 yanchor 1.0
show eve ranger scratch deepthink onlayer middle:
    ease 1.5 xpos 0.45 ypos 1.45 xanchor 0.5 yanchor 1.0

play sound "sfx/walking on cabin floor.ogg"
"Деревянный пол прогибается под ногами. Дохожу до камина, который всё это время притягивал мой взгляд. На куче пепла лежит несгоревшее полено."
show eve ranger scratch bored onlayer middle with dissolve

"Паутина опутывает хорошо подметённые углы и полированный пол, словно её намеренно пропускали. Здесь чисто, но кто бы ни был этот чистюля, кишка у него тонка."

"С потолка на паутине спускается пушистый паук. Я смотрю, чтобы убедиться, что Джесси не видит, а потом слегка машу ему, когда он качается передо мной."

"Мой голос переходит в шёпот."
show eve ranger scratch softsmile onlayer middle with dissolve:

Eve "Привет."

show jessie hat curious onlayer middle:
    ease 0.3 xpos 0.08 ypos 1.55 xanchor 0.5 yanchor 1.0 rotate 42
show eve ranger scratch scared onlayer middle:
    ease 0.1 xpos 0.45 ypos 1.43 xanchor 0.5 yanchor 1.0
    ease 0.1 xpos 0.50 ypos 1.43 xanchor 0.5 yanchor 1.0
    ease 0.1 xpos 0.50 ypos 1.45 xanchor 0.5 yanchor 1.0


Jessie "Что это было?"
show eve ranger hair blush onlayer middle with dissolve:

Eve "Н-Ничего!"

show jessie hat curious onlayer middle:
    ease 1.5 xpos -0.21 ypos 1.5 xanchor 0.5 yanchor 1.0 rotate 0.00
show eve ranger hair blush onlayer middle:
    ease 0.5 xpos 0.45 ypos 1.45 xanchor 0.5 yanchor 1.0

"Быстрым движением паук отскакивает от меня и приземляется на стену между тремя картинами, висящими над обеденным столом."

show eve ranger hair bored onlayer middle:
    xpos 0.45 ypos 1.45 xanchor 0.5 yanchor 1.0 alpha -0.13

$all_moves(camera_check_points={u'y': [(-1589, 0, u'linear')]})
show girls onlayer forward:
    subpixel True xpos 0.54 ypos 1.1 xanchor 0.5 yanchor 1.03 rotate None
with dissolve

"Расположенные треугольником картины демонстрируют великолепные пейзажи и живописные виды. Вместо подписи художника, в углу нацарапаны названия изображённых мест."

show jessie hat curious onlayer middle:
    xpos 1.2 ypos 1.5 xanchor 0.5 yanchor 1.0

"Йосемити. Зайон. Йеллоустон."

"Национальные парки. И все они прекрасны."

"Паук ползёт по картине Зайона. На ней, густая зелень простирается в глубокую долину, охраняемую с обеих сторон огненно-красными скалами."

"Картина Йеллоустона изображает извилистую тропу, спиралью поднимающуюся на вершину горы. Яркие пятна деревьев разбросаны по густому горному склону. А за горой, плоские равнины устремляются вдаль и затем погружаются в каньон."

"И, наконец, над ними, Йосемити."

"Это место я хорошо знаю. Отсюда нужно сделать лишь несколько шагов, чтобы увидеть его."

"Это вершина Купола Лемберта, с которой открывается захватывающий вид на все луга Туалэми. От густого леса до реки Туалэми, которая вьётся до покрытых снегом вершин Сьерра-Маунтинс. Я поднималась туда столько раз, что, наверное, могла бы точно указать, где находится это место."

"Боже, как бы я хотела сейчас оказаться там. Я бы заорала во всё горло. Кричала бы, пока не охрипла. И никто бы меня не услышал."

"Пожалуй, это моё самое любимое место, но что-то в нём было не таким."

"Ещё немного прищурившись и наклонив голову, я понимаю, что картина слишком неровно висит. Рама настолько смещена от центра, что если бы на этой картине был альпинист, он бы упал и разбился насмерть."

"Я аккуратно беру картину за края и начинаю бережно… медленно…, мягко поправлять--"
hide girls onlayer forward
$camera_move(0, 0, 0, 0, duration=0.5, warper='ease')
play sound "sfx/startling creak.ogg"
show eve ranger hair scared onlayer middle:
        xpos 0.45 ypos 1.45 xanchor 0.5 yanchor 1.0 alpha 1.0
$ persistent.unlock_girls = True

"{i}Скриииииииииип{/i}"

Eve "Уоох!"

"Пронзительный скрип, настолько громкий, что чувствуется через половицы, заполняет комнату. По спине пробегает дрожь, и я почти выпрыгиваю из униформы."

show jessie hat happy onlayer middle:
        ease 0.5 xpos 0.99 ypos 1.55 xanchor 0.5 yanchor 1.0 rotate -32.0

Jessie "Боже, такая нервная."

show jessie hat happy onlayer middle:
    xpos 0.7 ypos 1.55 xanchor 0.5 yanchor 1.0 rotate 0.00
show eve ranger hair blush onlayer middle:
    xpos 0.3 ypos 1.45 xanchor 0.5 yanchor 1.0
with dissolve

"Хихикая, Джесси подходит к обеденному столу и облокачивается на него."
show jessie hat neutral onlayer middle with dissolve:
voice "scripte01s02_fc36e17f"
Jessie "Всего лишь хижина оседает. Место старое, поэтому иногда шумит."

"Её голос падает на октаву. Не хватает только фонарика под лицом."
show jessie hat smug onlayer middle with dissolve:

Jessie "Жутковато, да?"
show eve ranger scratch deepthink onlayer middle with dissolve:

Eve "Не то чтобы."

play sound "sfx/cabin porch creak.ogg"
show eve ranger scratch scared onlayer middle with dissolve
show jessie hat happy onlayer middle with dissolve:
"Хижина снова скрипит, и мои плечи напрягаются. Джесси усмехается, её это явно забавляет."

show jessie hat neutral onlayer middle with dissolve:
Jessie "Некоторые из рейнджеров, что тут жили, только и говорили о призраках. Лично я думаю, что проблема в их кофе."

show eve ranger scratch flat onlayer middle with dissolve:

"Джесси берёт с плиты кофеварку и гремит ею. Откинув крышку, она достает со дна маленькую бутылочку дешёвого джина."
show eve ranger hair deepthink onlayer middle with dissolve:

Eve "Вот на что идут наши налоги."
show jessie hat happy onlayer middle with dissolve:

Jessie "Просто будь счастлива, что мы пока не приватизированы -- не забудь утилизировать это."

$camera_move(-815, 0, 300, 0, duration=2, warper='ease')
show jessie hat happy onlayer middle:
    ease 2.0 xpos 0.22 ypos 1.55 xanchor 0.5 yanchor 1.0
show eve ranger hair bored onlayer middle:
    ease 1.0 xpos 0.5 ypos 1.45 xanchor 0.5 yanchor 1.0

"Она протягивает мне бутылку. Я беру её и кладу на кухонную стойку."
show jessie hat curious onlayer middle:
    xpos 0.22
with dissolve
Jessie "Вопрос: как давно ты была на полигоне?"
show eve ranger scratch deepthink onlayer middle:
    xpos 0.5
with dissolve

Eve "Стрельба? Боже, я не знаю..."

"Почёсывая голову, я вспоминаю, когда в последний раз вытаскивала пистолет из кобуры. В моменты слабого искушения (в окружении назойливых туристов) его хочется достать. Но по-настоящему такое случается реже солнечного затмения."
show eve ranger scratch flat onlayer middle with dissolve:

Eve "Думаю, около года назад. Когда ты притащили нас всех туда в наш выходной день."

"Она открывает шкаф, оставляя ключ в двери. В шкафу лежит длинное ружьё."
show jessie hat happy onlayer middle with dissolve:
voice "scripte01s02_e56539c2"
Jessie "Выходной только для вас, ребята. А вот я бы убила ради одного свободного уик-энда."

"Как только слова сорвались с её языка, она бросила взгляд на меня, затем на ружьё."
show jessie hat stress onlayer middle with dissolve:

Jessie "Э-э... Не в этом смысле... Ну... ты знаешь, что я бы на самом деле не стала..."

"Я смотрю прямо сквозь неё, пока она растерянно бормочет."

"Откашливается."
show jessie hat ditzy onlayer middle with dissolve:

Jessie "{i}ТЕМ НЕ МЕНЕЕ{/i}, у нас здесь стандартный помповый Remington 870."

show jessie hat neutral onlayer middle with dissolve:

Jessie "Также известный как - дробовик."

"Ружьё переливается яркими отблесками, и приклад и цевьё имеют глянцевую деревянную поверхность."
show eve ranger hair flat onlayer middle with dissolve:

Eve "Удивительно. Этот даже не выглядит так, будто развалится прямо в руках."

"Я перевожу взгляд на настольное радио, которое наверняка использовали ещё шифровальщики навахо во время Второй мировой."
show jessie hat happy onlayer middle with dissolve:
voice "scripte01s02_b2f00863"
Jessie "Рассчитывай что Министерство внутренних дел расставит приоритеты. Я когда-нибудь отказывалась от нового оборудования?"

"Судя по похотливому взгляду, которым она смотрела на ружье, я думаю, ответ довольно ясен."
show eve ranger hair deepthink onlayer middle with dissolve:

Eve "Всё же, это немного... излишне. Мне не нужно столько оружия для рутинной работы."

"Пистолет {i}и{/i} дробовик? Четвёртое июля на носу?"

show jessie hat neutral onlayer middle with dissolve:
voice "scripte01s02_3662bb70"
Jessie "Это просто предосторожность. Надеюсь, тебе никогда не придётся его использовать. Никто не просит каждый раз брать его на патрулирование, которое, {i}я расчитываю{/i}, ты будешь проводить каждый день."
show eve ranger scratch annoyed onlayer middle with dissolve:

Eve "А я не могу его до рассвета проводить? Чтобы не пришлось ни с кем разговаривать. Вообще."
show jessie hat serious onlayer middle with dissolve:

Jessie "Я не позволю тебе так относиться к этому!"

Jessie "Пока ты под моим присмотром я не позволю тебе стать жутким лесным отшельником. Тебе нужен положительный опыт, ладно?"
show eve ranger hair deepthink onlayer middle with dissolve:

"От набирающих обороты нравоучений Джесси, мой разум затуманивается."

"Когда мои мысли блуждают, я начинаю слышать больше звуков."

"Скрип в доме."

"Завывание ветра."

"Какой-то жуткий вой."
show eve ranger hair annoyed onlayer middle with dissolve:
stop music fadeout 3.0
"Подождите. Какой-то жуткий вой?"

"Если Джесси его и слышала, то проигнорировала, так как её тирада - уже давно не про мою мизантропию - продолжалась."

"Из-за двери начало доноситься шуршание. Сначала мягкое, как шёпот, можно подумать, что это всего лишь шелест листьев. Но чем дальше, тем быстрее шуршание становится, и вскоре оно уже лихорадочно терзает деревянную дверь."

$camera_move(1971, 0, 500, 0, duration=3, warper='ease')
show eve ranger hair annoyed onlayer middle:
    ease 3.0 xpos 0.75 ypos 1.45 xanchor 0.5 yanchor 1.0
show coyote neutral neutral onlayer middle:
    xpos 1.45 ypos 0.56 xanchor 0.5 yanchor 1.0 zoom 0.75
show jessie hat happy onlayer middle with dissolve:
    xpos -0.29 ypos 1.55 xanchor 0.5 yanchor 1.0

play sound "sfx/walking on cabin floor.ogg"
"Я на цыпочках иду к двери."

Jessie "Эй! Не уходи, когда я тебя выгова--"
show eve ranger hair flat onlayer middle with dissolve:

Eve "ШШШ!"

"Я шикаю на Джесси, приложив палец к губам. Наступает тишина."

play sound "sfx/cabin door open.ogg"
"Покрутив холодную ручку, я с лёгкостью открываю дверь."

"Ничего."

show coyote neutral neutral onlayer middle:
    ease 0.5 xpos 0.88 ypos 0.56 xanchor 0.5 yanchor 1.0 zoom 0.75
show eve ranger hair scared onlayer middle:
    ease 0.7 xpos 0.53 ypos 1.45 xanchor 0.5 yanchor 1.0

M1 "{i}Гав!{/i}"
"Подо мной раздаётся гавканье."
show eve ranger hair bigsmile onlayer middle with dissolve:
play music audio.trails
"Я смотрю вниз и встречаюсь глазами с любовью всей жизни."

"Прелестный щеночек, с болтающимися ушками, едва достающими до моих лодыжек, стоит передо мной и тяжело дышит. Его маленькие лапки скребут мои ботинки."

Eve "Мой Бог… Приятель…"

"Я опускаюсь на одно колено. Я глажу его по мягкой, красной, как у лиса шерсти, и моё сердце тает."
show eve ranger hair softsmile onlayer middle with dissolve:

Eve "{i}Что ты здесь делаешь, щеночек? А? Ты потерялся?{/i}"

Pup "{i}Авввввв-- гав!{/i}"

"Отвечая, он слабо завыл, но вой перешёл в лай. С жалобным писком, он прижимается к моему колену."

"Я мертва. Умерла и попала в рай."

Jessie "Ева, отойди от него!"

play sound "sfx/jessie stomping.ogg"
$camera_move(-140, 0, 0, 0, duration=0.5, warper='ease')
show jessie hat serious onlayer middle:
    ease 0.5 xpos 0.53 ypos 1.55 xanchor 0.5 yanchor 1.0
show eve ranger hair nervous onlayer middle:
    ease 0.5 xpos 0.2 ypos 1.45 xanchor 0.5 yanchor 1.0
with dissolve

"Перебегая через всю комнату, Джесси бросается к двери. Изобразив матадора, я отскочила от неё, как от разъярённого быка."

"Джесси топает по полу, каждый раз приближая сапог к щенку."
show jessie hat yell onlayer middle with dissolve:

Jessie "Фу! Фу! Прочь отсюда! Прочь!"

show jessie hat serious onlayer middle:
    ease 0.1 xpos 0.63 ypos 1.55 xanchor 0.5 yanchor 1.0
    ease 0.1 xpos 0.53 ypos 1.55 xanchor 0.5 yanchor 1.0
show coyote neutral onlayer middle:
    ease 0.1 xpos 0.92 ypos 0.56 xanchor 0.5 yanchor 1.0 zoom 0.75
    ease 0.1 xpos 0.88 ypos 0.56 xanchor 0.5 yanchor 1.0 zoom 0.75
pause 0.5
show jessie hat serious onlayer middle:
    ease 0.1 xpos 0.63 ypos 1.55 xanchor 0.5 yanchor 1.0
    ease 0.1 xpos 0.53 ypos 1.55 xanchor 0.5 yanchor 1.0
show coyote neutral onlayer middle:
    ease 0.1 xpos 0.92 ypos 0.56 xanchor 0.5 yanchor 1.0 zoom 0.75
    ease 0.1 xpos 0.88 ypos 0.56 xanchor 0.5 yanchor 1.0 zoom 0.75
pause 0.5
show jessie hat serious onlayer middle:
    ease 0.1 xpos 0.63 ypos 1.55 xanchor 0.5 yanchor 1.0
    ease 0.1 xpos 0.53 ypos 1.55 xanchor 0.5 yanchor 1.0
show coyote neutral onlayer middle:
    ease 0.1 xpos 0.92 ypos 0.56 xanchor 0.5 yanchor 1.0 zoom 0.75
    ease 0.1 xpos 0.88 ypos 0.56 xanchor 0.5 yanchor 1.0 zoom 0.75
pause 0.5
show jessie hat serious onlayer middle:
    ease 0.1 xpos 0.63 ypos 1.55 xanchor 0.5 yanchor 1.0
show coyote neutral onlayer middle:
    ease 0.1 xpos 0.92 ypos 0.56 xanchor 0.5 yanchor 1.0 zoom 0.75

"Щенок гавкает в ответ, будто бросая ей вызов. Но каждый раз, когда этот огромный, беспощадный ботинок продвигается вперёд, его маленькое тельце отскакивает назад."

show jessie hat serious onlayer middle:
    ease 0.5 xpos 0.7 ypos 1.55 xanchor 0.5 yanchor 1.0
show coyote neutral onlayer middle:
    ease 0.5 xpos 1.18 ypos 0.56 xanchor 0.5 yanchor 1.0 zoom 0.75

play sound "sfx/short bush rustle.ogg"
"Противостояние продолжилось на крыльце. С последним оборонительным рыком, щенок удирает в кусты. Его уши торчат из листьев, видимо следит за нами."

show eve ranger hair furious onlayer middle with dissolve

Eve "Какого чёрта? Он же ничего не сделал! Ты напугала его!"

Jessie "Отлично! Может тогда он будет держаться подальше."

"Я уставилась на Джесси, словно на воплощение Дьявола. Именно им она сейчас и была."
show jessie hat yell onlayer middle with dissolve:

Jessie "Не смотри на меня так."
show eve ranger hair annoyed onlayer middle with dissolve

"Я добавила во взгляд ещё больше стали."
show jessie hat serious onlayer middle with dissolve:

Jessie "Осиротевший детёныш койота. Начал бродить возле лагеря, и {i}Смит,{/i} в приступе бесконечной мудрости, решил покормить его."
show eve ranger hair nervous onlayer middle with dissolve

"Я снова посмотрела на кусты, но щенок уже убежал, спрятался где-то среди теней ночного леса."

"Надо будет приготовить для него еду на потом."

show jessie hat yell onlayer middle:
    ease 0.1 xpos 0.67 ypos 1.55 xanchor 0.5 yanchor 1.0


Jessie "Ни при каких обстоятельствах!"

"Джесси пробрала меня до костей лишь одним взмахом пальца."

"Она что… прочитала мои мысли?"

show eve ranger hair furious onlayer middle:
    ease 0.5 xpos 0.25 ypos 1.45 xanchor 0.5 yanchor 1.0

Eve "Я ничего не говорила!"

$camera_move(-1008, 0, 300, 0, duration=1.5, warper='ease')
show jessie hat serious onlayer middle:
    ease 1.5 xpos 0.55 ypos 1.55 xanchor 0.5 yanchor 1.0

Jessie "Но ты {i}подумала{/i} об этом! И если в тебя есть хотя бы капля здравого смысла, ты не станешь…"

"Она делает паузу, взглянув вверх. На небе погас последний проблеск солнечного света."
show jessie hat stress onlayer middle with dissolve:

Jessie "Прочитаю тебе нотацию в следующий раз. Но сейчас я должна вернуться на станцию."
show jessie hat neutral onlayer middle with dissolve:

Jessie "Пока Эрнандес не съел весь йогурт."

show jessie hat ditzy onlayer middle:
    ease 0.2 xpos 0.50 ypos 1.55 xanchor 0.5 yanchor 1.0
    ease 0.2 xpos 0.55 ypos 1.55 xanchor 0.5 yanchor 1.0
    ease 0.2 xpos 0.50 ypos 1.55 xanchor 0.5 yanchor 1.0
    ease 0.2 xpos 0.55 ypos 1.55 xanchor 0.5 yanchor 1.0
pause 1.0
show jessie hat ditzy onlayer middle:
    ease 1.5 xpos 0.61 ypos 1.55 xanchor 0.5 yanchor 1.0
"Оттолкнувшись локтём, она начинает идти к машине."
show eve ranger scratch flat onlayer middle with dissolve:

Eve "Да… Надери ему зад за меня…"

"Я смотрю вниз, на следы от царапин на ботинках, которые истоптали грязь и пыль всех 1200 миль парка. Далеко не такие гладкие или блестящие, как у Джесси."
show jessie hat neutral onlayer middle with dissolve:

Jessie "Что не так? Я думала, ты любишь шутки Эрни."
show eve ranger scratch deepthink onlayer middle with dissolve:

Eve "Ничего. Я в порядке."

"Вдалеке, за стеной деревьев, виднеется оранжевое свечение костра. Приглушённые болтовня и смех туристов проносятся через лес."

show jessie hat happy onlayer middle:
    ease 0.6 xpos 0.46
show eve ranger scratch annoyed onlayer middle with dissolve
"Нежная улыбка расплывается по лицу Джесси. Она подхватывает меня под мышку и обнимает."
show eve ranger scratch deepthink onlayer middle with dissolve:

"Я думаю вырваться, но от неё исходит приятное тепло. А тут довольно холодно."
show jessie hat happy onlayer middle with dissolve:

Jessie "С тобой всё будет хорошо, дорогая."
show eve ranger hair flat onlayer middle with dissolve:

Eve "Ага, пока я не оторву голову очередному туристу."

"Я кладу лоб на её значок. Острые углы впиваются мне в кожу."
show jessie hat sad onlayer middle with dissolve:

Jessie "Эй, не надо тут таких мыслей. Я ручалась за тебя не для того, чтобы ты опять совершила ту же ошибку."
show jessie hat neutral onlayer middle with dissolve:
voice "scripte01s02_363de099"
Jessie "Ты хороший рейнджер, Ева. Если бы среди нас было больше таких, как ты, если бы все больше заботились о том, что нас окружает, и меньше о пособиях... Тогда усилия наши стали бы более действенными."
show jessie hat happy onlayer middle with dissolve:
voice "scripte01s02_0f77af51"
Jessie "Это будет полезным опытом для тебя. Если ты здесь сможешь привести себя в порядок, то ты сможешь что угодно."
show jessie hat neutral onlayer middle with dissolve:
    ease 1.5 xpos 0.61
voice "scripte01s02_94918a76"
Jessie "Хотя бы {i}попробуй{/i} получить от этого удовольствие, ладно?"
show eve ranger scratch deepthink onlayer middle with dissolve:

Eve "Ладно…"

"Она слишком сильно верит в меня. Когда-то всё это может и было правдой, но сейчас я могу взять пособие или отказаться от него {i}и{/i} от парка."

"Ничего из этого не имеет значения."

"Ни для шишек, сидящих наверху. Ни для общественности. Ни для меня."

show jessie hat ditzy onlayer middle:
    ease 1.5 xpos 0.45 ypos 1.55 xanchor 0.5 yanchor 1.0
pause 1.5
show jessie hat ditzy onlayer middle:
    ease 3.0 xpos 1.14 ypos 1.55 xanchor 0.5 yanchor 1.0
show eve ranger hair furious onlayer middle:
    ease 3.5 xpos 1.14 ypos 1.45 xanchor 0.5 yanchor 1.0
"Джесси берёт меня под руку, и мы топаем к машине."
stop ambient fadeout 1.5

$ camera_reset()
$ layer_move("background", 1700)
scene cabinoutdoor_dusk onlayer background:
    zoom 0.90
    xalign 0.2
    yalign 0.2
show jessie hat ditzy onlayer middle:
    ease 3.0 xpos 0.45 ypos 1.55 xanchor 0.5 yanchor 1.0
show eve ranger hair annoyed onlayer middle:
    ease 3.5 xpos 0.61 ypos 1.45 xanchor 0.5 yanchor 1.0
show jessie hat ditzy onlayer middle:
    ease 4.0 xpos 0.3 ypos 1.55 xanchor 0.5 yanchor 1.0
with dissolve

play ambient "ambience/outside daytime ambience with rustling leaves.ogg" fadein 3.0
voice "scripte01s02_653caefe"
Jessie "К тому же, я всего лишь на расстоянии радио-вызова, если соскучишься. Я буду звонить каждый день!"
show eve ranger scratch deepthink onlayer middle:
 xpos 0.61
with dissolve
Eve "Вау. Жду не дождусь."

play sound "sfx/car starting.ogg"
play ambient "ambience/outside daytime ambience with leaves and car.ogg"
"Она забирается в машину и заводит её. Рычание мотора такое громкое, что, кажется, ржавчина на бампере сама собой отвалится."

Jessie "Впредь, без сачкования."

play sound "sfx/car door closing.ogg"
"Она кладёт связку ключей в мою ладонь и хлопает дверью. Яркий свет фар прорезает ночной воздух и подсвечивает затемнённую хижину."

play sound "sfx/car window down.ogg"
"Окно опускается -- опускается до {i}самого{/i} конца. С уверенной ухмылкой, Джесси приподнимает край шляпы."

show black onlayer background
hide eve onlayer middle
hide jessie onlayer middle
hide cabinoutdoor_dusk onlayer background
with dissolve
stop music fadeout 1.5
stop ambient fadeout 1.5
Jessie "И, Ева -- ты не права."

window hide

jump scripte01s03
