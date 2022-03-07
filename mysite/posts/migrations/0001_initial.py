# Generated by Django 4.0.2 on 2022-03-04 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hashtag', '0003_delete_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('short_desc', models.CharField(default=None, max_length=500)),
                ('desc', models.TextField()),
                ('catagory', models.CharField(default='Article', max_length=50)),
                ('attachment', models.ImageField(null=True, upload_to='posts/')),
                ('post_time', models.TimeField(auto_now=True, null=True)),
                ('post_date', models.DateField(auto_now=True, null=True)),
                ('hashtag', models.ManyToManyField(related_name='plans', to='hashtag.Hashtag')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=220)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]