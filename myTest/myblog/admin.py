from django.contrib import admin
from myblog.models import Siteinfo,Classes,Userinfo

# Register your models here.
admin.site.register(Siteinfo)
admin.site.register(Classes)
admin.site.register(Userinfo)
