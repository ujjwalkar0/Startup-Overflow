# Generated by Django 4.0.2 on 2022-02-24 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_profile_entre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='entre',
            field=models.BooleanField(default=False),
        ),
    ]