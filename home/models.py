from distutils.command.upload import upload
from pickle import TRUE
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from categories.models import SuperCategory
# Create your models here.
class Homecarousel(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='homecarousel')
    designation=models.CharField(max_length=200,null=True,blank=True)
    Description=models.TextField(null=True,blank=True)

class Videoseeding(models.Model):
    supercategory=models.ForeignKey(SuperCategory,on_delete=models.PROTECT,related_name='videoseeding')
    image=models.FileField(upload_to='videoseeding')    

class Videocategory(models.Model):
    supercategory=models.ForeignKey(SuperCategory,on_delete=models.PROTECT,related_name='about_us')
    video=models.FileField(upload_to='about_us')

class home_image(models.Model):
    supercategory=models.ForeignKey(SuperCategory,on_delete=models.PROTECT,related_name='home_image')
    image_desktop=models.ImageField(upload_to='home_image')
    image_mobile=models.ImageField(upload_to='home_image')

class homePageHeading(models.Model):
    heading=models.CharField(max_length=200)

class homePageHeadingImage(models.Model):
    homePageHeadingImage=models.ForeignKey(homePageHeading,on_delete=models.PROTECT,related_name='homePageHeadingImage')
    image=models.ImageField(upload_to='homepageheading')     


from django.template.defaultfilters import slugify
from categories.models import Categories



def content_file_name_video(instance, filename):
    return '/'.join(['subcategory', instance.subcategory, filename])

class SubCategories(models.Model):
    serial_number=models.IntegerField(null=True,blank=True)
    category = models.ManyToManyField(
        to=Categories,related_name='categories')
    subcategory = models.CharField(max_length=254)
    image = models.ImageField(upload_to='category')
    video = models.FileField(
        upload_to=content_file_name_video, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.subcategory)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.subcategory

class MetaTags(models.Model):
    categories = models.ForeignKey(Categories,on_delete=models.PROTECT, null=True, blank=True, default=None)
    subcategories = models.ForeignKey(SubCategories, on_delete=models.PROTECT, null=True, blank=True, default=None)
    meta_name = models.CharField(max_length=254)
    meta_description = models.TextField()

    def __str__(self):
        if type(self.categories) is type(None):
            return self.meta_name + ' | ' +self.subcategories.subcategory
        elif type(self.subcategories) is type(None):
            return self.meta_name + ' | ' +self.categories.category
        else:
            return self.meta_name + ' | ' +self.categories.category + ' | ' +self.subcategories.subcategory

class Aboutus(models.Model):
    title=models.CharField(max_length=200,null=True,blank=True)
    subtitle=models.TextField()
    subtitle_mobile=models.TextField()
    heading=models.TextField(null=True,blank=True)
    title2=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    video=models.FileField(upload_to='abous-us')
    image_logo_bottum=models.ImageField(upload_to='abous-us',null=True,blank=True)
    video_bottum=models.FileField(upload_to='abous-us',null=True,blank=True)
    youtube_title=models.CharField(max_length=100,null=True,blank=True)
    youtube_title_desc=models.TextField(null=True,blank=True)
    
class aboutusattribute(models.Model):
    aboutus=models.ForeignKey(Aboutus,on_delete=models.CASCADE,related_name='attribute')    
    title=models.CharField(max_length=100,null=True,blank=True)
    discription=models.TextField()
    def __str__(self):
        return self.title
    

class aboutusteam(models.Model):
    serial_number=models.IntegerField(null=True,blank=True)
    aboutus=models.ForeignKey(Aboutus,on_delete=models.CASCADE,related_name='teamImage')    
    image=models.ImageField(upload_to='teamphoto') 
    name=models.CharField(max_length=100,null=True,blank=True)
    designation=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name
    
class about_us_youtube(models.Model):
    serial_number=models.IntegerField(null=True,blank=True)
    about_us_youtube = models.ManyToManyField(
        to=Aboutus, related_name='about_us_youtube')
    title = models.CharField(max_length=50, null=True, blank=True)
    brief = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(
        upload_to='about_us_youtube', null=True, blank=True)
    video_link = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
class Interest_Person(models.Model):
    fullname=models.CharField(max_length=254,null=True,blank=True)
    email=models.CharField(max_length=254,null=True,blank=True)
    mobile=models.CharField(max_length=254,null=True,blank=True)
    requirement=models.CharField(max_length=254,null=True,blank=True)
    message=models.TextField()
    def __str__(self):
        return self.fullname

class Home_page_video(models.Model):
    video=models.FileField(upload_to='HomeVideo')        
    
    
class work(models.Model):
    video=models.FileField(null=True,blank=True,upload_to='our_work')
    heading1=models.CharField(max_length=50,null=True,blank=True )
    heading2=models.CharField(max_length=50,null=True,blank=True ) 
    image=models.FileField(null=True,blank=True,upload_to='work')
    image_mobile=models.FileField(null=True,blank=True,upload_to='work')
    
    
class work_youtube_video(models.Model): 
    serial_number=models.IntegerField(null=True,blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    brief = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(
        upload_to='work_videos', null=True, blank=True)
    video_link = models.CharField(max_length=100)    
    def __str__(self):
        return self.title
    
class create_video(models.Model):
    video=models.FileField(upload_to='create_video',null=True,blank=True)
    title=models.CharField(max_length=100, null=True, blank=True)
    subtitle=models.CharField(max_length=100, null=True, blank=True)
    
class create_video_image(models.Model):
    serial_number=models.IntegerField(null=True,blank=True)
    create_video=models.ForeignKey(create_video,on_delete=models.PROTECT,related_name='createvideoimage') 
    image=models.ImageField(upload_to='create_video_image') 
        
class contact_us_image(models.Model):
    serial_number=models.IntegerField(null=True,blank=True)
    create_video=models.ForeignKey(create_video,on_delete=models.PROTECT,related_name='contactusimage') 
    image=models.ImageField(upload_to='contact_us_image')    
    
class Image_client_logo_and_Vi(models.Model):
    image_client=models.ImageField(upload_to='Image_client_logo_and_Vi',null=True,blank=True) 
    image_VI=models.ImageField(upload_to='Image_client_logo_and_Vi',null=True,blank=True) 
    watch_our_more_work=models.ImageField(null=True,blank=True,upload_to='watch_our_more_work')
    watch_our_more_work_mobile=models.ImageField(null=True,blank=True,upload_to='watch_our_more_work')

class MarketPlaceVideo(models.Model):
    heading=models.CharField(max_length=100, null=True, blank=True)
    title_youtube1 = models.CharField(max_length=50, null=True, blank=True)
    brief_youtube1 = models.CharField(max_length=100, null=True, blank=True)
    image_youtube1 = models.ImageField(
        upload_to="marketplacevideoimage", null=True, blank=True)
    video_link_youtube1 = models.CharField(max_length=100,null=True,blank=True)
    title_youtube2 = models.CharField(max_length=50, null=True, blank=True)
    brief_youtube2 = models.CharField(max_length=100, null=True, blank=True)
    image_youtube2 = models.ImageField(
        upload_to="marketplacevideoimage", null=True, blank=True)
    video_link_youtube2 = models.CharField(max_length=100,null=True,blank=True)
    
    title_youtube3 = models.CharField(max_length=50, null=True, blank=True)
    brief_youtube3 = models.CharField(max_length=100, null=True, blank=True)
    image_youtube3 = models.ImageField(
        upload_to="marketplacevideoimage", null=True, blank=True)
    video_link_youtube3 = models.CharField(max_length=100,null=True,blank=True)    
    
    
class SuperCategoryVideo(models.Model):
    supercategory=models.ManyToManyField(SuperCategory,related_name='supercategory_video')
    heading=models.CharField(max_length=100, null=True, blank=True)
    title_youtube1 = models.CharField(max_length=50, null=True, blank=True)
    brief_youtube1 = models.CharField(max_length=100, null=True, blank=True)
    image_youtube1 = models.ImageField(
        upload_to="marketplacevideoimage", null=True, blank=True)
    video_link_youtube1 = models.CharField(max_length=100,null=True,blank=True)
    title_youtube2 = models.CharField(max_length=50, null=True, blank=True)
    brief_youtube2 = models.CharField(max_length=100, null=True, blank=True)
    image_youtube2 = models.ImageField(
        upload_to="marketplacevideoimage", null=True, blank=True)
    video_link_youtube2 = models.CharField(max_length=100,null=True,blank=True)
    
    title_youtube3 = models.CharField(max_length=50, null=True, blank=True)
    brief_youtube3 = models.CharField(max_length=100, null=True, blank=True)
    image_youtube3 = models.ImageField(
        upload_to="marketplacevideoimage", null=True, blank=True)
    video_link_youtube3 = models.CharField(max_length=100,null=True,blank=True)

class TermsAndCondition(models.Model):
    terms_and_condition_name = models.CharField(max_length=150)
    tems_and_condition = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.terms_and_condition_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.terms_and_condition_name
    
class contact_us_location(models.Model):
    heading =models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=254, null=True, blank=True)
    
    
class creators(models.Model):
    image1=models.ImageField(upload_to='creators', null=True, blank=True)
    textcard1=models.TextField( null=True, blank=True)
    textcard2_heading=models.CharField(max_length=254, null=True, blank=True)
    textcard2=models.TextField( null=True, blank=True)
    textcard3_heading_black=models.CharField(max_length=254, null=True, blank=True)
    textcard3_heading_blue=models.CharField(max_length=254, null=True, blank=True)
    textcard3=models.TextField( null=True, blank=True)
    video1=models.FileField( upload_to='creators', null=True, blank=True)
    heading_black=models.CharField(max_length=254, null=True, blank=True)
    heading_blue=models.CharField(max_length=254, null=True, blank=True)
    description=models.TextField( null=True, blank=True)
    video_image2=models.ImageField(upload_to='creators', null=True, blank=True)
    video_image3=models.ImageField(upload_to='creators', null=True, blank=True)
    video_image4=models.ImageField(upload_to='creators', null=True, blank=True)
    video_image5=models.ImageField(upload_to='creators', null=True, blank=True)
    video_image6=models.ImageField(upload_to='creators', null=True, blank=True)
    video_image7=models.ImageField(upload_to='creators', null=True, blank=True)
    image_logo_bottum=ImageField(upload_to='creators', null=True, blank=True)
    video_bottum=models.FileField( upload_to='creators', null=True, blank=True)

     
     
     
class Customer(models.Model):     
    brand_name=models.CharField(max_length=254,null=True,blank=True)
    website=models.CharField(max_length=254,null=True,blank=True)
    first_name=models.CharField(max_length=254,null=True,blank=True)
    last_name=models.CharField(max_length=254,null=True,blank=True)
    email=models.CharField(max_length=254,null=True,blank=True)
    phone=models.CharField(max_length=254,null=True,blank=True)
    video_categories=models.CharField(max_length=254,null=True,blank=True)
    other_project_details=models.CharField(max_length=254,null=True,blank=True)
    project_description=models.TextField()
    project_country=models.CharField(max_length=254,null=True,blank=True)
    project_city_state=models.CharField(max_length=254,null=True,blank=True)
    project_pincode=models.CharField(max_length=254,null=True,blank=True)
    delivery_speed=models.CharField(max_length=254,null=True,blank=True)
    project_budget=models.CharField(max_length=254,null=True,blank=True)
    reference_link=models.TextField()
    def __str__(self):
        return str(self.first_name)+str(self.last_name)