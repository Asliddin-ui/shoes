# Generated by Django 4.2.3 on 2023-08-04 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_pagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
