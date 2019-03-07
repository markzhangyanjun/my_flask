import os


class mytest(object):
    def __init__(self):

        self.name = 'zyj'

    def get_name(self):
        pass


rv = os.environ.get('PATH')
print (rv)


#coding:utf-8

from dotenv import find_dotenv,load_dotenv
import os
load_dotenv(find_dotenv())

res = os.environ.get('URL')
print(res)




