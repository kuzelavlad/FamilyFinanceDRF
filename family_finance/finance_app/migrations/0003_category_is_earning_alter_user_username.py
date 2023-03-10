# Generated by Django 4.1.4 on 2022-12-25 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0002_alter_user_email_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_earning',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True, verbose_name='Имя'),
        ),
    ]
