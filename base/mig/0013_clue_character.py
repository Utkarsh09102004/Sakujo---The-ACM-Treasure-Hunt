# Generated by Django 5.0.2 on 2024-02-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_remove_clue_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='character',
            field=models.CharField(blank=True, null=True),
        ),
    ]