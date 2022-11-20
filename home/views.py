import json
import requests
from django.db.models import Q
from urllib import request
from django.http import Http404, HttpResponseNotAllowed, JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from categories.models import Categories, SuperCategory, YoutubeVideoLinks
from django.core.mail import send_mail
# models imported here
from django.contrib import messages
from django.core.mail import EmailMessage
from clients.models import Clients
from home.models import Homecarousel, MetaTags, SubCategories, TermsAndCondition, homePageHeading, Aboutus, Interest_Person, Home_page_video, work, aboutusteam, work_youtube_video, create_video, Image_client_logo_and_Vi, MarketPlaceVideo, contact_us_location, creators,Customer
# Create your views here.
MailID = 'viacomindia1@gmail.com'


def verifyHcaptchaToken(request):
    if request.method == "POST":
        SECRET_KEY = '0x27755d798822aB5939DAD45Dd32F4BB5bAe4462E'
        VERIFY_URL = 'https://hcaptcha.com/siteverify'

        token = request.POST.get('h-captcha-response')

        data = {'secret': SECRET_KEY, 'response': token}

        response = requests.post(url=VERIFY_URL, data=data)
        if response.json()['success']:
            return HttpResponse('SUCCESS')
        else:
            return HttpResponse('FAILED')
    else:
        return HttpResponseNotAllowed


def index(request):
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    clients = Clients.objects.all()[:10]
    super_categories = SuperCategory.objects.order_by('serial_number')
    homecarousel = Homecarousel.objects.all()
    homepageheading = homePageHeading.objects.all()
    homevideo = Home_page_video.objects.first()

    params = {
        'meta_title': 'Viacom India',
        'meta_description': "India’s Preferred Content Production Services",
        'clients': clients,
        'super_categories': super_categories,
        'carousels': homecarousel,
        'homepageheading': homepageheading,
        'homevideo': homevideo,
        'imageclientand_vi': imageclientand_vi,
    }
    return render(request, 'components/home.html', params)


def category(request, slug):
    supercategory = SuperCategory.objects.filter(slug=slug).first()
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    if supercategory:
        supercategory = SuperCategory.objects.get(slug=slug)
        params = {
            'meta_title': supercategory.super_category_name,
            'meta_description': supercategory.description,
            'supercategory': supercategory,
            'imageclientand_vi': imageclientand_vi
        }
        return render(request, 'components/allcategories.html', params)
    category = Categories.objects.filter(slug=slug).first()

    if category:
        supercategory = SuperCategory.objects.filter(sp__slug=slug).first()
        metas = MetaTags.objects.filter(categories=category)
        params = {
            'metas':metas,
            'meta_title': category.category,
            'meta_description': category.brief,
            'category': category,
            'supercategory': supercategory,
            'imageclientand_vi': imageclientand_vi,
        }
        return render(request, 'components/homecategory.html', params)
    subcategory = SubCategories.objects.filter(slug=slug).first()
    if subcategory:
        category = Categories.objects.filter(categories__slug=slug).first()
        supercategory = SuperCategory.objects.filter(
            sp__categories__slug=slug).first()
        metas = MetaTags.objects.filter(subcategories=subcategory)
        params = {
            'metas':metas,
            'meta_title': subcategory.subcategory,
            'meta_description': category.brief,
            'subcategory': subcategory,
            'category': category,
            'imageclientand_vi': imageclientand_vi,
            'supercategory': supercategory
        }
        return render(request, 'components/subcategory.html', params)
    return redirect('/')


def categories(request):
    if request.GET.get('query') == 'get_searched_query':
        search = request.GET.get('search')
        categories = list(SubCategories.objects.filter(
            Q(category__category__icontains=search) | Q(subcategory__icontains=search)).values())
            
        return JsonResponse(categories, safe=False)
    supercategories = SuperCategory.objects.exclude(
        slug='explore-our-most-popular-trending-video-content-types').order_by('serial_number')
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    params = {
        'meta_title': 'All categories',
        'meta_description': 'India’s Preferred Content Production Services',
        'supercategories': supercategories,
        'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/categories.html', params)


def create_videos(request):
    if request.method == 'POST':
        brand_name = request.POST.get('brand_name')
        website = request.POST.get('website')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        video_categories = request.POST.get('video_categories')
        other_project_details = request.POST.get('other_project_details')
        project_description = request.POST.get('project_description')
        project_country = request.POST.get('project_country')
        project_city_state = request.POST.get('project_city_state')
        project_pincode = request.POST.get('project_pincode')
        delivery_speed = request.POST.get('delivery_speed')
        project_budget = request.POST.get('project_budget')
        reference_link = request.POST.get('reference_link[]')
        Customer.objects.create(brand_name=brand_name, website=website, first_name=first_name, last_name=last_name, email=email, phone=phone, video_categories=video_categories, other_project_details=other_project_details,
                                project_description=project_description, project_country=project_country, project_city_state=project_city_state, project_pincode=project_pincode, delivery_speed=delivery_speed, project_budget=project_budget, reference_link=reference_link)
        send_mail(
            "A customer booked our service",
            str(brand_name) + str(website) + str(first_name) + str(last_name) + str(email) + str(phone) + str(video_categories) + str(other_project_details) +
            str(project_description) + str(project_country) + str(project_city_state) +
            str(project_pincode) + str(delivery_speed) +
            str(project_budget) + str(reference_link),
            MailID,
            ['viacomindiavideo@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Message has been sent successfully!')
    obj = create_video.objects.all().first()
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    params = {
        'meta_title': 'Create videos',
        'meta_description': 'Create videos',
        'create_video': obj,
        'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/createvideo.html', params)


def about(request):
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    aboutus = Aboutus.objects.all().first()
    Aboutusteam = aboutusteam.objects.order_by('serial_number')
    params = {
        'meta_title': 'About us',
        'meta_description': 'India’s Preferred Content Production Services',
        'aboutus': aboutus,
        'Aboutusteam': Aboutusteam,
        'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/about.html', params)


def contactus(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        mobile = request.POST.get('phone')
        requirement = request.POST.get('website')
        message = request.POST.get('description')
        Interest_Person.objects.create(fullname=fullname, email=email, mobile=mobile, requirement=requirement, message=message)
        email = EmailMessage(
             "A customer contacted us",
            'Name :'+str(fullname) + '\nEmail :'+str(email)+'\nMobile :' + str(mobile) +
            '\nRequirement :' + str(requirement)+'\nMessage :' + str(message),
            MailID,
            ['viacomindiavideo@gmail.com'],
            ['prasad.hunny03@gmail.com'],
         
        )
        email.send(fail_silently=False)
        
        messages.success(request, 'Message has been sent successfully!')
    Contact_us_location = contact_us_location.objects.all()
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    params = {
        'meta_title': "Contact us",
        'meta_description': "Contact viacom india",
        'contact_us_location': Contact_us_location,
        'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/contactus.html', params)


def works(request):
    our_woks = work.objects.all().first()
    videolinks = work_youtube_video.objects.order_by('serial_number')
    carousel = Homecarousel.objects.all()
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    params = {
        'meta_title': "Our works",
        'meta_description': "Viacom india works",
        'carousels': carousel,
        'our_woks': our_woks,
        'videolinks': videolinks,
        'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/work.html', params)


def marketplace(request):
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    marketplace = MarketPlaceVideo.objects.all().first()
    supercategory = SuperCategory.objects.filter(
        super_category_name='Curated Video Marketplace').first()
    params = {
        'meta_title': supercategory.super_category_name,
        'meta_description': supercategory.description,
        'supercategory': supercategory,
        'marketplace': marketplace, 'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/marketplace.html', params)


def industry(request):
    supercategory = SuperCategory.objects.filter(
        Q(slug__icontains='industry')).all()

    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()

    params = {
        'meta_title': "Industry",
        'meta_description': "Industry presented by viacom india",
        'supercategories': supercategory,
        'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/industry.html', params)


def subscription(request):
    supercategory = SuperCategory.objects.filter(slug='subscription').first()
    param = {
        'meta_title': supercategory.super_category_name,
        'meta_description': supercategory.description,
        'supercategory': supercategory
    }
    return render(request, 'components/subscription.html', param)


def allTermsAndCondition(request):
    terms_and_condition = TermsAndCondition.objects.all()
    params = {
        'meta_title': "Terms and conditions",
        'meta_description': "Viacom india terms and conditions",
        "terms_and_condition": terms_and_condition
    }
    return render(request, 'components/all-terms-and-conditions.html', params)


def termsAndCondition(request, slug):
    terms_and_condition = TermsAndCondition.objects.get(Q(slug=slug))
    params = {
        'meta_title': terms_and_condition.terms_and_condition_name,
        'meta_description': "Viacom india terms and conditions",
        "terms_and_condition": terms_and_condition
    }
    return render(request, "components/terms-and-condition.html", params)


def pricing(request):
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    params = {
        'meta_title': "Pricing",
        'meta_description': "Viacom india terms and conditions",
        'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/pricing.html', params)


def creator(request):
    creator = creators.objects.all().first()
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    params = {
        'meta_title': "Creators",
        'meta_description': "Viacom india creators",
        'creator': creator,
        'imageclientand_vi': imageclientand_vi,
    }
    return render(request, 'components/creators.html', params)
