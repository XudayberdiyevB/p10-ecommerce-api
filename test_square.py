def get_student_age_and_grade(data: dict):
    return f'Age: {data.get("age")}, ' \
           f'Grade: {data.get("grade")}'


def test_student_age():
    test_data = {
        "name": "John",
        "age": 20,
        "grade": 3,
    }
    print("expected result: ", get_student_age_and_grade(test_data))
    assert get_student_age_and_grade(test_data) == "Age: 20, Grade: 3"


test_student_age()
