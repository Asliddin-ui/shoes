import datetime
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify
from .decorators import i18n
from django_quill.fields import QuillField


@i18n
class Category(models.Model):
    parent = models.ForeignKey("Category", on_delete=models.CASCADE, default=None, blank=True, null=True, verbose_name='Ota kategoriya')
    name_uz = models.CharField(max_length=255, default=None)
    name_ru = models.CharField(max_length=255, default=None)
    name_en = models.CharField(max_length=255, default=None)
    path = models.CharField(max_length=50, db_index=True, default="-")
    slug = models.SlugField(max_length=255, blank=True, null=True)

    @staticmethod
    def fix_path(pid, path):
        for row in Category.objects.filter(parent_id=pid).order_by('id').all():
            row.path = '-' + '-'.join(path + [str(row.id)]) + '-'
            row.save(fix=False)
            Category.fix_path(row.id, path + [str(row.id)])

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None, fix=True
    ):
        if fix:
            Category.fix_path(None, [])
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        ret = super().save(force_insert, force_update, using, update_fields)
        return ret


    def __str__(self):
        return self.name
    
    

    # @property
    # def slug(self):
    #     return slugify(self.name, allow_unicode=True)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nomi")

    def str(self):
        return self.name

    class Meta:
        verbose_name = "Til"
        verbose_name_plural = "Tillar"


@i18n
class Burger(models.Model):
    
    STATUS_NEW = 0
    STATUS_PUBLISHED = 1
    STATUS_REJECTED = 2

    category = models.ForeignKey(Category, on_delete=models.RESTRICT, verbose_name='kategoriya')

    name_uz = models.CharField(max_length=255, default=None)
    name_ru = models.CharField(max_length=255, default=None)
    name_en = models.CharField(max_length=255, default=None)

    status = models.IntegerField(choices=(
        (STATUS_NEW,"YANGI"),
        (STATUS_PUBLISHED,'QABUL QILINGAN'),
        (STATUS_REJECTED,'INKOR QILINGAN')
    ), verbose_name='Status')

    description_uz = models.TextField(verbose_name="Ma'lumot uz")
    description_ru = models.TextField(verbose_name="Ma'lumot ru")
    description_en = models.TextField(verbose_name="Ma'lumot en")

    photo = models.ImageField(upload_to = 'burgers/')

    show_in_swiper = models.BooleanField(default=False)

    rating_stars = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)
    availability = models.BooleanField(default=False)

    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    price = models.DecimalField(max_digits=12,decimal_places=2,validators=[
        MinValueValidator(1000)
    ], verbose_name='Narxi')


    @property
    def slug(self):
        return slugify(self.name, allow_unicode=True)

    def __str__(self):
        return self.name

    

    class Meta:
        verbose_name = 'Burger'
        verbose_name_plural = 'Burgers'


@i18n
class WhyModel(models.Model):

    name_uz = models.CharField(max_length=255, default=None)
    name_ru = models.CharField(max_length=255, default=None)
    name_en = models.CharField(max_length=255, default=None)

    description_uz = models.TextField(verbose_name="Ma'lumot uz")
    description_ru = models.TextField(verbose_name="Ma'lumot ru")
    description_en = models.TextField(verbose_name="Ma'lumot en")

    photo = models.ImageField(upload_to='why/', default=None, blank=True, null=True)

    @property
    def slug(self):
        return slugify(self.name, allow_unicode=True)

    def __str__(self):
        return self.name

    

    class Meta:
        verbose_name = 'Why'
        verbose_name_plural = 'Why'

@i18n
class PageModel(models.Model):

    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    name_uz = models.CharField(max_length=255, default=None)
    name_ru = models.CharField(max_length=255, default=None)
    name_en = models.CharField(max_length=255, default=None)

    description_uz = QuillField(verbose_name="Ma'lumot uz")
    description_ru = QuillField(verbose_name="Ma'lumot ru")
    description_en = QuillField(verbose_name="Ma'lumot en")




    @property
    def slug(self):
        return slugify(self.name, allow_unicode=True)

    def __str__(self):
        return self.name