from django.contrib import admin


from .models import NpmPackage,NpmPackageDependecy

class NpmPackageAdmin(admin.ModelAdmin):
    list_display = ('npm_name', 'version', 'updated_at')

admin.site.register(NpmPackage, NpmPackageAdmin)


class NpmPackageDependecyAdmin(admin.ModelAdmin):
    list_display = ('npm_package_dep_name','npm_package', 'version', 'updated_at')

admin.site.register(NpmPackageDependecy, NpmPackageDependecyAdmin)
