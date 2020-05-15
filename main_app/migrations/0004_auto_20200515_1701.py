# Generated by Django 3.0.6 on 2020-05-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200514_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='Undefined', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Undefined', max_length=50),
            preserve_default=False,
        ),
    ]