
def rank_students(students: list[dict], *, min_score: int = 0) -> list[str]:
    students = filter(lambda s: s["score"] >= min_score, students)
    students = sorted(students, key=lambda s: (s["group"], -s["score"], s["name"]))
    return [s["name"] for s in students]


s = [
    {"name": "Олена", "group": "ПМі-12", "score": 92},
    {"name": "Андрій", "group": "ПМі-11", "score": 78},
    {"name": "Марта", "group": "ПМі-12", "score": 92},
    {"name": "Ігор", "group": "ПМі-11", "score": 85},
    {"name": "Софія", "group": "ПМі-12", "score": 67}
]

print(rank_students(s))
print(rank_students(s, min_score=80))
