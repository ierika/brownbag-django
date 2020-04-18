# Generated by Django 3.0.5 on 2020-04-14 16:46

import brownbags.models
import brownbags.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brownbags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedata',
            name='image_data',
            field=models.ImageField(blank=True, default='/static/brownbags/images/noimage.png', null=True, upload_to=brownbags.models.get_image_path, validators=[brownbags.validators.validate_file_extension], verbose_name='画像'),
        ),
    ]