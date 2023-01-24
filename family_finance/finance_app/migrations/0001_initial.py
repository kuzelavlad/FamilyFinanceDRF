# Generated by Django 4.1.4 on 2022-12-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=256, verbose_name='Имя')),
                ('password', models.TextField(max_length=256, verbose_name='Пароль')),
                ('email', models.EmailField(max_length=254, verbose_name='адрес электронной почты')),
            ],
        ),
    ]