label scripte01s04:
#Scene 04
$ camera_reset()
$ layer_move("background", 1860)
$camera_move(-3343, -2444, 400, 0, duration=0)
show cabininside_day1 onlayer background
with dissolve

play ambient "ambience/cabin daytime room tone.ogg"
play sound "sfx/pup panting.ogg" loop
window show

"На щеке чувствуется тёплая сырость. И чьё-то влажное дыхание."

"Я открываю заспанные глаза и перевожу взгляд на край кровати."

show coyote neutral onlayer middle with dissolve:
    xpos 0.17 ypos 0.02 zoom 1.3

"Там сидит щенок и упорно дышит мне в лицо. Длинный язык свисает из пасти."

show coyote neutral onlayer middle:
    ease 0.2 xpos 0.17 ypos -0.02 zoom 1.3
    ease 0.2 xpos 0.17 ypos 0.02 zoom 1.3
Pup "{i}Гав!{/i}"

Eve "Не может быть, что уже утро."

stop sound fadeout 1.5
play ambient "ambience/cabin daytime room tone.ogg"
show coyote neutral onlayer middle:
    ease 0.5 xpos 0.76 ypos 0.02 zoom 1.3
pause 1.0
hide coyote onlayer middle
"Щенок спрыгивает с кровати и убегает, скользя по полу, как по катку."

"Комната наполняется детским хихиканьем, за которым следует уже знакомый звук хлопающих крыльев. Зайон пыхтит, сворачивая за угол. Щенок бежит за ней."

"Я, должно быть, спала не больше часа."

"Глядя на настольные часы, я вспоминаю, как всю ночь смотрела то на них, то на незванных гостей, укутанных в спальные мешки."

"В 3:30… В 3:45… В 4:20… В 5:00… и наконец в 6:30."

"Я чувствую себя Златовлаской. Сплю на кровати, пока медведи дремлят в углу. Проверяю своё везение в надежде, что медведи не захотят со мной расправиться."

play sound "sfx/curtains.ogg"
$camera_move(375, -2444, -300, 0, duration=3, warper='ease')
show cabininside_day2 onlayer background
show eve ranger hair deepthink onlayer middle:
    xpos 0.5 ypos 1.2 xanchor 0.5 yanchor 1.0
with dissolve
"Я вылезаю из постели и задергиваю занавеску, которая разделяет комнату. Переодевшись в униформу, выскальзываю обратно, и до меня доносится какой-то вкусный запах."
show coyote onlayer middle:
    xpos 0.07 ypos 0.52 xanchor 0.5 yanchor 1.0
show zion hands happy onlayer middle:
    xpos 0.19 ypos 0.93 xanchor 0.5 yanchor 1.0 zoom 0.81
with dissolve
Zion "Доброе утро, мисс Ева."

"Зайон перестаёт играть с щенком и вежливо кланяется мне. В открытое окно влетает синяя птица и садится ей на плечо."

"Уже мечтаю снова оказаться в кровати."

play music audio.bursting
show yellow tea peace wink onlayer middle with dissolve:
    xpos 0.91 ypos 1.25 xanchor 0.5 yanchor 1.0 zoom 0.95
Yellowstone "Проснись и пой, Ева, которая здесь работает! Как прошло свидание с Песочным Человеком?"

"Йеллоустон выглядывает из кухни с миской в руках. И опять с чайником на голове."
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Эмм… Кажется, он решил долго не задерживаться."

show coyote onlayer middle:
    ease 1.0 xpos -0.25 ypos 0.52 xanchor 0.5 yanchor 1.0
show zion hands happy onlayer middle:
    ease 1.0 xpos -0.25 ypos 0.93 xanchor 0.5 yanchor 1.0 zoom 0.81
show eve ranger scratch annoyed onlayer middle:
    ease 0.8 xpos 0.15 ypos 1.2 xanchor 0.5 yanchor 1.0
show yosemite back bored onlayer middle with dissolve:
    xpos 0.53 ypos 1.3 xanchor 0.5 yanchor 1.0

Yosemite "Или не выдержал твоего храпа. Когда ты ворочаешься, звучишь как поломанный двигатель."

"Йосемити сидит по подбородок в книге и перелистывает страницы. Я бросаю взгляд на стол. Он завален бумагами. Одни валялись, как перетасованная колода карт, другие были сложены в покосившиеся башни. И посреди всего этого, словно глаз шторма, стоит картонная коробка."

"Не отрывая взгляда от книги, она поднимает руку с кофейной чашкой."
voice "scripte01s04_a2d0a98c"
Yosemite "Йеллоустон. Чай."
show yellow tea hips wink onlayer middle with dissolve

Yellowstone "Я мигом!"
show yellow tea hips wink onlayer middle with dissolve

play sound "sfx/pouring tea.ogg"
"Йеллоустон врывается в комнату. Наклоняет голову, и вода из чайника наливается в чашку. Очень точно и аккуратно. Она похожа на балерину, ихображающую лебедя. Несмотря на раскачивание и шатание, чайник остаётся сбалансированным на вершине её конусообразной головы."
show yellow tea hips happy onlayer middle with dissolve

Yellowstone "Тебе заменить пакетик? Там одна вода уже."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Не будь транжирой. Тут ещё осталось немного вкуса."
show yellow tea hips pout onlayer middle with dissolve

Yellowstone "Ладно, ладно."

"Йеллоустон побеждённо вздыхает. Я так вздыхаю каждый раз, когда приходится кому-то говорить, ‘да, вам нужно разрешение, чтобы ловить здесь рыбу.’"
show yellow tea hips wink onlayer middle with dissolve
voice "scripte01s04_691176c1"
Yellowstone "Как насчёт тебя Ева? Я видела, ты вчера хлебала кофе. Бьюсь об заклад, что чисто чёрный. Ты похожа на тех кошечек, что предпочитают чисто чёрный."

"Я беру паузу, чтобы разобраться в странном выборе слов Йеллоустон. Какой-то языковой Франкенштейн, серьёзно."
show eve ranger hair deepthink onlayer middle with dissolve

Eve "Вообще-то, с щепоткой сахара."
show yellow tea hips pout onlayer middle with dissolve

Yellowstone "Блин. Думала, что угадала."

"Она щёлкает пальцами и убегает на кухню."
show yellow tea hips wink onlayer middle with dissolve

Yellowstone "Ладно. Падай на корты. Притащу тебе кружку."
show eve ranger scratch nervous onlayer middle with dissolve

Eve "Падай… чего?"
show zion arms curious onlayer middle with dissolve

show zion arms curious onlayer middle:
    ypos 1.13 xanchor 0.5 yanchor 1.0 zoom 0.81 rotate 22
    ease 1.5 xpos 1.61 ypos 1.13 xanchor 0.5 yanchor 1.0 zoom 0.81 rotate 22
Zion "Она сказала, ‘присядь.’"
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Не могу. У меня работа, которую надо делать. Патрулировать. Выдавать разрешения. Отвечать на вызовы--"
show yosemite back bored onlayer middle with dissolve

Yosemite "Стучать на нас начальству."

"Она приподнимает бровь и отпивает из чашки."
show eve ranger scratch softsmile onlayer middle with dissolve

Eve "Приоритет номер один, уверяю тебя."
show eve ranger hair deepthink onlayer middle with dissolve

"Я фальшиво улыбаюсь и закатываю глаза. Надеюсь, она это заметила."

"Но да, она права. Это совершенно вылетело у меня из головы. Думаю, когда стало ясно, что они не собираются меня убивать, мой разум начал дрейфовать в сторону более абстрактных вопросов."
show yellow tea peace happy onlayer middle with dissolve

Yellowstone "Ты можешь всё это отложить на потом! Подыши пока свежим утренним воздухом. Я делаю блинчики!"

$camera_move(5904, -2444, 300, 0, duration=3.0, warper='ease')
show zion arms flat onlayer middle:
    xpos 1.33 ypos 1.05 xanchor 0.5 yanchor 1.0 rotate 0 zoom 0.81
    ease 3.0 xpos 0.56 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.81
show yosemite back bored onlayer middle:
    ease 4.5 xpos 0.15 ypos 1.3 xanchor 0.5 yanchor 1.0

Zion "Еееееей..."

"Вот только тихое веселье Зайон не соответствует её печальному лицу."
show yellow tea hips wink onlayer middle with dissolve

Yellowstone "Не волнуйся, милашка. Я сделаю овощной омлет {i}специально{/i} для тебя."
show coyote onlayer middle:
        xpos 1.47 ypos 0.52 xanchor 0.5 yanchor 1.0
show zion hands happy onlayer middle with dissolve

"Подавленное лицо Зайон оживляется. С надеждой, но настороженно."

Zion "А ты положишь грибы, которые я недавно собрала?"
show yellow tea hips happy onlayer middle with dissolve

Yellowstone "Положу, если ты мне их принесёшь."

show zion hands happy onlayer middle:
    ease 1.5 xpos -0.45 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.81
show coyote onlayer middle:
    ease 3.0 xpos -0.45 ypos 0.52 xanchor 0.5 yanchor 1.0
"Воодушевлённо кивнув, Зайон пошаркала к шкафу. А следом за ней щенок. Птицы тоже за ней следуют."

show yosemite back neutral onlayer middle with dissolve:
    xpos 0.52 ypos 1.4 xanchor 0.5 yanchor 1.0
Yosemite "Не забудь помыть их!"

"Йосемити кричит, но никто не отвечает. Зайон роется в шкафу. Йеллоустон напевает себе под нос, не попадая в ноты."
show yosemite back bored onlayer middle with dissolve

Yosemite "Отлично. Не жалуйтесь мне, когда покроетесь плесенью с ног до головы..."

play sound "sfx/pan sizzling.ogg" fadein 3.0 loop

hide yosemite onlayer middle
hide yellow onlayer middle
hide zion onlayer middle
hide coyote onlayer middle
with dissolve
$camera_move(-239, -2444, 0, 0, duration=3.0, warper='ease')
show eve ranger hair deepthink onlayer middle with dissolve:
    xpos 0.47 ypos 1.2 xanchor 0.5 yanchor 1.0
pause 3.5
$camera_move(4145, -2444, 0, 0, duration=2.0, warper='ease')
show eve ranger hair deepthink onlayer middle:
    ease 2.0 xpos 0.98 ypos 1.2 xanchor 0.5 yanchor 1.0

"На фоне шипит сковорода. Все занимаются утренними делами, вязнут в рутине, а я остаюсь в стороне. Делать мне нечего (кроме как трястись за свою жизнь, хотя, будем честными, причин бояться уже нет), поэтому я сажусь за стол и открываю тетрадь."


$camera_move(4725, -3062, 100, 0, duration=1.5, warper='ease')
show yosemite back bored onlayer middle with dissolve:
    xpos 0.46 ypos 1.35 xanchor 0.5 yanchor 1.0

"Стол круглый, поэтому приходится сидеть лицом к лицу с Йосемити. Если это и беспокоит её так же, как меня, она этого не показывает. Она берёт чистый лист бумаги с верха неустойчивой стопки и начинает выписывать что-то из книги."

"Я вполне могу разделить трапезу с кем-то (или чем-то), кто пытался выгнать меня с поста. И уж тем более могу посидеть с этим кем-то за одним столом."

"Тем не менее, я пытаюсь очистить свой разум и начать записывать события прошлой ночи. Но моя тесная униформа сжимает суставы, как питон. Писать неудобно, записи выходят сухими, будто отчёт для Джесси, а не глубокое, эмоциональное выражение Тедди. Не то чтобы во мне ещё остались эмоции."

"'{i}Нападающий{/i} вышел из шкафа. {i}Злоумышленник{/i} отобрал у меня дробовик.'"

"Это лишь пара примеров. Всё по существу. Достаточно связно, чтобы передать информацию. Но сухо, а поэтому расплывчато и непонятно. Это всё произошло со мной, но даже я с трудом понимаю что это было."

"Чёрт, я едва понимаю, что {i}они{/i} такое."

stop sound fadeout 3.0
"Они не призраки -- а я дура, потому что хотя бы секунду в это верила. Но они и не совсем люди. Если не считать их ушей, крыльев и вулканов на голове, они вполне могут быть людьми."

show yellow tea peace wink onlayer middle with dissolve:
    xpos 0.72 ypos 1.25 xanchor 0.5 yanchor 1.0 zoom 0.95
Yellowstone "С щепоткой сахара для сладенькой Евы."

play sound "sfx/setting down coffee cup.ogg"
"Йеллоустон ставит передо мной чашку кофе, в которой всё ещё кружится дорожка зернистого сахара."
show yellow tea peace concern onlayer middle with dissolve

play sound "sfx/frying pan explodey.ogg"
stop music fadeout 1.5
"Из кухни доносятся взрывные хлопки. Над сковородой клубится дым."

Yellowstone "Ай! Мои блинчики!"

show yellow tea hips comiccry onlayer middle:
    ease 0.5 xpos 1.42 ypos 1.25 xanchor 0.5 yanchor 1.0 zoom 0.95
show eve ranger hair deepthink onlayer middle:
    ease 0.5 xpos 0.9 ypos 1.2 xanchor 0.5 yanchor 1.0
"Она убегает, как заработавшаяся служанка на званом ужине."

"А что же я? Я чувствую себя исследователем космоса. Я нашла инопланетное общество, и всё, что они делают, удивляет своей обыкновенностью."
show yosemite back annoyed onlayer middle with dissolve
Yosemite "Глазеть не вежливо. Отвернись, если мы так тебя раздражаем. Или уходи. Это тоже решит проблему."
show eve ranger hair flat onlayer middle with dissolve
play music audio.bitter

Eve "Ты бы этого хотела, да? Чтобы я ушла, а ты могла продолжать спокойно жить на всём готовеньком?"
show yosemite back smug onlayer middle with dissolve

Yosemite "Ты ожидаешь услышать ‘нет’? Все остальные головорезы, как только пронюхивали о нас, тут же убегали подальше. Возвращались только, чтобы вещи забрать. И то, не по одиночке."

"Всё её вчерашнее сочувствие испарилось, как роса на траве. Осталась только снисходительная ухмылочка."

"Она сводит меня с ума."
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Что ж, я не такая, как остальные -- слава Богу. Их напугать проще лёгкого."

Yosemite "Но не тебя, да?"
show eve ranger hair deepthink onlayer middle with dissolve

Eve "Я открыта для предложений."

"Я опрокидываю в себя кофе, словно это самый отвратительный шот из дешёвого бара. Обжигающая жидкость стекает по горлу. Затем я сдаюсь на милость своему дневнику."
show yosemite back neutral onlayer middle with dissolve

"Йосемити смотрит на меня прищуренным взглядом."

Yosemite "Что это? Официальный отчёт главному головорезу?"

"От раздражения я нажимаю на карандаш, и кончик грифеля ломается, оставляя жирную полосу на бумаге."
show eve ranger hair annoyed onlayer middle with dissolve

Eve "Дневник. Извини, что разочаровала."
show yosemite back curious onlayer middle with dissolve

"От слова ‘дневник’ её уши начинают дёргаться."
show yosemite back happy onlayer middle with dissolve

Yosemite "Дневник для чего? Чтобы документировать информацию? Для учёбы?"
show eve ranger scratch deepthink onlayer middle with dissolve

Eve "Просто дневник. Я его использую, чтобы пробудить ту последнюю крупицу себя, которой не наплевать на всё. Не даёт мне оторваться от реальности."
show yosemite back neutral onlayer middle with dissolve

show eve ranger scratch flat onlayer middle with dissolve

"Я присматриваюсь к её волосам. Синие, с чёрными корнями и матово-белыми кончиками. Похожи на водопад, падающий, со скалы."
show eve ranger scratch deepthink onlayer middle with dissolve

Eve "И Боже мой, как мне это сейчас нужно."
show yosemite back bored onlayer middle with dissolve

Yosemite "Полагаю, я должна гордиться тобой."

"Я продолжаю писать. Даже взглядом её не удостою."

show yosemite back smug onlayer middle with dissolve

Yosemite "В конце концов, много ли работников парка вообще умеют писать?"
show eve ranger scratch annoyed onlayer middle with dissolve

"Проклятье, я не могу сдержаться."
show eve ranger scratch furious onlayer middle with dissolve

Eve "Думаешь, мы тупые?"
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Я думаю, что вы необразованные."
show eve ranger hair deepthink onlayer middle with dissolve

Eve "Слушай, я тоже от своих коллег не в восторге--"
show yosemite back bored onlayer middle with dissolve

Yosemite "Рада, что мы сошлись на этом."
show eve ranger hair annoyed onlayer middle with dissolve

Eve "{i}Но{/i}, отдай нам должное. Или хотя бы мне отдай должное. Ты же знаешь, что такое колледж?"
show yosemite back smug onlayer middle with dissolve

Yosemite "Полагаю, место, в которое ты не ходила?"
show eve ranger hair furious onlayer middle with dissolve
voice "scripte01s04_e63689f5"
Eve "Ха-ха-ха -- нет. Для меня, колледж был годами беспросветного дерьма, через которое пришлось продираться только, чтобы--"
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Это того стоило?"
show eve ranger hair annoyed onlayer middle with dissolve

"Вопрос, как ушат холодной воды. Заставляет меня решить, хочу ли я дать простой ответ или ответ, который скрывается в глубине моего сердца."
show eve ranger scratch deepthink onlayer middle with dissolve
voice "scripte01s04_fc156bc7"
Eve "Устоявшееся мнение - гигантское {i}нет{/i}. Все эти страдания не были бы напрасны, если бы людям было не плевать. Когда-то я думала, что это всё не зря. Но если я сохраняю землю для этих безразличных уродов, то вся затея никогда не будет иметь смысла."
show yosemite back bored onlayer middle with dissolve

"Йосемити зевает, изображая скуку, и возвращается к книге."

Yosemite "Вау. А я почти ожидала что-то глубокое."
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Не нравятся ответы? Не задавай вопросов."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Подобные ответы меня не волнуют. Исходящие из маленького прогнившего умишка."

"Между нами вспыхивает молния. Мы молча смотрим друг на друга. Я не моргну, даже если глаза начнут вываливаться."
voice "scripte01s04_e6b29de1"
stop music fadeout 1.0
Yellowstone "Перегрызть друг другу глотки можете после завтрака. Время заточить вкусняшки!"
play music audio.bursting
show yellow volcano hips wink onlayer middle
show yellow volcano hips wink onlayer middle:
    ease 1.5 xpos 0.75 ypos 1.25 xanchor 0.5 yanchor 1.0 zoom 0.95
show eve ranger scratch annoyed onlayer middle:
    ease 1.5 xpos 0.99 ypos 1.2 xanchor 0.5 yanchor 1.0
play sound "sfx/setting down plates.ogg"
"Йеллоустон влетает с двумя тарелками пышных, сложенных друг на друга блинчиков. Наверху каждой стопки лежит по куску масла, которое плавится и стекает по бокам блинчиков, смешиваясь с сиропом."
show eve ranger hair flat onlayer middle with dissolve

"Я тыкаю блинчики вилкой."

"Они отравлены?"
show eve ranger hair deepthink onlayer middle with dissolve

"{i}Выглядят{/i} нормально. На самом деле, {i}выглядят{/i} очень вкусно. Как фото из меню, которое, разумеется, к самому блюду имеет слабое отношение."
show eve ranger hair flat onlayer middle with dissolve

"Я отрезаю кусок боковой частью вилки, макаю его в сироп на краях тарелки."
show eve ranger scratch deepthink onlayer middle with dissolve

"Ээ, почему бы и нет? Даже если отравлюсь, то хотя бы вкусно поем."

"Я делаю решительный шаг."
show eve ranger scratch blush onlayer middle with dissolve

"Тёплый сахар стекает по языку. Из блинчика сочится масло. Поджаренные, пресные края слегка хрустят, идеально балансируя со сладким сахарным вкусом. Блинчик буквально тает у меня во рту."

"Я проглатываю."

Eve "Святые тефтельки."

"Из меня вырывается стон. Было бы неловко, если бы это не было так шокирующе. Или вкусно. Боже мой."
show yellow volcano hips happy onlayer middle with dissolve

"Йеллоустон хихикает."
show yellow volcano hips excited onlayer middle with dissolve

Yellowstone "Нравится?"

"Не в силах сопротивляться, я пихаю в рот следующий кусок. Киваю и пытаюсь прочавкать ответ."
show eve ranger scratch softsmile onlayer middle with dissolve

Eve "Ага! Это… типа невероятно. Как ты вообще…?"
show yellow volcano hips wink onlayer middle with dissolve

Yellowstone "Я типа местного шеф-повара."

"Она сияет гордой улыбкой."
show yellow volcano hips happy onlayer middle with dissolve

Yellowstone "... А ещё я горничная, посудомойка и стиралка."
show yellow volcano peace wink onlayer middle with dissolve
voice "scripte01s04_32c39275"
Yellowstone "Можно сказать, что я предоставляю все услуги по дому. И всё делаю, как мастер!"
show eve ranger hair softsmile onlayer middle with dissolve

Eve "Никаких сомнений. Что ты туда такого положила?"
show yellow volcano peace smug onlayer middle with dissolve

Yellowstone "Секрет фирмы."
show yosemite back bored onlayer middle with dissolve

"Йосемити переворачивает страницу."

Yosemite "Это ореховое масло."
show yellow smoke hips pout onlayer middle with dissolve

Yellowstone "Так нечестно!"

"Тёмное облако пара вырывается из отверстия в её голове. Кажется, я чувствую запах серы."
show eve ranger scratch deepthink onlayer middle with dissolve

Eve "Что бы это ни было, это вкусно."

"Я смываю шок глотком кофе."
show eve ranger scratch softsmile onlayer middle with dissolve

Eve "Спасибо."
show yellow volcano hips blush onlayer middle with dissolve

"Глаза Йеллоустон становятся большими, как тарелки с блинчиками."

Yellowstone "Ты реально это сказала? {i}Спасибо?{/i}"
show eve ranger scratch nervous onlayer middle with dissolve

"Она бы предпочла, чтобы я послала её подальше?"
voice "scripte01s04_f052b87d"
Eve "Эм… да? Я вообще собиралась жить на консервах, пока нахожусь здесь."
show yellow gayser hips comiccry onlayer middle with dissolve

play sound "sfx/yellowstone geyser.ogg" fadein 2.0 loop
"Слёзы подступают к уголкам её глаз. Затем из её головы вырывается водяной гейзер."
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Вау."

Yellowstone "Святые небеса, я и не знала, что похвала - это так приятно. Т-ты похоже хорошая девчонка."

"Из её головы вырывается вода. С таким водяным зонтиком она подошла и обняла меня одной рукой."
show eve ranger scratch deepthink onlayer middle with dissolve

"Я вжимаюсь в спинку кресла, так как не особый фанат обниманий. И прикосновений. И одежды, мокрой от слёз."
show yellow volcano hips excited onlayer middle with dissolve

stop sound fadeout 1.0
Yellowstone "А! Я кое-что придумала!"

"Она отскакивает обратно, как пружина."
show yellow volcano peace happy onlayer middle with dissolve
voice "scripte01s04_387af076"
Yellowstone "Что если -- проследите за моей мыслью -- вместо того, чтобы мы ушли, или ты ушла, или кто-либо ушёл -- мы бы пожили все вместе?!"
show yosemite back yelling onlayer middle with dissolve
voice "scripte01s04_447c9097"
Yosemite "Абсолютно нет!"
show eve ranger hair annoyed onlayer middle with dissolve

Eve "Чтобы всё было, как прошлой ночью? Только каждую ночь?"
show yellow volcano hips wink onlayer middle with dissolve

Yellowstone "Да просто подумайте! В хижине есть всё, что нужно для жизни! Мы могли бы держать дом в чистоте и порядке, пока ты работаешь!"
show eve ranger hair deepthink onlayer middle with dissolve

"Я слишком ошеломлена, чтобы решительно отказать. На такую бесстыдную, украшенную бантиком и протянутую вам в руки, наивность невозможно ответить суровым реализмом. Это искренность, и она мне знакома. А если еда будет всегда такой вкусной, может эта идея и не такая…"
show eve ranger hair annoyed onlayer middle with dissolve

"{i}Какая, Ева?{/i} Невозможная? Потому что этого {i}не{/i} случится."
show eve ranger scratch deepthink onlayer middle with dissolve

"Вспомни зачем ты здесь."

"Выгляни наружу. Посмотри на землю, которую ты любишь, и посмотри на падальщиков, которые топчут её."

"А теперь вспомни зачем ты здесь."
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Я здесь только из-за своей работы. А за няньченье лесных духов мне не доплачивают."
show eve ranger scratch flat onlayer middle with dissolve

Eve "Блинчики были вкусными, но я всё равно собираюсь доложить о вас."
show yellow volcano hips sad onlayer middle with dissolve

"Настрой Йеллоустон потух, как свечка."
show yellow volcano hips comiccry onlayer middle with dissolve

Yellowstone "Ээх… А мне казалось, я классно придумала."
show yosemite back bored onlayer middle with dissolve

"Йосемити с облегчением вздыхает."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Не пугай меня так. Я этой мисс Страдания и так уже сыта по горло."

show zion hands curious at floating onlayer middle with dissolve:
    xpos 0.83 ypos 0.85 xanchor 0.5 yanchor 1.0 zoom 0.81 subpixel True
show yosemite back annoyed onlayer middle:
    ease 1.0 xpos 0.47 ypos 1.35 xanchor 0.5 yanchor 1.0
show yellow volcano hips comiccry onlayer middle:
    ease 1.0 xpos 0.67 ypos 1.25 xanchor 0.5 yanchor 1.0 zoom 0.95
show eve ranger scratch flat onlayer middle:
    ease 1.0 xpos 0.96 ypos 1.2 xanchor 0.5 yanchor 1.0
$camera_move(4827, -3062, 300, 0, duration=1, warper='ease')

"Прежде, чем я успеваю огрызнуться в ответ, Зайон подбегает к Йеллоустон, держа в руках разделочную доску. На доске лежат сушёные грибы, которые поклёвывает синяя птичка."
show zion hands softcry at floating onlayer middle with dissolve

Zion "Это значит, что нам придётся искать новый дом?"

"Зайон уныло смотрит на грибы, но Йеллоустон успокаивающе улыбается ей."
show yellow volcano hips wink onlayer middle
show zion hands nervous at floating onlayer middle
with dissolve

Yellowstone "Не волнуйся! Йосемити знает много отпадных мест, где можно спрятаться! Мы можем довериться ей, как и всегда!"
show yosemite back bored onlayer middle with dissolve

Yosemite "Мы уйдём. А она тут долго не протянет."

"Она наклоняется к столу и смотрит мне в глаза."
show yosemite back smug onlayer middle with dissolve

Yosemite "Видно по её глазам. Понурые и безжизненные, почти, как у остальных."

"Я ей не уступаю, оставаясь спокойной и немигающей."
show yellow volcano hips pout onlayer middle with dissolve
voice "scripte01s04_1ddf0004"
Yellowstone "Твои блинчики станут понурыми и безжизненными, если не съешь их сейчас."

"Йеллоустон выхватывает книгу из рук Йосемити и пододвигает тарелку поближе. Блинчики уже впитали весь сироп, словно губка."
show yosemite back nervous onlayer middle with dissolve

"Йосемити упрямо тянется за книгой, но та в недосягаемости. Она дуется, потом накалывает блинчик на вилку."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Я же читала… Теперь придётся заново искать место."
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Слишком умная для закладки?"
show yosemite back smug onlayer middle with dissolve

Yosemite "Умнее тебя."
show eve ranger scratch softsmile onlayer middle with dissolve

"Мы синхронно откусываем блинчик.  я выдаю ей самую фальшивую, самую пластмассовую улыбку, на какую только способна, заставляя ямочки на щеках болеть."

"Она отвечает тем же. Я будто смотрю в зеркало в комнате смеха."
show yellow volcano hips sad onlayer middle with dissolve

voice "scripte01s04_69fcc9d1"
Yellowstone "То же мне проблема. Ты все книги здесь по пятьдесят раз перечитала, мозгосос."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Это{i}проблема{/i}, и ещё какая. Ты удивишься, как много всего можно пропустить при первом прочтении."
show yosemite back neutral onlayer middle with dissolve

"Её взгляд скользит на Зайон, которая присела на корточки рядом с щенком, позволяя ему понюхать грибы. Лицо Йосемити становится печальным, и я впервые замечаю у неё мешки под глазами."
show yosemite back nervous onlayer middle with dissolve

Yosemite "И как много можно забыть."
show yellow volcano hips happy onlayer middle with dissolve

Yellowstone "Фигово, что Ева не останется надолго. Не успеем её кредиткой воспользоваться. А ты могла бы столько книг заказать!"
show zion hands softsmile onlayer middle with dissolve

Zion "И продукты! Побольше свежих овощей, пожалуйста."
show eve ranger scratch furious onlayer middle with dissolve

Eve "Простите -- {i}что?{i}"
show yosemite back bored onlayer middle with dissolve

"Йосемити отпивает из чашки и пожимает плечами."

Yosemite "Радуйся, что вы, головорезы, вообще годны для чего-то. Они обычно аннулируют карту после первой пары платежей."
show eve ranger scratch softsmile onlayer middle with dissolve

"Я попыталась подавить смешок, но не получилось."
show eve ranger scratch blush onlayer middle with dissolve

"Я такое не должна оправдывать, но образ того, как кто-то вроде Эрни открывает свой счёт и видит неожиданный платёж на 600 долларов, приносит мне странное удовлетворение."
show eve ranger scratch deepthink onlayer middle with dissolve

"И, если честно, нахер Эрни."

"Зайон дёргает Йеллоустон за рукав и поднимает разделочную доску над головой в качестве напоминания."
show zion arms curious onlayer middle with dissolve

Zion "Омлет. Я сейчас окочурюсь от голода."

"Йосемити передёрнуло."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Пожалуйста, перестань учить её своему второму языку."

"Но Йеллоустон игнорирует её реплику. Она наклоняется и берёт доску, её лицо буквально тает от обожания, когда она смотрит на Зайон."
show yellow volcano hips happy onlayer middle with dissolve

Yellowstone "Прости, прости. Шпинат тоже положить?"
show zion arms happy onlayer middle with dissolve

Zion "Ага! Но готовь без масла. Слишком много жира."
show yellow volcano hips concern onlayer middle with dissolve
voice "scripte01s04_e67e4550"
Yellowstone "Эм? Ты уверена? Я хочу, чтобы у тебя было достаточно энергии, чтобы пойти со мной в поход."
show yosemite back bored onlayer middle with dissolve

Yosemite "Я так не думаю. Когда закончите с готовкой, вам ещё предстоит много уборки."
show yellow volcano hips sad onlayer middle with dissolve

Yellowstone "Дай мне передышку! Я только недавно прибиралась."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "А теперь кухня превратилась в зону боевых действий. Прибирись. Пока мы не ушли."
show yosemite back bored onlayer middle with dissolve
show yellow volcano hips pout onlayer middle with dissolve

"Ворча себе под нос, Йеллоустон возвращается на кухню."
voice "scripte01s04_25cf837e"
show yellow volcano hips pout onlayer middle:
    ease 4.0 xpos 1.15 ypos 1.25 xanchor 0.5 yanchor 1.0 zoom 0.95
Yellowstone "Посуда бы не пачкалась так быстро, удосужься ты иногда помыть за собой…"
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Что, прости?"
show yellow volcano hips seriouscry onlayer middle with dissolve
stop music fadeout 1.5
show yellow volcano hips seriouscry onlayer middle:
    ease 0.25 xpos 1.15 ypos 1.19 xanchor 0.5 yanchor 1.0 zoom 0.95
    ease 0.25 xpos 1.15 ypos 1.25 xanchor 0.5 yanchor 1.0 zoom 0.95
Yellowstone "Аргх! Н-ничего, босс!"
show yosemite back bored onlayer middle with dissolve
play music audio.memories
"Йосемити возвращается к книге. Время от времени подъедает блинчики."
show yellow volcano hips pout onlayer middle with dissolve

hide yellow onlayer middle
hide zion onlayer middle
with dissolve
show eve ranger scratch deepthink onlayer middle:
    ease 1.0 xpos 0.9 ypos 1.2 xanchor 0.5 yanchor 1.0
"Убедившись, что Йосемити не смотрит, Йеллоустон показывает ей язык."
show eve ranger hair flat onlayer middle with dissolve

"Это странно. Я не ожидала, что среди них существует какая-то иерархия, но пикси и конусоголовая, кажется, почитают её как старшую сестру. Для полного образа, Йосемити остаётся часами висеть на телефоне и небрежно полистывать модные журналы."
show eve ranger hair deepthink onlayer middle with dissolve

"Девчонки всё ещё подобным занимаются, так ведь?"
show eve ranger hair flat onlayer middle with dissolve

Eve "Наверное увлекательное чтиво, раз даже на пять секунд не можешь оторваться."
show yosemite chin neutral onlayer middle with dissolve

Yosemite "Не то чтобы. Просто кое-какие записи шахтёра, который проходил через эти места давным-давно. Но это помогает."
show eve ranger hair annoyed onlayer middle with dissolve

Eve "С твоим исследованием?"

"Она хмурит брови и искоса глядит на меня."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Не хочешь сказать, как ты узнала об этом?"
show eve ranger hair flat onlayer middle with dissolve

Eve "У тебя на папке буквально написано ‘исследования’. Не трудно было сложить два и два."
show yosemite back smug onlayer middle with dissolve

Yosemite "Смотрите-ка. И считать умеет."
show eve ranger hair annoyed onlayer middle with dissolve

Eve "Составлять фотороботы тоже умеет."

"Она со стоном закрывает глаза."
show yosemite back bored onlayer middle with dissolve

Yosemite "Я знала, что твоё вынюхивание будет проблемой."
show eve ranger scratch deepthink onlayer middle with dissolve

Eve "Не кисни. Внутрь я не заглядывала и ничего не видела."

"Объевшись блинчиками, я расслабляюсь в кресле. Не знаю сколько масла и сахара она в них запихала, но с моей униформы вот-вот слетят пуговицы."
show eve ranger scratch flat onlayer middle with dissolve

Eve "Но должна сказать. Мне любопытно, что может исследовать кто-то вроде тебя."

"Йосемити прижимается к столу. Её лицо возбуждённо вспыхивает."
show yosemite back happy onlayer middle with dissolve

Yosemite "Тебе любопытно?!"
show yosemite back annoyed onlayer middle with dissolve

"Возбуждение нисходит до подозрительности."

Yosemite "{i}Почему?{/i}"
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Просто так?"

"Находясь так близко, я хорошо вижу её чётко очерченное, заострённое лицо. Ни дряблой кожи, ни прыщей. Ни детского жира вокруг щёк."
show eve ranger scratch deepthink onlayer middle with dissolve

Eve "Можно мне немного личного пространства? Не хочу подцепить твой характер."

"Проклятье. Если сильно прищуриться, она даже миленькая."
show yosemite back bored onlayer middle with dissolve

"Она отстраняется и замолкает."
show eve ranger hair flat onlayer middle with dissolve

Eve "Моё любопытство угасает."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Заткнись."

"Она оглядывается по сторонам, покусывая нижнюю губу. Вздыхает и закрывает книгу."
show yosemite chin neutral onlayer middle with dissolve

Yosemite "Ты заметила голову Йеллоустон?"
$camera_move(6000, -3062, 300, 0, duration=1.5, warper='ease')
show eve ranger hair flat onlayer middle:
    ease 1.5 xpos 0.63 ypos 1.2 xanchor 0.5 yanchor 1.0
show yellow volcano hips happy onlayer middle with dissolve:
        xpos 1.05 ypos 1.25 xanchor 0.5 yanchor 1.0 zoom 0.95
"Она наклоняется поближе ко мне и переходит на хриплый шёпот."

"Я повторяю за ней."
show eve ranger scratch deepthink onlayer middle with dissolve

Eve "Как я могла не заметить?"
show yosemite chin curious onlayer middle with dissolve

Yosemite "Как думаешь, на что она похожа?"
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Какое отношение это имеет к--"
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Просто скажи на что она похожа."
show eve ranger scratch deepthink onlayer middle with dissolve

Eve "На вулкан. Похожа на вулкан."
show yosemite chin neutral onlayer middle with dissolve

Yosemite "Сможешь догадаться где есть вулкан?"
show eve ranger scratch flat onlayer middle with dissolve

Eve "В Йеллоустонском национальном парке, очевидно. Но вулканы на самом деле так не выглядят."
show yosemite chin bored onlayer middle with dissolve

Yosemite "С таким линейным мышлением ты ничего не добьёшься."

"Она продолжает."

show yosemite chin neutral onlayer middle
hide yellow onlayer middle
with dissolve
$camera_move(-5994, -3062, 300, 0, duration=2.5, warper='ease')
Yosemite "Теперь посмотри на Зайон."
show zion hands flat at floating onlayer middle:
        xpos 0.17 ypos 0.79 xanchor 0.5 yanchor 1.0 zoom 0.81
show coyote onlayer middle:
    xpos -0.08 ypos 0.52 xanchor 0.5 yanchor 1.0
with dissolve
"Я смотрю. Она парит в воздухе, уносит омлет подальше от щенка. С неё, как с осеннего дерева, опадают листья."
##PYUNYPUN Custom CG here

show coyote onlayer middle:
    ease 0.25 xpos -0.08 ypos 0.47 xanchor 0.5 yanchor 1.0
    ease 0.25 xpos -0.08 ypos 0.52 xanchor 0.5 yanchor 1.0
    ease 0.25 xpos -0.08 ypos 0.47 xanchor 0.5 yanchor 1.0
    ease 0.25 xpos -0.08 ypos 0.52 xanchor 0.5 yanchor 1.0
    ease 0.25 xpos -0.08 ypos 0.47 xanchor 0.5 yanchor 1.0
    ease 0.25 xpos -0.08 ypos 0.52 xanchor 0.5 yanchor 1.0

Zion "Нет. Эта еда не для койотов. Эта еда не для тебя."
show yosemite chin curious onlayer middle with dissolve

Yosemite "Видишь эти листья и ветки? Роскошные, правда?"
show eve ranger scratch deepthink onlayer middle with dissolve

Eve "Конечно."
show yosemite chin neutral onlayer middle with dissolve

Yosemite "Не напоминает тебе одну конкретную картину?"

hide zion onlayer middle
hide coyote onlayer middle
with dissolve
show eve ranger scratch deepthink onlayer middle:
    ease 2.5xpos 0.86 ypos 1.2 xanchor 0.5 yanchor 1.0
$camera_move(3715, -3062, 300, 0, duration=2.5, warper='ease')

"Она показывает большим пальцем на стену. Я оглядываюсь на восхитительную картину национального парка Зайон, с его тёмно-зелеными, огненно-красных и бежевыми оттенками."
show eve ranger scratch nervous onlayer middle with dissolve

Eve "Постой. Ты говоришь, что…?"
show yosemite back smallsmile onlayer middle with dissolve

Yosemite "Начинаешь понимать?"

"Мой разум скатывается к очевидному."
show eve ranger hair deepthink onlayer middle with dissolve

Eve "Ага -- вам троим нравится наряжаться. Очень миленько."
show yosemite back bored onlayer middle with dissolve

Yosemite "Удивительно, как ты умудряешься находишь новые способы разочаровать меня. Давай попробуем ещё раз."

"Я не обращаю внимания на сарказм, сочящийся из неё. В конце концов, разочарование людей - это вторая натура на данный момент. Моя вторая натура."

"Йосемити прижимается к столу. Указывает на своё лицо, а конкретно на веснушки."
show eve ranger hair annoyed onlayer middle with dissolve

Eve "Ты позволяешь дать тебе пощёчину?"
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Я позволяю тебе познать. Теперь потрогай."

"Закрыв глаза, она выпячивает подбородок застывает. Будто поцелуя ждёт."
show eve ranger scratch annoyed onlayer middle with dissolve

"Я протягиваю руку, но чрезмерная осторожность удерживает меня от дальнейших действий."
show eve ranger scratch deepthink onlayer middle with dissolve

"А вдруг это какой-то трюк. Она же пыталась меня запугать прошлой ночью. Что мешает ей сейчас откусить мне палец? Впрочем, на этой работе со мной и не такое пытались сделать."

"Я вздрагиваю, вспоминая налитые кровью глаза того мужчины. Он бредил, был весь в сосновых иголках и грязи, в лохмотьях. Неизвестно под каким веществом. В тот раз, убедившись, что со мной всё в порядке, Джесси лишь пожала плечами.{i}Оно принимает любые формы,{/i} сказала она."
show yosemite back bored onlayer middle with dissolve

"Йосемити нетерпеливо дёргает носом."
show eve ranger scratch annoyed onlayer middle with dissolve

"Я решаю, что она безобидна. То, что я проснулась живой - хорошее тому подтверждение. Несмотря на то, что мы обменялись любезностями, именно {i}она{/i} предложила перемирие. Это должно что-то значить."

"Я не могу полностью избавиться от подозрения, но всё же протягиваю руку и провожу ладонью по её щеке."
show eve ranger scratch nervous onlayer middle with dissolve

"Когда я дотрагиваюсь пальцами до веснушек, меня словно оцарапывает маленькими грубыми камешками."

"До меня наконец доходит."

"Это вовсе не веснушки. Они как раз похожи на камешки или чешую, приклеенную к коже."

"Чтобы убедиться, я провожу рукой вверх и вниз по её лицу. Между камешками её кожа нежная и розовая."
show yosemite back blush onlayer middle with dissolve

Yosemite "Я сказала потрогай, а не ласкай. Боже…"
show eve ranger scratch blush onlayer middle with dissolve
pause 1.0
show eve ranger scratch deepthink onlayer middle with dissolve

"Я сжимаю пальцами один из камешков и тяну его. Вместо того, чтобы сорваться, он тянет кожу Йосемити за собой."
show yosemite back frustrated onlayer middle with dissolve

Yosemite "Ааай!"
show eve ranger scratch nervous onlayer middle with dissolve

"Она резко отстраняется. В уголках её глаз блестят слезы."
show yosemite back crying onlayer middle with dissolve

Yosemite "Необязательно быть такой грубой!"

"У меня отвисает челюсть, а в голове, словно дикая лошадь, скачет неразбериха."

Eve "Это… камни?"
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Ну уж явно не бижутерия."

"Скуля, она пытается успокоить пульсирующую щёку."
show eve ranger scratch annoyed onlayer middle with dissolve

"Я поворачиваюсь и смотрю на верхнюю картину."

"Купол Лемберта. Я видела его по дороге сюда. Его и отсюда можно увидеть, надо только на крыльцо выйти. Каждый раз, когда я туда поднималась, путь был грубым и каменистым."

"Большинство гор в долине Йосемити такие."

"Я вспоминаю вчерашнее объяснение Йеллоустон. Но это же смехотворно. Абсурдно. Фэнтези какое-то. Но если другие объяснения и есть, то я не могу до них додуматься."
show eve ranger hair nervous onlayer middle with dissolve

Eve "Ты… Ты Йосемитский национальный парк."
show eve ranger hair blush onlayer middle with dissolve

"Господи, я правда сказала это вслух? Я схожу с ума? Я точно схожу с ума."

"Но Йосемити удовлетворённо кивает, и я убеждаюсь, что попала на поезд психов. Который мчится в обрыв."
show yosemite back smallsmile onlayer middle with dissolve

Yosemite "Теперь ты начинаешь понимать. Года не прошло."
show eve ranger hair deepthink onlayer middle with dissolve

"Я пытаюсь выдавить из себя вопросы, но получается лишь мычание и кряхтение. Йосемити смотрит на меня с весёлой ухмылкой."

play sound "sfx/dumbass campers from inside.ogg"
"Далекие смех и болтовня прорываются сквозь неловкую тишину. Снаружи доносится треск и хруст веток и листьев. Голоса становятся громче, проходят мимо хижины, затем стихают."
show eve ranger hair annoyed onlayer middle with dissolve

Eve "Что ты такое? Что ты такое {i}на самом деле{/i}?"
show yosemite back bored onlayer middle with dissolve

"Ухмылка Йосемити меняется на хмурое выражение. Её глаза сканируют беспорядок из книг и бумаг. Рука сжимает стол, ногти впиваются в дерево."
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "{i}Ты не знаешь?{/i}"

"С трудом верю искреннему шоку в своём голосе. Я ведь не собираюсь купиться на эту чушь?"

Yosemite "Вопрос на миллион, не правда ли?"
show yosemite back smallsmile onlayer middle with dissolve

"Она откидывается на спинку стула, нарушая прямую, как палка, позу. Она делает глубокий вдох и резко выдыхает. Её хмурое лицо вновь расплывается в улыбке. Это мягкая улыбка человека, который настольгирует по прежним временам или вспоминает ушедшего члена семьи."

Yosemite "{i}Мы не знаем или просто не помним?{/i}"
show eve ranger scratch flat onlayer middle with dissolve

Eve "Обойдусь без криптологической фигни."
show yosemite back neutral onlayer middle with dissolve

Yosemite "Как тебе угодно, {i}но{/i}. Я говорю то, что знаю. А я знаю, что я Йосемити. Также, как они знают, что они Зайон и Йеллоустон."
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Окей. Разумеется. Но {i}откуда{/i} ты это знаешь?"
show yosemite chin neutral onlayer middle with dissolve

Yosemite "Откуда ты знаешь, что живот урчит именно от голода? Кому-то приходилось объяснять тебе подобную концепцию?"
show eve ranger scratch deepthink onlayer middle with dissolve

Eve "Как {i}давно{/i} ты знаешь?"
show yosemite back bored onlayer middle with dissolve

Yosemite "Я не знаю."
show eve ranger scratch nervous onlayer middle with dissolve

Eve "Ты всегда знала?"
show yosemite back annoyed onlayer middle with dissolve

Yosemite "{i}Я не знаю!{/i}"
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Ты хоть что-нибудь знаешь?"
show yosemite back yelling onlayer middle with dissolve
stop music fadeout 1.0
Yosemite "Я бы не пыталась выяснить, если бы всё знала!"
show eve ranger hair nervous onlayer middle with dissolve
##PYUNPYUN chair scooting effect, I had one of these on MagiKilo, there's another later in the episode.
"Она вскакивает со стула и смотрит на меня сверху вниз. Её голос пронзает воздух, как кинжал."

"Её маленькая вспышка погружает комнату в тишину. Йеллоустон кашляет из кухни. Щенок встревоженно вскидывает хвост. Я смотрю на него, притворяясь невозмутимой, но втайне я напряжена. Мои мышцы напрягаются под униформой."
play music audio.north

"В разгаре тишины Зайон на цыпочках подходит к столу. Её крошечная ручка вцепляется в руку Йосемити, ухитряется обхватить только три пальца."

"Она молча смотрит на неё глубоким умоляющим взглядом."
show yosemite back bored onlayer middle with dissolve

"На остром лице Йосемити появляется печальная улыбка. Её рука полностью обхватывает ручку Зайон. Она гладит её ладонь. Зайон хихикает от щекотки."

Yosemite "Иногда бывает… фрагменты, всплывающие в голове. Крупицы и кусочки языка, которого я не знаю. Лица, мне неизвестные, но кажущиеся знакомыми."

"Она говорит дрожащим голосом, почти шёпотом. Срывается на конце каждого слова."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "И когда мне кажется, что я всё вспомнила, и ответ вертиться на языке, я снова забываю."

"Она крепко жмурится, будто представляет себе всё это. Она крепче сжимает ручку Зайон, но та не отстраняется и даже не морщится."
show yosemite back annoyed onlayer middle with dissolve
voice "scripte01s04_47f5c33c"
Yosemite "Они как эхо, которое уходит всё дальше с каждым новым прозрением. Становится всё тише и тише. От такого становится ужасно досадно."

"Слова прорываются сквозь стиснутые зубы."

Yosemite "Но если бы я только смогла понять, кто мы такие, откуда мы пришли. Может быть... может быть, тогда я наконец вспомню."

"Она открывает глаза, они словно постарели. Такое чувство, что она смотрит сквозь меня, смотрит на картины, висящие на стене."

"Будто я всего лишь очередное препятствие."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Да, я ничего не знаю. Но я собираюсь узнать всё."
show eve ranger scratch deepthink onlayer middle with dissolve

Eve "Ну, рада за тебя."

"Меня беспокоит то, как она на меня всегда смотрит. Это кипящий гнев? Неохотное любопытство? Я не знаю хороший это взгляд или плохой. В любом случае, меня не должно волновать это."

"Я подзываю щенка к себе. Он подпрыгивает и, проявив невероятное терпение, садится у моих ног. Он смотрит на меня, его печальные карие глаза встречаются с моими."
show eve ranger hair softsmile onlayer middle
show coyote onlayer middle:
    xpos 0.66 ypos 0.48 xanchor 0.5 yanchor 1.0
with dissolve

"А вот {i}этот{/i} взгляд меня действительно волнует."

"Я отрываю кусочек от оставшегося блинчика и бросаю щенку. Вскочив на задние лапы, он подпрыгивает, чтобы схватить его. Кусок отскакивает от его носа, и вместо какого-либо удивительного акробатического трюка, щенок вертится туда-сюда, пока не находит кусок на полу."

"Браво."

$camera_move(-5994, -3062, 300, 0, duration=2.5, warper='ease')
show zion hands flat at floating onlayer middle with dissolve:
        xpos 0.17 ypos 0.79 xanchor 0.5 yanchor 1.0 zoom 0.81
"Зайон обиженно смотрит на меня."

show eve ranger hair flat onlayer middle with dissolve
$camera_move(3715, -3062, 300, 0, duration=2.5, warper='ease')
hide coyote onlayer middle
hide zion onlayer middle
with dissolve

Eve "Просто угощение. Это его не убьёт."

"Голоса, доносившиеся с улицы, начинают звучать громче прежнего. Они далеко, но я все ещё могу уловить беспричинные маты и раздражающий смех."
show eve ranger hair annoyed onlayer middle with dissolve

"Детишки уже набухались?"
show eve ranger scratch deepthink onlayer middle with dissolve

"Конечно, кто я такая, чтобы судить? Ещё пара месяцев этой работы и я сама начну подливать виски в свой утренний кофе. Рейнджер Смит вполне может стать моей ролевой моделью. Хвала Смиту."
show yosemite back bored onlayer middle with dissolve

"Йосемити выглядывает в окно."

Yosemite "Твои друзья?"
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Нет. Господи, нет!"

"Я усмехаюсь, но это больше похоже на шипение."
show eve ranger scratch deepthink onlayer middle with dissolve

Eve "День, когда не надо иметь дело с подобыными адскими исчадиями, - день, проведённый прекрасно."
show yosemite back smug onlayer middle with dissolve

Yosemite "Так я и думала."

"Она усмехается себе под нос. Это напоминает мне, какими ехидными были некоторые из моих профессоров в колледже. Кружка латте в руке и голова в заднице."
show eve ranger hair annoyed onlayer middle with dissolve

Eve "И что же, ради всего святого, ты думаешь на этот раз?"
show yosemite back smallsmile onlayer middle with dissolve

Yosemite "Что я была не права на твой счёт."
show eve ranger scratch deepthink onlayer middle with dissolve

"Я полностью переключаюсь на щенка, отрываю ему ещё кусок блинчика. Максимально стараюсь дать понять, что не обращаю на Йосемити внимание, но всё равно держу её в поле зрения."
show yosemite chin annoyed onlayer middle with dissolve

Yosemite "Прошлой ночью я могла бы поклясться, что видела, как в тебе бушевал конфликт."
show yosemite chin smug onlayer middle with dissolve

Yosemite "Шмыгала носом в углу. Плакала о том, как ты устала."

"Расстегнув куртку, она начинает обмахиваться. Подобный лёгкий ветерок не охладит мою кипящую кровь. Она собирается издеваться надо мной, пока я не сгорю заживо?"

"Кто дал ей право вмешиваться? Она будет тыкать меня, пока я душу наизнанку не выверну? Я здесь не для того, чтобы меня осуждали."
show eve ranger hair annoyed onlayer middle with dissolve

Eve "Прошлой ночью меня беспокоил лишь один конфликт - вы трое. Конечно я устала. Почему тебя это волнует?"
show yosemite back bored onlayer middle with dissolve
voice "scripte01s04_c3d5413d"
Yosemite "Потому что... Я тоже устала. Устала от того, что вы так держитесь за этот образ Рейнджера, чтобы люди не понимали, что вы на самом деле наёмные головорезы."
show yosemite back annoyed onlayer middle with dissolve
voice "scripte01s04_0a99f262"
Yosemite "Ты всего лишь одна из веток дерева, которому на тебя наплевать. Бюрократическая рука, которую лучше отрезать, чем позволить ей гноиться. Ты здесь не для обучения, ты здесь не для защиты природы. Разве что, выдача разрешений считается защитой."
voice "scripte01s04_0a99f262_2"
Yosemite "Нет. Ты здесь, чтобы защищать их прибыль. Обчищать людей, когда они просто хотят свалить из ада, который вы здесь устроили. Удостоверяться, что все ресурсы направлены на выкачку денег, чтобы быть чистенькой перед начальством."
show yosemite back smug onlayer middle with dissolve
voice "scripte01s04_41bbdc99"
Yosemite "Я видела таких же, как ты. Таким всё равно. Надевают дурацкую шляпу только для вида, будто им не наплевать."
show eve ranger scratch deepthink onlayer middle with dissolve

"Она ошибается. Я была другой. Мне было не всё равно, так ведь? Но не было никакой гордости за это. Просто медленное погружение в пучину страданий. А может гордость есть в другом. Гордость за то, что я прославленный охранник, который одновременно и уборщик, убирающий беспорядок людей ниже меня по рангу."

"Потому что единственное, что отличает меня от них… что же? Что я беспокоюсь достаточно, чтобы страдать из-за этого. Но конечно, если я страдаю, это значит..."
show eve ranger scratch flat onlayer middle with dissolve

Eve "Ты права. Может мне и правда всё равно."
show eve ranger hair deepthink onlayer middle with dissolve

play sound "sfx/chair scoot.ogg"
"Я наклоняюсь и глажу щенка по голове. Он хватает меня за ногу, но я встаю."

Eve "Забота стала слишком тягостной. Может быть, она не стоит той боли, которую причиняет."

$camera_move(-4780, -3062, 300, 0, duration=2.0, warper='ease')
show eve ranger hair deepthink onlayer middle:
    ease 2.0 xpos 0.14 ypos 1.2 xanchor 0.5 yanchor 1.0
"Я делаю несколько шагов и останавливаюсь у её кресла."
show eve ranger hair annoyed onlayer middle with dissolve

Eve "Но всё же есть дело, на которую мне не плевать."
show yosemite back bored onlayer middle with dissolve
"Пот ручьями стекает по лицу Йосемити. Она тяжело дышит, её грудь вздымается и опускается."
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Отправить вас ко всем чертям. Я иду докладывать о вас."

"Так держать, Ева. Сделай то, что должна сделать. То, что уже давно надо было сделать."
play sound "sfx/angry chair scoot.ogg"
"Я начинаю идти к окаменелому радио, но Йосемити вскакивает с кресла. Зайон съёживается."
show yosemite chin cringe onlayer middle with dissolve
stop music fadeout 1.5
voice "scripte01s04_30dc4879"
Yosemite "Давай. Сделай это. Докажи мне, что ты очередная… очередная… подделк…"
play sound "sfx/yosemite thud.ogg"

show yosemite chin cringe onlayer middle:
    ease 0.5 xpos 0.47 ypos 1.32 xanchor 0.5 yanchor 1.0
    ease 2.0 xpos 0.47 ypos 2.24 xanchor 0.5 yanchor 1.0
pause 1.0
hide yosemite onlayer middle with dissolve
"Её голос растворяется в воздухе. Раздаётся глухой удар. Когда я оборачиваюсь, она лежит на полу."
$camera_move(-1364, -3062, -300, 0, duration=0)
show yellow volcano hips concern onlayer middle:
    xpos 0.82 ypos 1.37 xanchor 0.5 yanchor 1.0 zoom 0.95
show zion hands nervous onlayer middle:
    xpos 0.47 ypos 0.97 xanchor 0.5 yanchor 1.0 zoom 0.81
with dissolve

Yellowstone "Йосемити!"
show eve ranger hair nervous onlayer middle with dissolve

"Прежде чем я успеваю сообразить, что к чему, Зайон и Йеллоустон уже стоят на коленях рядом с ней."

"Йеллоустон хватает со стола пачку бумаг и обмахивает лежащую Йосемити. Зайон сжимает ей руку."

"Я бегу назад и опускаюсь на колени. От Йосемити исходит жар, как от печи. Я прижимаю руку к её лбу. Как только я касаюсь её кожи, руку ошпаривает. Я вскрикиваю и отдёргиваю руку. Ощущение было такое, будто я дотронулась до сковородки."
show eve ranger scratch nervous onlayer middle with dissolve

Eve "Лихорадка?"
show zion arms sad onlayer middle with dissolve

"Зайон качает головой."

Zion "Пожар."

"Йосемити открывает глаза, блестящие и рассеянные. Она пытается встать, и её дыхание учащается."
show yellow volcano hips angry onlayer middle with dissolve

Yellowstone "Не двигайся! Только хуже сделаешь."

Yosemite "Уже… близко…"
show yellow volcano hips concern onlayer middle with dissolve

Yosemite "Ааа…!"

"Она издает болезненный стон. В рукаве её куртки зияет дырочка, по краям которой хрустят оранжевые угольки. Она шипит, как потушенная сигарета."

"Как сигарета…"
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "О нет."
show eve ranger scratch annoyed onlayer middle:
    ease 1.5 xpos 1.22 ypos 1.2 xanchor 0.5 yanchor 1.0
pause 1.5
hide cabininside_day2 onlayer background
hide cabininside_day1 onlayer background
hide yellow onlayer middle
hide zion onlayer middle
$ camera_reset()
$ layer_move("background", 1700)
show eve ranger scratch annoyed onlayer middle:
    xpos 0.5 ypos 1.45 xanchor 0.5 yanchor 1.0
show cabinoutdoor_day onlayer background:
    xpos 0.04 ypos 0.04 zoom 0.81
with dissolve
stop music fadeout 1.5
stop ambient fadeout 1.5
play sound "sfx/panic door opening.ogg"
"Я распахиваю дверь и выбегаю на крыльцо."

"Слабый запах дыма щекочет нос. Может, просто костёр."
show eve ranger hair nervous onlayer middle with dissolve

Eve "Не хорошо."
$ camera_reset()
$ layer_move("background", 1860)
$camera_move(3954, -3062, 0, 0, duration=0)
hide cabinoutdoor_day onlayer background
show cabininside_day2 onlayer background
show eve rangerhat scratch annoyed onlayer middle:
    xpos 1.03 ypos 1.2 xanchor 0.5 yanchor 1.0
show yellow volcano hips concern onlayer middle:
    xpos 0.72 ypos 1.25 xanchor 0.5 yanchor 1.0 zoom 0.95
show zion hands nervous at floating onlayer middle:
    xpos 0.37 ypos 0.85 xanchor 0.5 yanchor 1.0 zoom 0.81 subpixel True
with dissolve

show eve rangerhat scratch annoyed onlayer middle with dissolve
"Я возвращаюсь в хижину за шляпой. Йеллоустон в панике оглядывается по сторонам, бормоча слова утешения Йосемити. Зайон шмыгает носом, сдерживая слёзы. Смотрит на меня с дрожащим спокойствием. Её тоненький голосок слегка срывается."

show zion hands softcry at floating onlayer middle with dissolve

Zion "Как далеко он?"

"Я не отвечаю. Знакомый запах дыма уже проникает в хижину."

"Я не знаю, что происходит, не знаю, как {i}они знают{/i} что происходит, но, учитывая последние двенадцать часов, рисковать я не собираюсь."
show eve rangerhat scratch furious onlayer middle with dissolve

Eve "Положите её на диван! И что бы вы не делали, оставайтесь здесь!"
show yellow volcano hips sad onlayer middle with dissolve

Yellowstone "Но Ева, мы можем--"
play sound "sfx/door slaming.ogg"
hide eve onlayer middle
hide zion onlayer middle
hide yellow onlayer middle
hide cabininside_day2 onlayer background
with dissolve
"Я выбегаю наружу и захлопываю дверь, не услышав слов Йеллоустон."
play music audio.devastation
play ambient "ambience/raging fire.ogg" fadein 5.0
"Я бегу по тропинке, отмахиваясь от веток и листьев. Мои глаза начинает покалывать, как будто я их слишком долго держала открытыми. Но сколько бы я не моргала, покалывание не проходит."

"Впереди слышны голоса. Все кричат друг на друга и все напуганы."

DCamperG "Туши его! Туши его!"

DCamper "Я делаю, что могу! Теперь отойди и перестань орать!"

DCamper2 "Ну мы чё тебе говорили, чел? Ты просто {i}не мог{/i} не сделать по-своему!"

DCamperG2 "Да понял он! Он это не специально сделал!"
$ camera_reset()
$ layer_move("background", 1860)
show fiyah onlayer background:
   xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0
show fiyah onlayer background
show eve rangerhat scratch annoyed onlayer middle:
    xpos 0.5 ypos 1.45 xanchor 0.5 yanchor 1.0
$ fire_tint = True
with dissolve
"Я наконец-то прорываюсь к полянке, окружённой деревьями. Достаточно места для дебилов, чтобы устроить неприятности."

"На куче веток под деревом пляшет ярко-красное пятно. Огонь разветвляется, образует форму буквы ‘V’. Ствол дерева почернел от сажи."

"Знакомые туристы (я узнаю их только по курткам) стоят, окружённые пламенем, их лица искажены страхом. Тот, с кем я разговаривала прошлой ночью, прихлопывает пламя зелёной курткой. Как будто теперь это что-то изменит."
show eve rangerhat hair furious onlayer middle with dissolve

Eve "ЧТО ЗА ХРЕНЬ ВЫ УСТРОИЛИ?"

"Большинство из них бледнеют и на мгновение забывают об огне. Парень с зелёной курткой продолжает попытки потушить пламя, но оно только увеличивается."
show eve rangerhat hair annoyed onlayer middle with dissolve

Eve "Ты! У тебя три секунды, чтобы сказать, что произошло!"

"Я указываю на него, он уже перестал размахивать курткой и отошёл от огня. Он поворачивается ко мне, его глаза стали красными от дыма."

DCamper "Я… Мы…"

"Один."

DCamper "Я думал, что вытащил…"

"Два."

DCamper "Я… Я же не хотел…"

"Три."

Eve "Свали с дороги! Пока куртку свою не поджог!"

show eve rangerhat scratch annoyed onlayer middle:
    ease 0.2 xpos 0.45 ypos 1.45 xanchor 0.5 yanchor 1.0
    ease 0.2 xpos 0.50
"Я подхожу и оттолкиваю его к остальным. Он не сопротивляется, падая в их объятия, как безжизненная кукла."
show eve rangerhat scratch furious onlayer middle with dissolve

Eve "Все вы! Валите отсюда! Возвращайтесь в лагерь!"
show eve rangerhat scratch annoyed onlayer middle with dissolve

"Они смотрят на меня широко раскрытыми пустыми глазами. Будь я водителем грузовика, они бы уже давно превратились в лепёшку на дороге."
show eve rangerhat scratch furious onlayer middle with dissolve

Eve "ШЕВЕЛИТЕСЬ!"
show eve rangerhat scratch annoyed onlayer middle with dissolve

"Все, кроме одного, кивают и начинают пробираться через лес. Парень в зелёной куртке смотрит на огонь, колени у него дрожат."

"Его маленькая подружка оглядывается и складывает руки в рупор."

DCamperG "Пошли! Пусть она позаботиться об этом!"

"Он встряхивается, вытирает глаза и убегает в лес."

"Моё внимание переключается на огонь. Если случайно наступлю не туда, то окажусь по пояс в пламени."

"Основание ствола дерева загорается, и горящие угли плавно опускаются на ветки ближайших деревьев."

"Я зарываюсь ботинком в землю и пинаю на огонь облако грязи. Угольки гаснут, но огонь остается таким же высоким."

"Отстегнув от пояса рацию, я нажимаю кнопку связи и начинаю говорить. Хотя для того, кто слушает, это скорее похоже на приступ тревоги."
show eve rangerhat hair furious onlayer middle with dissolve

Eve "Станция Туалэми, это рейнджер Адамс. У нас проблема возле хижины! 10-70! Повторяю, 10-70! Запросите у диспетчера пожарный отряд!"

"Сквозь помехи доносится прерывистый голос."
voice "scripte01s04_d9a29c01"
WalkieTalkie "Адамс… 10-71… Повторите… Пожар…?"
show eve rangerhat hair annoyed onlayer middle with dissolve

Eve "Станция Туалэми, как слышно? Станция Туалэми!"

WalkieTalkie "Аа… Повт… ожа…"
show eve rangerhat scratch nervous onlayer middle with dissolve

"Я оглядываюсь вокруг и понимаю, насколько плотно окружена деревьями. Неудивительно, что сигнал такой беспорядочный."

"В хижине огнетушителя нет, а станция находится менее чем в миле отсюда. Если побегу, то успею предупредить их, но, учитывая как быстро распространяется огонь, всё может выйти из=под контроля…"

"Я осматриваю поляну. На земле всё ещё есть снег, полурастаявший, разбросанный мелкими кучами."
show eve rangerhat scratch annoyed onlayer middle with dissolve

"Снега не много, но может сработать."

"Я собираю столько снега, сколько умещается в руках. Сгустки чёрной грязи пятнают белизну. Похоже, будто я держу сухой лёд в руках."

"Я бросаю его в огонь. Большая часть снега тает в одно мгновение, но немного огня исчезает вместе с ним."
show eve rangerhat nervous onlayer middle with dissolve

"На краткий миг меня охватывает облегчение; но так же быстро оно и исчезает. Огонь вспыхивает, поглощая дерево. Я вздрагиваю, когда жар касается моей кожи. Пламя приближается."

"Лесной пожар в первый же день. Прекрасно."

"Я нервно шагаю назад и оглядываюсь через плечо."

show eve rangerhat scratch annoyed onlayer middle with dissolve

"Придётся бежать на станцию, у меня нет другого выбора."

"Мои ноги подгибаются, и я совершаю первый рывок, но прежде, чем я делаю второй, пронзительный голос прорывается через лес."

show yellow volcano hips concern onlayer middle:
    xpos 1.46 ypos 1.55 xanchor 0.5 yanchor 1.0
    pause 2.5
    ease 2.0 xpos 0.76
$ fire_tint = True

show eve rangerhat scratch annoyed onlayer middle:
    pause 4.0
    ease 1.0 xpos 0.24 ypos 1.45 xanchor 0.5 yanchor 1.0

Yellowstone "Хеееееейо! Ееееееева!"

play sound "sfx/short bush rustle.ogg"
"Йеллоустон проносится мимо деревьев и выбегает на поляну. Ветки и листья цепляются за её одежду. Она резко останавливается, не сводя глаз с огня."
show yellow volcano hips sad onlayer middle with dissolve

Yellowstone "Окей, всё-таки это происходит."
show eve rangerhat scratch furious onlayer middle with dissolve

Eve "Что ты здесь делаешь?!"
show yellow volcano hips excited onlayer middle with dissolve

Yellowstone "Ева! Вот и ты!"
show yellow volcano peace happy onlayer middle with dissolve

"Она отдает честь."

Yellowstone "Мы здесь, чтобы помочь!"

"Её голос заглушается потрескиванием огня."
show eve rangerhat scratch nervous onlayer middle with dissolve

Eve "{i}Мы?{/i}"

show eve rangerhat scratch nervous onlayer middle:
    ease 1.0 xpos 0.16 ypos 1.45 xanchor 0.5 yanchor 1.0
show yellow volcano peace happy onlayer middle:
    ease 1.0 xpos 0.82 ypos 1.55 xanchor 0.5 yanchor 1.0
show zion hands sad at floating onlayer middle:
    xpos 0.48 ypos 0.98 xanchor 0.5 yanchor 1.0 zoom 0.85
    ease 1.0 ypos 1.14 subpixel True
with dissolve
"Зайон пикирует в мою сторону, и останавливается, оказываясь со мной лицом к лицу."

Zion "Тебе одной не справиться!"
show eve rangerhat scratch furious onlayer middle with dissolve
voice "scripte01s04_98062b27"
Eve "Я велела вам оставаться в хижине!"

show zion hands nervous at floating onlayer middle with dissolve:
    subpixel True

Zion "Мисс Ева, если мы не уладим это как можно скорее, никакой хижины не останется!"
show eve rangerhat scratch nervous onlayer middle with dissolve

"Её обычный кроткий голос звучит со зрелой доходчивостью."

"Как неукротимый сорняк, пламя поднимается всё выше. Ветви похожи на фитили свечей. Пламя змеится к окружающим деревьям, поджигая саму землю."

"Ненавижу впутывать в подобное непричастных к Службе, но выбора нет."
show eve rangerhat scratch annoyed onlayer middle with dissolve

Eve "Ладно! Но если всё выйдет из-под контроля, я хочу, чтобы вы сразу же убегали!"

"Они поспешно кивают. Мне больше и не надо. Поздравляю, девочки, вы заместители."
show eve rangerhat scratch furious onlayer middle with dissolve
voice "scripte01s04_1205d5ee"
Eve "Собирите столько снега, сколько сможете. Земля тоже подойдёт, но не подкидывайте огню больше топлива!"

show yellow volcano hips happy onlayer middle with dissolve

Yellowstone "Мэм, есть мэм!"
show eve rangerhat scratch annoyed onlayer middle with dissolve

$camera_move(0, 0, 300, 0, duration=1.0)
show eve rangerhat scratch annoyed onlayer middle:
    ease 1.0 xpos 0.47 ypos 1.45 xanchor 0.5 yanchor 1.0
show zion hands nervous at floating onlayer middle:
    ease 1.0 xpos 0.18 ypos 1.14 xanchor 0.5 yanchor 1.0 zoom 0.85 subpixel True
"Мы все поспешно начинаем. Йеллоустон и я подбираем разбросанные кучи снега. Сгребаем их в охапку и бросаем в огонь. Снег испаряется у нас на глазах."

show zion hands nervous at floating onlayer middle:
    ease 1.0 ypos 0.99
"Зайон взмывает к вершинам деревьев, встряхивая покрытые снегом ветви. Снег осыпается, заглушая большую часть пламени. Звук такой, будто бекон кинули на раскалённую сковородку."

"Но как бы Зайон ни старалась, она только уничтожают связующие части огня. Два больших дерева уже охвачены пламенем, их кора моментально обугливается. Три других дерева только начинают гореть."

"Дым резкий и удушливый, забирается в ноздри и наполняет лёгкие литрами обжигающего воздуха. Щуриться - единственный способ видеть сквозь режущую глазную боль."

"Сквозь приступ болезненного кашля я зову Зайон и Йеллоустон, которые стали похожи на два пятна акварели."
show eve rangerhat scratch disgusted onlayer middle with dissolve

Eve "Всё плохо! Нам надо убираться отсюда! Как можно скорее!"
show zion hands curious at floating  onlayer middle with dissolve

Zion "Подожди! У меня есть идея!"
show eve rangerhat scratch annoyed onlayer middle with dissolve

Eve "Забудь о ней! Если останемся, то превратимся в угли!"

$camera_move(0, 0, 0, 0, duration=3.5, warper='ease')
show eve rangerhat scratch annoyed onlayer middle:
    ease 1.5 xpos 0.15 ypos 1.45 xanchor 0.5 yanchor 1.0
show zion hands curious onlayer middle:
    ease 1.5 xpos 0.47 ypos 0.99 xanchor 0.5 yanchor 1.0 zoom 0.85
    ease 0.5 xpos 0.47 ypos 1.15 xanchor 0.5 yanchor 1.0 zoom 0.85
"Пятно Зайон меня игнорирует и поворачивается к пятну Йеллоустон."
show zion arms nervous onlayer middle with dissolve

Zion "Йеллоустон, ты знаешь, что я люблю тебя, правильно?"
show yellow volcano hips sad onlayer middle with dissolve

Yellowstone "Ясен пень знаю! Тоже люблю тебя! Но тут пожар как бы!"
show zion hands nervous onlayer middle with dissolve
voice "scripte01s04_84e32d47"
Zion "Я знаю! Поэтому я супер сильно извиняюсь за то, что собираюсь сделать. Пожалуйста, не возненавидь меня…"

Yellowstone "Э? Как я вообще могу ненавидеть моего Земного Анге--"
show zion hands nervous onlayer middle:
    ease 1.0 xpos 0.47 ypos 1.1 xanchor 0.5 yanchor 1.0 zoom 0.85
    ease 0.2 xpos 0.47 ypos 1.15 xanchor 0.5 yanchor 1.0 zoom 0.85
pause 1.2
with vpunch
show yellow volcano hips concern onlayer middle
stop music
play sound "sfx/zion stepping on yellowstone feet.ogg"
"Зайон поднимает свою крошечную ножку и топает по ноге Йеллоустон. На секунду к звукам хрустящих веток и потрескиванию огня, добавляется хруст пальцев Йеллоустон."
show yellow volcano hips seriouscry onlayer middle with dissolve

"Раздаётся прерывистый визг."
show yellow volcano hips comiccry onlayer middle with dissolve

Yellowstone "З-зачем…?"


"Ужасный вой увеличивает частоту, становясь резким и пронзительным, как пожарная тревога. Визг и рёв раскалённым металлом льются на мои барабанные перепонки."
show yellow volcano hips seriouscry onlayer middle with dissolve
show yellow gayser hips seriouscry onlayer middle with dissolve
play sound "sfx/yellowstone geyser.ogg" fadein 5.0 loop
Yellowstone "Ау… Ауу… АААААААААААААААААААААААААА!"

"Теперь вместо того, чтобы прикрывать глаза от дыма, я прикрываю уши от визгов Йеллоустон."
play music audio.anchors
"Душераздирающий крик пронзает мой череп. Вода пузырится из отверстия на голове Йеллоустон, кипя, как котёл на плите. Со взрывной силой из её головы вылетает гейзер воды, разбрызгиваясь в воздухе."
show eve rangerhat scratch nervous onlayer middle with dissolve

Eve "Воу воу воу воу! Что?"
show zion hands happy onlayer middle with dissolve

Zion "Отлично! Ты здорово справляешься! Просто продолжай плакать!"

Yellowstone "Я-я попытаааааюсь!"

"Йеллоустон продолжает рыдать. Вода брызгает на меня, охлаждая от адского жара."

"Подождите... Это оно!"
show eve rangerhat scratch bigsmile onlayer middle with dissolve

Eve "Я слышу тебя громко и ясно, малыш!"

"Я показываю Зайон большой палец. Должна отдать ей должное, этот план умнее, чем всё, что я сама могла бы придумать."
show eve rangerhat scratch furious onlayer middle with dissolve

Eve "Йеллоустон! Целься в огонь!"

Yellowstone "О-Океееееееееей!"

hide eve onlayer middle
hide zion onlayer middle
hide yellow onlayer middle
with dissolve

"Рыдая, как ребенок, заблудившийся в супермаркете, Йеллоустон повинуется, наклоняет голову и стреляет гейзером в горящие деревья."

"Зайон хватает Йеллоустон за пояс и направляет её в сторону огня. Это напоминает мне пожарного, орудуещего шлангом."

"Волнующиеся красные и оранжевые пятна уменьшаются, когда на них падает вода. Постепенно огонь угасает. Дым понемногу разряжается, становится похожим на туман."

stop sound fadeout 10.0
stop ambient fadeout 10.0
$ fire_tint = False
show fiyah onlayer background:
 "clearing_morning" with Dissolve (20.0)

"Рёв пламени стихает до щелчков и хлопков костра. Слезы и гейзер Йеллоустон высохли. Будто кран в ванной закрыли."


show eve rangerhat scratch annoyed onlayer middle:
    xpos 0.15 ypos 1.45 xanchor 0.5 yanchor 1.0
show zion hands nervous onlayer middle:
    xpos 0.47 ypos 1.15 xanchor 0.5 yanchor 1.0 zoom 0.85
show yellow volcano hips comiccry onlayer middle:
    xpos 0.82 ypos 1.55 xanchor 0.5 yanchor 1.0
with dissolve

"Мы все втроём отступаем от дыма, чтобы лучше видеть."
show yellow volcano hips concern onlayer middle with dissolve

play ambient "ambience/outside daytime ambience.ogg" fadeout 5.0
Yellowstone "Э-это всё? Мы всё потушили?"

"Йеллоустон смахивает с глаз оставшиеся слёзы."
show eve rangerhat scratch nervous onlayer middle with dissolve

Eve "Похоже на то."

"Я шаркаю каблуком ботинка по грязи, на случай, если там остались тлеющие угли."
show zion arms laugh onlayer middle with dissolve:
    ease 0.8 xpos 0.6 ypos 1.15 xanchor 0.5 yanchor 1.0 zoom 0.85

Zion "Йеллоустон!"

"Зайон хватает Йеллоустон за ноги и утыкается лицом ей в куртку."

show eve rangerhat scratch nervous onlayer middle:
    ease 1.0  xpos -0.21 ypos 1.45 xanchor 0.5 yanchor 1.0
show zion hands softsmile onlayer middle:
    ease 1.0 xpos 0.37
show yellow volcano hips happy onlayer middle:
    ease 1.0 xpos 0.59 ypos 1.55 xanchor 0.5 yanchor 1.0


Zion "Я так горжусь тобой! Ты очень хорошо постаралась. Ты была… такой крутяшной? Т-так же надо говорить, да?"
show yellow volcano hips happy onlayer middle with dissolve

Yellowstone "Боженьки, ты так думаешь?"

"Она обхватывает Зайон и заключает её в объятия."
show yellow volcano hips excited onlayer middle with dissolve

Yellowstone "Ты тоже хорошо постаралась! У кого-то тут очень шустрые мозги!"

$camera_move(-612, -1055, 600, 0, duration=0)
show eve rangerhat hair softsmile onlayer middle:
    xpos 0.46 ypos 1.45 xanchor 0.5 yanchor 1.0
show yellow volcano hips excited onlayer middle:
     xpos 1.59 ypos 1.55 xanchor 0.5 yanchor 1.0
show zion hands softsmile onlayer middle:
     xpos 1.3 ypos 1.15 xanchor 0.5 yanchor 1.0 zoom 0.85
with dissolve
"Я улыбаюсь, а как я могу не улыбаться? Мы только что не дали целому участку парка превратиться в пепел. А ещё, эти двое бывает -- {i}бывают{/i} -- очень умилительными."

"И всё же ... я не могу не содрогнуться от того, что случилось бы, если бы меня здесь не было."
show eve rangerhat hair deepthink onlayer middle with dissolve

"И всё из-за этих уродов. Очередная группа беспечных туристов. Если это не живопись на камнях, то охота без лицензии. Если это не охота без лицензии, то провоцирование лесного пожара в холодную раннюю весну."
show eve rangerhat hair annoyed onlayer middle with dissolve

"Моя улыбка -- этот маленький всплеск счастья -- недолговечна. Пылающее чувство долга сжигает мои внутренности. Я начинаю выбираться с поляны."

$camera_move(0, 0, 0, 0, duration=0)
show eve rangerhat hair annoyed onlayer middle:
    xpos 0.15 ypos 1.45 xanchor 0.5 yanchor 1.0
show zion arms curious onlayer middle:
    xpos 0.60 ypos 1.10 xanchor 0.5 yanchor 1.0 zoom 0.81
show yellow hips concern onlayer middle:
     xpos 0.82 ypos 1.45 xanchor 0.5 yanchor 1.0 zoom 0.91
with dissolve

Zion "Мисс Ева?"
show eve rangerhat scratch deepthink onlayer middle with dissolve

Eve "Спасибо за помощь, но вам нужно вернуться в хижину."
show yellow volcano hips concern onlayer middle with dissolve

Yellowstone "Куда ты уходишь?"
show eve rangerhat scratch annoyed onlayer middle with dissolve


show eve rangerhat scratch annoyed onlayer middle:
    ease 1.0   xpos 0.45 ypos 1.45 xanchor 0.5 yanchor 1.0
pause 0.5
show yellow volcano hips concern onlayer middle:
    ease 0.8 xpos 1.26 ypos 1.45 xanchor 0.5 yanchor 1.0 zoom 0.91
show zion arms curious onlayer middle:
    ease 0.8 xpos 1.23 ypos 1.1 xanchor 0.5 yanchor 1.0 zoom 0.81
Eve "Тушить остальное пламя. Пока оно не распространилось."
hide clearing_morning onlayer background
stop music fadeout 1.5


$camera_move(-1044, -1023, 809, 0, duration=0, warper='ease')
with dissolve
"Я закипаю от ярости, как скороварка. Выбегаю из леса. Когда я прохожу мимо хижины, из неё доносится щенячий визг."
play music audio.bitter
"Конечно такое бы случилось. {i}Конечно{/i}. Как Джесси могла подумать, что здесь дела пойдут нормально? Зачем я вообще потакала этому оптимистическому бреду?"

"После всех этих лет мне следовало знать."

"Следовало знать, как всё устроено."

"Следовало знать, что каждый безмозглый ублюдок верит, что он не проблема и что один прокол никак не повредит."

"Как старики ворчат по поводу разрешений и считают себя в праве бросать пустые пивные банки в озеро, потому что кидают в нас чеки на шестизначные суммы. Всё равно что бросать объедки собакам."

"Мало того, что я подчиняюсь алчным, ленивым бюрократам. Земля тоже должна подчиняться."

"Её яркая роскошь, летом пронизанная зеленью и желтизной, а в росистые осенние дни коричневым и оранжевым цветами урожая."

"Чёрно-белые вершины скал и бурные водопады."

"От непроходимых Скалистых гор и суровой красоты бесплодных земель, до сверкающих берегов Тихого и Атлантического океанов."

"Всего лишь очередной ресурс для экплуатации. Для получения прибыли. Попользоваться и выкинуть."

"Если так и будет -- если это и есть мир, что мы построили -- я первой попытаюсь его низвергнуть."

$ camera_reset()
$ layer_move("background", 1860)
hide fiyah onlayer background
show camp_morning onlayer background:
    xpos 0.5 ypos 1.03 xanchor 0.5 yanchor 1.0
with dissolve
"Я добираюсь до лагеря и вижу стаю тех сопляков. Жмутся к палатке, трепетающей под сильными порывами ветра."

"Они переговариваются тревожным шёпотом, не подозревая о моём присутствии. тот парень в зелёной куртке затягивается сигаретой, приглаживая пальцами растрёпанные волосы."

"Его подружка первая замечает моё приближение. Она бубнит его имя, но когда он меня замечает, я уже стою с ним лицом к лицу."
show eve rangerhat hair annoyed onlayer middle with dissolve

"Я хватаю его за шиворот и выдергиваю из группы. Я скручиваю его рубашку так, что костяшки моих пальцев прижимаются к его шее."
voice "scripte01s04_48681964"
Eve "Я встречала много идиотов на этой работе, но ты похоже настоящий уникум!"

"Словно воды Красного моря, его друзья расступаются подальше от нас."

DCamper2 "Вау! Полегче, дамочка!"

DCamperG2 "Это нападение! Ты хоть понимаешь, как это неэтично?"
show eve rangerhat hair flat onlayer middle with dissolve

Eve "Ага, почти так же плохо, как поджёг. Заявишь на меня?"

"Это её заткнуло. Я не собираюсь терять сон из-за попытки надавить на них каплей своего авторитета. Не сейчас."
show eve rangerhat hair furious onlayer middle with dissolve
voice "scripte01s04_c7b9368d"
Eve "Что творилась в твоей голове? Ты пироманьяк? Это заводит тебя, или ты просто тупой?"

"Этот дебил, с его отутюженным, лишённым извилин мозгом, только заикается. Он трясётся, пачка сигарет в его нагрудном кармане подпрыгивает."
show eve rangerhat hair flat onlayer middle with dissolve

Eve "Так я и думала."

"Я притягиваю его ближе. Он сглатывает, его кадык задевает мой кулак."

$camera_move(-996, -416, 586, 0, duration=0.5, warper='ease')
show eve rangerhat hair annoyed onlayer middle with dissolve
Eve "Слушай сюда, говнюк мелкий."

"Наконец, он выходит из своего кататонического состояния и пытается вырваться. Это меня ещё больше бесит. Я выхватываю у него изо рта зажжённую сигарету и комкаю её в руке."
show eve rangerhat hair furious onlayer middle with dissolve

Eve "Я сказала слушай сюда!"

"Сигарета обжигает ладонь. Спасибо адреналину, я почти не чувстую боль. Может быть, именно это в конце концов вселяет в него страх передо мной. Он начинает тяжело дышать. Из его рта вырываются последние струйки дыма."
show eve rangerhat hair annoyed onlayer middle with dissolve
voice "scripte01s04_04df7b18"
Eve "Знаешь как меня тошнит от такого? Как часто мне приходится сидеть и смотреть, как подобные тебе разрушают хорошие вещи?"

Eve "Ты вообще осознаёшь что-то? Это просто игра для тебя?"

"Моё горло сжимается, а глаза щиплет от слёз. Я моргаю, но моё незамутнённое зрение показывает только кулак, сжимающий его рубашку. В неловкой тишине его друзья отводят глаза. Даже он начинает подрагивать, но я только крепче сжимаю его."
show eve rangerhat hair disgusted onlayer middle with dissolve

Eve "Что даёт тебе право сжигать последние остатки достоинства, которые остались от этой покрытой шрамами земли? Чтобы уничтожить все доказательства того, что когда-то мы были достаточно скромны, чтобы жить, дышать и умирать вместе с миром, в который мы попали. Прежде чем мы настолько привязались к себе и почувствовали потребность сделать различие.."

"Его глаза устремляются на меня и застывают."
show eve rangerhat hair furious onlayer middle with dissolve

Eve "ОТВЕЧАЙ!"
show eve rangerhat hair crying onlayer middle with dissolve
voice "scripte01s04_f8e712d4"
Eve "Говори, я тебе не пустышка, на которую можно лишь высокомерно смотреть!"

DCamper "Я ПЫТАЛСЯ РАЗЖЕЧЬ КОСТЁР СИГАРЕТОЙ, ЯСНО?"
show eve rangerhat hair nervous onlayer middle with dissolve
stop music fadeout 1.0
play sound "sfx/crow.ogg"
"Вдалеке кричат вороны. На мгновение я слышу только ветер. Слёзы рассеянно скатываются по щекам."

"Костёр. Сигаретой."
show eve rangerhat scratch furious onlayer middle with dissolve

"Четыре года сдерживаемого гнева, забытой страсти, разочарования и замешательства... всё это устремляется наружу, когда я замахиваюсь кулаком в его лицо."
show eve rangerhat scratch nervous onlayer middle with dissolve

"Кто-то хватает меня за руку, прежде чем я успеваю что-либо сделать."

$camera_move(-996, -416, 186, 0, duration=1, warper='ease')
show yosemite back neutral onlayer middle with dissolve:
    xpos 0.7 ypos 1.5 xanchor 0.5 yanchor 1.0
Yosemite "Достаточно, Ева."

"Я оборачиваюсь, кипя от ярости."

"Йосемити смотрит на меня сверху вниз, немного потрёпанная, но высокая и прямая, как Секвойя. Она возвышается над туристами. По сравнению с ней они выглядят как кусты."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Ты уже устроила им разнос. Они всё равно собирались сейчас уходить."

"Голос у неё суровый и уверенный. Она оглядывает группу туристов, её стальной взгляд прерывается потом, капающим с волос."

"Каждый из них утвердительно кивает. Парень в зелёной куртке вырывается из моей мёртвой хватки, и все они уходят вглубь лагеря."
show eve rangerhat scratch furious onlayer middle with dissolve

Eve "Какого чёрта ты делаешь? Они же теперь--"
window hide
show whiteflash onlayer forward with flash
$ camera_reset()
hide eve onlayer middle
hide yellow onlayer middle
hide coyote onlayer middle
hide zion onlayer middle
hide yosemite onlayer middle
hide camp_morning onlayer middle
hide fiyah onlayer middle
show cg3bg onlayer background
show cg3e gay onlayer background
show cg3y hug onlayer middle


$all_moves(camera_check_points={u'y': [(-2032, 0, u'linear')], u'x': [(0, 0, u'linear')], u'z': [(-553, 0, u'linear')]})
$camera_move(-2025, -3546, 81, 4, duration=15, warper='ease')
play music audio.memories
hide whiteflash onlayer forward with dissolve
window show
"Йосемити обвивает руки вокруг меня и затягивает в объятия. Моя шляпа падает на землю."

Yosemite "Спасибо. Мне нужно было это услышать."

Eve "Ч-что?"

"Её шепот ласкает мое ухо."

Yosemite "Ты сделала достаточно. По крайней мере, на сегодня."

"Я сделала… достаточно?"
show cg3e cry onlayer background with dissolve
"Я обмякла, услышав эти слова."

"За её плечом, в гуще леса, я вижу хижину, уютно устроившуюся под соснами, словно забытый рай. Куртка Йосемити источает цитрусовый аромат лемонграсса. Её кожа, хотя и не лихорадочная, тёплая, как объятия одеяла."

"Образ хижины расплывается, и у меня перехватывает дыхание. И впервые за четыре года я плачу не из-за злости, разочарованности или растерянности. Только из-за грусти."

"Я наконец могу позволить слёзам быть грустными."

Eve "Я только… хочу защитить то, что люблю."
show cg3y up onlayer middle with dissolve

"Йосемити прижимает мою голову к своему плечу и гладит меня по волосам."

"Мои слёзы пропитывают её куртку."
Yosemite "Ты дурак."

"Она хихикает, и я слышу мягкую усмешку в её голосе."
voice "scripte01s04_7992f23d"
show cg3y hug onlayer middle with dissolve

Yosemite "Но, может, нам нужно побольше дураков."

"Слёзы продолжают литься. Так много, что я вот-вот захлебнусь ими. С каждым вдохом, с каждым всхлипом моё горло сжимается всё сильнее. Может быть, оно пытается выжать всё это после стольких лет."

"Такая похвала значит для меня больше, чем одобрение или похлопывание по спине со стороны Джесси. Это подтверждение. Это признание. Даже если то, что я делаю, бессмысленно, я всё равно посвятила себя этому и страдала. И, может быть, это страдание не совсем бесполезно."

"И пока Йосемити обнимает меня, пока ветер воет в ветвях, а жаворонки над нами свистят, я начинаю думать, что, может быть, оно того стоит. Держаться и страдать. Хотя бы ещё немного."
stop ambient fadeout 3.0
stop music fadeout 2.0
window hide
show blackflash onlayer forward with fade
$ persistent.unlock_e1c3v1 = True
$ persistent.unlock_e1c3v2 = True
hide cg3e onlayer background
hide cg3bg onlayer background
hide cg3y onlayer middle
$ achievement.grant("Tree Hugger")

pause 3.0

#Passage of Time
$ camera_reset()
$ layer_move("background", 1860)
$camera_move(0, -1712, 0, 0, duration=0)
show cabininside_day1 onlayer background
show eve ranger scratch flat onlayer middle:
    xpos 0.5 ypos 1.30 xanchor 0.5 yanchor 1.0

play ambient "ambience/cabin daytime room tone.ogg"
play music audio.mariposa
hide blackflash onlayer forward with dissolve
window show
with dissolve
show jessie pocket stressed onlayer middle:
    subpixel True xpos 0.21 ypos 0.42 xanchor 0.5 yanchor 1.0 rotate None
with dissolve
Jessie "Даже рассказ обо всём этом вызывает головную боль. Как ты сумела отыскать столько неприятностей в первый же день?"

"В наушниках раздаётся голос Джесси. Я поворачиваюсь и снова смотрю на девочек. Йеллоустон протирает углы, не пропуская даже мельчайшие пылинки. Зайон сидит перед потрескивающим камином и гладит щенячье пузико. Йосемити делает пометки на листке бумаги, который она выкопала из завала таких же листков."
show eve ranger scratch deepthink onlayer middle with dissolve

Eve "Думаю, что у меня склонность к этому."
show jessie pocket curious onlayer middle with dissolve

Jessie "Но всё же, вот так просто наткнуться на такой пожар…"

"Она это говорит со смесью фальшивого любопытства и искренней заботы."

"Она что-то подозревает и пытается вытянуть это из меня. Джесси хитра, как и всегда."
show jessie pocket happy onlayer middle with dissolve

Jessie "Что ж, в любом случае, я рада, что ты в порядке. Нам ужасно повезло на этот раз."
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Со всем этим ветром, тебе лучше поверить, что нам правда повезло. Это могло стать ещё большей костью в горле."
show jessie pocket ditzy onlayer middle with dissolve

Jessie "Кость в горле - всё ещё кость в горле, Ева. Будет тяжко со всей этой бумажной работой."

"Как понимать это высказывание? Она сочувствует, что мне придётся писать десяток отчётов, или сокрушается, потому что ей придётся их читать?"
show eve ranger scratch deepthink onlayer middle with dissolve

Eve "Ага… Постараюсь приступить к ней побыстрее."
show jessie pocket smug onlayer middle with dissolve

Jessie "Сдашь мне отчёт, когда я приеду в следующий раз. Может на соседней станции перепишут всё за тебя, если будешь добра к ним."

"Её садисткий голос так и сочится солнечным светом. Я уже чувствую судороги в руке."
show jessie pocket sad onlayer middle with dissolve

Jessie "Но Ева…"

"Атмосфера становится серьёзной."

Jessie "Ты уверена, что больше ничего не хочешь мне сказать?"
show eve ranger scratch flat onlayer middle with dissolve

Eve "Больше абсолютно ничего."
show jessie pocket serious onlayer middle with dissolve

Jessie "Хм. Тогда ладно."

"Она меняет тему, хотя я не уверена, что смогла убедить её."
show jessie pocket ditzy onlayer middle with dissolve

Jessie "В таком случае, свяжусь с тобой завтра! И послезавтра тоже!"
show eve ranger scratch annoyed onlayer middle with dissolve

Eve "Ты правда не обязана."
show jessie pocket happy onlayer middle with dissolve

Jessie "О, но мне {i}хочется{/i}."
show eve ranger scratch flat onlayer middle with dissolve

Eve "Конец связи, Джесси."

"Она хихикает."

show jessie pocket yell onlayer middle with dissolve


Jessie "Конец связи, Ева. ЭРНИ УБЕРИ СВОИ ГРЯЗНЫЕ РУКИ ОТ МОИХ СУХОФРУКТОВ--"
show jessie pocket yell onlayer middle:
    ease 0.8 xpos -1.20
show eve ranger hair annoyed onlayer middle:
    ease 0.8 xpos 0.25 ypos 1.30 xanchor 0.5 yanchor 1.0
"Радио отключается, оставляя в покое мои лопнувшие барабанные перепонки. Отложив наушники в сторону, я поворачиваюсь и вижу, что все, кроме Йосемити, смотрят на меня."
show yellow volcano hips smug onlayer middle:
    subpixel True xpos 0.58 ypos 1.45 xanchor None yanchor 1.0 zoom 0.95
with dissolve
Yellowstone "Я так и знала. Ты мягкотелая слабачка."
hide jessie onlayer middle
show zion hands softsmile onlayer middle:
    xpos 0.63 ypos 1.04 xanchor 0.5 yanchor 1.0 zoom 0.81
with dissolve
Zion "С вишенкой наверху."
hide yellow onlayer middle
hide zion onlayer middle with dissolve
show yosemite back bored onlayer middle:
    subpixel True xpos 0.81 ypos 1.38 xanchor 0.5 yanchor 1.0 rotate None
with dissolve
"Йосемити берёт ещё бумажку и усмехается."
show yosemite chin smug onlayer middle with dissolve

Yosemite "Вишенка может быть и с косточкой. Осторожно, если такую укусить, можно и зубы сломать."

show whiteflash onlayer forward with flash
hide eve onlayer middle
hide zion onlayer middle
hide yosemite onlayer middle
hide yellow onlayer middle
hide cabininside_day1 onlayer background
hide camp_morning onlayer background
$ camera_reset()
$camera_move(2618, -2019, 54, 11, duration=0, warper='ease')
$camera_move(204, -1725, -444, 0, duration=20, warper='ease')
hide fiyah onlayer background
show table_background onlayer background
show cg4e annoyed onlayer middle
show cg4y smug onlayer middle
hide whiteflash onlayer forward with dissolve

"Я присоединяюсь к ней за столом и падаю в кресло."
voice "scripte01s04_6ab18cd1"
Eve "Не болтай, или в следующий раз позволю тебе сгореть дотла."
show cg4y annoyed onlayer middle with dissolve

Yosemite "Это была всего лишь лихорадка. Я бы поправилась -- рано или поздно."
show cg4e smug onlayer middle with dissolve

Eve "Как будто в этом есть смысл. Что, если здесь разожгут костёр или молния ударит в дерево? Что будет потом, а?"
show cg4y annoyed onlayer middle with dissolve

Yosemite "Что я тебе говорила про линейное мышление? Если это перемирие будет продолжаться, тебе нужно будет расширить его до абстрактного."
show cg4e annoyed onlayer middle with dissolve

Eve "Твое существование уже достаточно абстрактно для меня."

"Йосемити отрывает взгляд от своих бумажек."
show cg4y smug onlayer middle with dissolve

show cg4e smirk onlayer middle with dissolve

"Она поднимает глаза и ухмыляется. Я ухмыляюсь в ответ."

"Кто знает? Было бы забавно иметь спарринг-партнёра. По крайней мере, она интереснее, чем любой турист, с которым я собачилась. Она всегда кусает в ответ."
show cg4e smug onlayer middle with dissolve
stop music fadeout 2.0

Eve "Так, все меня слушаем!"

"Йеллоустон и Зайон вытягиваются по стойке ‘смирно’. Щенок перекатывается на свою щенячью задницу."
show cg4e annoyed onlayer middle with dissolve

Eve "Если остаётесь здесь, я хочу, чтобы это место оставалось безупречным! Свинарник - последнее, что я хочу видеть после рабочего дня!"
show cg4y smirk onlayer middle with dissolve

Yosemite "Йеллоустон позаботится об этом."
show table_zion onlayer forward with dissolve
Zion "Она может начать готовить и на тебя тоже."
show cg4b curious onlayer forward with dissolve
Yellowstone "Это так подло ребята. Вот так просто мной откупаетесь?"

Zion "О, мне это напомнило. Что вы сделаете с этими туристами, мисс Ева?"
Yellowstone "Оторвёшь им башни?"

Zion "Попросишь извинений?"
show cg4b dork onlayer forward with dissolve

Yellowstone "Выведешь их на задний двор?"

Zion "Заставишь покляться на мизинчиках больше так не делать?"
show cg4e smirk onlayer middle with dissolve

Eve "Ничего из вышеперечисленного. Я отвязалась от них. Если мне повезёт, их зарежет какой-нибудь убийца в лесу. В противном случае,они получают путёвку на свободу."
show table_pup onlayer middle with dissolve

"Обе выглядели шокированными, но, взглянув друг на друга, пожали плечами. Щенок подбежал и свернулся у моих ног."
show cg4y smug onlayer middle with dissolve
show screen unskip_text()
voice "scripte01s04_17d91b50"
play music "music/NPG_Insert_F_Instrumental.mp3"
Yosemite "А вот {i}это{/i} уже забавно.{w=0.1}{nw}"
show cg4e annoyed onlayer middle with dissolve
voice "scripte01s04_693fd6ef"
Eve "Что на этот раз?{w=0.1}{nw}"
$ persistent.unlock_promo = True
$ persistent.unlock_e1c4v1 = True
$ persistent.unlock_e1c4v2 = True
$ persistent.unlock_e1c4v3 = True
show cg4y smirk onlayer middle with dissolve
voice "scripte01s04_0d515be9"
Yosemite "Для того, кому на всё наплевать, ты вкладываешь в это удивительно много сил.{w=0.1}{nw}"
window hide
pause 0.3
play music "music/NPG_Insert_Vocal_E.mp3"
show blackflash onlayer forward with fade
hide table_background onlayer background
hide black onlayer background
hide cg4e onlayer middle
hide cg4y onlayer middle
hide table_pup onlayer middle
hide cg4b onlayer forward
hide table_zion onlayer forward
$ camera_reset()
hide blackflash onlayer forward with fade
show creditsblock onlayer background
with dissolve
show NPGCreditse1Card onlayer middle:
    yanchor 0.5 ypos 0.5
    xanchor 0.5 xpos 0.5
with dissolve
with Pause(3.5)
jump creditse01
