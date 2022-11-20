from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.


class SuperCategory(models.Model):
    serial_number=models.IntegerField(null=True,blank=True)
    super_category_name = models.CharField(max_length=254)
    slug = models.SlugField(editable=False, unique=True, max_length=255)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.super_category_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.super_category_name




def content_file_name(instance, filename):
    return '/'.join(['category', instance.category, filename])

def content_file_name_video(instance, filename):
    return '/'.join(['category', instance.super_category.super_category_name, filename])


class Categories(models.Model):
    price=models.IntegerField()
    serial_number = models.IntegerField()
    super_category = models.ManyToManyField(
        to=SuperCategory, related_name='sp')
    category = models.CharField(max_length=254)
    brief = models.CharField(max_length=254)
    image = models.ImageField(upload_to=content_file_name)
    landscapeImage=models.ImageField(upload_to=content_file_name,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    video = models.FileField(
        upload_to=content_file_name, null=True, blank=True)
    slug = models.SlugField(editable=False)
    heading_for_youtube=models.CharField(max_length=100,null=True,blank=True)
    title_youtube1 = models.CharField(max_length=50, null=True, blank=True)
    brief_youtube1 = models.CharField(max_length=100, null=True, blank=True)
    image_youtube1 = models.ImageField(
        upload_to=content_file_name, null=True, blank=True)
    video_link_youtube1 = models.CharField(max_length=100,null=True,blank=True)
    title_youtube2 = models.CharField(max_length=50, null=True, blank=True)
    brief_youtube2 = models.CharField(max_length=100, null=True, blank=True)
    image_youtube2 = models.ImageField(
        upload_to=content_file_name, null=True, blank=True)
    video_link_youtube2 = models.CharField(max_length=100,null=True,blank=True)
    
    title_youtube3 = models.CharField(max_length=50, null=True, blank=True)
    brief_youtube3 = models.CharField(max_length=100, null=True, blank=True)
    image_youtube3 = models.ImageField(
        upload_to=content_file_name, null=True, blank=True)
    video_link_youtube3 = models.CharField(max_length=100,null=True,blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.category


class YoutubeVideoLinks(models.Model):
    serial_number=models.IntegerField(null=True,blank=True)
    super_category = models.ManyToManyField(
        to=SuperCategory, related_name='work_yt_videos')
    title = models.CharField(max_length=50, null=True, blank=True)
    brief = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(
        upload_to='Inspired_with_our_video', null=True, blank=True)
    video_link = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class CategoriesVideo(models.Model):
    category = models.ManyToManyField(to=Categories)
    video_name = models.CharField(max_length=254)
    video_description = models.TextField()
    video_link = models.CharField(max_length=254)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.video_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.video_name

