# Generated by Django 3.2.5 on 2021-08-31 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages__app', '0002_npmsecuritypackagedeatails'),
    ]

    operations = [
        migrations.AddField(
            model_name='npmsecuritypackagedeatails',
            name='num_critical_severity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
