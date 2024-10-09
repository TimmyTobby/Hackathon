from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    home_location = Column(String, nullable=False)
    gender = Column(String(1), nullable=False)  # 'M' or 'F'
    age = Column(Integer, nullable=False)
    SES = Column(String, nullable=False)  # Socioeconomic Status
    parental_education = Column(String, nullable=False)  # Parent's education level


class AcademicHistory(Base):
    __tablename__ = 'academic_history'

    academic_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.student_id'), nullable=False)
    cgpa = Column(Float, nullable=False)
    attendance_rate = Column(Float, nullable=False)
    homework_completion = Column(Float, nullable=False)


class StudyHabits(Base):
    __tablename__ = 'study_habits'

    habit_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.student_id'), nullable=False)
    study_hours_per_week = Column(Integer, nullable=False)
    preferred_study_method = Column(String, nullable=False)
    access_to_resources = Column(Boolean, nullable=False)
    time_management = Column(Float, nullable=False)


class ExtracurricularActivities(Base):
    __tablename__ = 'extracurricular_activities'

    activity_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.student_id'), nullable=False)
    activity = Column(String, nullable=False)
    sleep_hours = Column(Float, nullable=False)
    nutrition_status = Column(String, nullable=False)


class ParentalTeacherInvolvement(Base):
    __tablename__ = 'parental_teacher_involvement'

    involvement_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.student_id'), nullable=False)
    parental_engagement = Column(Float, nullable=False)
    teacher_feedback = Column(String, nullable=False)
    extra_tutoring = Column(Boolean, nullable=False)


class MockExamScores(Base):
    __tablename__ = 'mock_exam_scores'

    mock_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.student_id'), nullable=False)
    mock_cgpa = Column(Float, nullable=False)
    improvement_since_mock = Column(Float, nullable=False)


# Connect to the database
engine = create_engine('postgresql://datafest_project_68mw_user:iuzi3jnmjiAKsJ1DVsdTdVDOvQEtTuTT@dpg-crvaaag8fa8c73cubtug-a.oregon-postgres.render.com/datafest_project_68mw')
# Drop existing tables
#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
#print("schema created")

# Session creation
Session = sessionmaker(bind=engine)
session = Session()
