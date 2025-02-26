# enrolment urls of all courses to enroll to
my_courses2 = {
    "V-Software-Engineering-1": "",
    "L-Software Engineering-1": "",
    "V-Theoretische-Informatik": "https://elearning.hs-flensburg.de/dispatch.php/course/details/index/14bc021c02a7db4d13e006c28494fbed",
    "Ü-Theoretische-Informatik": "https://elearning.hs-flensburg.de/dispatch.php/course/details/index/13fd1e6cbe0c6227d2751b482756a4c7",
    "V-Mobile-Computing": "",
    "L-Mobile-Computing": "",
    "V-3D-Engine-Technology": "",
    "L-3D-Engine-Technology": "",
    "V-Mathe": "",
    "Ü-Mathe": "",
    "Grundlagen-der-IT-Security": "",
    "V-Datenbanken": "",
    "L-Datenbanken": "",
}

class Course: 
    def __init__(self, name: str, url_v: str, url_l: str, enrollment_in_groups: bool, group_number: int):
        self.name = name
        self.url_v = url_v
        self.url_l = url_l
        self.enrollment_in_groups = enrollment_in_groups
        self.group_number = group_number


my_courses = [
    Course(
        "Software Engineering",
        "",
        "",
        False,
        0
    ),
    Course(
        "Theoretische Informatik",
        "https://elearning.hs-flensburg.de/dispatch.php/course/details/index/14bc021c02a7db4d13e006c28494fbed",
        "https://elearning.hs-flensburg.de/dispatch.php/course/details/index/13fd1e6cbe0c6227d2751b482756a4c7",
        False,
        0
    ),
    Course(
        "IID Test",
        "",
        "https://elearning.hs-flensburg.de/dispatch.php/course/statusgroups?cid=33eea4084e102559b03e312185e7ce5e",
        True,
        2
    ),
]