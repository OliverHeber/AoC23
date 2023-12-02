import re

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
        nums = []
        for ch in line:
            if ch.isdigit():
                nums.append(ch)
        ans += int(nums[0] + nums[-1])
print(ans)