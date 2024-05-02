from food_search.models import Food

def seed_foods():
    foods = [
        {'name': '사과', 'calorie': 52},
        {'name': '바나나', 'calorie': 96},
        {'name': '오렌지', 'calorie': 43},
        # 추가 음식 데이터를 이곳에 계속해서 추가할 수 있습니다.
    ]

    for food_data in foods:
        Food.objects.create(name=food_data['name'], calorie=food_data['calorie'])
