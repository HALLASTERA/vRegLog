# Generated by Django 2.0.2 on 2019-07-02 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='headshot',
            field=models.ImageField(blank=True, null=True, upload_to='hero_headshots/'),
        ),
    ]