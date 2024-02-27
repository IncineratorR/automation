def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average
def find_maximum(numbers):
    maximum = max(numbers)
    return maximum

def main():
    # Define an array of numbers
    numbers = [5, 10, 15, 20, 25]
    # Call functions to perform operations on the array
    average_result = calculate_average(numbers)
    maximum_result = find_maximum(numbers)
    # Print the results
    print("Array:", numbers)
    print("Average:", average_result)
    print("Maximum:", maximum_result)