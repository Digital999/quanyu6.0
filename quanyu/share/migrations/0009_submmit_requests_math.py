# Generated by Django 2.2.3 on 2019-08-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0008_pictest'),
    ]

    operations = [
        migrations.AddField(
            model_name='submmit',
            name='requests_math',
            field=models.IntegerField(null=True, verbose_name='访问量'),
        ),
    ]