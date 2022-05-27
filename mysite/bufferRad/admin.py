from django.contrib import admin

# Register your models here.

from .models import UserRadius


# class UserRadiusAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('field description1', {'fields': ['uRadius_text',]},),
#         ('field description2', {'fields': 'pub_date', 'classes': ['collapse',]}),
#         ]
    
#     list_display = ('uRadius_text', 'pub_date')
#     list_filter = ['pub_date']
#     search_fields = ['uRadius_text']


admin.site.register(UserRadius)

# superuser username: kuuku pswd: quainoo1!
# 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
