from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name='home'),
    path('us', views.us, name='us'),
    path('books', views.books, name='books'),
    path('courses', views.courses, name='courses'),
    path('books/create', views.create, name='create'),
    path('books/edit', views.edit, name='edit'),
    path('courses/create', views.create_course, name='create_course'),
    path('courses/edit', views.edit, name='edit'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)