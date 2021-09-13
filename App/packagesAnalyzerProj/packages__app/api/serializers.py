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

    npm_package = serializers.SlugRelatedField(
        
        read_only=True,
        slug_field='npm_name'
    )
    return_version_npm = serializers.ReadOnlyField()

    
    class Meta:
        model = NpmSecurityPackageDeatails
        #fields = '__all__'
        fields = ('id', 'return_version_npm', 'npm_package','number_of_maintainers', 'unpackedsize','license','updated_at','is_exploite','num_high_severity',
        'num_moderate_severity','num_low_severity','num_info_severity','num_critical_severity')