# Generated by Django 4.0.2 on 2022-02-19 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_aboutus_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image_logo_bottum',
            field=models.ImageField(blank=True, null=True, upload_to='abous-us'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='video_bottum',
            field=models.FileField(blank=True, null=True, upload_to='abous-us'),
        ),
    ]
