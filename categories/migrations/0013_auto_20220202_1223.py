# Generated by Django 3.2.5 on 2022-02-02 06:53

import categories.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0012_auto_20220202_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubevideolinks',
            name='brief',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='youtubevideolinks',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=categories.models.content_file_name),
        ),
        migrations.AddField(
            model_name='youtubevideolinks',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=categories.models.content_file_name),
        ),
        migrations.AlterField(
            model_name='youtubevideolinks',
            name='category',
            field=models.ManyToManyField(related_name='work_yt_videos', to='categories.SuperCategory'),
        ),
    ]
