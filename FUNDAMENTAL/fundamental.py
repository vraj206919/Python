
try:
    marks_str = input("Enter student marks, separated by commas (e.g., 85, 92, 78): ")
    marks = [int(mark) for mark in marks_str.split(',')]
except ValueError:
    print("Invalid input. Please enter a list of numbers separated by commas.")
else:
    total_students = len(marks)
    if total_students == 0:
        print("No marks entered. Please try again.")
    else:
        passed_students = sum(1 for mark in marks if mark >= 40)
        failed_students = total_students - passed_students
        total_marks = sum(marks)
        average_marks = total_marks / total_students
        pass_percentage = (passed_students / total_students) * 100

   
        sorted_marks_asc = sorted(marks)

        
        second_highest_mark = sorted_marks_asc[-2] if len(sorted_marks_asc) > 1 else "N/A"
        second_lowest_mark = sorted_marks_asc[1] if len(sorted_marks_asc) > 1 else "N/A"

   
        all_passed = all(mark >= 40 for mark in marks)
        any_failed = any(mark < 40 for mark in marks)

     
        user_mark_input = input("Enter a mark to check if it exists in the list: ")
        try:
            user_mark = int(user_mark_input)
            if user_mark in marks:
                mark_exists_message = f"The mark {user_mark} exists in the list."
            else:
                mark_exists_message = f"The mark {user_mark} does not exist in the list."
        except ValueError:
            mark_exists_message = "Invalid input. Please enter a valid number."


        grade_a_count = sum(1 for mark in marks if mark >= 90)
        grade_b_count = sum(1 for mark in marks if 80 <= mark < 90)
        grade_c_count = sum(1 for mark in marks if 70 <= mark < 80)
        grade_d_count = sum(1 for mark in marks if 60 <= mark < 70)
        grade_e_count = sum(1 for mark in marks if 40 <= mark < 60)
        grade_f_count = sum(1 for mark in marks if mark < 40)

    
        print("\n--- Output ---")

        print(f"Total Students: {total_students}")
        print(f"Highest Marks: {max(marks)}")
        print(f"Lowest Marks: {min(marks)}")
        print(f"Average Marks: {average_marks:.1f}")

        print(f"Passed: {passed_students}")
        print(f"Failed: {failed_students}")
        print(f"Pass Percentage: {pass_percentage:.1f}%")

        print(f"Sorted Marks: {sorted_marks_asc}")
        print(f"Second Highest Mark: {second_highest_mark}")
        print(f"Second Lowest Mark: {second_lowest_mark}")

        print(f"\nGrade A: {grade_a_count} Students")
        print(f"Grade B: {grade_b_count} Students")
        print(f"Grade C: {grade_c_count} Students")
        print(f"Grade D: {grade_d_count} Students")
        print(f"Grade E: {grade_e_count} Students")
        print(f"Grade F: {grade_f_count} Students")

        
        print(f"\nAll students passed? {'Yes' if all_passed else 'No'}")
        print(f"Any student failed? {'Yes' if any_failed else 'No'}")
        print(f"\n{mark_exists_message}")
        print("--------------")
        