# Generated by Django 2.0 on 2018-08-01 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_post1_user1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post1',
            name='user1',
        ),
    ]
