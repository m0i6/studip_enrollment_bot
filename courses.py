import json

# enrollment urls of all courses to enroll to
class Course: 
    def __init__(self, name: str, url_v: str, url_l: str, enrollment_in_groups: bool, group_number: int):
        self.name = name
        self.url_v = url_v
        self.url_l = url_l
        self.enrollment_in_groups = enrollment_in_groups
        self.group_number = group_number

def read_courses_from_json(filename: str):
    with open(filename, 'r') as file:
        course_data = json.load(file)
    
    courses = []
    for data in course_data:
        course = Course(
            name=data["name"],
            url_v=data["url_v"],
            url_l=data["url_l"],
            enrollment_in_groups=data["enrollment_in_groups"],
            group_number=data["group_number"]
        )
        courses.append(course)
    
    return courses

my_courses = read_courses_from_json("./course_data.json")