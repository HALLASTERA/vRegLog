# Generated by Django 2.0 on 2018-08-01 14:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('about', '0006_remove_post1_user1'),
    ]

    operations = [
        migrations.AddField(
            model_name='post1',
            name='user1',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
