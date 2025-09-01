


class Course:
    def __init__(self, uniq_id, course_name, course_number):
        self.uniq_id = uniq_id
        self.course_name = course_name
        self.course_number = course_number.strip()

    def __str__(self):
        return f"{self.uniq_id} | {self.course_name} --- {self.course_number}"


    def get_course_number(self):
        return self.course_number

