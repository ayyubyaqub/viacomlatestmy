# Generated by Django 4.0.2 on 2022-02-19 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_aboutus_image_logo_bottum_aboutus_video_bottum'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='youtube_title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]