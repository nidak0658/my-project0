def calculate_gpa(grades, credits):
    total_credit_hours = sum(credits)
    total_grade_points = 0.0
    
    for i in range(len(grades)):
        grade = grades[i].upper()
        credit = credits[i]
        
        if grade == 'A':
            grade_points = 4.0
        elif grade == 'A-':
            grade_points = 3.7
        elif grade == 'B+':
            grade_points = 3.3
        elif grade == 'B':
            grade_points = 3.0
        elif grade == 'B-':
            grade_points = 2.7
        elif grade == 'C+':
            grade_points = 2.3
        elif grade == 'C':
            grade_points = 2.0
        elif grade == 'C-':
            grade_points = 1.7
        elif grade == 'D+':
            grade_points = 1.3
        elif grade == 'D':
            grade_points = 1.0
        elif grade == 'F':
            grade_points = 0.0
        else:
            raise ValueError(f"Invalid grade '{grade}' encountered.")
        
        total_grade_points += grade_points * credit
    
    gpa = total_grade_points / total_credit_hours
    return gpa

def calculate_cgpa(semesters):
    total_cumulative_credit_hours = 0
    total_cumulative_grade_points = 0.0
    
    for semester in semesters:
        grades = semester['grades']
        credits = semester['credits']
        
        semester_gpa = calculate_gpa(grades, credits)
        
        total_cumulative_credit_hours += sum(credits)
        total_cumulative_grade_points += semester_gpa * sum(credits)
    
    cgpa = total_cumulative_grade_points / total_cumulative_credit_hours
    return cgpa

def main():
    semesters = []
    
    num_semesters = int(input("Enter the number of semesters: "))
    
    for i in range(1, num_semesters + 1):
        print(f"\nSemester {i}:")
        num_courses = int(input("Enter the number of courses: "))
        
        grades = []
        credits = []
        
        for j in range(1, num_courses + 1):
            course_grade = input(f"Enter grade for course {j} (e.g., A, B+, C): ").strip().upper()
            credit_hours = float(input(f"Enter credit hours for course {j}: "))
            
            grades.append(course_grade)
            credits.append(credit_hours)
        
        semesters.append({
            'grades': grades,
            'credits': credits
        })
    
    cgpa = calculate_cgpa(semesters)
    
    print(f"\nCGPA Calculation Results:")
    for i, semester in enumerate(semesters):
        semester_gpa = calculate_gpa(semester['grades'], semester['credits'])
        print(f"Semester {i + 1} GPA: {semester_gpa:.2f}")
    
    print(f"\nOverall CGPA: {cgpa:.2f}")

if __name__ == "__main__":
    main()
