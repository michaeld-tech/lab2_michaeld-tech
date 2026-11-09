GRADE EVALUATOR
The grade evaluator is a python tool that tells students how they are doing academically by taking their assignment scores from a CSV file . It also tells them their gpa , if they pass or not and the assignments they should redo .

HOW THE SYSTEM FUNCTIONS
You upload a CSV with the assignment name, score , weight and the assignment group (summative or formative). The formative is the quizzes, exercise and the lab which count for 60% and the summative which is the midterm and final project which counts for 40%
It then :
Calculate the grade for each assignment group and generate combined grade
Calculate the gpa out of 5.0
Confirms whether the student passed if has above 50% in each group
Flags the failed formative due resubmission

BUILT IN CHECKS
IT detects mistakes before doing any calculation such as missing files, blank files , scores below 0 or above 100 , negative weights and categories that are unknown

The organizer.sh
It keeps the files tidy. It moves the current grades.csv to archive/ with a timestamp and then generates a new grades.csv which is recorded on the organizer.log

Testing
Valid data was tested plus a range of wrong values like scores above 100 , negative values and invalid weights and the python file behaved as it was expected to behave.

Conclusion
The project was a practical concept that shows how python , CSV , shell scripting and Git work together to automate a realistic grading workflow

