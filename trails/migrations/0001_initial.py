# Generated by Django 3.1.2 on 2021-04-16 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('descriptions', models.TextField()),
                ('country', models.CharField(choices=[('Polska', 'Polska'), ('Niemcy', 'Niemcy')], max_length=15)),
                ('region', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('Krajoznawcza', 'krajoznawcza'), ('Rodzinna', 'Rodzinna'), ('Górska', 'Górska'), ('Wymagająca', 'Wymagająca'), ('Wakacyjna', 'Wakacyjna'), ('Inna', 'Inna')], max_length=15)),
                ('image', models.ImageField(blank=True, upload_to='media/img_trail/%Y/%m%d')),
                ('average_grade', models.DecimalField(decimal_places=1, max_digits=2)),
                ('watched', models.IntegerField()),
                ('popular', models.BooleanField(default=False)),
                ('points', models.ManyToManyField(to='map.Point')),
            ],
        ),
        migrations.CreateModel(
            name='Rate_trail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=1, max_digits=2)),
                ('opinion', models.TextField()),
                ('trail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trails.trail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
