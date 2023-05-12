#!/usr/bin python
# _*_coding:utf-8_*_

"""
@Time :    2023/4/5 16:39
@Author:  tiansong
@File: Install.py
@Software: PyCharm
1.创建初始化配置
2.创建安装目录
3.安装依赖软件
4.安装python及依赖包
"""
import os
import configparser
import subprocess
import time


class AppInstall(object):

    def __init__(self ):

        self.dir_name_list = ["data","index","bin","etc","searchengine","front"]
        # print(self.dir_name_list)


    def create_init_dir(self):
        install_path = os.path.join(".", "tisonsearch")
        subprocess.run("mkdir {dir}".format(dir=install_path), shell=True)

        #create file dirs
        sec_dir_dict = {}
        for name in self.dir_name_list: sec_dir_dict[name] = self.create_dir(install_path,name)
        return sec_dir_dict

    def create_install_config(self,sec_dir_dict):
        pwd = os.getcwd()
        time_stamp = time.time()
        time_local = time.localtime(time_stamp)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        conf = configparser.ConfigParser()  # 类的实例化
        # print(sec_dir_dict)
        config_path = os.path.join("./tisonsearch/etc", 'tison_config.ini')
        # print(config_path)
        conf.add_section('change_state')
        conf.set('change_state',"change_time",dt)
        conf.add_section('search_dir')  # 添加一个新的section
        conf.set('search_dir', 'searth_path_list', '["~/Desktop","~/Library/Containers"]')
        conf.set('search_dir', 'jpg_path_list', '["~/Desktop"]')
        conf.add_section('txt_store_dir')  # 添加一个新的section

        conf.add_section('install_dir')  # 添加一个新的section
        conf.set('install_dir', 'app_path', "./tisonsearch")
        conf.set('install_dir', 'file_dir_list',str(self.dir_name_list))

        conf.set('txt_store_dir', 'new_add_file_save_path', os.path.join(sec_dir_dict["index"],'ftp_new_file_list.txt'))  # 往配置文件写入数据
        conf.set('txt_store_dir', 'file_save_path', os.path.join(sec_dir_dict["index"],'file_type_file_list.txt'))  # 往配置文件写入数据

        conf.add_section('search_type')  # 添加一个新的section
        conf.set('search_type', 'light', '["ppt"]')
        conf.set('search_type', 'professional', '["ppt","picture","pdf"]')
        conf.set('search_type', 'ultimate', '["ppt","picture","pdf","word","excel","mindmap"]')
        conf.add_section('file_type_dict')  # 添加一个新的section
        conf.set('file_type_dict', 'ppt', '["ppt","pptx"]')
        conf.set('file_type_dict', 'picture', '["jpg","jpeg","png"]')
        conf.set('file_type_dict', 'pdf', '["pdf"]')
        conf.set('file_type_dict', 'word', '["docx","doc"]')
        conf.set('file_type_dict', 'excel', '["xlsx","csv","xls"]')
        conf.set('file_type_dict', 'mindmap', '["xmind","mmp"]')
        conf.add_section('endpoint')  # 添加一个新的section
        conf.set("endpoint","httpserver",'http://127.0.0.1:8000')
        conf.set("endpoint","tisondataserver",'http://127.0.0.1:8000'+pwd)
        conf.set("endpoint","meilisearchserver",'http://localhost:7700')
        conf.set("endpoint","interserver",'http://127.0.0.1:8099')
        conf.set("endpoint", "index", 'presentation')
        conf.add_section('database')  # 添加一个新的section
        conf.set("database","sqlite",'sqlite:///tison_search.db')
        conf.set("database", "meili_master_key", 'bf02d93e-ed8f-11ed-84c8-3e848e7eb0ba')
        conf.write(open(config_path, 'w'))
        # subprocess.run("cp {dir} {etc_dir}".format(dir=config_path,etc_dir = sec_dir_dict["etc"]), shell=True)
        # print(conf)

    def create_dir(self,root_dir,dir_name):
        sub_dir = os.path.join(root_dir,dir_name)
        # print(sub_dir)

        # os.makedirs(sub_dir, exist_ok=True)
        subprocess.run("mkdir {dir}".format(dir = sub_dir),shell=True)
        return sub_dir


if __name__ =="__main__":
    appint = AppInstall()
    print(appint.dir_name_list)
    dir_dict = appint.create_init_dir()
    appint.create_install_config(dir_dict)


