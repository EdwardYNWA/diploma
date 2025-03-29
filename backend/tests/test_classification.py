from utils import classify_student

def test_classification():
    assert classify_student(90) == "Продвинутый"
    assert classify_student(60) == "Средний"
    assert classify_student(30) == "Начинающий"
