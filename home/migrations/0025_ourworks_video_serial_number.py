# Generated by Django 4.0.2 on 2022-02-16 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_work_ourworks_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourworks_video',
            name='serial_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]