from django import forms
from django.core.exceptions import ValidationError
from .models import Category, Burger
import datetime

def build_burger_category_tree(choice=False):
    parents = {}
    for row in Category.objects.order_by("id").all():
        if row.parent_id not in parents:
            parents[row.parent_id] = []

        parents[row.parent_id].append(row)

    result = []

    def build_tree(parent_id=None, depth=0):
        if parent_id not in parents:
            return

        margin = ">> " * depth

        for row in parents[parent_id]:
            txt = f"{margin} {row.name}"
            if choice:
                result.append((row.id, txt))
            else:
                result.append({"value": row.id, "text": txt})
            build_tree(row.id, depth + 1)
    build_tree()

    return result


class BurgerForm(forms.ModelForm):
    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)

        self.fields["category"].choices = build_burger_category_tree(True)
    def clean(self):
        rating_stars = self.cleaned_data["rating_stars"]
        rating_count = self.cleaned_data["rating_count"]
        if rating_stars > 0 and rating_stars / rating_count > 5:
            raise ValidationError({
                "rating_stars": f"Ustun qiymati {rating_stars} dan/ga teng/kichik bo'lishi lozim!"
            })
        return self.cleaned_data

    class Meta:
        model = Burger
        fields = "__all__"