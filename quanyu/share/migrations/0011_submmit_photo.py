# Generated by Django 2.2.3 on 2019-08-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0010_auto_20190816_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='submmit',
            name='photo',
            field=models.TextField(blank=True, null=True, verbose_name='图片base64'),
        ),
    ]
