numbers = [10, 12, 11, 13, 100, 12, 11]
print(numbers)

threshold = 50

for number in numbers:
    if number > threshold:
        print("Outlier found:", number)
