# Generated by Django 3.1.3 on 2024-02-05 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabins', '0003_alter_cabin_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabin',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
