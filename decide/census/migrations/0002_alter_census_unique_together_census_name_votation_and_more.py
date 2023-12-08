# Generated by Django 4.1 on 2023-11-14 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20180921_1119'),
        ('census', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='census',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='census',
            name='name',
            field=models.CharField(default='Standard', max_length=200),
        ),
        migrations.CreateModel(
            name='Votation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('census', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='census.census')),
            ],
        ),
        migrations.CreateModel(
            name='Foe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.auth')),
                ('census', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='census.census')),
            ],
        ),
        migrations.RemoveField(
            model_name='census',
            name='voter_id',
        ),
        migrations.RemoveField(
            model_name='census',
            name='voting_id',
        ),
    ]