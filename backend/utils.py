def classify_competence(total_points):
    if total_points <= 30:
        return "низкий уровень"
    elif 31 <= total_points <= 70:
        return "средний уровень"
    else:
        return "высокий уровень"

from test_data import test_data

def evaluate_test(subject, student_answers):
    total_points = 0
    for answer_index, question in zip(student_answers, test_data[subject]):
        points = question["options"][answer_index]["points"]
        total_points += points
    
    competence_category = classify_competence(total_points)
    return total_points, competence_category

