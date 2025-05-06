from django.shortcuts import render, redirect
from .models import Habit

def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'habits/habit_list.html', {'habits': habits})

def add_habit(request):
    if request.method == 'POST':
        name = request.POST['name']
        Habit.objects.create(name=name)
        return redirect('habit_list')
    return render(request, 'habits/add_habit.html')

def mark_as_done(request, habit_id):
    habit = Habit.objects.get(id=habit_id)
    habit.is_completed = True
    habit.save()
    return redirect('habit_list')

