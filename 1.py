import re

def extract_digits(input_string):
    spelled_digits = re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', input_string)
    digit_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    # Return either the spelled integer, or the integer itself as the get() default value
    actual_digits = [digit_mapping.get(digit, digit) for digit in spelled_digits]
    return actual_digits[0],actual_digits[-1]
 
def replaceStringsWithNumbers(line):
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")
    return line

with open('input.txt') as f:
    ans = 0
    for line in f:
        line = replaceStringsWithNumbers(line)
        first_digit, last_digit = extract_digits(line)
        ans += int(first_digit + last_digit)
print(ans)