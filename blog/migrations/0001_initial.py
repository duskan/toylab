# Generated by Django 2.1.1 on 2018-09-06 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='Created datetime')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='Modified datetime')),
                ('title', models.CharField(help_text='제목', max_length=100, verbose_name='제목')),
                ('contents', models.TextField(blank=True, help_text='Species name in English', verbose_name='컨텐츠')),
                ('secret', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
