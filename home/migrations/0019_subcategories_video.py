# Generated by Django 3.2.5 on 2022-02-05 07:26

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20220205_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategories',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=home.models.content_file_name_video),
        ),
    ]
