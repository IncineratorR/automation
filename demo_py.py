'''
demo script for run program via terminal
Run this
'''
import time
from automation.VSCodeScript import RunPythonProgram
from automation.ReadConfig import *

obj = RunPythonProgram(url,profile_path,profile_name,chrome_driver_path)
time.sleep(10)

obj.remote_write_line("# Define a function to calculate the average of a list of numbers")
time.sleep(2)
    
obj.remote_write_line("def calculate_average(numbers):")
time.sleep(2)
    
obj.remote_write_line("# Calculate the sum of the numbers using the built-in sum function")
time.sleep(2)
    
obj.remote_write_line("total = sum(numbers)")
time.sleep(2)
    
obj.remote_write_line("# Calculate the average by dividing the total by the length of the list")
time.sleep(2)
    
obj.remote_write_line("average = total / len(numbers)")
time.sleep(2)
    
obj.remote_write_line("# Return the calculated average")
time.sleep(2)
    
obj.remote_write_line("return average")
time.sleep(2)
    
obj.key_enter()
time.sleep(2)

obj.key_backspace()
obj.remote_write_line("# Define a function to find the maximum value in a list of numbers")
time.sleep(2)
    
obj.remote_write_line("def find_maximum(numbers):")
time.sleep(2)
    
obj.remote_write_line("# Use the built-in max function to find the maximum value in the list")
time.sleep(2)
    
obj.remote_write_line("maximum = max(numbers)")
time.sleep(2)
    
obj.remote_write_line("# Return the maximum value")
time.sleep(2)
    
obj.remote_write_line("return maximum")
time.sleep(2)
    
obj.key_enter(" ")
time.sleep(2)

obj.key_backspace()
obj.remote_write_line("# Define the main function that contains the core logic of the program")
time.sleep(2)
    
obj.remote_write_line("def main():")
time.sleep(2)
    
obj.remote_write_line("# Define an array of numbers")
time.sleep(2)
    
obj.remote_write_line("numbers = [5, 10, 15, 20, 25]")
time.sleep(2)
    
obj.remote_write_line("# Call the calculate_average function and store the result in a variable")
time.sleep(2)
    
obj.remote_write_line("average_result = calculate_average(numbers)")
time.sleep(2)
    
obj.remote_write_line("# Call the find_maximum function and store the result in a variable")
time.sleep(2)
    
obj.remote_write_line("maximum_result = find_maximum(numbers)")
time.sleep(2)
    
obj.remote_write_line("# Print the original array of numbers")
time.sleep(2)
    
obj.remote_write_line("print(\"Array:\", numbers)")
time.sleep(2)
    
obj.remote_write_line("# Print the calculated average")
time.sleep(2)
    
obj.remote_write_line("print(\"Average:\", average_result)")
time.sleep(2)
    
obj.remote_write_line("# Print the maximum value in the array")
time.sleep(2)
    
obj.remote_write_line("print(\"Maximum:\", maximum_result)")
time.sleep(2)
    
obj.key_enter()
time.sleep(2)

obj.key_backspace()
obj.remote_write_line("# Define the main function that contains the core logic of the program")
time.sleep(2)
    
obj.remote_write_line("main()")

time.sleep(30)