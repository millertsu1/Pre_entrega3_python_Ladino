# Generated by Django 4.2 on 2023-06-26 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_course_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='images', verbose_name='Course Image'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]