# Generated by Django 5.0.1 on 2024-01-29 00:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cabin_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('capacity', models.IntegerField(max_length=10)),
                ('description', models.CharField(max_length=300)),
                ('value', models.FloatField()),
                ('image', models.ImageField(null=True, upload_to='static/service_images')),
                ('status', models.BooleanField(default=True)),
                ('cabin_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cabin_types.cabin_type')),
            ],
        ),
    ]
