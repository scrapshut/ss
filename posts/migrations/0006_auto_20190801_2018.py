# Generated by Django 2.2.2 on 2019-08-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
    ]
