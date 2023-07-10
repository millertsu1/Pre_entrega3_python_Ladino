from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Course
from .forms import BookForm, CourseForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from libreria.forms import UserEditForm, ChangePasswordForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def us(request):
    return render(request, 'us.html')

""" access to books """
@login_required
def books(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

@login_required
def create(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('books')
    return render(request, 'books/create.html', {'form':form})

@login_required
def edit(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid() and request.method =='POST':
        form.save()
        return redirect('books')
    return render(request, 'books/edit.html', {'form':form})

@login_required
def remove(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books')

""" access to courses"""
@login_required
def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})

@login_required
def create_course(request):
    form = CourseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('courses')
    return render(request, 'courses/create.html', {'form': form})

@login_required
def edit_course(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(request.POST or None, request.FILES or None, instance=course)
    if form.is_valid() and request.method =='POST':
        form.save()
        return redirect('courses')
    return render(request, 'courses/edit.html', {'form': form})

@login_required
def remove_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('courses')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method =='POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form
    return render(request, 'registration/register.html', data)


def exit(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'registration/profile.html')

@login_required
def editProfile(request):
    user = request.user
    user_basic_info = User.objects.get(id = user.id)
    if request.method =="POST":
        form = UserEditForm(request.POST, instance = user )
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'registration/profile.html')
    else:
        form = UserEditForm(initial = {'username': user.username, 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name})
        return render(request, 'registration/editProfile.html', {"form": form})

@login_required
def changePassword(request):
    user = request.user 
    if request.method =="POST":
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            if  request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
            return HttpResponse('Passwords do not match')
        return render(request, 'home.html')
    else:
        form = ChangePasswordForm(user = user)
        return render(request, 'registration/changePassword.html', {"form": form})
    

def changeAvatar(request):
    pass