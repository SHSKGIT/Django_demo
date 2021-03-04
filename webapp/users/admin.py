from django.contrib import admin
from .models import House, OpportunitieBuying, OpportunitieSelling, Proposals, LocationBuying, Features, Condition, RealtorQualities, Realtor, Services, Languages, TypeBuilding, Cities, Special, RealtorImages, PostingImageBuying, BlogPost, Heading, GeoLocation

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

UserAdmin.list_display = ('username',
                          'email',
                          'first_name',
                          'last_name',
                          'is_active',
                          'date_joined',
                          )

class HeadingAdmin(admin.ModelAdmin):
#    def save_model(self, request, obj, form, change):
#        obj.date_joined = obj.date_joined.replace(tzinfo=tz.gettz(settings.TIME_ZONE))
#        obj.last_login = obj.last_login.replace(tzinfo=tz.gettz(settings.TIME_ZONE))
#        super(HeadingAdmin, self).save_model(request, obj, form, change)
    list_display = ('user_name',
                    'first_name',
                    'last_name',
                    'email',
                    'company_name',
                    'role',
                    'date_joined',
                    'city',
                    'active_posting',
                    'proposals_made',
                    'proposals_recd',
                    'accepted_proposals',
                    'last_login',
                    )
    list_filter = ('date_joined',
                   'last_login',
                   )

class GeoLocationAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'latitude',
                    'longitude',
                    'feature_class',
                    'feature_code',
                    'country',
                    # admin can't parse special charaters, so just comment the below
#                    'admin1_code',
#                    'admin2_code',
#                    'admin3_code',
#                    'admin4_code',
                    'population',
                    'timezone',
                    'last_modified_date',
                    )
    list_filter = ('last_modified_date',
                   )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(House)
admin.site.register(OpportunitieBuying)
admin.site.register(OpportunitieSelling)
admin.site.register(Proposals)
admin.site.register(LocationBuying)
admin.site.register(Features)
admin.site.register(Condition)
admin.site.register(RealtorQualities)
admin.site.register(Realtor)
admin.site.register(Services)
admin.site.register(Languages)
admin.site.register(TypeBuilding)
admin.site.register(Cities)
admin.site.register(Special)
admin.site.register(RealtorImages)
admin.site.register(PostingImageBuying)
admin.site.register(BlogPost)

admin.site.register(Heading, HeadingAdmin)
admin.site.register(GeoLocation, GeoLocationAdmin)

