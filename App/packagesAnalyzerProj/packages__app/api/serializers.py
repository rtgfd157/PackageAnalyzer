from rest_framework import serializers
from packages__app.models import NpmPackage, NpmPackageDependecy, NpmSecurityPackageDeatails

class NpmPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NpmPackage
        fields = ('id', 'npm_name', 'version', 'updated_at')


class NpmPackageDependecySerializer(serializers.ModelSerializer):
    class Meta:
        model = NpmPackageDependecy
        fields = ('id', 'npm_package', 'npm_package_dep_name','version', 'updated_at')

class NpmSecurityPackageDeatailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NpmSecurityPackageDeatails
        fields = '__all__'