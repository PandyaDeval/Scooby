# encoding: utf-8
from __future__ import print_function
from os import path
from pywinauto import Desktop, Application

def start_app(app_name):
    try:
        app=Application().start(app_name)
        apps.append(app)
    
    except:
        with open("paths.txt") as f:
            for line in f:
                try:
                    app_path = line[:-1] + app_name
                    #print(app_path)
                    app=Application(backend='win32').start(app_path + " --renderer-force-accessibility")
                    break
                except:
                    continue

obj="zeta"
apps=[]
start_app(obj)



