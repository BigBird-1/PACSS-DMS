from readConfig import read_config


class GeturlParams(object):  # 定义一个方法，将从配置文件中读取的进行拼接
    @staticmethod
    def get_url():
        base_url = read_config.get_http('base_url')
        # logger.info('new_url'+new_url)
        return base_url


if __name__ == '__main__':  # 验证拼接后的正确性
    print(GeturlParams().get_url())
