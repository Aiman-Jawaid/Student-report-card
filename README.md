# Student Report Card Program

## Overview
This Python program allows users to enter student marks for five subjects and automatically generates a report card with total marks, percentage, and grade. It also includes input validation to ensure correct data entry.

## Features
- Input student details (name and roll number).
- Enter marks for subjects: Math, Physics, Urdu, English, and Computer.
- Validate marks input (only numbers between 0 and 100 are accepted).
- Calculate total marks, percentage, and grade based on the entered marks.
- Generate a formatted report card for each student.
- Allow multiple students to be entered in one session.

## Grade Calculation
The program assigns grades based on the percentage achieved:

| Percentage Range | Grade |
|-----------------|-------|
| 80% and above  | A+    |
| 70% - 79%      | A     |
| 60% - 69%      | B     |
| 50% - 59%      | C     |
| 40% - 49%      | D     |
| Below 40%      | F     |

## How to Use
1. Run the script in a Python environment.
2. Enter student details and marks when prompted.
3. After entering a student's details, the program will ask if you want to enter another student's data.
4. Once all students' data is entered, the program will generate report cards for each student.

## Installation
No external libraries are required. Ensure you have Python installed, then run the script using:
```sh
python student_report.py
```

## Example Output
```
📌 Enter details for a new student:
Student Name: John Doe
Roll Number: 101
Enter marks for Math: 85
Enter marks for Physics: 78
Enter marks for Urdu: 90
Enter marks for English: 88
Enter marks for Computer: 92

✅ Record for John Doe inserted successfully. Do you want to insert more? (Y/N): N

📄 Generating Report Cards...
========================================
📜 Report Card for John Doe (Roll No: 101)
========================================
📌 Math: 85
📌 Physics: 78
📌 Urdu: 90
📌 English: 88
📌 Computer: 92
----------------------------------------
🎯 Total Marks: 433 / 500
📊 Percentage: 86.60%
🏆 Grade: A+
========================================
```

## Author
Developed by [Aiman]




