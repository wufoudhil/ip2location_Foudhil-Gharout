# Generated by Django 4.0.6 on 2022-08-26 23:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access', models.DateTimeField(default=django.utils.timezone.now)),
                ('ip', models.CharField(max_length=15)),
                ('country_short', models.CharField(max_length=3)),
                ('country_long', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('coordinates', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=15)),
                ('timezone', models.CharField(max_length=15)),
            ],
        ),
    ]