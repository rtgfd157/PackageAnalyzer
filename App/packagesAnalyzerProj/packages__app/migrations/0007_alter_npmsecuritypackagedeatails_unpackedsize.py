# Generated by Django 3.2.5 on 2021-09-09 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages__app', '0006_npmproblemcallapi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='npmsecuritypackagedeatails',
            name='unpackedsize',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
