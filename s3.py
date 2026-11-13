import s1
import s2

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1.calculate Student Marks")
    print("2.Exit")

    choice = int(input("Enter your choice:"))
    if choice == 1:
        name = input("Enter Student Name:")
        marks=[]

        for i in range(1,6):
            mark=int(input("Enter Subject"+str(i)+"Mark :"))

            if mark>=0 and mark<=100:
                marks.append(mark)

            else:
                print("Invalid Mark")
                break

        if len(marks)==5:

            total, average, percentage, =s1.calculate_marks(marks)

            grade= s1.calculate_grade(average)

            result = s1.check_result(marks)

            s2.display_report(name,marks,total,average,percentage,grade,result)

    elif choice == 2:
        print("Thank You")
        break

    else:
        print("Invalid Choice")


