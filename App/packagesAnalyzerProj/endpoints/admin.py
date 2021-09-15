from django.contrib import admin

# Register your models here.



from .models import MLAlgorithm, MLAlgorithmStatus

class MLAlgorithmAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'parent_endpoint')
    search_fields = ['name', 'version', 'parent_endpoint', ]

admin.site.register(MLAlgorithm, MLAlgorithmAdmin)


class MLAlgorithmStatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'active', 'created_by', 'parent_mlalgorithm',)
    search_fields = ['status', 'active', 'created_by', 'parent_mlalgorithm', ]

admin.site.register(MLAlgorithmStatus, MLAlgorithmStatusAdmin)