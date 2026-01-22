from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .models import University, Student
from .forms import UniversityForm, StudentForm

def university_list(request):
    universities = University.objects.all()
    return render(request, 'university_list.html', {'universities': universities})

def university_create(request):
    if request.method == 'POST':
        form = UniversityForm(request.POST)
        if form.is_valid():
            university = form.save()
            return redirect('university_detail', pk=university.pk)
    else:
        form = UniversityForm()
    return render(request, 'university_form.html', {'form': form, 'title': 'Создать университет'})

def university_detail(request, pk):
    university = get_object_or_404(University, pk=pk)
    return render(request, 'university_detail.html', {'university': university})

def university_update(request, pk):
    university = get_object_or_404(University, pk=pk)
    if request.method == 'POST':
        form = UniversityForm(request.POST, instance=university)
        if form.is_valid():
            form.save()
            return redirect('university_detail', pk=pk)
    else:
        form = UniversityForm(instance=university)
    return render(request, 'university_form.html', {'form': form, 'title': 'Обновить университет'})

def university_delete(request, pk):
    university = get_object_or_404(University, pk=pk)
    if request.method == 'POST':
        university.delete()
        return redirect('university_list')
    return render(request, 'university_confirm_delete.html', {'university': university})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form, 'title': 'Создать студента'})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', {'student': student})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form, 'title': 'Обновить студента'})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})