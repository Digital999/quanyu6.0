# Generated by Django 2.2.3 on 2019-08-16 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0007_auto_20190816_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_pic', models.ImageField(upload_to='booktest/')),
            ],
        ),
    ]
