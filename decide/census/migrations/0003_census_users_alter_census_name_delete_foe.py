# Generated by Django 4.1 on 2023-11-14 19:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('census', '0002_alter_census_unique_together_census_name_votation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='census',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='census',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Foe',
        ),
    ]