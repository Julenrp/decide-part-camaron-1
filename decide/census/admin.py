from django.contrib import admin

from .models import Census


class CensusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name', )

    search_fields = ('name', )


admin.site.register(Census, CensusAdmin)
