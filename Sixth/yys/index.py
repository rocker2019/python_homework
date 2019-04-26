import people
import scene

# 角色字典
roles = {
    '1': {'name': '大天狗', 'gender': '男', 'god': True, 'master': '黑晴明', 'aggressivity': 3136, 'life': 10026},
    '2': {'name': '雪女', 'gender': '女', 'god': True, 'master': '黑晴明', 'aggressivity': 3048, 'life': 10634},
    '3': {'name': '九命猫', 'gender': '女', 'god': False, 'master': '黑晴明', 'aggressivity': 2968, 'life': 9905},
}

# 场景字典
scene_dict = {
    '4': {'name': '阴界裂缝', 'cost_aggressivity': 220, 'cost_life': 2000},
    '5': {'name': '鬼王封印', 'cost_aggressivity': 3100, 'cost_life': 3000}
}

print('----阴阳师人物介绍----------------------')
for index, info in roles.items():
    print(f'*****{index}：{info["name"]}, [性别：{info["gender"]},'
          f'式神：{info["god"]}, 主人：{info["master"]}, '
          f'攻击力：{info["aggressivity"]}, 生命值：{info["life"]}]')

flag = True

while flag:

    role_id = input('请选择角色：')
    if role_id not in roles.keys():
        print('请选择正确的角色')
        continue

    #实例化角色，打印选中角色详细信息
    user = people.People(roles[role_id])
    user.get_info()

    print('-----您将进入游戏场景选择-----------------------')
    for scene_id, scene_info in scene_dict.items():
        print(f'*****{scene_id}：{scene_info}')
    chose_scene = input('请选择场景：')
    if chose_scene not in scene_dict.keys():
        print('请选择正确的场景')
        continue

    # 实例化场景
    game_scene = scene.Scene(user)

    if chose_scene == '4':
        status = game_scene.yin_jie_lie_feng()
    else:
        status = game_scene.gui_wang_feng_yin()

    # 判断是否成功过关
    if status is True:
        print(f'成功通过{scene_dict[chose_scene]["name"]}')
        print('目前攻击力：{}，生命值：{}'.format(user.get_aggressivity(), user.get_life()))
        cont = input('继续游戏（Y/N）：')
        if cont == 'N':
            break
    else:
        print('生命或攻击力不够，失败')
        flag = False
        break
