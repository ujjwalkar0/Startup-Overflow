# Generated by Django 4.0.2 on 2022-02-26 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_remove_groupname_owner_remove_message_reciever_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Plans',
        ),
    ]
