from django.shortcuts import render, redirect
from .models import FoodItem
from .forms import FoodItemForm
from django.utils import timezone

def index(request):
    today = timezone.now().date()
    food_items = FoodItem.objects.filter(date_added=today)
    total_calories = sum(item.calories for item in food_items)
    return render(request, 'calorie_tracker/index.html', {
        'food_items': food_items,
        'total_calories': total_calories
    })

def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FoodItemForm()
    return render(request, 'calorie_tracker/add_food.html', {'form': form})

def delete_food(request, pk):
    item = FoodItem.objects.get(id=pk)
    item.delete()
    return redirect('index')

def reset_calories(request):
    today = timezone.now().date()
    FoodItem.objects.filter(date_added=today).delete()
    return redirect('index')
