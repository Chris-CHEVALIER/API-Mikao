# Generated by Django 2.2.6 on 2019-12-18 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Treatment',
                'verbose_name_plural': 'Treatments',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('treatments', models.ManyToManyField(to='mikao.Treatment', verbose_name='list of treatments')),
            ],
            options={
                'verbose_name': 'Symptom',
                'verbose_name_plural': 'Symptoms',
            },
        ),
        migrations.CreateModel(
            name='FavoriteList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptoms', models.ManyToManyField(to='mikao.Symptom', verbose_name='list of symptoms')),
                ('treatments', models.ManyToManyField(to='mikao.Treatment', verbose_name='list of treatments')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mikao.User')),
            ],
            options={
                'verbose_name': 'FavoriteList',
                'verbose_name_plural': 'FavoriteLists',
            },
        ),
    ]
