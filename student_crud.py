import unittest


class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

class StudentRegistrationSystem:
    def __init__(self):
        self.students = {}

    # CREATE
    def create_student(self, student_id, name, age, major):
        if student_id in self.students:
            print("Student with this ID already exists.")
            return False
        else:
            self.students[student_id] = Student(student_id, name, age, major)
            print("Student created successfully.")
            return True

    # READ
    def read_student(self, student_id):
        if student_id in self.students:
            print(str(self.students[student_id]) + "\n")
            return student_id
        else:
            print("Student not found.")

    def read_all_students(self):
        if not self.students:
            print("No students registered.")
            return []
        else:
            for student in self.students.values():
                print(str(student))
            return self.students.values()

    # UPDATE
    def update_student(self, student_id, name=None, age=None, major=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if major:
                student.major = major
            print("Student updated successfully.")
            return True
        else:
            print("Student not found.")
            return False

    # DELETE
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
            return True
        else:
            print("Student not found.")
            return False


class testStudentRegistrationSystem(unittest.TestCase):
    def setUp(self):
        """Set up a new StudentRegistrationSystem before each test"""
        self.system = StudentRegistrationSystem()
        self.test_id = "12345"
        self.test_name = "Caleb Garza"
        self.test_age = 20
        self.test_major = "Computer Science"

    def test_create_student_success(self):
        result = self.system.create_student(
            self.test_id, self.test_name, self.test_age, self.test_major
        )
        self.assertTrue(result)
        self.assertIn(self.test_id, self.system.students)
        student = self.system.students[self.test_id]
        self.assertEqual(student.name, self.test_name)
        self.assertEqual(student.age, self.test_age)
        self.assertEqual(student.major, self.test_major)

    def test_create_student_duplicate(self):
        self.system.create_student(
            self.test_id, self.test_name, self.test_age, self.test_major
        )
        result = self.system.create_student(
            self.test_id, "Caleb Garza", 22, "Physics"
        )
        self.assertFalse(result)
        student = self.system.students[self.test_id]
        self.assertEqual(student.name, self.test_name)

    def test_read_student_success(self):
        self.system.create_student(
            self.test_id, self.test_name, self.test_age, self.test_major
        )
        result = self.system.read_student(self.test_id)
        self.assertEqual(result, self.test_id)

    def test_read_student_not_found(self):
        result = self.system.read_student("nonexistent")
        self.assertIsNone(result)

    def test_read_all_students_empty(self):
        result = self.system.read_all_students()
        self.assertEqual(list(result), [])

    def test_read_all_students_multiple(self):
        self.system.create_student(
            "1", "Random User", 20, "CS"
        )
        self.system.create_student(
            "2", "CS Student", 22, "Physics"
        )
        result = list(self.system.read_all_students())
        self.assertEqual(len(result), 2)

    def test_update_student_success(self):
        self.system.create_student(
            self.test_id, self.test_name, self.test_age, self.test_major
        )
        # Test partial update
        result = self.system.update_student(self.test_id, name="Caleb Garza")
        self.assertTrue(result)
        student = self.system.students[self.test_id]
        self.assertEqual(student.name, "Caleb Garza")
        self.assertEqual(student.age, self.test_age)
        
        # Test complete update
        result = self.system.update_student(
            self.test_id, 
            name="Bob Smith",
            age=25,
            major="Physics"
        )
        self.assertTrue(result)
        student = self.system.students[self.test_id]
        self.assertEqual(student.name, "CS Nerd")
        self.assertEqual(student.age, 25)
        self.assertEqual(student.major, "Computer Science")

    def test_update_student_not_found(self):
        result = self.system.update_student(
            "nonexistent",
            name="Minecraft Steve"
        )
        self.assertFalse(result)

    def test_delete_student_success(self):
        self.system.create_student(
            self.test_id, self.test_name, self.test_age, self.test_major
        )
        result = self.system.delete_student(self.test_id)
        self.assertTrue(result)
        self.assertNotIn(self.test_id, self.system.students)

    def test_delete_student_not_found(self):
        result = self.system.delete_student("nonexistent")
        self.assertFalse(result)

    def test_student_str_representation(self):
        student = Student(self.test_id, self.test_name, self.test_age, self.test_major)
        expected_str = f"ID: {self.test_id}, Name: {self.test_name}, Age: {self.test_age}, Major: {self.test_major}"
        self.assertEqual(str(student), expected_str)

if __name__ == '__main__':
    unittest.main()