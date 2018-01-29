#coding=utf-8

import requests,random
from resource.resource import *
import logging,time,sys


class Login(object):
    def __init__(self,username,pwd):
        self.username = username
        self.pwd = pwd

    def login(self):
        s=[]
