# Generated by Django 2.2.10 on 2020-10-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='answer',
            name='user_identifier',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]