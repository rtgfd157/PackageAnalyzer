# Generated by Django 3.2.5 on 2021-09-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages__app', '0009_alter_npmsecuritypackagedeatails_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='npmsecuritypackagedeatails',
            name='license',
            field=models.CharField(blank=True, default='', max_length=36, null=True),
        ),
    ]
