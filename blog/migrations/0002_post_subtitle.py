# Generated by Django 2.1.1 on 2018-09-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(blank=True, help_text='부제목', max_length=100, null=True, verbose_name='부제목'),
        ),
    ]