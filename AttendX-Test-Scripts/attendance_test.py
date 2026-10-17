

def test_mark_attendance():
    student_id = "D24IT142"
    attendance_status = "Present"
    
    if student_id and attendance_status == "Present":
        print("Attendance test: PASS - Attendance data provided")
    else:
        print("Attendance test: FAIL")

def test_missing_student_id():
    student_id = ""
    
    if not student_id:
        print("Missing student ID test: PASS")
    else:
        print("Missing student ID test: FAIL")

test_mark_attendance()
test_missing_student_id()
