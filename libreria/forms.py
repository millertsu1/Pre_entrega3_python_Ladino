from django import forms
from .models import Book, User, Course


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields ='__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
