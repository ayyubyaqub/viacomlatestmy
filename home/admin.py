from django.contrib import admin
from categories.models import Categories, CategoriesVideo, SuperCategory, YoutubeVideoLinks
from clients.models import ClientVideos, Clients
from subscription.models import Subscription
from .models import MetaTags, TermsAndCondition, work
from home.models import Homecarousel,Videoseeding,Videocategory,home_image,homePageHeading,homePageHeadingImage,SubCategories,Aboutus,aboutusteam,aboutusattribute,Home_page_video,about_us_youtube,work_youtube_video,create_video,create_video_image,Image_client_logo_and_Vi,MarketPlaceVideo,Customer,SuperCategoryVideo,contact_us_location,Interest_Person,creators
# Register your models here.

admin.site.register(SuperCategoryVideo)

admin.site.register(YoutubeVideoLinks)
admin.site.register(CategoriesVideo)

admin.site.register(Subscription)
admin.site.register(Clients)
admin.site.register(ClientVideos)
admin.site.register(Homecarousel)
admin.site.register(Videoseeding)
admin.site.register(Videocategory)
admin.site.register(home_image)
admin.site.register(homePageHeading)
admin.site.register(homePageHeadingImage)

admin.site.register(Aboutus)
admin.site.register(aboutusteam)
admin.site.register(aboutusattribute)
admin.site.register(Home_page_video)
admin.site.register(work)          
admin.site.register(about_us_youtube)
admin.site.register(work_youtube_video)
admin.site.register(create_video)
admin.site.register(create_video_image)
admin.site.register(Image_client_logo_and_Vi)
admin.site.register(MarketPlaceVideo)
admin.site.register(TermsAndCondition)
admin.site.register(contact_us_location)
admin.site.register(Interest_Person)
admin.site.register(creators)
admin.site.register(Customer)

@admin.register(MetaTags)
class MetaTagsAdmin(admin.ModelAdmin):
    search_fields = ('meta_name','categories', 'subcategories','meta_description')
    list_display = ('meta_name','categories', 'subcategories')

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ('category','slug', 'price','brief')
    list_display = ('category','slug', 'price','brief')

@admin.register(SuperCategory)
class SuperCategoryAdmin(admin.ModelAdmin):
    search_fields = ('super_category_name','slug', 'description')
    list_display = ('super_category_name','slug', 'description')

@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    search_fields = ('subcategory','slug')
    list_display = ('subcategory','slug', 'is_active')