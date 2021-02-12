# Generated by Django 3.1.2 on 2021-02-07 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
        ('trails', '0006_remove_trail_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='points',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='map.point'),
            preserve_default=False,
        ),
    ]