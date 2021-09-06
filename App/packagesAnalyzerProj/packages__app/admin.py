from django.contrib import admin


from .models import NpmPackage,NpmPackageDependecy, NpmProblemCallApi, NpmSecurityPackageDeatails

class NpmPackageAdmin(admin.ModelAdmin):
    list_display = ('npm_name', 'version', 'updated_at')
    search_fields = ['npm_name', 'version', ]

admin.site.register(NpmPackage, NpmPackageAdmin)


class NpmPackageDependecyAdmin(admin.ModelAdmin):
    list_display = ('npm_package_dep_name','npm_package', 'version', 'updated_at')
    search_fields = ['npm_package_dep_name', 'npm_package', ]

admin.site.register(NpmPackageDependecy, NpmPackageDependecyAdmin)


class NpmProblemCallApiAdmin(admin.ModelAdmin):
    list_display = ('npm_package_name_problem','version_problem')
    search_fields = ['npm_package_name_problem', 'version_problem', ]

admin.site.register(NpmProblemCallApi, NpmProblemCallApiAdmin)


class NpmSecurityPackageDeatailsAdmin(admin.ModelAdmin):
    list_display = ('npm_package','is_exploite')
    search_fields = ['npm_package','is_exploite', ]

admin.site.register(NpmSecurityPackageDeatails, NpmSecurityPackageDeatailsAdmin)
