import pandas as pd
import random

# Expanded list of common Nigerian first and last names (Example)
first_names = [
    'Chidera', 'Ayo', 'Temitope', 'Ifeoma', 'Uche', 'Fatimah', 'Ngozi',
    'Damilola', 'Emeka', 'Adaobi', 'Oluwaseun', 'Chinonso', 'Tobi',
    'Amaka', 'Kelechi', 'Bola', 'Ibrahim', 'Abigail', 'Folake', 'Seyi',
    'Jumoke', 'Tolu', 'Chukwuemeka', 'Olamide', 'Ife', 'Chiamaka',
    'Nneka', 'Chizoba', 'Obinna', 'Opeoluwa', 'Khadijat', 'Ijeoma',
    'Adebisi', 'Chinaza', 'Dara', 'Oyinlola', 'Temiloluwa', 'Taiwo'
] * 10  # Replicating to ensure we have more entries

last_names = [
    'Okeke', 'Nwosu', 'Abubakar', 'Ojo', 'Adeyemi', 'Ogunleye',
    'Adebayo', 'Eze', 'Adamu', 'Alabi', 'Nwankwo', 'Afolabi',
    'Obinna', 'Olaniyi', 'Ige', 'Salami', 'Chukwu', 'Musa',
    'Adetokunbo', 'Ibrahim', 'Oladipo', 'Ogunbiyi', 'Ajayi', 'Akingbade'
] * 10  # Replicating to ensure we have more entries

# Expanded list of common Nigerian locations
locations = ["Urban", "Suburban", "Rural"] * 10  # Replicating to ensure we have more entries

# Number of students
n_students = 100
below_50_percent_cutoff = int(0.77 * n_students)  # 77% students will have CGPA < 50%

# Mock SES distribution (socioeconomic status)
SES_distribution = [random.choice(['High-income', 'Middle-income', 'Low-income']) for _ in range(n_students)]

# Mock parental education levels
parental_education_distribution = [random.choice(['Primary', 'Secondary', 'Tertiary']) for _ in range(n_students)]

# Mock age distribution
age_distribution = [random.randint(15, 25) for _ in range(n_students)]  # Age between 15 and 25

# Mock gender distribution
gender_distribution = [random.choice(['Male', 'Female']) for _ in range(n_students)]

# Create an empty list to store student information
students = []
for i in range(n_students):
    students.append((i + 1, random.choice(first_names), random.choice(last_names), random.choice(locations)))

# Creating DataFrame
students_df = pd.DataFrame(list(students), columns=['student_id', 'first_name', 'last_name', 'home_location'])
students_df['gender'] = gender_distribution[:len(students_df)]  # Assigning genders from the existing list
students_df['age'] = age_distribution[:len(students_df)]  # Assigning ages from the existing list
students_df['SES'] = SES_distribution[:len(students_df)]  # Assigning SES from the existing list
students_df['parental_education'] = parental_education_distribution[:len(students_df)]  # Assigning parental education

# Lists to hold generated data
cgpa = []
study_hours_per_week = []
time_management = []
sleep_hours = []
nutrition_status = []
parental_engagement = []
teacher_feedback = []
access_to_resources = []

# Loop to generate data, ensuring 77% CGPA < 50% and logical consistency
for i in range(n_students):
    # Adjust CGPA according to 77% below 50% rule
    if i < below_50_percent_cutoff:  # 77% with CGPA below 50%
        if SES_distribution[i] == 'High-income':
            resources = True
            hours = random.uniform(2, 4)  # Less study hours for low GPA
            time_mgmt = round(random.uniform(2.0, 3.0), 2)
            gpa = round(random.uniform(1.5, 2.5) * 20, 2)  # CGPA below 50%
            sleep = round(random.uniform(6.0, 7.0), 2)
            nutrition = 'Good'
            engagement = round(random.uniform(35.0, 45.0), 2)
            feedback = "Needs improvement"
        elif SES_distribution[i] == 'Middle-income':
            resources = random.choice([True, False])
            hours = random.uniform(1.5, 3.5)
            time_mgmt = round(random.uniform(2.0, 3.0), 2)
            gpa = round(random.uniform(1.5, 2.5) * 20, 2)  # CGPA below 50%
            sleep = round(random.uniform(6.0, 7.0), 2)
            nutrition = random.choice(['Good', 'Average'])
            engagement = round(random.uniform(30.0, 40.0), 2)
            feedback = "Needs improvement"
        else:  # Low-income
            resources = False
            hours = random.uniform(1, 3)  # Lower study hours
            time_mgmt = round(random.uniform(1.5, 2.5), 2)
            gpa = round(random.uniform(1.0, 2.0) * 20, 2)  # Lower CGPA
            sleep = round(random.uniform(5.5, 6.5), 2)
            nutrition = 'Poor'
            engagement = round(random.uniform(25.0, 35.0), 2)
            feedback = "Needs improvement"
    else:  # 23% with CGPA >= 50%
        if SES_distribution[i] == 'High-income':
            resources = True
            hours = random.uniform(6, 8)  # More study hours for higher GPA
            time_mgmt = round(random.uniform(4.0, 5.0), 2)
            gpa = round(random.uniform(3.5, 4.0) * 20, 2)  # Higher CGPA
            sleep = round(random.uniform(7.0, 8.0), 2)
            nutrition = 'Good'
            engagement = round(random.uniform(40.0, 50.0), 2)
            feedback = "Good performance"
        elif SES_distribution[i] == 'Middle-income':
            resources = random.choice([True, False])
            hours = random.uniform(4, 6)
            time_mgmt = round(random.uniform(3.0, 4.0), 2)
            gpa = round(random.uniform(2.5, 3.5) * 20, 2)  # Mid-range CGPA
            sleep = round(random.uniform(6.5, 7.5), 2)
            nutrition = random.choice(['Good', 'Average'])
            engagement = round(random.uniform(35.0, 45.0), 2)
            feedback = random.choice(["Good performance", "Needs improvement"])
        else:  # Low-income
            resources = False
            hours = random.uniform(3, 5)
            time_mgmt = round(random.uniform(2.5, 3.5), 2)
            gpa = round(random.uniform(2.0, 3.0) * 20, 2)  # CGPA >= 50%
            sleep = round(random.uniform(6.0, 7.0), 2)
            nutrition = random.choice(['Average', 'Poor'])
            engagement = round(random.uniform(30.0, 40.0), 2)
            feedback = random.choice(["Good performance", "Needs improvement"])

    # Add values to the respective lists
    cgpa.append(gpa)
    study_hours_per_week.append(hours)
    time_management.append(time_mgmt)
    sleep_hours.append(sleep)
    nutrition_status.append(nutrition)
    parental_engagement.append(engagement)
    teacher_feedback.append(feedback)
    access_to_resources.append(resources)

# Study habits table
study_habits_df = pd.DataFrame({
    'habit_id': range(1, n_students + 1),
    'student_id': students_df['student_id'],
    'study_hours_per_week': study_hours_per_week,
    'preferred_study_method': [
        'Self-study' if gpa > 75 else random.choice(['Group-study', 'Tutoring'])
        for gpa in cgpa
    ],
    'time_management': time_management,
    'sleep_hours': sleep_hours,
    'nutrition_status': nutrition_status,
    'parental_engagement': parental_engagement
})

# Extracurricular activities table
extracurricular_activities_df = pd.DataFrame({
    'activity_id': range(1, n_students + 1),
    'student_id': students_df['student_id'],
    'involvement': [
        random.choice(['Sports', 'Music', 'Drama', 'Volunteer Work', 'None'])
        for _ in range(n_students)
    ],
    'hours_per_week': [random.randint(2, 10) for _ in range(n_students)]
})

# Parental and teacher involvement table
parental_teacher_involvement_df = pd.DataFrame({
    'involvement_id': range(1, n_students + 1),
    'student_id': students_df['student_id'],
    'parental_involvement': [
        random.choice(['High', 'Medium', 'Low']) for _ in range(n_students)
    ],
    'teacher_feedback': teacher_feedback,
    'student_feedback': [
        random.choice(['Good', 'Bad', 'Average']) for _ in range(n_students)
    ]
})

# Academic history table
academic_history_df = pd.DataFrame({
    'academic_id': range(1, n_students + 1),
    'student_id': students_df['student_id'],
    'CGPA': cgpa,
    'attendance_rate': [
        random.randint(70, 100) for _ in range(n_students)  # Random attendance between 70% and 100%
    ]
})

# Exporting DataFrames to CSV files
students_df.to_csv('students_data.csv', index=False)
study_habits_df.to_csv('study_habits_data.csv', index=False)
extracurricular_activities_df.to_csv('extracurricular_activities_data.csv', index=False)
parental_teacher_involvement_df.to_csv('parental_teacher_involvement_data.csv', index=False)
academic_history_df.to_csv('academic_history_data.csv', index=False)

print("DataFrames have been exported as CSV files.")
