# Generated by Django 4.0.2 on 2022-03-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile_no',
            field=models.IntegerField(default=None),
        ),
    ]