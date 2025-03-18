from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Grade, Goal, History
from .forms import GradeForm, GoalForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import logout



@login_required
def dashboard(request):
    grades = Grade.objects.filter(student=request.user)
    incomplete_goals = Goal.objects.filter(student=request.user, completed=False)  # Incomplete goals
    completed_goals = Goal.objects.filter(student=request.user, completed=True)    # Completed goals
    history = History.objects.filter(student=request.user)
    return render(request, 'grades/dashboard.html', {
        'grades': grades,
        'incomplete_goals': incomplete_goals,
        'completed_goals': completed_goals,
        'history': history,
    })

@login_required
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.student = request.user
            grade.save()
            History.objects.create(student=request.user, action=f"Added grade: {grade.subject} - {grade.grade}")
            return redirect('dashboard')
    else:
        form = GradeForm()
    return render(request, 'grades/add_grade.html', {'form': form})

@login_required
def set_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.student = request.user
            goal.save()
            History.objects.create(student=request.user, action=f"Set goal: {goal.subject} - {goal.target_grade}")
            return redirect('dashboard')
    else:
        form = GoalForm()
    return render(request, 'grades/set_goal.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.student = request.user
            grade.save()
            History.objects.create(student=request.user, action=f"Added grade: {grade.subject} - {grade.grade}")
            messages.success(request, 'Grade added successfully!')
            return redirect('dashboard')
    else:
        form = GradeForm()
    return render(request, 'grades/add_grade.html', {'form': form})

@login_required
def set_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.student = request.user
            goal.save()
            History.objects.create(student=request.user, action=f"Set goal: {goal.subject} - {goal.target_grade}")
            messages.success(request, 'Goal set successfully!')
            return redirect('dashboard')
    else:
        form = GoalForm()
    return render(request, 'grades/set_goal.html', {'form': form})

def custom_logout(request):
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to the login page

@login_required
def complete_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, student=request.user)
    goal.completed = True
    goal.save()
    return redirect('dashboard')

@login_required
def delete_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, student=request.user)
    goal.delete()
    return redirect('dashboard')