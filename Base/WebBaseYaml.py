# -*- coding:utf-8 -*-

import yaml
from yaml.scanner import ScannerError
import os


def getYaml(path):
    try:
        with open(path, encoding='utf-8') as f:
            x = yaml.load(f, Loader=yaml.FullLoader)
            return [True, x]
    except FileNotFoundError:
        print("==用例文件不存在==")
        app = {'check': [{'element_info': '', 'operate_type': 'get_value', 'find_type': 'ids', 'info': '用例文件不存在'}],
               'testinfo': [{'title': '', 'id': '', 'info': ''}],
               'testcase': [{'element_info': '', 'info': '', 'operate_type': '', 'find_type': ''},
                            {'element_info': '', 'msg': "", 'operate_type': '', 'find_type': '', 'info': ''},
                            {'element_info': '', 'msg': '', 'operate_type': '', 'find_type': '', 'info': ''},
                            {'element_info': '', 'info': '', 'operate_type': '', 'find_type': ''}]}

        return [False, app]
    except yaml.scanner.ScannerError:
        app = {'check': [{'element_info': '', 'operate_type': 'get_value', 'find_type': 'ids', 'info': '用例文件格式错误'}],
               'testinfo': [{'title': '', 'id': '', 'info': ''}],
               'testcase': [{'element_info': '', 'info': '', 'operate_type': '', 'find_type': ''},
                            {'element_info': '', 'msg': "", 'operate_type': '', 'find_type': '', 'info': ''},
                            {'element_info': '', 'msg': '', 'operate_type': '', 'find_type': '', 'info': ''},
                            {'element_info': '', 'info': '', 'operate_type': '', 'find_type': ''}]}
        print("==用例格式错误==")
        return [False, app]


if __name__ == '__main__':
    PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
    )
    t = getYaml(PATH("../Yamls/Home/Login.yaml"))
    print(t)
