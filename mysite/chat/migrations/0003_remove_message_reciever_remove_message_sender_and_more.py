# Generated by Django 4.0.2 on 2022-02-26 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_groupname_member_alter_message_sender_delete_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='reciever',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.DeleteModel(
            name='GroupName',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
