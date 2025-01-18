# 游戏的脚本可置于此文件中。

init python:
    def voice(event, **kwargs):
        import time
        if event == "show":
            renpy.sound.play("graze.wav",loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define rm = Character("博丽灵梦", callback=voice)
define mrs = Character("雾雨魔理沙", callback=voice)
define kjsj = Character("鬼人正邪", callback=voice)
define pov = Character("[povname]")

# 游戏在此开始。

image splash = "splash.png"

label splashscreen:
    scene black
    with Pause(1)

    play voice "splash-baka.mp3"

    show splash with dissolve
    with Pause(2)

    hide splash with dissolve

    return

label start:

    stop music fadeout 1.0

    "这是一个东方Project的二次创作同人游戏。"

    "与原作设定有所出入"

    "请勿将本作任何设定、剧情带入原作。"

    "エンジョイてぇゲームです(笑)"

    jump Intro

label Intro:

    python:
        povname = renpy.input("你的名字是？", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Player"

    scene bg hakurei_shrine night

    "幻想乡的夜晚，一切都那么安静。"

    scene bg kishinjou night with fade

    show kjsj nm p7 at right with dissolve

    kjsj "哎哟卧槽"
    kjsj "日本人咋这么好"
    kjsj "说话为什么都不带有攻击性呢"

    hide kjsj nm p7 with dissolve
    scene black
    "少女祈祷中"
    "几分钟后"

    scene bg kishinjou night with dissolve
    show kjsj nm p8 at right

    kjsj "哦错了"

    show kjsj idle p8 at right
    image TakeThat = "TakeThat.png"

    play audio "kurae.wav"
    
    transform TakeThat_size :
        zoom 0.1 xalign 0.7
    show TakeThat at TakeThat_size
    camera:
        linear 0.3 zoom 5.0 xalign 0.8 yalign 0

    kjsj "把她们的素质颠倒不就坏了吗"
    hide TakeThat
    camera:
        linear 0.3 zoom 1.0 xalign 0.5
    "（真是个天才的说）"

    hide kjsj idle p8 with dissolve

    scene black
    
    show text "此时，在雾雨邸：" at truecenter with dissolve

    jump intro_mrs

label intro_mrs:

    scene bg computers night with dissolve