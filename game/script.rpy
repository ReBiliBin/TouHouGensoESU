# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define rm = Character("博丽灵梦")
define mrs = Character("雾雨魔理沙")
define kjsj = Character("鬼人正邪")

# 游戏在此开始。

label start:

    stop music fadeout 1.0

    "这是一个东方Project的二次创作同人游戏。"

    "与原作设定有所出入"

    "请勿将本作任何设定、剧情带入原作。"

    "エンジョイてぇゲームです(笑)"

    jump Intro

label Intro:

    scene bg hakurei_shrine night

    "幻想乡的夜晚，一切都那么安静。"
    with dissolve
    scene bg kishinjou night
    show kjsj nm p13 at right

    kjsj "哎哟卧槽"
    kjsj "日本人咋这么好"
    kjsj "说话为什么都不带有攻击性呢"

    show kjsj nm p7 at right

    "少女祈祷中"
    "几分钟后"

    show kjsj nm p8 at right 

    kjsj "哦错了"
    show kjsj idle p0 at right

    kjsj "把她们的素质颠倒不就坏了吗"
    kjsj "（真是个天才的说）"
    hide kjsj idle p0

    "此时正在休息的众人并不知道，由天邪鬼发动的另一场异变开始了。"

    return