# Generated by Django 5.0.2 on 2024-02-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='hint',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clue',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clue',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]