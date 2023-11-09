from django.contrib import admin
from .models import Avto

admin.site.register(Avto)
admin.site.site_header = 'MySite Administration'
admin.site.index_title = 'MySite Site administration'
admin.site.site_title = 'MySite site admin'