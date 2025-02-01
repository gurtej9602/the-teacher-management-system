#teacher management system
import pandas as pd
import matplotlib.pyplot as plt 
import os

#Add Teacher
def add(file_name = 'teacher_data.csv'):
    print("+++++++++++++++++++++++++++++++++++++")
    print("+      Add Teacher Details          +")
    print("+++++++++++++++++++++++++++++++++++++")

    teacher_id = input("Enter Teacher ID: ")
    name = input("Enter Teacher Name: ")
    subject = input("Enter Subject: ")
    qualification = input("Enter Qualification: ")
    contact = input("Enter Contact Number: ")
    email = input("Enter Email Address: ")
    experience = input("Enter Years of Experience: ")

    teacher_details = {
        "Teacher ID": teacher_id,
        "Name": name,
        "Subject": subject,
        "Qualification": qualification,
        "Contact": contact,
        "Email": email,
        "Experience": experience
    }
    teacher_df = pd.DataFrame([teacher_details])
    print(teacher_df)
    
    if os.path.exists(file_name):
        # If the file exists, append the data without overwriting
        teacher_df.to_csv(file_name, mode='a', index=False, header=False)
    else:
        # If the file does not exist, create a new file with a header
        teacher_df.to_csv(file_name, index=False)

    print("Teacher details added successfully and saved to file!")

def view(file_name = 'teacher_data.csv'):
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("+       View All Teacher Details         +")
    print("++++++++++++++++++++++++++++++++++++++++++")

    if os.path.exists(file_name):
        # Read the CSV file into a DataFrame
        teacher_df = pd.read_csv(file_name)
        
        # Check if the DataFrame is empty
        if teacher_df.empty:
            print("No teacher data available.")
        else:
            # Display the DataFrame
            print("\nTeacher Details:\n")
            print(teacher_df.to_string(index=False))
    else:
        print("No data file found! Please add teacher details first.")

    
def search(file_name='teacher_data.csv'):
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+     Search Teacher Details          +")
    print("+++++++++++++++++++++++++++++++++++++++")

    # Check if the file exists
    if os.path.exists(file_name):
        teacher_df = pd.read_csv(file_name)
        
        # Check if the DataFrame is empty
        if teacher_df.empty:
            print("No teacher data available to search.")
            return
        
        # Prompt the user for search criteria
        print("Search by:\n1. Teacher ID\n2. Name\n3. Subject")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            teacher_id = input("Enter Teacher ID: ")
            result = teacher_df[teacher_df['Teacher ID'].astype(str) == teacher_id]
        elif choice == "2":
            name = input("Enter Teacher Name: ")
            result = teacher_df[teacher_df['Name'].str.contains(name, case=False, na=False)]
        elif choice == "3":
            subject = input("Enter Subject: ")
            result = teacher_df[teacher_df['Subject'].str.contains(subject, case=False, na=False)]
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
            return
        
        # Check if any results were found
        if not result.empty:
            print("Search Results:\n")
            print(result.to_string(index=False))
        else:
            print("No matching teacher details found.")
    else:
        print("No data file found! Please add teacher details first.")


def update(file_name="teacher_data.csv"):
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("+        Update Teacher Details          +")
    print("++++++++++++++++++++++++++++++++++++++++++")

    if os.path.exists(file_name):
        # Read the CSV file into a DataFrame
        teacher_df = pd.read_csv(file_name)
        
        # Check if the DataFrame is empty
        if teacher_df.empty:
            print("No teacher data available to update.")
            return
        
        # Prompt the user to enter the Teacher ID to update
        teacher_id = input("Enter the Teacher ID of the teacher to update: ")
        
        # Ensure Teacher ID is treated as a string for matching
        teacher_df['Teacher ID'] = teacher_df['Teacher ID'].astype(str)
        
        # Check if the Teacher ID exists
        if teacher_id in teacher_df['Teacher ID'].values:
            print("\nTeacher found! Current details:")
            print(teacher_df[teacher_df['Teacher ID'] == teacher_id].to_string(index=False))
            
            # Prompt the user for new details
            print("\nEnter new details (leave blank to keep existing values):")
            name = input("New Name: ")
            subject = input("New Subject: ")
            qualification = input("New Qualification: ")
            contact = input("New Contact Number: ")
            email = input("New Email Address: ")
            experience = input("New Years of Experience (numeric): ")
            
            # Update the details (if provided)
            teacher_df.loc[teacher_df['Teacher ID'] == teacher_id, 'Name'] = name or teacher_df.loc[teacher_df['Teacher ID'] == teacher_id, 'Name']
            teacher_df.loc[teacher_df['Teacher ID'] == teacher_id, 'Subject'] = subject or teacher_df.loc[teacher_df['Teacher ID'] == teacher_id, 'Subject']
            teacher_df.loc[teacher_df['Teacher ID'] == teacher_id, 'Qualification'] = qualification or teacher_df.loc[teacher_df['Teacher ID'] == teacher_id, 'Qualification']
            teacher_df.loc[teacher_df['Teacher ID'] == teacher_id, 'Contact'] = contact or teacher_df.loc[teacher_df['Teacher ID'] == teacher_id, 'Contact']
            teacher_df.loc[teacher_df['Teacher ID'] == teacher_id, 'Email'] = email or teacher_df.loc[teacher_df['Teacher ID'] == teacher_id, 'Email']
            
            # Update Experience only if numeric input is provided
            if experience.isdigit():
                teacher_df.loc[teacher_df['Teacher ID'] == teacher_id, 'Experience'] = int(experience)
            elif experience.strip() == "":
                print("Experience not updated (kept existing value).")
            else:
                print("Invalid Experience input! It must be numeric.")
                return
            
            # Save the updated DataFrame back to the CSV
            teacher_df.to_csv(file_name, index=False)
            print("\nTeacher details updated successfully!")
        else:
            print("No teacher found with the given Teacher ID.")
    else:
        print("No data file found! Please add teacher details first.")

    
def delete(file_name="teacher_data.csv"):
    print("+++++++++++++++++++++++++++++++++")
    print("+    Delete Teacher Details     +")
    print("+++++++++++++++++++++++++++++++++")
    
    if os.path.exists(file_name):
        teacher_df = pd.read_csv(file_name)
        
        # Check if the DataFrame is empty
        if teacher_df.empty:
            print("No teacher data available to delete.")
            return
        
        teacher_id = input("Enter the Teacher ID of the teacher to delete: ")
        
        # Ensure Teacher ID is treated as a string for matching
        teacher_df['Teacher ID'] = teacher_df['Teacher ID'].astype(str)
        
        # Check if the Teacher ID exists
        if teacher_id in teacher_df['Teacher ID'].values:
            print("Teacher found! Current details:")
            print(teacher_df[teacher_df['Teacher ID'] == teacher_id].to_string(index=False))
            
            # Confirm deletion
            confirmation = input("Are you sure you want to delete this teacher? (yes/no): ")
            if confirmation == "yes" or confirmation == "yes":
                # Drop the row corresponding to the Teacher ID
                teacher_df = teacher_df[teacher_df['Teacher ID'] != teacher_id]
                
                # Save the updated DataFrame back to the CSV
                teacher_df.to_csv(file_name, index=False)
                print("Teacher details deleted successfully!")
            else:
                print("Deletion cancelled.")
        else:
            print("No teacher found with the given Teacher ID.")
    else:
        print("No data file found! Please add teacher details first.")
def manage(file_name="teacher_attendance.csv"):
    print("++++++++++++++++++++++++++++++++++")
    print("+    Manage Teacher Attendance   +")
    print("++++++++++++++++++++++++++++++++++")

    if not os.path.exists(file_name):
        # Create an empty DataFrame with required columns if the file doesn't exist
        columns = ["Date", "Teacher ID", "Name", "Status"]
        pd.DataFrame(columns=columns).to_csv(file_name, index=False)
    
    # Load the attendance file into a DataFrame
    attendance_df = pd.read_csv(file_name)
    
    # Display options to the user
    print("1. Add Attendance\n2. View Attendance")
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        # Adding attendance
        print("--- Add Attendance ---")
        date = input("Enter Date (YYYY-MM-DD) [Leave blank for default date '2024-01-01']: ") or "2024-01-01"
        teacher_id = input("Enter Teacher ID: ")
        name = input("Enter Teacher Name: ")
        status = input("Enter Attendance Status (Present/Absent): ")
        
        # Validate input
        if status not in ["Present", "Absent","present","absent"]:
            print("Invalid status! Please enter 'Present' or 'Absent'.")
            return
        
        # Create a new record as a DataFrame
        new_record = pd.DataFrame([{"Date": date, "Teacher ID": teacher_id, "Name": name, "Status": status}])
        
        # Concatenate the new record with the existing DataFrame
        attendance_df = pd.concat([attendance_df, new_record], ignore_index=True)
        
        # Save the updated DataFrame back to the file
        attendance_df.to_csv(file_name, index=False)
        print("Attendance added successfully!")
    
    elif choice == "2":
        # Viewing attendance
        print("--- View Attendance ---")
        
        if attendance_df.empty:
            print("No attendance records found.")
        else:
            print("Attendance Records:")
            print(attendance_df.to_string(index=False))
    
    else:
        print("Invalid choice! Please select 1 or 2.")

def salary(file_name="teacher_data.csv", salary_file="salary_report.csv"):
    print("+++++++++++++++++++++++++++++++++++")
    print("+      Generate Salary Report     +")
    print("+++++++++++++++++++++++++++++++++++")

    # Check if the teacher data file exists
    if not os.path.exists(file_name):
        print("No teacher data file found! Please add teacher details first.")
        return
    
    # Load the teacher data
    teacher_df = pd.read_csv(file_name)
    
    # Check if the DataFrame is empty
    if teacher_df.empty:
        print("No teacher data available to generate the salary report.")
        return
    
    # Parameters for salary calculation
    BASE_SALARY = 30000  # Fixed base salary
    EXPERIENCE_BONUS = 1000  # Bonus per year of experience
    ALLOWANCE = 5000  # Fixed allowance for all teachers (can be modified)
    
    # Calculate salary for each teacher
    teacher_df["Base Salary"] = BASE_SALARY
    teacher_df["Experience Bonus"] = teacher_df["Experience"] * EXPERIENCE_BONUS
    teacher_df["Allowance"] = ALLOWANCE
    teacher_df["Total Salary"] = teacher_df["Base Salary"] + teacher_df["Experience Bonus"] + teacher_df["Allowance"]
    
    # Save the salary report to a new CSV file
    teacher_df[["Teacher ID", "Name", "Subject", "Base Salary", "Experience Bonus", "Allowance", "Total Salary"]].to_csv(
        salary_file, index=False
    )
    print(f"Salary report generated successfully! Saved to '{salary_file}'")
    
    # Display the report
    print("--- Salary Report ---")
    print(teacher_df[["Teacher ID", "Name", "Subject", "Total Salary"]].to_string(index=False))

def data(file_name="teacher_data.csv"):
    print("++++++++++++++++++++++++++++++++++++")
    print("+       Data Visualization         +")
    print("++++++++++++++++++++++++++++++++++++")
    
    # Check if the data file exists
    if not os.path.exists(file_name):
        print("No data file found! Please add teacher details first.")
        return
    
    # Load the teacher data
    teacher_df = pd.read_csv(file_name)
    
    # Check if the DataFrame is empty
    if teacher_df.empty:
        print("No data available for visualization.")
        return
    
    while True:
        print("Choose a visualization type:")
        print("1. Experience Distribution")
        print("2. Subjects Taught (Proportion)")
        print("3. Qualification Distribution")
        print("4. Experience vs Qualification")
        print("5. Subject Distribution")
        print("6. Top 5 Most Experienced Teachers")
        print("++++++++++++++++++++++++++++++++++++++")
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":  # Experience Distribution
            print("Generating Experience Distribution Chart...")
            teacher_df.plot(
                x="Name", 
                y="Experience", 
                kind="bar", 
                color="skyblue", 
                title="Experience Distribution of Teachers"
            )
            plt.xlabel("Teachers")
            plt.ylabel("Years of Experience")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.show()
        
        elif choice == "2":  # Subjects Taught 
            print("Generating Subjects Taught Pie Chart...")
            subject_counts = teacher_df["Subject"].value_counts()
            subject_counts.plot(
                kind="pie", 
                autopct="%1.1f%%", 
                startangle=90, 
                title="Subjects Taught (Proportion)"
            )
            plt.ylabel("")  # Remove y-label for better aesthetics
            plt.show()
        
        elif choice == "3":  # Qualification Distribution
            print("Generating Qualification Distribution Chart...")
            qualification_counts = teacher_df["Qualification"].value_counts()
            qualification_counts.plot(
                kind="bar", 
                color="lightgreen", 
                title="Qualification Distribution of Teachers"
            )
            plt.xlabel("Qualifications")
            plt.ylabel("Number of Teachers")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.show()
        
        elif choice == "4":  # Experience vs Qualification
            print("Generating Experience vs Qualification Chart...")
            exp_qual = teacher_df.groupby("Qualification")["Experience"].mean().sort_values()
            exp_qual.plot(
                kind="bar", 
                color="purple", 
                title="Average Experience by Qualification"
            )
            plt.xlabel("Qualification")
            plt.ylabel("Average Experience (Years)")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.show()
        
        elif choice == "5":  # Top 5 Most Experienced Teachers
            print("Generating Top 5 Most Experienced Teachers Chart...")
            top_experienced = teacher_df.nlargest(5, "Experience")
            top_experienced.plot(
                x="Name", 
                y="Experience", 
                kind="bar", 
                color="red", 
                title="Top 5 Most Experienced Teachers"
            )
            plt.xlabel("Teachers")
            plt.ylabel("Years of Experience")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.show()
        
        elif choice == "6":  # Exit
            print("Exiting Data Visualization.")
            break
        
        else:
            print("Invalid choice! Please select a number between 1 and 6.")

    
while True:
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+                     Main Menu                        +")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+ 1) Add  Teacher                                      +")
    print("+ 2) View All Teachers                                 +")
    print("+ 3) Search Teacher                                    +")
    print("+ 4) Update Teacher Details                            +")
    print("+ 5) Delete Teacher                                    +")
    print("+ 6) Manage Attendance                                 +")
    print("+ 7) Generate Salary Report                            +")
    print("+ 8) Data Visualization                                +")
    print("+ 9) Exit                                              +")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    n = int(input("Enter your choice: "))

    if n == 1:
        add()
    elif n == 2:
        view()
    elif n == 3:
        search()
    elif n == 4:
        update()
    elif n == 5:
        delete()
    elif n == 6:
        manage()
    elif n == 7:
        salary()
    elif n == 8:
        data()
    elif n == 9:
        break
    else:
        print("Enter the correct choice" )

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+        thank you for using this Program            +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
