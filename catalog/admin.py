from django.contrib import admin
from .models import Teacher,Subject,Literature,Takyryp,Zert_jumys,Keste
# Register your models here.



admin.site.register(Takyryp)
admin.site.register(Literature)
admin.site.register(Teacher)
admin.site.register(Zert_jumys)
admin.site.register(Keste)

@admin.register(Subject)
class BookAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'credit', 'display_takyryp','display_literature')