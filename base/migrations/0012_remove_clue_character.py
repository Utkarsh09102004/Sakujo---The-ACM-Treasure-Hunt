# Generated by Django 5.0.2 on 2024-02-23 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_clue_character'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clue',
            name='character',
        ),
    ]
