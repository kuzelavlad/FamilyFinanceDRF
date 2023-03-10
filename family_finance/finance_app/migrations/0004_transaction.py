# Generated by Django 4.1.4 on 2022-12-25 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0003_category_is_earning_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_earning', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='finance_app.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='finance_app.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
