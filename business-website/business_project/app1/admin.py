from django.contrib import admin
from app1.models import Contact
from app1.models import GetQuote
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message','created_at')
admin.site.register(Contact,StudentAdmin)

class GetQuoteAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','service','details','created_at')
admin.site.register(GetQuote,GetQuoteAdmin)