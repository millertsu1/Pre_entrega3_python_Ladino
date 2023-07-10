from django.contrib import admin
from .models import Book, User, Course, Avatar

# Register your models here.
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Avatar)
