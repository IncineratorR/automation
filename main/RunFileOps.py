'''
demo script for load folder,add file and save file
Run this
'''
import time
from automation.VSCodeScript import RunFileOps
from automation.ReadConfig import *

obj = RunFileOps(url,chrome_driver_path)
time.sleep(5)
obj.load_folder(file_path)
time.sleep(5)
obj.new_file()
time.sleep(5)
obj.write_file("print('hello')")
time.sleep(1)
obj.key_enter()
obj.write_file("print('hello one')")
time.sleep(5)
obj.save_file(file_name)
time.sleep(30)
