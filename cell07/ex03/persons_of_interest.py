women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecilia Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

def famous_births(persons):
    """รับ dictionary ของบุคคลสำคัญและแสดงข้อมูลเรียงตามวันเกิด"""
    sorted_persons = sorted(persons.items(), key=lambda item: int(item[1]["date_of_birth"]))
    for key, value in sorted_persons:
        print(f"{value['name']} is a great scientist born in {value['date_of_birth']}.")

women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecilia Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

famous_births(women_scientists)