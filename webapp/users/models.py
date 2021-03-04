from django.db import models
from django.db.models import Count
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# from datetimeutc.fields import DateTimeUTCField

class House(models.Model):
    title = models.CharField(max_length=100) 
    content = models.TextField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

import os
from uuid import uuid4

from django.utils.deconstruct import deconstructible

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

path_and_rename = PathAndRename("images/")

# def path_and_rename(path):
#     def wrapper(instance, filename):
#         ext = filename.split('.')[-1]
#         filename = '{}.{}'.format(uuid4().hex, ext)
#         return os.path.join(path, filename)
#     return wrapper


class RealtorImages(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to=path_and_rename, null=True)
    cover = models.ImageField(upload_to=path_and_rename, null=True)

class Features(models.Model):
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description



class Condition(models.Model):
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description

class Services(models.Model):
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description

class Special(models.Model):
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description

class Languages(models.Model):
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description

class TypeBuilding(models.Model):
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description

class Cities(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class RealtorQualities(models.Model):
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description

class Realtor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(null=True,blank=True, max_length=60) 
    work_phone = models.CharField(null=True,blank=True, max_length=30)
    cell_phone = models.CharField(null=True,blank=True, max_length=30)
    about_me = models.CharField(null=True,blank=True, max_length=500)
    why_work = models.CharField(null=True,blank=True, max_length=500)
    services = models.ManyToManyField(Services)
    cities = models.ManyToManyField(Cities)
    special = models.ManyToManyField(Special)
    languages = models.ManyToManyField(Languages)
    building_types = models.ManyToManyField(TypeBuilding)
    website = models.CharField(null=True,blank=True, max_length=60)
    strip_id = models.CharField(null=True, max_length=100)
    subscription_id = models.CharField(null=True,blank=True, max_length=100)

    def __str__(self):
        return self.user.username


class LocationBuying(models.Model):
    city = models.TextField(null=True, max_length=250)
    neighborhood = models.TextField(null=True, max_length=250)
    postal_code = models.TextField(null=True, max_length=250)
    province = models.TextField(null=True, max_length=250)
    country = models.TextField(null=True, max_length=250)

class OpportunitieBuying(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    location = models.ForeignKey(LocationBuying, on_delete=models.CASCADE, null=True)
    neighbourhood = models.TextField(null=True, max_length=500)
    bedrooms = models.FloatField(null=True)
    bathrooms = models.FloatField(null=True)
    budget = models.TextField(null=True, max_length=250)
    sq_ft = models.TextField(null=True, max_length=250)
    looking_for = models.TextField(null=True, max_length=500)
    features = models.ManyToManyField(Features)
    notes_to_agent = models.TextField(null=True, max_length=250)
    notes_about = models.TextField(null=True, max_length=250)
    condition = models.ManyToManyField(Condition)
    insite1 = models.TextField(null=True, max_length=500)
    insite2 = models.TextField(null=True, max_length=500)
    insite3 = models.TextField(null=True, max_length=500)
    insite4 = models.TextField(null=True, max_length=500)
    phone = models.CharField(max_length=15, null=True)
    urgency = models.IntegerField(null=True)
    realtorqualities = models.ManyToManyField(RealtorQualities)
    investment = models.BooleanField(null=True)
    
    created_date = models.DateTimeField('created date', default=datetime.now)
    created_date = models.DateTimeField('updated date', default=datetime.now)



class LocationSelling(models.Model):
    street_number = models.TextField(null=True, max_length=50)
    route = models.TextField(null=True, max_length=50)
    city = models.TextField(null=True, max_length=250)
    neighborhood = models.TextField(null=True, max_length=250)
    postal_code = models.TextField(null=True, max_length=250)
    province = models.TextField(null=True, max_length=250)
    country = models.TextField(null=True, max_length=250)

class OpportunitieSelling(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    bedrooms = models.FloatField(null=True)
    bathrooms = models.FloatField(null=True)
    sq_ft = models.TextField(null=True, max_length=250)
    building_types = models.ManyToManyField(TypeBuilding)
    year_built = models.IntegerField(null=True)
    asking_price = models.IntegerField(null=True)
    unique_value = models.TextField(null=True, max_length=500)
    details = models.TextField(null=True,max_length=500)
    love = models.TextField(null=True,max_length=500)
    features = models.ManyToManyField(Features)
    realtorqualities = models.ManyToManyField(RealtorQualities)
    notes_to_agent = models.TextField(null=True, max_length=250)
    urgency = models.IntegerField(null=True)
    phone = models.CharField(max_length=15, null=True)
    location = models.ForeignKey(LocationSelling, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField('created date', default=datetime.now)


class Proposals(models.Model):
    agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    subject = models.TextField(max_length=120, null=True)
    about_me = models.TextField(max_length=500, null=True)
    reasons = models.TextField(max_length=500,null=True)
    services = models.ManyToManyField(Services)
    #optional services
    fee = models.TextField(max_length=500,null=True)
    note = models.TextField(max_length=500,null=True)
    buying = models.ForeignKey(OpportunitieBuying, null=True, on_delete=models.CASCADE)
    selling = models.ForeignKey(OpportunitieSelling, null=True, on_delete=models.CASCADE)
    accepted_user = models.BooleanField(default=False)
    accepted_agent = models.BooleanField(default=False)
    created_date = models.DateTimeField('created date', default=datetime.now)

    
    #def __str__(self):
    #    return self.subject

class PostingImageBuying(models.Model):
    posting = models.ForeignKey(OpportunitieBuying, on_delete=models.CASCADE)
    #image = models.ImageField(upload_to=path_and_rename('images/'), null=True)
    image = models.ImageField(upload_to=path_and_rename, null=True)

class PostingImageSelling(models.Model):
    posting = models.ForeignKey(OpportunitieSelling, on_delete=models.CASCADE)
    #image = models.ImageField(upload_to='images/', null=True)
    image = models.ImageField(upload_to=path_and_rename, null=True)

class BlogPost(models.Model):
    #image = models.ImageField(upload_to='images/', null=True)
    #models.IdmageField(upload_to=path_and_rename('images/'), null=True)
    image = models.ImageField(upload_to=path_and_rename, null=True)
    title = models.TextField(max_length=500,null=True)
    post = HTMLField(max_length=10000, null=True)
    created_date = models.DateTimeField('created date', default=datetime.now)

    def __str__(self):
        return self.title

TYPE_CHOICES = (
                ('Paid Realtor', 'Paid Realtor'),
                ('Unpaid Realtor', 'Unpaid Realtor'),
                ('Seller','Seller'),
                ('Buyer', 'Buyer'),
                )

class Heading(models.Model):
    # user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='UserName')
    user_name = models.CharField(max_length=200, blank=True, null=True)
    # first_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='FirstName')
    first_name = models.CharField(max_length=200, blank=True, null=True)
    # last_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='LastName')
    last_name = models.CharField(max_length=200, blank=True, null=True)
    # email = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Email')
    email = models.CharField(max_length=200, blank=True, null=True)
    # company_name = models.ForeignKey(Realtor, on_delete=models.CASCADE, related_name='CompanyName')
    company_name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, choices=TYPE_CHOICES, default='Buyer', blank=True, null=True)
    # date_joined = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='DateJoined')
    # for sqlite3
    date_joined = models.DateTimeField('datejoined', default=datetime.now, blank=True, null=True)
    # for postgresql
    # date_joined = models.DateTimeField('datejoined', default=datetime.now)
    #date_membership = leave it for now
    # city = models.ForeignKey(Realtor, on_delete=models.CASCADE, related_name='City')
    city = models.CharField(max_length=200, blank=True, null=True)
    active_posting = models.IntegerField(blank=True, null=True)
    #successful_postings = leave it for now
    #expired_postings = leave it for now
    proposals_made = models.IntegerField(blank=True, null=True)
    proposals_recd = models.IntegerField(blank=True, null=True)
    accepted_proposals = models.IntegerField(blank=True, null=True)
    #active_proposals = leave it for now
    # for sqlite3
    last_login = models.DateTimeField('lastlogin', default=datetime.now, blank=True, null=True)
    # for postgresql
    # last_login = models.DateTimeField('lastlogin', default=datetime.now)
    #chats_engaged = leave it for now
    def __str__(self):
        return self.user_name

class GeoLocation(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    feature_class = models.CharField(max_length=200, blank=True, null=True)
    feature_code = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    admin1_code = models.IntegerField(blank=True, null=True)
    admin2_code = models.IntegerField(blank=True, null=True)
    admin3_code = models.IntegerField(blank=True, null=True)
    admin4_code = models.IntegerField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    timezone = models.CharField(max_length=200, blank=True, null=True)
    # last_modified_date = models.DateTimeField('lastmodificationdate', blank=True, null=True)
    last_modified_date = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name

