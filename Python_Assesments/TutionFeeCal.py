Student_name = input("Enter the student's name: ")
Student_grade_level = int(input("Enter the student's grade level(1-12): "))
Base_tuition_fee = 30000 # Base tuition fee in Rs.
Discount_percentage = 0
Academic_Topper_status = input("Is the student an academic topper? (yes/no): ").strip().lower()

if Student_grade_level <= 12 and Student_grade_level >= 1:
    if Student_grade_level <= 12 and Student_grade_level >= 9:
        if Academic_Topper_status == 'yes':
            Discount_percentage = 20
            match Student_grade_level:
                case 10:
                    Discount_percentage = Discount_percentage + 3
                case 12:
                    Discount_percentage = Discount_percentage + 5         
        else:
            Discount_percentage = 10
    elif Student_grade_level <= 8 and Student_grade_level >= 6:
        Discount_percentage = 5                                                     
    Discount_percentage = Discount_percentage / 100
    Tuition_fee = Base_tuition_fee * (1 - Discount_percentage)
    print(f"Student Name: {Student_name}")
    print(f"Grade Level: {Student_grade_level}")    
    print(f"Academic Topper status: {Academic_Topper_status}")
    print(f"Base Tuition Fee: Rs.{Base_tuition_fee}")
    print(f"Discount Percentage: {Discount_percentage * 100}%")
    print(f"Discounted Tuition Fee: Rs.{Base_tuition_fee-Tuition_fee:.2f}")
    print(f"Final Tuition Fee: Rs.{Tuition_fee:.2f}")
else:
    print("Invalid grade level. Please enter a number between 1 and 12.")