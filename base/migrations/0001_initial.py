# Generated by Django 5.0.2 on 2024-03-18 08:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Storyline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('hint', models.TextField(blank=True, null=True)),
                ('code', models.CharField(max_length=10)),
                ('character', models.CharField(blank=True, null=True)),
                ('storyline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.storyline')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sec_code', models.CharField(max_length=8)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('color', models.CharField(blank=True, default='red', null=True)),
                ('hangman', models.TextField(blank=True, default='not reached', null=True)),
                ('summon', models.TextField(blank=True, default='not reached', null=True)),
                ('betrayal', models.TextField(blank=True, default='not reached', null=True)),
                ('current_clue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.clue')),
                ('storyline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.storyline')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('roll_no', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('phone_no', models.CharField(max_length=15)),
                ('branch', models.CharField(max_length=100)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
