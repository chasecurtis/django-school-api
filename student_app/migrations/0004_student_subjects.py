# Generated by Django 5.2.4 on 2025-07-30 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_alter_student_locker_combination'),
        ('subject_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(related_name='students', to='subject_app.subject'),
        ),
    ]
