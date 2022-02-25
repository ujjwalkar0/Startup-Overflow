# Generated by Django 4.0.2 on 2022-02-25 14:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0023_delete_tagfollow'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkunique', models.CharField(max_length=16)),
                ('follower', models.ManyToManyField(null=True, related_name='tag_follower_name', to=settings.AUTH_USER_MODEL)),
                ('name', models.ManyToManyField(null=True, related_name='tag_name', to='api.Hashtag')),
            ],
        ),
    ]