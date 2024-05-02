# views.py

from django.shortcuts import render, redirect
from .forms import FoodForm
from .models import Food
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings

def get_food_data(food_name):
    # API 호출을 위한 URL
    url = f"https://openapi.foodsafetykorea.go.kr/api/{settings.FOOD_API_KEY}/I2790/json/1/1000/DESC_KOR={food_name}"

    # API 호출
    response = requests.get(url)
    data = response.json()

    # 필요한 데이터 추출
    if data.get("I2790"):
        food_data = data["I2790"]["row"]

        # 원하는 데이터 처리 (예: 모델에 저장)
        for food in food_data:
            # 음식 데이터 처리
            # ...

        # 처리된 데이터 반환 (옵션)
         return food_data

    return None

@login_required  
def search_food(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')

        # 음식 데이터 가져오기
        food_data = get_food_data(search_query)

        if food_data:
            # 검색 결과를 템플릿으로 전달
            context = {'food_data': food_data}
            return render(request, 'search.html', context)
        else:
            context = {'error_message': '음식을 찾을 수 없습니다.'}
            return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')



def save_food(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        calorie = request.POST.get('calorie')
        food = Food(name=name, calorie=calorie)
        food.save()
        return redirect('food_search:search')

  
def food_list(request):
    foods = Food.objects.all()
    context = {'foods': foods}
    return render(request, 'food_list.html', context)
    