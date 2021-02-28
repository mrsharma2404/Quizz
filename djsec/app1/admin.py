from django.contrib import admin

# Register your models here.
from app1.models import *

# Register your models here.


class actadmin1(admin.ModelAdmin):
    search_fields = ('stream','level')


admin.site.register(quizmodel2, actadmin1)
admin.site.register(quizcatogery)
admin.site.register(faculty)


