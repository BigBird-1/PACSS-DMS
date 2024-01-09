import os
import configparser
import getpathInfo  # 引入我们自己的写的获取路径的类

path = getpathInfo.get_path()  # 调用实例化，还记得这个类返回的路径为 F:\PACSS-DMS
config_path = os.path.join(path,
                           'config.ini')  # 这句话是在path路径下再加一级，最后变成 F:\PACSS-DMS\config.ini
config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')


class ReadConfig(object):
    @staticmethod
    def get_http(name):
        value = config.get('HTTP', name)
        return value

    @staticmethod
    def get_email(name):
        value = config.get('EMAIL', name)
        return value

    @staticmethod
    def get_mysql(name):  # 写好，留以后备用。但是因为我们没有对数据库的操作，所以这个可以屏蔽掉
        value = config.get('DATABASE', name)
        return value


read_config = ReadConfig()

if __name__ == '__main__':  # 测试一下，我们读取配置文件的方法是否可用
    print('HTTP中的baseurl值为：', ReadConfig().get_http('base_url')[:-11:])


