# Generated by Django 3.0.4 on 2020-08-10 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_trails', '0002_auto_20200806_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertrail',
            name='image',
        ),
    ]