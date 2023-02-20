class Grades:
    def __init__(self, Course_Code, Course_Units, Course_Grade):
        self.Course_Code = Course_Code
        self.Course_Units = Course_Units
        self.Course_Grade = Course_Grade

    def __str__(self):
        return f"Course: {self.Course_Code}, Units: {self.Course_Units}, Grade: {self.Course_Grade}"