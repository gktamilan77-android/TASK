import datetime

def display_report(name,marks,total,average,percentage,grade,result):
    print("\n===== STUDENT REPORT =====")

    print("Student Name : ",name)
    print("Student Marks : ",marks)
    print("Total Marks : ",total)
    print("Average : ",round(average,2))
    print("Percentage : ",round(percentage,2),"%")
    print("Grade : ",grade)
    print("Result : ",result)

    today = datetime.datetime.now()

    print("date : ",today.strftime("%d-%m-%Y %H:%M %p"))

    if result == "Pass":
        print("Congratulations! You've passed the test!")

    else:
        print("Sorry :Better luck next time!")
