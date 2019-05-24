init:
    image cg_2 = "images/cg/cg_2.png"

transform floating:
    ease 1.0 yoffset -20
    ease 1.0 yoffset 0
    subpixel True
    repeat

label scripte01s03:

#Scene 03
#Eve’s Journal begins here

play ambient "ambience/fireplace with wind from inside the cabin.ogg"
play music audio.bitter
$ camera_reset()
$ layer_move("background", 1860)
hide black onlayer background
show cabininside_night1 onlayer background
with dissolve

show teddy onlayer middle with dissolve
show page01 onlayer forward with dissolve
Journal ""
hide page01 onlayer forward with dissolve
show page02 onlayer forward with dissolve
Journal ""
hide page02 onlayer forward with dissolve
show page03 onlayer forward with dissolve
Journal ""
hide page03 onlayer forward with dissolve
show page04 onlayer forward with dissolve

Journal ""
hide page04 onlayer forward with dissolve
show page05 onlayer forward with dissolve

Journal ""
hide page05 onlayer forward with dissolve
hide teddy onlayer middle with dissolve

#Eve’s journal entry ends here

$all_moves(camera_check_points={u'x': [(-1490, 0, u'linear')], u'z': [(400, 0, u'linear')]})
show eve casual hair bored onlayer middle:
        subpixel True xpos 0.36 ypos 1.45 xanchor 0.5 yanchor 1.0 rotate None
with dissolve

window show

"Ручка парит над бумагой, буква за буквой облачая мысли в слова. Однажды записанные, назад их уже не вернуть никогда. Довольно пугающе."
show eve casual scratch deepthink onlayer middle with dissolve:

"Вздыхая, я бросаю ручку и тянусь за чашкой. Но вместо противного, тепловатого кофе, в чашке меня ждал лишь коричневый осадок."

"Я потягиваюсь в кресле и издаю самый длинный зевок за последние двадцать минут. Или даже тридцать."

$all_moves(camera_check_points={u'y': [(0, 0, None), (0, 0.86, u'linear')], u'x': [(-1490, 0, None), (1846, 3, u'ease')]})

show eve casual scratch deepthink onlayer middle:
    subpixel True xpos 0.36 ypos 1.45 xanchor 0.5 yanchor 1.0 rotate None
    parallel:
        xpos 0.36
        ease 3 xpos 0.67
##PYUNPYUN What do I put here for edits
"Тащу своё туловище к плите и наливаю остатки кофе. Над чашкой поднимается пар."

"Кофе густой, на вид напоминает моторное масло. Горький и переваренный, по вкусу тоже, как масло. Но я не сноб, кофе есть кофе, хоть на захолустной заправке, хоть сваренный в дешёвом кофейнике."

"К тому же, в этом есть какая-то прелесть, не правда ли? Наслаждаться низкосортными просроченными продуктами."
show eve casual scratch flat onlayer middle with dissolve:

"Делаю глоток, и приходится смотреть на своё отражение, но вскоре оно превращается в неразличимую мутную пелену."
show eve casual hair deepthink onlayer middle with dissolve:

"Это то самое масло поднимается на поверхность. Противно, но без разницы, главное, даёт мне энергию, чтобы оставаться на ногах. Вести дневник тяжело. Может, даже сложнее, чем работать в Службе парков."

"Изначально это был просто способ избавиться от всей энергии, что бурлила внутри меня. Бабочки в животе. Надежды на будущее. Мечты о том, чтобы сделать парк лучше."

"Но стремление начало осуществляться и спустя время превратило меня в то, чем бы я сейчас ни была. Дневник стал местом для резкой сфокусированной рефлексии."

"Это хороший способ справляться. Кто-то пьёт. Кто-то укуривается. Я же мучаю тетради жалобами на всё на свете. Я их уже дюжину исписала. ‘Тедди, тома с 1 по 12.’ Мне нравится думать, что у них общее сознание."

"Я облокачиваюсь на рабочий стол, чашка согревает руку. Ветер бьёт и пинает хижину, и если прислушаться, можно услышать снаружи ночной шёпот. Стрекотание сверчков. Равномерное покачивание листьев."

"Все эти звуки дают меня понять, насколько тонким барьером от внешнего мира является это место. Тесный, обнесённый забором ящик. Единственное, что спасает меня от той же тьмы, лишь несколько тусклых ламп."

play sound "sfx/dumbass campers from inside.ogg"
"Снаружи эхом доносятся смех и разговоры. Когда я раскрываю занавески и вглядываюсь в окно, реальность даёт мне увесистую пощёчину. По зарослям возле хижины шатается группа из четырёх студентов. Один из них падает и растягивается на земле. Все начинают смеяться сильнее прежнего."

"Словом о барьере от внешнего мира."

$camera_move(1307, 0, 300, 0, duration=3, warper='ease')
show eve casual scratch bored onlayer middle:
 ease 3.5 xpos 0.4 ypos 1.45 xanchor 0.5 yanchor 1.0
with dissolve

play sound "sfx/walking on cabin floor.ogg"
"Я топаю к столу и хватаю фонарик. Направляясь к двери, я вспоминаю, что сменила форму на рваные джинсы и фланелевую рубашку. Не особо авторитарный вид."

show eve casual scratch deepthink onlayer middle with dissolve
pause 0.5
show eve casual scratch bored onlayer middle:
 ease 1.5 xpos 1.35 ypos 1.45 xanchor 0.5 yanchor 1.0
with dissolve
"Протягиваю руку к дивану и беру свою шляпу. Так-то лучше."

play sound "sfx/cabin door open.ogg"
play ambient "ambience/wind ambience with rustling leaves and night life.ogg" fadein 3.0
$ camera_reset()
$ layer_move("background", 2265)
$ night_tint = True
scene cabinoutdoor_night onlayer background:
 xpos 0.11 ypos 0.13 xanchor 0.2 yanchor 0.27
show eve casual hair bored onlayer middle:
 xpos 0.51 ypos 1.45 xanchor 0.5 yanchor 1.0
with dissolve
"Я распахиваю дверь, меня тут же приветствует свежий ветер. Затем я включаю фонарик и направляю луч на незванных гостей."

"Они застывают, словно олень, завидевший фары приближающегося грузовика. Смех затихает до негромких смешков, и единственный с каплей мозга велит им заткнуться. Другой под куртку прячет бутылку."

"Тот, что впереди -- наверное, самый умный -- щурится на меня сквозь свет фонарика. Его плечи расслабляются, и он небрежно машет мне рукой."

DCamper "Чао! Ты тоже на каникулах? Хочешь потусоваться?"
show eve casual hair annoyed onlayer middle with dissolve

"Ещё тысяча таких ребят могут принять меня за студента их возраста, и это всё равно не помешает мне лоботомировать их взглядом."
show eve casualhat hair annoyed onlayer middle with dissolve

"Я поправляю шляпу и угрожающе молчу. Ветхозаветный страх тенью появляется на их лицах. Они дружно делают шаг назад."

Eve "Знаешь, сколько тут пропавших без вести?"

DCamper "Ч-что?"
show eve casualhat hair furious onlayer middle with dissolve

Eve "Я спросила, знаешь ли ты сколько людей пропадает в этих местах? Ежегодно."

"Он вопросительно смотрит на приятелей. Они мотают головами. Он снова поворачивается ко мне и мотает головой. Вся группа мотает головами."

DCamper "М-мне очень жаль. Я не знаю."
show eve casualhat hair annoyed onlayer middle with dissolve

"Его руки подняты в знак капитуляции, между пальцами тлеет сигаретный окурок."
show eve casualhat hair furious onlayer middle with dissolve

Eve "Другой вопрос!"

DCamper "Д-да, мэм!"

"Наши голоса проносятся по лесу."

Eve "Знаете ли вы, сколько у меня будет бумажной работы, если кто-то из вас {i}хотя бы{/i} на сосновую шишку наступит?"

DCamper "Наверное… много?"
show eve casualhat hair annoyed onlayer middle with dissolve

"Друзья ему кивают. Он кивает в ответ."

DCamper "Да! Много! Верно?"
show eve casualhat hair furious onlayer middle with dissolve

Eve "Будем считать, что больше работы, чем вы, скорее всего, сделали за весь семестр."

"Это рассмешило одного из его приятелей. Тот затыкается, как только я свечу на него фонариком."
show eve casualhat hair annoyed onlayer middle with dissolve
voice "scripte01s03_64109489"
Eve "Сделайте мне одолжение и топайте обратно в лагерь, окей? Тогда мне не придётся объяснять своему куратору, почему вы все упали с обрыва."

"Две девушки, которые прячутся за остальными, смотрят на меня злобнымы взглядами. Таким взглядом идиоты смотрят на работников фаст-фуда, когда те им говорят, что картошка закончилась. Я включаю самый яркий режим на фонарике. Они дружно стонут, пытаясь прикрыть глаза от света."
show eve casualhat hair furious onlayer middle with dissolve

Eve "Давайте. Вы меня слышали. Сможете продолжить тут болтаться, когда солнце взойдёт."

"Я подсвечиваю фонариком тропинку."

"Он отходит на несколько шагов назад и любезно кивает."

DCamper "Безусловно. Извините за беспокойство. Приятной ночи."
show eve casualhat scratch deepthink onlayer middle with dissolve

Eve "Она такой не будет, но спасибо."

"Они следуют за лучом света обратно к тропинке. Один из них не поленился показать мне средний палец. Я выключаю фонарик, как только они исчезают в поросле деревьев."

"Надеюсь, что они на самом деле упадут с обрыва. Придурки."

play sound "sfx/short bush rustle.ogg"
stop music fadeout 1.5
"Когда я поворачиваюсь, чтобы войти внутрь, в кустах что-то шуршит."
show eve casualhat scratch scared onlayer middle with dissolve

"Моё тело цепенеет. Я застываю и перевожу взгляд на источник шума."

"Ничего."
show eve casualhat hair annoyed onlayer middle with dissolve

"Я медленно спускаюсь с крыльца, пытаясь дотянуться до пистолета, который не взяла с собой."

play sound "sfx/cabin porch creak.ogg"
"Я ступаю на землю, крыльцо скрипит у меня за спиной. Куст вздрагивает от резкого движения."

play sound "sfx/long bush rustle.ogg"
show coyote neutral onlayer middle:
 xpos 1.25 ypos 0.65 xanchor 0.5 yanchor 1.0
 ease 0.8 xpos 0.72 ypos 0.65 xanchor 0.5 yanchor 1.0
pause 0.3
show eve casualhat hair scared onlayer middle:
 ease 0.8 xpos 0.39 ypos 1.45 xanchor 0.5 yanchor 1.0
with dissolve
play music audio.anchors

"Из листьев вырывается пушистый шар. Его лапы царапают землю, прежде чем остановиться у моих ног."

Pup "{i}Аав!{/i}"
show eve casualhat hair flat onlayer middle with dissolve

"Вздыхая с облегчением, я наклоняюсь, чтобы поприветствовать своего принца."
show eve casualhat hair softsmile onlayer middle with dissolve

Eve "Решил вернуться, да? Не смог противостоять моему шарму?"

"Он прижимает уши, когда я чешу ему загривок. Он выглядит, как сумасшедший, пока я его ласкаю. Его зрачки пляшут туда-сюда."
show eve casualhat hair bigsmile onlayer middle with dissolve

Eve "Ты просто невозможный дурашка."

"Его ухо заворачивается. Если бы у моего сердца были струны, на нём можно было бы играть, как на скрипке."
show eve casualhat hair softsmile onlayer middle with dissolve

Eve "Это нечестно. Я ведь правда могу умереть."

"Я бросаю взгляд на пустую тарелку у двери. Ни крошки не оставил. Он должно быть сейчас сонный. Только посмотрите на этот живот. Он такой круглый, и милый, и розовый, и я умру сейчас, я просто знаю, что не выдержу."

play sound "sfx/whoosh.ogg"
show coyote neutral onlayer middle:
 ease 0.5 xpos -0.22 ypos 0.65 xanchor 0.5 yanchor 1.0 zoom 0.75

"Не понадобилось много усилий, чтобы заманить его внутрь. Я только освободила дверной проём, и щенок уже забегал в хижину, врезаясь в каждый предмет мебели, как пинбольный мяч."

Eve "Обычно я сначала подаю кофе!"


"Он чуть не кувыркается на полу, и мой пыльный смех наконец пригождается."
show eve casualhat hair annoyed onlayer middle with dissolve
show eve_hat onlayer middle:
 xpos 0.39 ypos 1.54 xanchor 0.5 yanchor 1.0
 linear 0.7 xpos 0.39 ypos 1.47 xanchor 0.5 yanchor 1.0 rotate 10
 ease 0.2 xpos 0.39 ypos 1.54 xanchor 0.5 yanchor 1.0 rotate 0
show eve casual hair annoyed onlayer middle


play sound "sfx/wind gust.ogg"
stop ambient fadeout 20.0
"Мимо меня проносится порыв холодного ветра. Почти срывает с меня шляпу, но я вовремя её ухватываю. Деревья яростно раскачиваются, сердито потрясая ветвями, как кулаками."

"Облака затягивают последний осколок Луны, погружая лес в глубокую тьму."
show eve casual hair bored onlayer middle with dissolve

show eve casual hair bored onlayer middle:
 ease 1.5 xpos -0.2 ypos 1.45 xanchor 0.5 yanchor 1.0
show eve_hat onlayer middle:
 ease 1.5 xpos -0.2 ypos 1.54 xanchor 0.5 yanchor 1.0 rotate 0

play sound "sfx/locking door.ogg"
"Холод пробегает по позвоночнику. Подрагивая, я втираю тепло обратно в тело, захожу внутрь и запираю дверь."

$ camera_reset()
$ layer_move("background", 1860)
hide cabinoutdoor_night onlayer background
$ night_tint = False
show cabininside_night1 onlayer background
hide eve_hat onlayer middle
show eve casualhat hair bored onlayer middle:
 xpos 0.28 ypos 1.45 xanchor 0.5 yanchor 1.0
show coyote neutral onlayer middle:
 xpos 0.8 ypos 0.65 xanchor 0.5 yanchor 1.0 zoom 0.75
with dissolve

play ambient "ambience/fireplace with wind from inside the cabin.ogg" fadein 3.0

show coyote neutral onlayer middle:
 ease 0.5 xpos 0.55 ypos 0.65 xanchor 0.5 yanchor 1.0 zoom 0.75
show eve casualhat hair softsmile onlayer middle with dissolve

show coyote neutral onlayer middle:
 ease 0.5 xpos 0.8 ypos 0.65 xanchor 0.5 yanchor 1.0 zoom 0.75
"Когда я вхожу, щенок подбегает ко мне, быстро, как молния, и сразу бросается обратно на диван."

pause 0.5
show eve casualhat hair softsmile onlayer middle:
 ease 1.0 xpos 0.49 ypos 1.45 xanchor 0.5 yanchor 1.0

"Я хватаю подушку с кровати и встречаю щенка у дивана. Он уже успел забраться на спинку дивана, и теперь смотрит на меня оттуда."
show eve casualhat hair annoyed onlayer middle with dissolve
Eve "О нет, ты не посмеешь."

show eve casualhat hair annoyed onlayer middle:
 ease 0.5 xpos 0.49 ypos 1.4 xanchor 0.5 yanchor 1.0
show coyote neutral onlayer middle:
 ease 0.5 xpos 0.8 ypos 0.6 xanchor 0.5 yanchor 1.0 zoom 0.75
pause 0.5
show eve casualhat hair annoyed onlayer middle:
 ease 0.5 xpos 0.49 ypos 1.45 xanchor 0.5 yanchor 1.0
show coyote neutral onlayer middle:
 ease 0.5 xpos 0.8 ypos 0.65 xanchor 0.5 yanchor 1.0 zoom 0.75
"Я хватаю его за шею. Он покусывает моё запястье, но это не больно, а скорее щекотно. Я роняю подушку, потом кладу на неё щенка."

"Сначала он пытается высвободиться, но я продолжаю давить ему на спину. В конце концов до него доходит сообщение, и он спокойно ложится."
show eve casualhat hair softsmile onlayer middle with dissolve
Eve "Скоро я принесу тебе что-нибудь более удобное."

"Поднимаясь, я задеваю ногой кофейный столик. Моё внимание привлекает случайный журнал."
show eve casualhat scratch annoyed onlayer middle with dissolve

Eve "Боже, Джесси, ты и это тут оставила?"

"Между страницами как закладка лежит пакетик чая."

"У неё вообще ничего лучше пакетика не нашлось, или она просто поленилась?"

"Хижина скрипит от порывов ветра. Щенок тихо смотрит на дверь шкафа, его уши настороженно напрягаются."

"Я рассматриваю журнал. Карта парка в паре со статьей. Все выходы из парка обведены красным."

show window onlayer master:
    subpixel True xpos 0.85 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None alpha -0.03
$camera_move(0, 0, -900, 0, duration=3, warper='ease')
pause 0.1
show black onlayer background
hide coyote neutral onlayer middle
hide cabininside_night1 onlayer background
with Dissolve (3.0)
stop music fadeout 3.0

"{i}Завершение вашего путешествия: Покидая Йосемити!{/i}"


window hide

hide eve onlayer middle with Dissolve(3.0)
pause 5.0
$ camera_reset()
$ layer_move("background", 1860)
$camera_move(-1843, 0, 471, 0, duration=0)
hide black onlayer background
show cabininside_night1 onlayer background
show eve casual hair bored onlayer middle:
    xpos 0.26
    ypos 1.45
    xanchor 0.5
    yanchor 1.0
with dissolve
#Passage of Time

window show

"Ночь проносится мимо меня. Часы проходят словно минуты, ночь углубляется всё дальше."

"В углу щенок грызёт свою лапу. Его зубы щёлкают в попытке поймать шустрых блох."

"Я пролистываю толстую пачку страниц, которые сегодня исписала, и взвешиваю их между пальцами."

"Неплохое начало для новой тетради."

"Я закрываю тетрадь, и до меня доносится успокаивающий запах свежего праймера."

show eve casual hair bored onlayer middle:
 ease 1.0 xpos 0.38 ypos 1.45 xanchor 0.5 yanchor 1.0

"Ковыляю к книжному шкафу."

"Лёгкое чтение перед сном - никогда не плохой способ закончить ночь. Особенно такую жуткую ночь, как эта."

"Окна хижины по краям обмёрзли. Лёгкий туман касается стекла, а темнота за ним напоминает чёрный зрачок."

"Тепло и комфорт наполняют мою грудь, когда я пробегаюсь пальцем по корешкам книг."

"{i}Направляясь в Йосемити: Карта и Путеводитель; Лучшие Места для Походов -- Йосемитский Национальный Парк; Коррупция в Службе Национальных Парков -- Йосемитская Мафия; Полный Справочник Йосемитского Национального Парка.{/i}"

"Почти каждая книга, брошюра и журнал отсылают к Йосемити, другим паркам или к самой Службе национальных парков. Даже жудожественные книги этому подвержены. Романы типа {i}Йосемити{/i} или {i}Йосемитский Гром.{/i}"

"Книги аккуратно расставлены в алфавитном порядке, но иногда встречаются пропуски. Недостающие тома. Пробелы между книгами. Такие часто можно увидеть в библиотеках."

"На нижней полке дела обстоят ещё более запутанно."

"На шкафу стоит гигантская картонная коробка, переполненная папками и бумагами. На самом верху балансирует розовая папка с яркими пузырчатыми буквами, нарисованными мелком."

"{i}ИССЛЕДОВАНИЕ МИВОКОВ!{/i}"

"Буквы окружены грубо нарисованными зубастыми кроликами и белками. Некоторые раскрашены аккуратными штрихами, строго внутри линий. А остальные были настолько небрежными и так сильно выходили за линии, что, казалось, восьмилетний под сахарным угаром справится лучше."

play sound "sfx/cabinet creak.ogg"
play music audio.bitter
"{i}Скрииииииииии…{/i}"
show eve casual hair scared onlayer middle
$camera_move(2121, 0, 471, 0, duration=0.5, warper='ease')

"Когда я тянусь за коробкой, из кухни начинает доноситься протяжный скрип."

"Отчётливый звук гнущихся петель заставляет моё сердце колотиться в горле."

"Это точно не осадка хижины."

"Щенок обнажает клыки. Низкое, вибрирующее рычание раздаётся из его маленького тела. Звучит, как большой и первобытный зверь."

"Его уши направлены вверх. Он пялится в угол, я прослеживаю его взгляд."

"Шкаф."

"Буфет возле раковины, всего в нескольких шагах от меня, открывается нараспашку."

"Я начинаю медленно идти к шкафу. Неожиданно, я теряю сцепление с полом. Ноги выскальзывают из-под меня, и я падая навстречу кухонной стойке."
play sound "sfx/eve slipping.ogg"

show eve casual hair disgusted onlayer middle:
 ease 0.2 xpos 0.38 ypos 1.5 xanchor 0.5 yanchor 1.0 rotate None
 ease 0.5 xpos 0.38 ypos 1.45 xanchor 0.5 yanchor 1.0 rotate None

Eve "Ай!"

"Я вскрикиваю, мой лоб чуть не ударяется об острый угол кухонной стойки. Я протягиваю руку и хватаюсь за него. Край царапает мою ладонь."

Eve "Это… было чересчур близко."
show eve casual hair annoyed onlayer middle with dissolve

"Я бросаю на щенка суровый взгляд, но он по-прежнему смотрит на дверь шкафа."

Eve "Это ты сделал?"

"На этот раз я надеюсь, что самый простой ответ и будет правильным. Но таинственный водяной след, ведущий к шкафу, намекает, что я не такая везучая."

play sound "sfx/whispering.ogg"
"Из шкафа доносится приглушённый шёпот. Тяжелое дыхание. Быстрые всплески движения, затем затишье."
show eve casual scratch deepthink onlayer middle with dissolve

"В моём мозгу всплывает то, что Джесси сказала днём."
show eve casual scratch flat onlayer middle with dissolve

"Насчёт этого места."
show eve casual scratch scared onlayer middle with dissolve

"Предыдущие рейнджеры думали, что здесь водятся привидения."
show eve casual scratch annoyed onlayer middle with dissolve

"Нет. Возьми себя в руки, Ева."

"Я хлопаю себя по щекам и отодвигаю эту мысль подальше."

"Здесь может быть только одно объяснение."

"Один из тех студентов как-то пробрался сюда и пытается меня напугать."
show eve casual hair deepthink onlayer middle with dissolve

"Да. Только и всего. Конечно."
show eve casual hair annoyed onlayer middle with dissolve
voice "scripte01s03_93ab0067"
Eve "Что я вам говорила, придурки, насчёт шатания здесь?"

"Я начинаю говорить громко и чётко, имитируя браваду своего школьного учителя физкультуры."
show eve casual hair furious onlayer middle with dissolve

Eve "Вы вторглись в федеральную собственность. Это серьёзная хрень. Выходите сейчас и, может быть, не окажетесь в наручниках."

"Шум прекратился. Я считаю секунды, но никто из шкафа не выходит."
show eve casual hair annoyed onlayer middle with dissolve

Eve "Отлично. Не говорите, что я вас не предупреждала."

play sound "sfx/eve stomping and opening door.ogg"
show eve casual hair annoyed onlayer middle:
 ease 2.0 xpos 0.69
"Я топаю к двери, стараясь, чтобы мои шаги были достаточно громкими. Повернув ручку, я приоткрываю дверь наполовину."
show eve casual hair disgusted onlayer middle with dissolve
stop music fadeout 0.8
window hide
play sound "sfx/horror stinger.ogg"
play ambient "ambience/full ghosty.ogg" fadein 3.0
show cg_2  onlayer forward:
    subpixel True xpos 0.33 ypos 1.25 xanchor 0.5 yanchor 1.0 zoom 1.29 rotate None
with flash
window show
"Из-под пожелтевшей простыни на меня смотрят два бледных глаза."
hide cg_2 onlayer forward
with flash
show eve casual hair disgusted onlayer middle:
 ease 0.5 xpos 0.44
play sound "sfx/door slaming.ogg"
"Я наглухо захлопываю дверь."

"Вот дерьмо. Я совсем не ожидала, что там правда кто-то будет!"
play music audio.fever

play sound "sfx/door bang 1.ogg"
"Я чуть не вскрикиваю от резкого удара в дверь."

play sound "sfx/door bang 2.ogg"
"Ещё удар. Громкий, как выстрел. От этих ударов дверь начинает выгибаться наружу."

$all_moves(camera_check_points={u'y': [(0, 0, None), (-49, 1.47, u'ease')], u'x': [(2121, 0, None), (1050, 1.47, u'ease')], u'z': [(471, 0, None), (371, 1.47, u'ease')]})
"Я отшатываюсь. Моя нога скользит по луже, но я, каким-то образом, удерживаю равновесие."

play sound "sfx/door bang 3 with thud.ogg"
"Наконец финальный, взрывной удар. Дверь распахивается и ударяется об стену."

show cabininside_dark1  onlayer background:
    xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
$ night_tint = True
with dissolve
"Все огни в хижине гаснут. Электричество покинуло это место."

"Внезапная темнота заставляет меня закричать. Я закрываю рот рукой и проглатываю ужас."

"Чёрт. Оно знают, где я сейчас."

play sound "sfx/yosemite scary stomps.ogg"
"Я делаю быстрые, панические вдохи. Затем доносятся шаги."

show red onlayer forward with ironspy_flash
$ camera_reset()
hide eve onlayer middle

$all_moves(camera_check_points={u'y': [(-2022, 0, u'linear')], u'x': [(-81, 0, u'linear')], u'z': [(-500, 0, u'linear')]})
show scary_background onlayer background
show cg2e scared onlayer background
show cg2y scary onlayer background
show cg2z onlayer middle
show cg2p bark onlayer middle
hide red onlayer forward with dissolve

"В дверном проёме шкафа начинает вырисовываться силуэт."

"Щенячье рычание перехолит в злобный лай."

"Я стою на месте, выпятив грудь и расправив плечи."

"Призрак, домушник, медведь… Кто бы это ни был, вариант у меня только один."

$camera_move(-4425, -4622, 700, 0, duration=2.0, warper='ease')
Eve "Ч-что тебе надо?"

"Я обращаюсь к медлительной тени. Её голова наклоняется, будто я застала её врасплох."

$camera_move(-2169, -4622, 700, 0, duration=1.0, warper='ease')
GShadow "Тебе… здесь не место."

"Во тьме звучит голос, сухой и замогильный. Но в то же время чистый. На мой взгляд, красивее, чем должен быть у демонического явления."

"Не то чтобы я верю, что это демоническое явление или что-то в этом роде."
show cg2e annoyed onlayer background with dissolve

$camera_move(-4425, -4622, 700, 0, duration=1.0, warper='ease')
Eve "Это мой пост. И если верить моему куратору, здесь мне как раз и место."

$camera_move(-2169, -4622, 700, 0, duration=1.0, warper='ease')
GShadow "Нас не волнуют законы и правила смертных."
show cg2e scared onlayer background with dissolve

Eve "Нас…?"

$camera_move(-81, -2022, -500, 0, duration=3.0, warper='ease')
"Тусклое свечение загорелось в приоткрытом шкафу, подсвечивая фигуру кроваво-красным светом. Вода стекает с её намокших волос, чёлка отбрасывает тень на глаза. Она стоит неестественно прямо, как палка, а руки висят, как у трупа. На её кожаной одежде переплетаются красочные узоры. Шею обвивают бусы."

"Девушка?"

"Мимо неё прямо по воздуху проплывает призрак в простыне. Дрожь пробегает по моему позвоночнику, когда он левитирует в нескольких футах передо мной."

"Это должно быть розыгрыш. Меня дурачат. Это точно дело рук Джесси и Эрни."

GShadow "Покинь место нашего упокоения!"

M1 "Ага! Я обделалась!"

"Из шкафа доносится высокий энергичный голос. Мрачная фигура, не поворачиваясь, пинает шкаф. Раздаётся визг, красное свечение мигает несколько секунд, а затем снова приходит в норму."

GShadow "СЕЙЧАС ЖЕ!"

"Громовой ветер колотит по хижине. Выкрик мрачной фигуры отдаётся в деревянных досках."

"Из-под простыни доносится приглушённый тканью стон. Почти так же жутко, как ребёнок, изображающий призрака в Хеллоуин."
show cg2e annoyed onlayer background with dissolve

$camera_move(-4425, -4622, 700, 0, duration=2.0, warper='ease')
Eve "Как бы мне не хотелось, - а мне хочется, поверь - я не могу. Я и так хожу по тонкому льду."

"Высокая мрачная фигура заикается, и, хотя я не вижу её глаз, я могу различить глубокую хмурость."
show cg2y annoyed onlayer background with dissolve

$camera_move(-2169, -4622, 700, 0, duration=1.0, warper='ease')
GShadow "Т-ты пытаешься спорить со мстительным духом? Ты хоть понимаешь насколько это смехотворно?"

$camera_move(-4425, -4622, 700, 0, duration=1.0, warper='ease')
voice "scripte01s03_6b7a6c48"
Eve "А понимаешь ли {i}ты{/i} насколько смехотворно {i}твоё{/i} требование?"

$camera_move(-2169, -4622, 700, 0, duration=1.0, warper='ease')
GShadow "Это не моя проблема! Базовый инстинкт ставит выживание выше дохода. Ты ведь понимаешь это? Не так уж сложно."


$camera_move(-4425, -4622, 700, 0, duration=1.0, warper='ease')

voice "scripte01s03_e4fab3cc"
Eve "Базовые инстинкты были переписаны базовой тренировкой. К тому же, дело совсем не в деньгах. А ты не очень-то проницательна для духа."

show cg2y scary onlayer background with dissolve

$camera_move(-2169, -4622, 700, 0, duration=1.0, warper='ease')
GShadow "ТИШИн--"

$camera_move(-81, -2022, -500, 0, duration=3.0, warper='ease')
"Она кричит своим угрюмым, хриплым голосом, но срывается и заходится кашлем."
show cg2y annoyed onlayer background with dissolve

GShadow "Просто заткнись, ладно? Заткнись!"

"Бравада полностью выветрилась из её голоса. Теперь это не мстительный, а всего лишь раздражённый дух."
show cg2y scary onlayer background with dissolve

GShadow "Если останешься, вини только себя за то, что произойдёт!"

"Красное сияние позади неё вспыхивает, озаряя стены ярким отблеском. Щенок отвечает лаем. Простынный призрак устремляется ко мне по воздуху."

$camera_move(-6400, -4780, 1100, 0, duration=1.5, warper='ease')
"Я разворачиваюсь и ныряю к оружейному шкафу."

"Ну же, Джесси. Давай. Пожалуйста, скажи, что забыла закрыть его."

"Я дёргаю ручку и дверца моментально открывается."

"Да! Я знала, что всегда могу положиться на тебя, Джесси. Напомни мне пригласить тебя на ужин, если я выживу."

"Дробовик всё ещё подпирает заднюю стенку шкафа, нетронутый и неиспользованный. Я тянусь и хватаю его. Встаю наизготовку, приклад дробовика упирается в грудь."

"Адреналин пульсирует в венах. Я снимаю предохранитель. Обхватываю пальцем спусковой крючок."

"Пряди волос прилипают к лицу. Призрак в простыне смотрит на меня, теперь твердо стоящюю на земле."

"Он точно у меня на мушке."

"Палец на спуске дрожит. {i}Я{/i} дрожу. Температура крови резко падает, и моё тело отрезвляет холодом."

"Это не то, чего я хотела от этой работы. Я никогда не хотела причинять вред людям. Целиться в них ружьём или бить по лицу."

"Я только хотела защищать--"
window hide
show red onlayer forward with ironspy_flash
hide scary_background onlayer background
hide cg2e onlayer background
hide cg2y onlayer background
hide cg2p onlayer middle
hide cg2z onlayer middle
hide cabininside_dark1 onlayer background
show test_spooky onlayer background
$ fire_tint = True
$camera_move(0, -696, 0, 0, duration=0)
$ layer_move("background", 1860)
show eve casual hair disgusted onlayer middle:
    xpos 0.15 ypos 1.50 xanchor 0.5 yanchor 1.0 rotate None
hide red onlayer forward with dissolve
window show

"Ткань, наброшенная на призрака, начинает стягиваться. Щенок хватает её зубами и тоже начинает стягивать, будто это игра в перетягивание каната."

$ persistent.unlock_e1c2v1 = True
$ persistent.unlock_e1c2v2 = True
play ambient "ambience/half ghosty.ogg" fadein 1.5
"Простыня падает на пол, и я наконец могу увидеть чему -- или скорее {i}кому{/i} -- принадлежат эти тонике ножки."

show zion arms nervous onlayer middle at floating:
    subpixel True
    xpos 0.76
    ypos 1.05
    xanchor 0.5
    yanchor 1.0
    zoom 0.81

with dissolve
stop music fadeout 1.5
play music audio.bitter

"Она стоит с широко раскрытыми глазами, дрожащая, как грабитель, застигнутый на месте преступления. Листья шелестят на её крошечном бежевом платье. Из длинных, расчёсанных волос торчат веточки, а на макушке покоятся листья в форме венка."

"Но больше всего меня удивляет пара крыльев, торчащих из её спины, пушистых и белых, как у ангелочка."
show eve casual hair scared onlayer middle with dissolve
Eve "Ребёнок?"

"И совсем маленькая. Я могла подхватить её обеими руками, если бы захотела."
show yosemite back bored onlayer middle:
    subpixel True xpos 1.2 ypos 1.45 xanchor 0.5 yanchor 1.0 rotate None
show yosemite back bored onlayer middle:
 ease 1.0 xpos 0.67
show zion arms nervous onlayer middle at floating:
 ease 1.0 xpos 0.94
GShadow "Что, чёрт возьми, ты делаешь?"


"Мрачный призрак топает по скрипящим половицам, направляясь прямо ко мне."

"Запаниковав, я перевожу дробовик на неё, но она уже возвышается надо мной."
show eve casual hair furious onlayer middle with dissolve
Eve "Н-ни шагу дальше!"
show yosemite back annoyed onlayer middle with dissolve

"Её зеленые глаза сверкают. В своем сильном гневе они почти светятся, когда она хватается за дробовик."

"Я закрываю глаза, и мой голос срывается на крик."
show eve casual hair disgusted onlayer middle with dissolve

Eve "ОТВАЛИ!"

play sound "sfx/trigger.ogg"
"Я нажимаю на спуск."
show yosemite back neutral onlayer middle with dissolve
play sound "sfx/trigger.ogg"
"Нажимаю второй раз."

"Ничего."

"Этого… этого не может быть."
show yosemite back bored onlayer middle:
 ease 0.8 xpos 0.51
 ease 1.0 xpos 0.67
"Я открываю глаза, как раз чтобы увидеть, как она вырывает дробовик их моих рук."
show yosemite back annoyed onlayer middle with dissolve

GShadow "А я думала, что они вас, головорезов, обучали чему-то получше, чем направлять эти штуки на всех подряд!"

"Она пытается вытащить из дробовика патроны... которых там нет."
show yosemite back smug onlayer middle with dissolve

GShadow "... И если всё-таки тычешь - убедись, что он заряжен. Они тебя наняли из жалости?"
show eve casual hair annoyed onlayer middle with dissolve

"Я снова заглядываю в оружейный шкаф. В углу стоит маленькая коробка с патронами."
show eve casual hair scared onlayer middle with dissolve
"Ну конечно."
show eve casual hair scared onlayer middle:
 ease 0.9    ypos 1.55
"Я начинаю вжиматься в стену."

"Вот и всё. Я мертва. Скорее всего, я это заслужила."
show zion arms softcry onlayer middle at floating with dissolve
"Маленькая девочка, бледнее, чем простыни, под которыми пряталась, смотрит на высокого призрака. Её глаза наполняются слезами."

SGhost "Йо… Йосемити!"
show zion arms softcry onlayer middle at floating:
 ease 0.7 xpos 0.80
show yosemite back nervous onlayer middle with dissolve

"Она издает робкий писк и бросается за спину своей подруги. Она обхватывает её ноги, выглядывает из-за них, словно из укрытия, и шмыгает носом."

SGhost "Я больше не хочу этим заниматься."
show yosemite back cringe onlayer middle with dissolve
GShadow "Зайон…"
show zion arms softcry onlayer middle at floating:
 ease 0.7 xpos 0.81
show yosemite back cringe onlayer middle:
 ease 0.5 xpos 0.68
"Она подносит малышку поближе и хмурится, глядя, как по её щекам текут слезинки."

"Издалека она выглядела как существо из фильма ужасов. Неестественно синие волосы с матово-белыми кончиками. А все её тело было залито этим красным сиянием."

"Но видя её вблизи и наблюдая, как её охватывает беспокойство, я начинаю думать, что она похожа на почти обычную девушку."

"Почти."
show eve casual hair annoyed onlayer middle with dissolve

Eve "Зайон? Йосемити? Да кто вы вообще такие?"
show yosemite chin neutral onlayer middle with dissolve
show eve casual hair nervous onlayer middle:
 ease 0.8 xpos 0.10
with dissolve
"Её голова поворачивается ко мне. Мои плечи напрягаются. Я стою у стены, идти больше некуда."
show yosemite back yelling onlayer middle:
 ease 0.4 xpos 0.52

Yosemite "Тишина, смертный! Мы навождали эти земли задолго до тебя…"
show cabininside_night1 onlayer background
hide test_spooky onlayer background
$ night_tint = False
$ fire_tint = False
stop music fadeout 0.8
with dissolve
"Красный свет, проникающий в комнату из шкафа, гаснет. Лампы снова включаются вместе с остальным электричеством."
show yosemite back annoyed onlayer middle with dissolve


stop ambient fadeout 3.0
Yosemite "... и будем ещё долго наваждать после того, как ты вернёшься... в... землю."
show yosemite back neutral onlayer middle with dissolve

"Она замолкает."

"Я моргаю"
show yosemite back blush onlayer middle with dissolve

"Она моргает."
show yosemite back bored onlayer middle with dissolve

Yosemite "Йеллоустон?"

M1 "Да, босс?"

"Из шкафа ей отзывается энергичный голос."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Не хочешь мне сказать почему свет включился?"

M1 "Ну, потому что я его включила, прикинь."

Yosemite "Это я поняла, но зачем?"
show yellow hat hips pout onlayer middle:
    subpixel True xpos 1.3 ypos 1.45 xanchor 0.5 yanchor 1.0 zoom 0.95 rotate None
show eve casual hair disgusted onlayer middle with dissolve
"Я медленно тянусь к дробовику. Есть шанс забрать его обратно. Может, даже до патрон дотянусь."

play ambient "ambience/fireplace.ogg"
show yellow volcano hips sad onlayer middle:
    ease 1.2 xpos 0.90 ypos 1.45
show zion arms softcry onlayer middle at floating:
    ease 1.2 xpos 0.74 ypos 1.04 xanchor 0.5 yanchor 1.0
voice "scripte01s03_e2abe5a3"
M1 "Так игра окончена! Она больше не ведётся."

"Из шкафа выскакивает девочка-подросток. Её одежда окрашена в пастельные тона, а яркие хвостики подпрыгивают вверх-вниз. Она была бы самой нормальной из них, если бы не одна отвлекающая деталь."

"Из её макушки, словно гора, торчит гигантский конус. Приплюснутый сверху, с разными оттенками коричневого, он напоминает вулкан из детского научного проекта."
show eve casual hair annoyed onlayer middle with dissolve
"Это типа костюм? Или шляпа? Оно будто сливается с её волосами."
show yellow volcano hips pout onlayer middle with dissolve

M1 "Посмотри! Она уже готовится снести тебе крышу."
show yosemite back neutral onlayer middle with dissolve

"Та, которая мрачная и высокая, поглядывает на меня. В смущённом оцепенении я совершенно забыла о своей руке, нависшей над дробовиком."

show yosemite back annoyed onlayer middle:
    ease 0.5 xpos 0.38 ypos 1.45 xanchor 0.5 yanchor 1.0
    ease 0.5 xpos 0.52 ypos 1.45 xanchor 0.5 yanchor 1.0

"Закатив глаза, она выдергивает его и отправляет по полу в другой конец комнаты."
show yosemite chin neutral onlayer middle with dissolve

$camera_move(-6000, 0, 400, 0, duration=1.5, warper='ease')
show yosemite chin neutral onlayer middle:
     ease 1.0 xpos 0.41
     ease 1.0 ypos 1.60
show yellow volcano hips pout onlayer middle with dissolve:
     xpos 1.3
show zion arms softcry onlayer middle with dissolve:
     xpos 1.3

"Она садится на корточки, и, с бесстрастным взглядом, щёлкает меня по лбу. Тупая боль пронзает мой череп."

Yosemite "Я знаю, ты намерена снова забрать у меня мой дом, но позволь мне сначала кое-что уладить. Окей, стрелок?"

"Пока мой лоб приходит в себя, я скриплю зубами, стирая их в пыль."
show eve casual hair furious onlayer middle with dissolve

Eve "Нет, {i}не окей{/i}. Лучше попробуй ещё раз меня щёлкнуть."
show yosemite chin smug onlayer middle with dissolve
show coyote neutral onlayer forward:
 xpos -0.7 ypos 0.8
"Скользкая ухмылка расползается по её лицу, и она снова поднимает руку, держа наготове большой и указательный пальцы."
show yosemite back neutral onlayer middle with dissolve

$camera_move(0, -696, 0, 0, duration=1, warper='ease')
show coyote bark onlayer forward:
 ease 0.5 xpos 0.43 ypos 0.63 xanchor 0.5 yanchor 1.0 zoom 0.9 rotate None
show yosemite back neutral onlayer middle:
 ease 0.5 ypos 1.45 xpos 0.88
"Я готовлюсь к следующему щелбану, но тут щенок бросается мне на помощь и пытается схватить её лодыжку. Она вовремя отшатывается, а щенок загораживает меня и рычит."
show eve casual hair softsmile onlayer middle with dissolve
Eve "Хех. Хороший мальчик."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Что я тебе такого сделала? Я же чесала тебе живот и всё остальное!"

"Она скулит. Щенок воет. Я думаю, что люблю этого маленького парня всё больше с каждой минутой."
show yosemite back neutral onlayer middle with dissolve
hide zion onlayer middle
show zion arms softcry onlayer forward:
 xpos 1.30 ypos -0.39 zoom 0.81
Yosemite "Зайон, дорогая, можешь отвлечь этот пушистый шар на себя?"
show eve casual hair nervous onlayer middle with dissolve
"Маленькая девочка, которая с тех пор удалилась на кухню со своей конусоголовой подругой, быстро кивает."

Zion "А! О-окей!"
show yosemite back neutral onlayer middle:
     ease 1.0 xpos 0.92 ypos 1.45 xanchor 0.5 yanchor 1.0
show zion arms nervous onlayer forward at floating:
     ease 0.8 xpos 0.49 ypos -0.39 zoom 0.81 subpixel True
"Сосредоточившись, она хлопает своими маленькими крылышками и плывёт по комнате, подзывая щенка к себе."
show zion arms softsmile onlayer forward at floating with dissolve
Zion "Эй, мальчик! Хочешь поиграть?"

"Она складывает губы, чтобы свистнуть, но лишь выдувает из себя воздух. Когда понимает, что это не сработает, начинает щёлкать языком. Запустив руку в волосы, она распутывает из них веточку и машет ею перед глазами."
show zion arms happy onlayer forward with dissolve
Zion "Я вырастила для тебя новую палку. Пожалуйста, как тебе?"
show coyote neutral onlayer forward with dissolve
show coyote neutral onlayer forward:
 ease 1.2 xpos 1.6
show zion arms happy onlayer forward:
 ease 1.2 xpos 1.2
"Щенок вскидывает голову. Его злобный оскал превращается в улыбку, и он совершенно забывает о своём долге защищать меня."

show yosemite back cringe onlayer middle with dissolve
show yosemite back cringe onlayer middle:
        ease 1.0 xpos 0.6 ypos 1.45 xanchor 0.5 yanchor 1.0
Yosemite "Это был провал."

"Высокая девушка щиплет себя за переносицу и вздыхает."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Немалой степени благодаря отсутствию усилий с {i}твоей{/i} стороны."

"Она поворачивается к той, что стоит на кухне и качает голову взад-вперед под тихую мелодию."

show yellow volcano hips pout onlayer middle:
 ease 1.5 xpos 0.84
M1 "Я {i}устааалаа.{/i}"
show eve casual hair annoyed onlayer middle with dissolve

"Она падает на стойку и стонет."
show yellow volcano hips comiccry onlayer middle with dissolve
M1 "Мы это уже в миллионный раз делаем. Но это такой отстой."
## If you mean like a peach pit, where you eat a delicious peach and you look at it and see the pit and go "ahhh I'm satisfied"
show yosemite back yelling onlayer middle with dissolve

Yosemite "Мы делаем это, потому что это работает! Последний парень редко заходил сюда после того, как мы его хорошенько напугали."
show eve casual scratch nervous onlayer middle with dissolve

Eve "Получается… предыдущие жильцы и правда думали, что здесь есть привидения…"
show yosemite back annoyed onlayer middle with dissolve

Yosemite "А они здесь как раз есть. А теперь уходи."
show yellow volcano hips happy onlayer middle with dissolve
voice "scripte01s03_a0337a12"
M1 "Но она другая! Куколка попыталась затеять драку!"

"{i}Куколка?{/i} Я была бы раздражена, если бы это так сильно не сбивало с толку."
show yosemite back neutral onlayer middle with dissolve

Yosemite "Она мне не нравится."
show yellow volcano hips pout onlayer middle with dissolve

M1 "Тебе никто не нравится."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Она слишком высматривающая."

"Она бросает на меня подозрительный взгляд."
show eve casual scratch annoyed onlayer middle with dissolve

"Чувства взаимны."

"Конусоголовая хватает чайник с плиты и скачет к нам."
show yellow volcano hips wink onlayer middle with dissolve

M1 "Это меня в ней и привлекает."

"Она открывает крышку чайника и протягивает его своей высокой подруге."
show yosemite back neutral onlayer middle with dissolve

"Высокая выжимает волосы, как мокрую тряпку. Вода, словно из здоровенной губки, начинает течь в чайник."

"Чайник наполняется до краёв, а её волосы становятся совершенно сухими."

"Что за херня."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Что ж, я рада, что ты так думаешь, хоть ты и не права."
show yellow smoke hips wink onlayer middle with dissolve
"Из отверстия на голове конусоголовой начинает вырываться пар. Под ним потрескивает красное зарево."

"Нет, серьёзно. Что за херня."
show yellow tea hips wink onlayer middle with dissolve

"Она осторожно ставит чайник себе на голову."
show yellow tea hips happy onlayer middle with dissolve

M1 "Снова лемонграсс?"
show yosemite back bored onlayer middle with dissolve

Yosemite "Пожалуйста. И, в этот раз, не подсыпай туда сахар."

"Из носика чайника начинает подниматься пар, сопровождаемый свистом."

"Свист становится громче, болтовня набирает обороты. Щенок тявкает, бросаясь через комнату за палкой. Клубы пара становятся гуще."

"И пока шум нарастает, нарастает и нарастает, я чувствую, как закипаю изнутри."

"Все мои страхи были подавлены сильной потребностью в тишине и покое."

"И в каких-нибудь разъяснениях."

"В чём-нибудь, что хотя бы отдалённо будет иметь смысл."

"Я поднимаюсь на ноги и вдыхаю столько воздуха, сколько могут уместить мои лёгкие."
show eve casual scratch furious onlayer middle:
 ease 1.0 ypos 1.35
show yellow tea hips concern onlayer middle
show yosemite back curious onlayer middle with dissolve
stop music fadeout 0.5
Eve "МНЕ КТО-НИБУДЬ ОБЪЯСНИТ КАКОГО ХРЕНА ЗДЕСЬ ПРОИСХОДИТ?!"


"Болтовня стихает. Крылатая девочка отпрянула, прижимая щенка к груди. Чайник гудит, как паровоз. Все взгляды устремлены на меня."

"Наконец-то."
show eve casual scratch annoyed onlayer middle with dissolve
voice "scripte01s03_5286e8fe"
Eve "А теперь кто-нибудь из вас скажет мне, кто вы такие? Я никогда не слышала о призраках, которые могут касаться людей. Или у которых есть крылья. Или что там у тебя на голове. Вы косплееры? Что за чертовщина?"
show yosemite back annoyed onlayer middle with dissolve

"Их высокая предводительница насмешливо хмыкает и отворачивается, скрестив руки на груди."
show yellow tea hips wink onlayer middle with dissolve

M1 "А, так это всё, что ты хочешь знать? Про это я могу пояснить."
show yosemite back yelling onlayer middle with dissolve

Yosemite "Эй! Не раскрывай ей наши секреты!"
show yellow tea hips happy onlayer middle with dissolve

M1 "Остуди сопла, я всего лишь расскажу, кто мы такие. Но сначала, я хочу узнать кто она такая!"
show eve casual scratch flat onlayer middle
show yosemite back neutral onlayer middle
with dissolve

"Она смотрит на меня с широкой, выжидающей улыбкой. Остальные тоже смотрят, ожидая, когда ответ наконец вырвется из мёртвой тишины."
show eve casual scratch annoyed onlayer middle with dissolve
show eve casual scratch annoyed onlayer middle:
    ease 1.0 xpos 0.15

Eve "Меня зовут Ева. Я…"
show eve casual scratch deepthink onlayer middle with dissolve

"Рейнджер?"

show eve casual hair annoyed onlayer middle with dissolve
show zion arms nervous onlayer forward:
 ypos -0.21

Eve "Я здесь работаю."
"Удовлетворённая моим не-ответом, она утвердительно кивает. Чайник аккуратно покачивается на её голове."
show yellow tea peace wink onlayer middle with dissolve

Yellowstone "Как делишки, Ева! Приятно познакомиться! Если ты ещё не въехала, {i}Я{/i} Йеллоустон!"

"Она тычит на стену с картинами."
show yellow tea peace wink onlayer middle:
 ease 0.9 xpos 1.30
pause 0.7
$camera_move(0, -1214, -300, 0, duration=1, warper='ease')
show zion arms nervous onlayer forward at floating:
 ease 0.9 xpos 0.57 ypos -0.39 subpixel True

show yellow tea hips excited onlayer middle:
 ease 0.9 xpos 0.95
Yellowstone "Этот Земной Ангел - Зайон! Она милашечка, очень её люблю!"

"Бледные щеки Зайон краснеют, и она слегка машет рукой."

show zion hands softsmile onlayer forward at floating with dissolve


Zion "Т-тоже люблю тебя."
show yellow tea hips happy onlayer middle with dissolve

Yellowstone "А это у нас Йосемити! Она нам типа старшей сестры. Её я тоже очень люблю, хоть она и большая брюзга."
show yosemite back bored onlayer middle with dissolve

"Йосемити сохраняет молчание."
show eve casual hair deepthink onlayer middle with dissolve

"Я смотрю на картины и пытаюсь соотнести их с девушками."

show eve casual scratch nervous onlayer middle with dissolve

Eve "Так вас назвали в честь парков? Или это такие прозвища?"
show yellow tea hips sad onlayer middle with dissolve

"Йеллоустон наклоняет голову и моргает."

Yellowstone "{i}Нееее.{/i}"

"Она указывает на себя."
show yellow tea hips happy onlayer middle with dissolve

Yellowstone "{i}Я и есть{/i} Йеллоустон."
show yellow tea peace wink onlayer middle with dissolve

"Она бросается к Зайон и обнимает её сзади."

show yellow tea hips happy onlayer middle with dissolve
Yellowstone "{i}Она и есть{/i} Зайон."
show yellow tea hips happy onlayer middle with dissolve

"Она бежит обратно к Йосемити и хлопает её по спине. Я практически чувствую эти громкие шлепки, а Йосемити чуть не выпрыгивает из кожи."

Yellowstone "А это Йосемити {i}собственной персоной{/i}."

"Каким-то образом чайник умудряется не свалиться с головы Йеллоустон во время её передвижений."

"Я пытаюсь сложить два и два, но всё равно выходит пять."
show eve casual scratch annoyed onlayer middle with dissolve

Eve "Так ты что говоришь? Вы {i}и есть{/i} эти самые парки?"
show yellow tea hips sad onlayer middle with dissolve

"Её лицо морщится в раздумьях. Поднимающийся из головы пар, кажется, может исходить прямо её напрягшегося мозга. Она смотрит на Йосемити в поисках ответов."

"Йосемити кивает."
show yellow tea peace happy onlayer middle with dissolve

Yellowstone "Ага! Так и есть!"
show eve casual hair deepthink onlayer middle with dissolve

Eve "Отлично, я вызываю своего куратора."
show yellow tea hips sad onlayer middle

Yellowstone "Эээй? Почему?"
show yosemite back annoyed onlayer middle with dissolve
Yosemite "Я говорила, что никто не поймёт."
show eve casual hair annoyed onlayer middle with dissolve
Eve "Я не знаю, как вы проворачиваете все эти фокусы, но проблема есть проблема. А вы трое - как раз одна из них."

"Я разворачиваюсь и начинаю идти к столу с радио."
show yellow tea hips seriouscry onlayer middle
show yosemite back neutral onlayer middle
with dissolve

"Лицо Йеллоустон искажает паника, её взгляд переключается то на меня, то на Йосемити. Чайник свистит над ней, пока, наконец, она не решает передать его Йосемити."
show yellow volcano hips pout onlayer middle with dissolve

Yellowstone "Пять сек."

show zion hands softsmile onlayer forward at floating:
    ease 1.0 xpos 0.75 subpixel True
show yosemite back neutral onlayer middle:
    ease 1.0 xpos 0.79 ypos 1.45 xanchor 0.5 yanchor 1.0
show yellow volcano hips pout onlayer middle:
     ease 1.5 xpos 0.51 ypos 1.45 xanchor 0.5 yanchor 1.0

"Она хватает меня за запястье. Дым от её головы клубится у неё за спиной. Я пытаюсь вырваться."
show eve casual hair furious onlayer middle with dissolve

Eve "Отпусти!"
show yellow volcano hips sad onlayer middle with dissolve

show yellow volcano hips pout onlayer middle:
    ease 0.5 xpos 0.45 ypos 1.45 xanchor 0.5 yanchor 1.0
pause 0.5
show yellow volcano hips pout onlayer middle:
    ease 0.2 xpos 0.51 ypos 1.45 xanchor 0.5 yanchor 1.0
show eve casual hair furious onlayer middle:
    ease 0.2 xpos 0.24 ypos 1.35 xanchor 0.5 yanchor 1.0
Yellowstone "Ты просто нам не веришь?"

show eve casual hair annoyed onlayer middle:
    ease 0.5 xpos 0.29 ypos 1.35 xanchor 0.5 yanchor 1.0
pause 0.5
show eve casual hair annoyed onlayer middle:
    ease 0.2 xpos 0.215 ypos 1.35 xanchor 0.5 yanchor 1.0
show yellow volcano hips pout onlayer middle:
    ease 0.2 xpos 0.42 ypos 1.45 xanchor 0.5 yanchor 1.0

Eve "Я вам не верю. Я вам не доверяю. И, что самое главное, я не хочу иметь с вами никаких дел."

"Я волочу ногами, пытаясь утащить Йеллоустон за собой. Её хват удивительно крепкий. С каждым шагом она сжимает мою руку всё сильнее, пока я не начинаю чувствовать, как её пальцы впиваются мне в кость."
show yellow volcano hips angry onlayer middle with dissolve

show yellow volcano hips angry onlayer middle:
    ease 0.5 xpos 0.4 ypos 1.45 xanchor 0.5 yanchor 1.0
pause 0.5
show yellow volcano hips angry onlayer middle:
    ease 0.2 xpos 0.51 ypos 1.45 xanchor 0.5 yanchor 1.0
show eve casual hair annoyed onlayer middle:
    ease 0.2 xpos 0.28 ypos 1.35 xanchor 0.5 yanchor 1.0

Yellowstone "Что если… я могу… доказать!"
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Не утруждайся. Просто забери свою картину и остальные вещи. Нам надо уйти на какое-то время."

"Она игнорирует Йосемити и продолжает тянуть меня за руку, упираясь пятками в пол. Её мычание становится совсем болезненным, когда она подлючает к делу вторую руку."
show yellow volcano hips seriouscry onlayer middle with dissolve

Yellowstone "Пожалуйста…! Всего лишь один шанс!"

"Наш паровозик проезжает мимо Зайон и щенка. Он виляет хвостом, глядя на Зайон, ожидая от неё поглаживаний."

show zion hands softcry at floating onlayer forward with dissolve:
 subpixel True
"Зайон смотрит на меня своими большими грустными глазами, которые, кажется, синеют по мере того как она печалится."

show coyote neutral onlayer forward with dissolve:
    xpos 0.8 ypos 0.67 xanchor 0.5 yanchor 1.0 zoom 0.9

"Щенок топчется по её платью. Его, обычно приподнятые, уши небрежно свисают."
show eve casual hair deepthink onlayer middle with dissolve

"Единственная струна моего сердца была задета. Опять этот пушистый скрипач."
show eve casual scratch annoyed onlayer middle with dissolve

"Я вздыхаю и останавливаюсь прежде, чем Йеллоустон успевает выдернуть мою руку из сустава."

"Я просто слишком сильно люблю этого щенка."
show eve casual scratch annoyed onlayer middle with dissolve

Eve "Тридцать секунд."
show yellow volcano hips excited onlayer middle with dissolve

"Йеллоустон ухмыляется. В её глазах вспыхивает огонёк."

"Она крепко хватает меня за руку и поворачивается к Йосемити."

Yellowstone "Вернёмся в тот же миг!"

stop ambient fadeout 3.0
$camera_move(5993, -3333, 600, 0, duration=3, warper='ease')
hide coyote onlayer forward
hide zion onlayer forward
hide yellow onlayer middle
hide eve onlayer middle
show yosemite chin curious onlayer middle
with dissolve

Yosemite "Вернётесь в тот же…"

window hide
play sound "sfx/big think.ogg"
pause 1.8

window show
show yosemite chin yelling onlayer middle with dissolve
Yosemite "Стой! Йеллоус--"
hide yosemite onlayer middle

hide cabininside_night1 onlayer background

show staticshockwasacoolshow onlayer forward:
    subpixel True xpos 0.64 ypos 0.84 xanchor 0.5 yanchor 1.0 zoom 3.52 rotate None
play sound "sfx/electricity of consciousness.ogg" loop
"В глазах потрескивают помехи. Земля уходит у меня из-под ног, и я падаю."


"Всё дальше и дальше. Падение в никуда."

"Безнадёжный ужас накатывает на меня удушающей волной."
hide tuo_night onlayer background
stop sound
hide staticshockwasacoolshow onlayer forward
"А затем -- тьма."
play ambient "ambience/howling wind.ogg" fadein 3.0
"Завывающий ветер треплет мои волосы."

"Я слышу шелест листьев, мимо меня проносятся порывы ветра."

"Мои ноги болтаются подо мной. Я смотрю вниз."
$ night_tint = True
"Лучше бы я этого не делала."

show tuo_night  onlayer background:
    subpixel True xpos 0.88 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.61 rotate None
    parallel:
        ypos 1.03
        ease 8.00 ypos 1.50
with fade
"Далеко внизу, на зазубренном склоне горы, виднеется густой лес. Между мной и землёй сотни футов воздуха."

Eve "Ааааа… Ааааааа…"

show yellow volcano peace wink onlayer middle:
 xpos 0.65 ypos 0.57 xanchor 0.5 yanchor 1.0 zoom 0.55 rotate -180.0
with dissolve
Yellowstone "Эй, как там, держишься?"

"Я поднимаю глаза и вижу, что Йеллоустон все ещё держит меня за руку. Лунный свет освещает её огромную ухмылку."
show eve casual hair disgusted onlayer middle:
    subpixel True xpos 0.81 ypos 0.83 xanchor 0.5 yanchor 1.0 zoom 0.57 rotate None
with dissolve
Eve "Где… Что… О Боже…"

show yellow volcano hips excited onlayer middle with dissolve
Yellowstone "Крутой вид, правда? Теперь-то мне веришь?"

"Я мотаю головой во все стороны, но вижу лишь далёкие силуэты холмов и гор. Отсюда все они похожи на муравейники."

"Крик наконец прорывается наружу. Громче и выше, чем я предполагала."
show eve casual hair furious onlayer middle with dissolve

Eve "СПАСИТЕ! СПАСИТЕ! СПАСИТЕ! СПАСИТЕ! СПАСИТЕ! ПОДНИМИ МЕНЯ!"
show yellow volcano hips concern onlayer middle with dissolve

Yellowstone "Воу, не дёргайся ты так. Иначе я не удержу тебя."
show eve casual hair scared onlayer middle with dissolve

Eve "Не отпускай… Не отпускай…"

"Моё тело раскачивается, как маятник. Я крепче сжимаю руку Йеллоустон."
show yellow volcano hips sad onlayer middle with dissolve

Yellowstone "Мм. Тебе не нравится?"
show eve casual hair furious onlayer middle with dissolve

Eve "НЕТ! А ТЕПЕРЬ ВЕРНИ МЕНЯ НАЗАД!"
show yellow volcano hips pout onlayer middle with dissolve

"Она хнычет, надувая щёки и губы."

Yellowstone "Боже мой. Не переживай ты так."
hide yellow onlayer middle
hide eve onlayer middle
hide tuo_night onlayer background
stop ambient
play sound "sfx/electricity of consciousness.ogg"
show staticshockwasacoolshow onlayer forward:
    subpixel True xpos 0.64 ypos 0.84 xanchor 0.5 yanchor 1.0 zoom 3.52 rotate None
"Меня тянет вверх, как будто засасывая в вакуум."
hide staticshockwasacoolshow onlayer forward
$camera_move(-546, -2053, 100, 0, duration=0)
$ layer_move("background", 2444)
show cabininside_night1 onlayer background
with vpunch
stop sound
"А затем я появляюсь в хижине."
$ night_tint = False
play ambient "ambience/fireplace.ogg"
"Тепло хижины берёт меня в объятия, а ноги превращаются в желе. Я падаю на колени и хватаю ртом воздух."

show yosemite chin neutral onlayer middle with dissolve:
 xpos 0.5 ypos 1.4 xanchor 0.5 yanchor 1.0
"Йосемити расхаживает по комнате и останавливается, как только видит нас."
show yosemite back yelling onlayer middle with dissolve
voice "scripte01s03_8c847d5f"
Yosemite "Ты! У тебя {i}пюре{/i} вместо мозгов? О чём ты вообще думала?"
show yellow volcano hips happy onlayer middle:
    subpixel True xpos 0.75 ypos 1.45 xanchor 0.5 yanchor 1.0 rotate None
show yosemite back yelling onlayer middle:
    xpos 0.3 ypos 1.4 xanchor 0.5 yanchor 1.0
with dissolve

"Йеллоустон выставляет руки, как крылья самолета, и кружится по комнате. Зайон хихикает, пока Йеллоустон кружит вокруг неё. Щенок нетерпеливо сидит возле них, виляя хвостом по полу взад=вперёд."
show yellow volcano hips happy onlayer middle:
    ease 1.0 xpos -0.3 ypos 1.45 xanchor 0.5 yanchor 1.0
    xpos 1.23
    ease 1.5 xpos -0.3 ypos 1.45 xanchor 0.5 yanchor 1.0
    repeat

show yellow volcano hips excited onlayer middle with dissolve
Yellowstone "Думала, что смогу убедить её, прикинь? МНе кажется, что мой план сработал хорошо!"
show yosemite back annoyed onlayer middle with dissolve

Yosemite "По-твоему, это похоже на {i}хорошо{/i}?"

hide yellow onlayer middle with dissolve
$camera_move(1159, -2053, 100, 0, duration=1, warper='ease')
show eve casual hair disgusted onlayer middle with dissolve:
        xpos 0.84 ypos 1.3 xanchor 0.5 yanchor 1.0
"Я пытаюсь согреться, мои зубы стучат. Меня трясет. Всё моё тело дрожит."

Eve "Я была здесь… А-а потом не была. А теперь я… Что за… Господи…"

$camera_move(-546, -2053, 100, 0, duration=1, warper='ease')
hide eve onlayer middle with dissolve
show yellow volcano hips happy onlayer middle with dissolve:
    subpixel True xpos 0.75 ypos 1.45 xanchor 0.5 yanchor 1.0 rotate None
"В самолёте заканчивается топливо, и Йеллоустон останавливается."
show yellow volcano hips concern onlayer middle with dissolve
voice "scripte01s03_b443e0aa"
Yellowstone "Нет… но я подумала, что мы могли наконец--"


Yosemite "{i}Послушай меня.{/i}"

$camera_move(1868, -2053, 500, 0, duration=1.5, warper='ease')
show yosemite back annoyed onlayer middle:
    ease 1.0 xpos 0.45 ypos 1.4 xanchor 0.5 yanchor 1.0
    ease 0.5 ypos 1.50
"Голос Йосемити резок и серьёзен. Зайон морщится. Йосемити садится на корточки и хватает Йеллоустон за плечи, сомтрит её прямо в глаза."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "А если бы что-то пошло не так? А если бы она потерялась или поранилась? Что бы ты тогда делала?"
show yosemite back nervous onlayer middle with dissolve

Yosemite "Или, что ещё хуже, если бы с тобой что-то случилось? Есть причина, по которой я пытаюсь нас спрятать. Ты знаешь, на что они способны. Что они могут сделать."

"Она что-то бормочет себе под нос."
show yosemite back bored onlayer middle with dissolve

Yosemite "Разумеется, что случилось, то случилось…"

"Жизнерадостность, сачащаяся из Йеллоустон, кажется, иссякла. Йосемити ослабляет хватку, и Йеллоустон отшатывается."
show yellow volcano hips sad onlayer middle with dissolve

Yellowstone "Кажется, я снова напортачила, а?"

"Йосемити в ответ глубоко вздыхает. Словно разочарованный родитель."

$camera_move(3618, -955, 500, 0, duration=1, warper='ease')
show zion arms softsmile onlayer middle with dissolve :
        xpos 0.95 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.81
"Зайон дёргает Йеллоустон за руку."

Zion "Я думаю, ты хорошо сработала, Йеллоустон."
show yellow volcano hips sad onlayer middle with dissolve

"Йеллоустон опускается к ней с печальной улыбкой, и жмёт её маленькую ручку."

$camera_move(-335, -1398, 300, 0, duration=1.5, warper='ease')
show yosemite back bored onlayer middle:
    ease 0.5 ypos 1.45
show yosemite back bored onlayer middle:
    ease 1.0 xpos 0.59 ypos 1.45 xanchor 0.5 yanchor 1.0
show zion arms softsmile onlayer middle:
    ease 1.5 xpos 0.74 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.81
show yellow volcano hips sad onlayer middle:
    ease 1.5 xpos 0.39 ypos 1.45 xanchor 0.5 yanchor 1.0

"Зайон протяжно зевает."
show yosemite back smallsmile onlayer middle with dissolve

Yosemite "Кажется, кто-то здесь сонный."

"Зайон протирает усталые глаза и кивает."
show zion hands nervous onlayer middle with dissolve

Zion "Угу…"

"Йосемити проводит пальцами по сказочным волосам Зайон."
show yosemite back neutral onlayer middle with dissolve
voice "scripte01s03_e9a50e6e"
Yosemite "Приготовь её ко сну, пока... я переговариваю с {i}человеком{/i}."

Yellowstone "Оки-доки…"

"Это самые печальные оки-доки, которые я слышала в своей жизни."
show yosemite back smallsmile onlayer middle with dissolve

Yosemite "Я скоро приду и уложу тебя. Может, даже расскажу тебе историю о ласточке, которая тебе так нравится."

Zion "История про ласточку? Я такую не помню…"
show yosemite back nervous onlayer middle with dissolve

show coyote onlayer middle:
    xpos 1.08 ypos 0.56 xanchor 0.5 yanchor 1.0

"На мгновение Йосемити застывает. Затем трясёт головой и усмехается."
show yosemite back smallsmile onlayer middle with dissolve
play music audio.memories
Yosemite "Нет, конечно… С чего бы ты её помнила?"

show yellow volcano hips sad onlayer middle:
    ease 2.0 xpos -0.15 ypos 1.45 xanchor 0.5 yanchor 1.0
show zion hands nervous onlayer middle:
    ease 2.2 xpos -0.15 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.81
show coyote onlayer middle:
    ease 5.7 xpos -0.15 ypos 0.56 xanchor 0.5 yanchor 1.0

"Йеллоустон берёт Зайон за руку и ведёт в ванну. Щенок бежит за ними."

show yosemite back neutral onlayer middle with dissolve

"Когда дверь закрывается, Йосемити поворачивается ко мне."

"Её осанка остаётся неизменной, идеально прямая. Она начинает идти в мою сторону."
$camera_move(2399, -1777, 300, 0, duration=1, warper='ease')
show yosemite back bored onlayer middle with dissolve
show yosemite back bored onlayer middle:
    ease 1.0 xpos 0.43 ypos 1.45 xanchor 0.5 yanchor 1.0
show eve casual hair crying onlayer middle with dissolve:
        xpos 0.88 ypos 1.4 xanchor 0.5 yanchor 1.0

Yosemite "Ты жива?"

"Она нависает надо мной, как гигантская секвойя. Я чувствую, как её шаги вибрируют подо мной, когда она подходит ближе."
show eve casual hair crying onlayer middle with dissolve

Eve "Просто оставь меня в покое!"

"Я заползаю в ближайший угол и опускаюсь на корточки, прикрываясь одной из упавших веток Зайон."
show yosemite back annoyed onlayer middle with dissolve

Yosemite "Расслабься. Я не собираюсь тебя съесть, или что ты там себе придумала."

"Я швыряю в неё веткой. Та проскальзывает мимо её плеча."
show eve casual hair disgusted onlayer middle with dissolve

Eve "Мне плевать! Просто уйди!"

"В горле встаёт комок. Я оглядываюсь на беспорядок, который тут образовался. Полосы воды на полу. Брошенное ружьё и открытые шкафы."

"Я осматриваю хижину. Маленькая и уютная. Но я знаю, для чего она нужна на самом деле."

"Это чистилище."

"Изолятор, призванный очистить меня от застоявшейся гордости."

"Это моё наказание. И если так, то это вовсе и не чистилище даже."

"Может это Ад?"

"Я опускаю голову на колени и держу её там."
show yosemite back nervous onlayer middle with dissolve
voice "scripte01s03_01ab16f4"
Yosemite "Эй. Ты в порядке? Мне жаль, что она выкинула этот трюк. Йеллоустон всегда причиняет проблемы, когда становится такой возбуждённой."

"Её голос смягчается. Звучит так, будто она обращается к Зайон, а не к ‘глупому смертному’."
show eve casual hair crying onlayer middle with dissolve

Eve "Просто уходи… пожалуйста."

"Я проглатываю эмоции, но мой голос всё ещё срывается."
voice "scripte01s03_88045929"
Eve "Я просто хочу, чтобы этот день закончился. Я устала."

"Она опускается передо мной."
show yosemite back smallsmile onlayer middle with dissolve

Yosemite "Что ж, тебе повезло, потому что я хочу предложить перемирие."

"Я поднимаю глаза и принюхиваюсь. Йосемити в нескольких дюймах от моего лица. Смотрит на меня с нежной улыбкой."
show eve casual hair disgusted onlayer middle with dissolve

Eve "Я слушаю."
show yosemite back neutral onlayer middle with dissolve

Yosemite "Если уж на то пошло, мы тоже вымотаны. Это был долгий день для нас. Как насчёт того, что мы дадим тебе поспать? А утром ты можешь позвонить своему начальнику и отправить нас восвояси."
show eve casual hair annoyed onlayer middle with dissolve
voice "scripte01s03_58b0742d"
Eve "Ты думаешь, я настолько тупа, чтобы клюнуть на это? Ты убьёшь меня во сне."
show yosemite back bored onlayer middle with dissolve

Yosemite "За время, необходимое, чтобы задушить тебя, я могу полкниги прочитать. Зачем тратить силы на подобное? Кроме того, разве ты не предпочла бы, чтобы трое ‘нарушителей’ не бродили по парку ночью?"

"Она не ошибается. Мне и о соседнем лагере надо подумать. Если они начнут создавать проблемы туристам, ситуация может выйти из-под контроля."
show yosemite back annoyed onlayer middle with dissolve
voice "scripte01s03_70e48900"
Yosemite "Ну давай, просто прими уже оливковую ветвь, я {i}пытаюсь{/i} играть по-хорошему."

show yosemite back bored onlayer middle with dissolve

"Я задумываюсь на пару секунд. О том, как могу проснуться, задыхаясь под подушкой. О том, что могу вообще не проснуться. И о том, что если проснусь, а их здесь уже не будет."

"Но сейчас темно и поздно. И мой мозг весь как в тумане."

"Поэтому я решаю согласиться."
show eve casual hair nervous onlayer middle with dissolve

Eve "Я не словлю пулю, пока буду спать, не так ли?"
show yosemite back smug onlayer middle with dissolve

Yosemite "Только неандертальцы используют ружья. Я думаю, ты - достаточное тому доказательство."

"Она оскорбляет, но при этом хихикает. Мне как-то не очень смешно."

"Я снова задумываюсь."
show eve casual hair annoyed onlayer middle with dissolve

Eve "И я сплю на кровати?"
show yosemite back bored onlayer middle with dissolve

"Её шутливая улыбка испаряется. Она вздыхает."
show yosemite chin bored onlayer middle with dissolve

Yosemite "Я {i}полагаю{/i}, здесь есть спальные мешки, которые мы можем использовать."
show yosemite chin neutral onlayer middle with dissolve

Yosemite "Ну, что скажешь? Мы договорились, или эта ночь будет длиться вечно?"

"Она протягивает руку, и, впервые, я замечаю её уши, торчащие из-под волос. Тонкие, с кончиками, заострёнными, как кинжалы."

"Я не знаю кто эти люди -- или даже что они такое. Но я {i}точно{/i} знаю, что мне нужно поспать."

"Я беру её тёплую руку, и она помогает мне встать на ноги."

show eve casual hair annoyed onlayer middle:
    ease 1.0 xpos 0.80
    ease 1.0 xpos 0.80 ypos 1.3 xanchor 0.5 yanchor 1.0
show eve casual scratch deepthink onlayer middle with dissolve
voice "scripte01s03_462a65b7"
Eve "Мы договорились, но утром вы первым же делом уберётесь отсюда."

stop ambient fadeout 3.0

window hide
hide yellow onlayer middle
hide eve onlayer middle
hide coyote onlayer middle
hide yosemite onlayer middle
hide zion onlayer middle
hide cabininside_night1 onlayer background
show black onlayer background
with dissolve
$ achievement.grant("Кабинная лихорадка")

stop music fadeout 0.3
pause 5.0

jump scripte01s04
