# Generated by Django 3.2.5 on 2022-01-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_aboutus_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
