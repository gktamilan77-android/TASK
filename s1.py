import math
def calculate_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    percentage = (total / (len(marks)*100)) * 100

    return total, average, percentage

def calculate_grade(average):
    if average >= 90:
        return "A Grade"
    elif average >= 75:
        return "B Grade"
    elif average >= 50:
        return "C Grade"
    else:
        return "Fail"

def check_result(marks):
    for mark in marks:
        if mark <35:
            return "Fail"

    return "Pass"