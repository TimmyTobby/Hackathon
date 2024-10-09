
# Student's Exam Performance Analytics

## The Data

### Students Table

| Columns                     | Description |
| ---------------------------- | ----------- |
| **Student ID**               | A unique identifier assigned to each student for record-keeping purposes. |
| **Stream**                   | The academic stream a student is enrolled in, such as Science, Art, or Commercial, reflecting their focus area of study. |
| **Gender**                   | The gender of the student, typically categorized as male or female. |
| **Family Income (SES)**      | The socioeconomic status (SES) of the student's family, measured through family income. It reflects financial background and can influence educational resources. |
| **SS1 Score**                | The student's overall academic performance in their first year of their senior secondary school (SS1). |
| **SS2 Score**                | The student's overall academic performance in their second year of their senior secondary school (SS2). |
| **Mock Exam Score**          | The student's score in the preparatory mock exams that simulate final exam conditions. |
| **Attendance Rate (%)**      | The percentage of days the student attended school, out of the total possible school days. |
| **Distance from Home (km)**  | The distance, in kilometers, between the student's home and the school. |
| **Study Hours per Day**      | The number of hours a student dedicates to studying per day. |
| **Extracurricular Activity** | Whether the student is involved in activities outside the standard curriculum, such as sports, clubs, or other non-academic pursuits. |
| **Age**                      | The student's age at the time of data collection. |
| **Extra Tutoring**           | Whether the student receives additional academic support outside of school, like private tutoring. |
| **Internet Access**          | Whether the student has access to the internet at home, which could support research, studying, and digital learning. |
| **Parental Education**       | The highest level of education attained by the student's parents, which may influence the student's academic support at home. |
| **Library Usage**            | The frequency with which the student uses the school or public library for studying or accessing learning materials. |
| **Study Method**             | The study strategies and techniques a student uses, such as group study, independent study. |
| **Student-Teacher Relationship** | An assessment of the overall quality of the relationship between the student and their teachers, which can affect motivation and academic performance. |
| **Student Status**           | The status of the student in their final Mock Exams if the student scores above average _(above 50%)_ or below average _(below 50%)_ |



### Teachers Table

| Columns         | Description |
| --------------- | ----------- |
| **Teacher ID**  | A unique identifier assigned to each teacher for record-keeping purposes. |
| **Subject**     | The subject taught by the teacher, such as Biology, Mathematics, etc. |
| **Stream**      | The academic stream or streams the teacher teaches in (Science, Art, Commercial, or All). |
| **Experience**  | The years of experience the teacher has, categorized as either below or above 5 years. |
| **Qualification** | The teacher's educational qualification (e.g., B.Sc., NCE, HND), indicating their level of training. |


### Student-Teacher Preference Table

| Columns                           | Description |
| ---------------------------------- | ----------- |
| **Student ID**                     | A unique identifier assigned to each student for record-keeping purposes. |
| **Stream**                         | The academic stream a student is enrolled in, such as Science, Art, or Commercial, reflecting their focus area of study. |
| **Chemistry_Teacher_ID**           | The ID of the student's preferred Chemistry teacher. |
| **Economics_Teacher_ID**           | The ID of the student's preferred Economics teacher. |
| **English Language_Teacher_ID**    | The ID of the student's preferred English Language teacher. |
| **Government_Teacher_ID**          | The ID of the student's preferred Government teacher. |
| **Biology_Teacher_ID**             | The ID of the student's preferred Biology teacher. |
| **Business Studies_Teacher_ID**    | The ID of the student's preferred Business Studies teacher. |
| **Geography_Teacher_ID**           | The ID of the student's preferred Geography teacher. |
| **Literature-in-English_Teacher_ID** | The ID of the student's preferred Literature-in-English teacher. |
| **Physics_Teacher_ID**             | The ID of the student's preferred Physics teacher. |
| **Commerce_Teacher_ID**            | The ID of the student's preferred Commerce teacher. |
| **History_Teacher_ID**             | The ID of the student's preferred History teacher. |
| **Accounting_Teacher_ID**          | The ID of the student's preferred Accounting teacher. |
| **Mathematics_Teacher_ID**         | The ID of the student's preferred Mathematics teacher. |