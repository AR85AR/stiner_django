# Generated by Django 3.1.2 on 2020-11-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_message_important'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='delete',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
