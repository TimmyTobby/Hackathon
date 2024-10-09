import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from new_schema import Base, Student, AcademicHistory, StudyHabits, ExtracurricularActivities, ParentalTeacherInvolvement, MockExamScores  # Adjust import as necessary

# Connect to the database
engine = create_engine('postgresql://datafest_project_68mw_user:iuzi3jnmjiAKsJ1DVsdTdVDOvQEtTuTT@dpg-crvaaag8fa8c73cubtug-a.oregon-postgres.render.com/datafest_project_68mw')
Base.metadata.create_all(engine)  # Create tables if they don't exist

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Load the CSV files into DataFrames
students_df = pd.read_csv('students.csv')  # Replace with actual path
academic_history_df = pd.read_csv('academic_history.csv')  # Replace with actual path
study_habits_df = pd.read_csv('study_habits.csv')  # Replace with actual path
extracurricular_activities_df = pd.read_csv('extracurricular_activities.csv')  # Replace with actual path
parental_teacher_involvement_df = pd.read_csv('parental_teacher_involvement.csv')  # Replace with actual path
mock_exam_scores_df = pd.read_csv('mock_exam_scores.csv')  # Replace with actual path

# # Inserting data into the database
try:
    # Insert students
    for _, row in students_df.iterrows():
        existing_student = session.query(Student).filter_by(student_id=row['student_id']).first()
        if not existing_student:
            student = Student(
                student_id=row['student_id'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                gender=row['gender'],
                age=row['age'],
                home_location=row['home_location'],
                SES=row['SES'],
                parental_education=row['parental_education']
            )
            session.add(student)

    # Commit the students to the database
    session.commit()

    # Insert academic history
    for _, row in academic_history_df.iterrows():
        academic_history = AcademicHistory(
            academic_id=row['academic_id'],
            student_id=row['student_id'],
            cgpa=row['cgpa'],
            attendance_rate=row['attendance_rate'],
            homework_completion=row['homework_completion']
        )
        session.add(academic_history)

    # Commit the academic history to the database
    session.commit()

    #Insert study habits
    for _, row in study_habits_df.iterrows():
        study_habit = StudyHabits(
            habit_id=row['habit_id'],
            student_id=row['student_id'],
            study_hours_per_week=row['study_hours_per_week'],
            preferred_study_method=row['preferred_study_method'],
            access_to_resources=row['access_to_resources'],
            time_management=row['time_management']
        )
        session.add(study_habit)

    # Commit the study habits to the database
    session.commit()

    # Insert extracurricular activities
    for _, row in extracurricular_activities_df.iterrows():
        extracurricular_activity = ExtracurricularActivities(
            activity_id=row['activity_id'],
            student_id=row['student_id'],
            activity=row['activity'],
            sleep_hours=row['sleep_hours'],
            nutrition_status=row['nutrition_status']
        )
        session.add(extracurricular_activity)

    # Commit the extracurricular activities to the database
    session.commit()

    # Insert parental and teacher involvement
    for _, row in parental_teacher_involvement_df.iterrows():
        parental_involvement = ParentalTeacherInvolvement(
            involvement_id=row['involvement_id'],
            student_id=row['student_id'],
            parental_engagement=row['parental_engagement'],
            teacher_feedback=row['teacher_feedback'],
            extra_tutoring=row['extra_tutoring']
        )
        session.add(parental_involvement)

    # Commit the parental and teacher involvement to the database
    session.commit()

    # Insert mock exam scores
    for _, row in mock_exam_scores_df.iterrows():
        mock_exam_score = MockExamScores(
            mock_id=row['mock_id'],
            student_id=row['student_id'],
            mock_cgpa=row['mock_cgpa'],
            improvement_since_mock=row['improvement_since_mock']
        )
        session.add(mock_exam_score)

    # Commit the mock exam scores to the database
    session.commit()

except Exception as e:
    session.rollback()  # Rollback the session in case of error
    print(f"An error occurred: {e}")
finally:
    session.close()  # Close the session
