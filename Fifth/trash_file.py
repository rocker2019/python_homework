import os


def trash_file(file_path, file_name):
    """
    删除指定目录下的指定文件
    :param file_path:
    :param file_name:
    :return: 如果目录不存在直接返回
    """
    # 判断文件目录是否存在
    if not os.path.exists(file_path):
        print('file path {} is not exist'.format(file_path))
        return

    # 列出查询目录下的所有文件，查询的文件位于其中则删除，否则提示文件不存在
    files = os.listdir(file_path)
    if file_name in files:
        os.remove(file_path + '/' + file_name)
        print('file {} removed success'.format(file_name))
    else:
        print('file {} is not exist'.format(file_name))


filePath = '../Xdata1'
filename = 'rocker.jpg'
trash_file(filePath, filename)

# trash_file('../Xdata', 'rocker.png')
# trash_file('../Xdata', 'rocker.jpg')
