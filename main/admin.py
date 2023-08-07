from django.contrib import admin
from .models import Language, Category, Burger, PageModel, WhyModel
from .forms import BurgerForm
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent', 'name']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(WhyModel)
class WhyAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(PageModel)
class WhyAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.action(description="Status: NEW")
def burger_status_new(modeladmin, request, queryset):
    queryset.update(status = Burger.STATUS_NEW)

@admin.action(description="Status: PUBLISHED")
def burger_status_publish(modeladmin, request, queryset):
    queryset.update(status=Burger.STATUS_PUBLISHED)

@admin.action(description="Status: REJECTED")
def burger_status_reject(modeladmin, request, queryset):
    queryset.update(status=Burger.STATUS_REJECTED)

@admin.register(Burger)
class burgerAdmin(admin.ModelAdmin):
    form = BurgerForm
    actions = [burger_status_new, burger_status_publish, burger_status_reject]
    list_display = ['id', 'slug', 'availability','status','category', 'price', 'get_rating_stars', 'updated_at']
    list_filter = ['status', 'category']

    def get_status_title(self, obj):
        txt = obj.get_status_display()
        color = ""
        if obj.status == Burger.STATUS_NEW:
            txt = "⏳ " + txt
            color = "#d35400"
        elif obj.status == Burger.STATUS_PUBLISHED:
            txt = "✅ " + txt
        else:
            txt = "❌ " + txt
            color = "#c0392b"
        
        return format_html(f"""<span style = "color: {color}">{txt}</span> """)

    get_status_title.short_description = "Status"

    def get_rating_stars(self, obj):
        n = 0
        COLORY = "#feca57"
        COLORW = "#bdc3c7"
        if obj.rating_count > 0:
            n = round(obj.rating_stars / obj.rating_count)
        
        yellow_stars = f"""<span style = "color: {COLORY}">&#9733;</span> """ * n
        white_stars = f"""<span style = "color: {COLORW}">&#9733;</span> """ * (5 - n)
        return format_html(yellow_stars) + format_html(white_stars)

    get_rating_stars.short_description = "Reyting"





