# Generated by Django 4.0.2 on 2022-02-16 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_alter_work_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Work',
        ),
    ]