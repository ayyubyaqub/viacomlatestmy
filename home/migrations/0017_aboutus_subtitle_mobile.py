# Generated by Django 3.2.5 on 2022-01-31 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_subcategories_brief'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_mobile',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
