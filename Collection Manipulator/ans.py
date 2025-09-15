

students = {}


while True:
    
    print("\nExample Console Interaction:")
    print("Welcome to the Student Data Organizer!")
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    
    choice = input("Enter your choice: ")

    
    if choice == '1':
        print("\nEnter student details:")
        student_id = input("Student ID: ")

      
        if student_id in students:
            print(f"Error: A student with ID '{student_id}' already exists.")
            continue  
        name = input("Name: ")
        
        
        try:
            age = int(input("Age: "))
        except ValueError:
            print("Error: Invalid input for age. Please enter a number.")
            continue

        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ")

        
        students[student_id] = {
            'Name': name,
            'Age': age,
            'Grade': grade,
            'Date of Birth': dob,
            'Subjects': subjects
        }
        print("\nStudent added successfully!")

  
    elif choice == '2':
        print("\n--- Display All Students ---")
        if not students:
            print("No students found.")
        else:
            for student_id, details in students.items():
                print(f"Student ID: {student_id} | Name: {details['Name']} | Age: {details['Age']} | Grade: {details['Grade']} | Subjects: {details['Subjects']}")
        print("...")

 
    elif choice == '3':
        student_id = input("Enter Student ID to update: ")

        if student_id in students:
            print("\nEnter new details (press Enter to keep current value):")
            
           
            current_details = students[student_id]
            
            new_name = input(f"New Name ({current_details['Name']}): ")
            if new_name:
                students[student_id]['Name'] = new_name
                
            new_age_str = input(f"New Age ({current_details['Age']}): ")
            if new_age_str:
                try:
                    students[student_id]['Age'] = int(new_age_str)
                except ValueError:
                    print("Invalid input for age. Age not updated.")

            new_grade = input(f"New Grade ({current_details['Grade']}): ")
            if new_grade:
                students[student_id]['Grade'] = new_grade
                
            new_dob = input(f"New Date of Birth ({current_details['Date of Birth']}): ")
            if new_dob:
                students[student_id]['Date of Birth'] = new_dob

            new_subjects = input(f"New Subjects ({current_details['Subjects']}): ")
            if new_subjects:
                students[student_id]['Subjects'] = new_subjects
                
            print(f"\nStudent with ID {student_id} information updated successfully.")
        else:
            print("Error: Student with this ID not found.")


    elif choice == '4':
        student_id = input("Enter Student ID to delete: ")

        if student_id in students:
            del students[student_id]
            print(f"\nStudent with ID {student_id} deleted successfully.")
        else:
            print("Error: Student with this ID not found.")

   
    elif choice == '5':
        print("\n--- Subjects Offered ---")
        print("Math, Science, English, History, Art")


    elif choice == '6':
        print("\nExiting the program. Goodbye!")
        break  

    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.")