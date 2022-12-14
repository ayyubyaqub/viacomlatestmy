# Generated by Django 4.0.2 on 2022-02-22 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_create_video_create_video_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='contact_us')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('heading', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='create_video_image',
            name='serial_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='contact_us_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='contact_us_image')),
                ('create_video', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contactusimage', to='home.create_video')),
            ],
        ),
    ]
