# Generated by Django 3.1.2 on 2021-06-03 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0011_trail_done_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trail',
            name='sound',
        ),
    ]
