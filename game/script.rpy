# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Незнакомка', color="#c8ffc8")
image bg room = im.Scale("images/backgrounds/terasroom.jpg", 1920, 1080)
image Tera st = im.Scale("images/characters/Tera.jpg", 500, 600)

define name = ''

define gg_gender = ''
define partner_gender = ''

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room
    show Tera st at Position(xpos=0.3, ypos=1.0)

    

    e "Привет"

    e "Мы не знакомы..."

    e "...Но скоро это изменится..."

    e "Давай начнём"

    e ""

    e "Как тебя зовут?"

    $ name = renpy.input('Меня зовут: ')

    e 'Привет [name]! Очень приятно познакомится.. Расскажи ещё немного о себе?'

    e '[name], выбери пол'

    e 'Свой и партнёра'

    menu:
        'Я мальчик':
            e 'Замечательно! а теперь пол партнёра...?'
            $ gg_gender = 'm'
            
        'Я девочка':
            e 'Замечательно! а теперь пол партнёра...?'
            $ gg_gender = 'f'
            
    menu:
        'Мой партнёр девочка...':
            e 'Поняла тебя'
            $ partner_gender = 'f'
            
                    
        'Мой партнёр мальчик...':
            e 'Поняла тебя'
            $ partner_gender = 'm'

    if gg_gender == 'm' and partner_gender == 'f':
        "Всё хорошо, поняла тебя, давай начинать!"
    else:
        "Ох... Прости, но данный контент не доступен в этой версии..."
        "Давай пока попробуем сделать так, ты мальчик, а партнёр девочка, хорошо?"
        "Ответ мне не нужен, я сама решу как должно быть Хех"
        $ gg_gender = 'm'
        $ partner_gender = 'f'

    e 'Кстати, я Тера'
    $ e = Character('Тера', color="#00ff00")        
    e 'Давай начали!'        
    e 'На данный момент параметры таковы: 
    Имя: [name]
    Пол гг: [gg_gender]
    Пол партнёра: [partner_gender] (...отладка...)'

    jump prologue