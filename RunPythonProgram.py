'''
demo script for run program via terminal
Run this
'''
import time
from VSCodeScript import RunPythonProgram
from ReadConfig import *

obj = RunPythonProgram(url,profile_path,profile_name,chrome_driver_path)
obj.remote_connect_folder(folder_name)
time.sleep(60)
obj.remote_new_file()
time.sleep(5)

obj.remote_write_line("# Let's create a Python recipe for a simple program.")
time.sleep(4)

obj.remote_write_line("#Creating a tuple of dishes on the wedding thali")
time.sleep(4)
    
obj.remote_write_line("wedding_thali = ('biryani', 'dal', 'paneer curry', 'naan', 'raita')")
time.sleep(4)
    
obj.remote_write_line("# Displaying the contents of the thali.")
time.sleep(4)
    
obj.remote_write_line("print('Contents of the wedding thali:', wedding_thali)")
time.sleep(4)
    
obj.remote_write_line("#Accessing elements in the tuple using indexing")
time.sleep(4)
    
obj.remote_write_line("print('The main course includes:', wedding_thali[0])")
time.sleep(4)
   
obj.remote_write_line("print('Side dish:', wedding_thali[2])")
time.sleep(4)
    
obj.remote_write_line("#Trying to modify the tuple (this will result in an error)")
time.sleep(4)

obj.remote_write_line("#Uncommenting the line below will raise a TypeError")
time.sleep(4)

obj.remote_write_line("# wedding_thali[1] = 'butter chicken'")
time.sleep(4)

obj.remote_write_line("# Adding a new dish to the tuple (this will result in an error)")
time.sleep(4)
    
obj.remote_write_line("# Uncommenting the line below will raise an AttributeError")
time.sleep(4)

obj.remote_write_line("# wedding_thali.append('gulab jamun')")
time.sleep(4)

obj.remote_write_line("# The tuple remains unchanged, just like your thali at the wedding!")
time.sleep(4)

obj.remote_write_line("print('The untouched wedding thali:', wedding_thali)")
time.sleep(4)

        
    

time.sleep(5)

obj.remote_save_file(folder_name,file_name)
time.sleep(5)
obj.remote_open_terminal()
time.sleep(5)
obj.remote_write_terminal(command,file_name)
time.sleep(10)