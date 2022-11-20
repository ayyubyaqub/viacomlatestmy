# Generated by Django 4.0.2 on 2022-02-23 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_image_client_logo_and_vi'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketPlaceVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=100, null=True)),
                ('title_youtube1', models.CharField(blank=True, max_length=50, null=True)),
                ('brief_youtube1', models.CharField(blank=True, max_length=100, null=True)),
                ('image_youtube1', models.ImageField(blank=True, null=True, upload_to='marketplacevideoimage')),
                ('video_link_youtube1', models.CharField(blank=True, max_length=100, null=True)),
                ('title_youtube2', models.CharField(blank=True, max_length=50, null=True)),
                ('brief_youtube2', models.CharField(blank=True, max_length=100, null=True)),
                ('image_youtube2', models.ImageField(blank=True, null=True, upload_to='marketplacevideoimage')),
                ('video_link_youtube2', models.CharField(blank=True, max_length=100, null=True)),
                ('title_youtube3', models.CharField(blank=True, max_length=50, null=True)),
                ('brief_youtube3', models.CharField(blank=True, max_length=100, null=True)),
                ('image_youtube3', models.ImageField(blank=True, null=True, upload_to='marketplacevideoimage')),
                ('video_link_youtube3', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
