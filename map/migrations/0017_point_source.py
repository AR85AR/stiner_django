# Generated by Django 3.1.2 on 2021-05-30 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0016_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='source',
            field=models.CharField(default='brak', max_length=100),
            preserve_default=False,
        ),
    ]