# Generated by Django 4.1 on 2023-11-14 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0004_census_has_voted'),
        ('voting', '0004_alter_voting_postproc_alter_voting_tally'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='census',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='census.census'),
        ),
    ]