# -*- coding:utf8 -*-
# 初始化指令字典及通讯录
instructions = {
    '1': '查询联系人资料',
    '2': '插入新的联系人',
    '3': '更新联系人资料',
    '4': '删除已有联系人',
    '5': '退出通讯录程序',
}
contactList = {}

# 欢迎界面
print('|---欢迎使用通讯录程序---|')
for instruction, instructionName in instructions.items():
    print(f'|---{instruction}、{instructionName}---|')

# 设置标识 是否退出
flag = True
while flag:
    instructionId = input('请输入指令代码：')

    if instructionId not in instructions.keys():
        print('warning: 请输入合法指令')

    if instructionId == '1':
        contactName = input('请输入联系人姓名：')
        if contactName in contactList.keys():
            print(contactName + ': ' + contactList[contactName])
        else:
            print('该联系人不存在')

    if instructionId == '2':
        contactName = input('请输入联系人姓名：')
        if contactName in contactList.keys():
            print('该联系人已存在，修改请转至指令3')
        else:
            contactPhone = input('请输入联系人电话：')
            contactList[contactName] = contactPhone
            print('联系人添加成功')

    if instructionId == '3':
        contactName = input('请输入联系人姓名：')
        if contactName in contactList.keys():
            contactPhone = input('请输入联系人电话：')
            contactList[contactName] = contactPhone
            print('联系人资料更新成功')
        else:
            print('该联系人不存在')

    if instructionId == '4':
        contactName = input('请输入联系人姓名：')
        if contactName in contactList.keys():
            del contactList[contactName]
            print('联系人{}已删除'.format(contactName))
        else:
            print('该联系人不存在')

    if instructionId == '5':
        flag = False
        print('|---感谢使用通讯录系统---|')
