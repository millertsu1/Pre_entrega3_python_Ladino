from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Course
from .forms import BookForm, UserForm, CourseForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def us(request):
    return render(request, 'us.html')

""" access to books """

def books(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def create(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('books')
    return render(request, 'books/create.html', {'form':form})

def edit(request):
    return render(request, 'books/edit.html')

""" access to courses"""

def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})

def create_course(request):
    form = CourseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('courses')
    return render(request, 'courses/create.html', {'form': form})

