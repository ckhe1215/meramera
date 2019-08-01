# Generated by Django 2.2.3 on 2019-07-24 06:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
                ('rent_date', models.DateTimeField(verbose_name='rent date')),
                ('price', models.PositiveIntegerField()),
                ('choice_parcel', models.BooleanField()),
                ('use', models.TextField()),
                ('region_sido', models.CharField(max_length=10)),
                ('region_sigungu', models.CharField(max_length=10)),
                ('sort', models.CharField(max_length=10)),
            ],
        ),
    ]
