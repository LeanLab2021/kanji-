# Generated by Django 3.2.4 on 2021-06-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_blogmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='category',
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='content',
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='title',
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='birthday',
            field=models.CharField(default='jg', max_length=10),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='sex',
            field=models.CharField(choices=[('男', 'boy'), ('女', 'girl')], default='lo', max_length=50),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='username',
            field=models.CharField(default='g', max_length=100),
        ),
    ]
