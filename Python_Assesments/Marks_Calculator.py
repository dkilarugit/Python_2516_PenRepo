Student_ID = input("Enter Student ID: ")
Student_Name = input("Enter Student Name: ")
Student_Age = input("Enter Student Age: ")
Quiz_Score = int(input("Enter Quiz Score: "))
Assignment_Score = int(input("Enter Assignment Score: "))
Exam_Score = int(input("Enter Exam Score: "))
Average_Score = (Quiz_Score + Assignment_Score + Exam_Score)/ 3
print(f"Total Score: {Quiz_Score + Assignment_Score + Exam_Score}")
print(f"Average Score: {(Quiz_Score + Assignment_Score + Exam_Score) / 3:.2f}")
if Average_Score >= 75:
    print("Status: Pass")
else:
    print("Status: Fail")
print("\nStudent Details: ")
print(f"ID: {Student_ID}")
print(f"Name: {Student_Name}")
print(f"Age: {Student_Age}")
print(f"Quiz Score: {Quiz_Score}")
print(f"Assignment Score: {Assignment_Score}")
print(f"Exam Score: {Exam_Score}")
print(f"Average Score: {Average_Score:.2f}")
    
