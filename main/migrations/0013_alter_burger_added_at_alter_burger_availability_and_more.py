# Generated by Django 4.2.3 on 2023-08-04 09:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_burger_added_at_alter_burger_availability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burger',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='burger',
            name='availability',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='burger',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.category', verbose_name='kategoriya'),
        ),
        migrations.AlterField(
            model_name='burger',
            name='description_en',
            field=models.TextField(verbose_name="Ma'lumot en"),
        ),
        migrations.AlterField(
            model_name='burger',
            name='description_ru',
            field=models.TextField(verbose_name="Ma'lumot ru"),
        ),
        migrations.AlterField(
            model_name='burger',
            name='description_uz',
            field=models.TextField(verbose_name="Ma'lumot uz"),
        ),
        migrations.AlterField(
            model_name='burger',
            name='name_en',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='burger',
            name='name_ru',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='burger',
            name='name_uz',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='burger',
            name='photo',
            field=models.ImageField(upload_to='burgers/'),
        ),
        migrations.AlterField(
            model_name='burger',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(1000)], verbose_name='Narxi'),
        ),
        migrations.AlterField(
            model_name='burger',
            name='rating_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='burger',
            name='rating_stars',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='burger',
            name='show_in_swiper',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='burger',
            name='status',
            field=models.IntegerField(choices=[(0, 'YANGI'), (1, 'QABUL QILINGAN'), (2, 'INKOR QILINGAN')], verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='burger',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
