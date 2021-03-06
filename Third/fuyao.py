# -*- coding:utf8 -*-

# 1 构建一个字典，包括演员名字，饰演角色，配音演员
Fuyao_Actor_Profile = {
    '杨幂': {'姓名': '杨幂', '角色': '扶摇', '配音': '王潇倩'},
    '阮经天': {'姓名': '阮经天', '角色': '长孙无忌', '配音': '马正阳'},
    '刘奕君': {'姓名': '刘奕君', '角色': '齐震', '配音': '刘奕君'},
    '高伟光': {'姓名': '高伟光', '角色': '战北野', '配音': '赵成晨'},
    '王劲松': {'姓名': '王劲松', '角色': '长孙炯', '配音': '王劲松'},
    '黄宥明': {'姓名': '黄宥明', '角色': '燕惊尘', '配音': '文森'},
    '高瀚宇': {'姓名': '高瀚宇', '角色': '江枫', '配音': '袁聪宇'},
    '顾又铭': {'姓名': '顾又铭', '角色': '战北恒', '配音': '林强'},
    '秦焰': {'姓名': '秦焰', '角色': '周叔', '配音': '宣晓明'},
    '蒋龙': {'姓名': '蒋龙', '角色': '小七', '配音': '苏尚卿'},
}

# 2 打印出杨幂扮演的角色
print('杨幂扮演的角色：{}' .format(Fuyao_Actor_Profile['杨幂']['角色']))

# 3 创建一个备份字典
Copy_Fuyao = Fuyao_Actor_Profile.copy()

# 4 删除演员阮经天
actor = Fuyao_Actor_Profile.pop('阮经天')


# 5 更替为陈晓
Fuyao_Actor_Profile['陈晓'] = Copy_Fuyao['阮经天']
Fuyao_Actor_Profile['陈晓']['姓名'] = '陈晓'

# 6 增加新的角色
newActors = {
    '张雅钦': {'姓名': '张雅钦', '角色': '雅兰珠', '配音': '吟良犬'},
    '王鹤润': {'姓名': '王鹤润', '角色': '凤净梵', '配音': '蔡娜'},
    '周骊威': {'姓名': '周骊威', '角色': '时岚', '配音': '张晗'},
    '魏晖倪': {'姓名': '魏晖倪', '角色': '简雪', '配音': '曹一茜'},
}
Fuyao_Actor_Profile.update(newActors)

# 7 打印阮经天信息
print('阮经天字典信息：{}'.format(actor))

# 8 角色总数
print('一共有{}个角色'.format(len(Fuyao_Actor_Profile)))

# 9 10 创建一个新的字典表并存储信息
New_Profile_Info = {
    '扶摇': {
        'name': '杨幂',
        'be_liked_role': ['长孙无极', '站北野', '小七'],
        'visited_country': ['太渊', '天权', '天煞', '璇玑']
    }
}

