from django.contrib import admin

from newbankapp.models import district, dist_branch

# Register your models here.
admin.site.register(district)
admin.site.register(dist_branch)