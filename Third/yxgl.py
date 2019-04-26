# -*- coding:utf8 -*- 

# 1. 列出所有人列表，并用3中方式打印信息
yanXiPalace = '延禧宫'
yuGarden = '御花园'
partyPlace = yanXiPalace
invitees = ['太后', '皇后', '纯妃', '小嘉嫔', '舒妃', '皇上']
print('春节将至，请大家过来%s相聚，受邀名单：%s' % (partyPlace, invitees))
print('春节将至，请大家过来{}相聚，受邀名单：{}'.format(partyPlace, invitees))
print(f'春节将至，请大家过来{partyPlace}相聚，受邀名单：{invitees}')

# 2. 小嘉嫔拒绝邀请，并打印不能参加的人
refusedPerson = invitees.pop(3)
print('{}拒绝参加'.format(refusedPerson))

# 3. 尔晴参加，重新修改列表，打印出邀请名单
invitees.append('尔晴')
print(invitees)

# 4. 地点从延禧宫变成御花园
partyPlace = yuGarden

# 5. insert方法将`哥哥`放在邀请名单的开头；append方法将`傅恒`放在名单最后
invitees.insert(0, '哥哥')
invitees.append('傅恒')

# 5.1 重新打印所有人名单，并用len方法打印邀请人数，并复制一个新的列表作为备份
print(invitees)
print('受邀人数：{}'.format(len(invitees)))
inviteesBak = invitees.copy()

# 6. 打印前、后三个人名，并颠倒顺序
print('前3个人：{}'.format(invitees[:3]))
print('后3个人：{}'.format(invitees[-3:]))
invitees.reverse()
print(invitees)

# 7. 只请皇后和尔晴，告知依然在受邀之列
# 8. 删除多于人员，并告知“特别遗憾不能请大家吃饭”
excess = list()
excess.append(invitees.pop(0))
excess.append(invitees.pop(1))
excess.append(invitees.pop(1))
excess.append(invitees.pop(1))
excess.append(invitees.pop(2))
excess.append(invitees.pop(2))

print('依然在邀请之列：{}'.format(invitees))
print('特别遗憾不能邀请大家吃饭：{}'.format(excess))

# 9. del删除名单
del invitees


