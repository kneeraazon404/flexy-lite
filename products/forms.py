# forms.py
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    # https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
    widgets = {
        "name": forms.TextInput(attrs={"class": "form-control"}),
        "email": forms.EmailInput(attrs={"class": "form-control"}),
        "contact": forms.TextInput(attrs={"class": "form-control"}),
    }

    class Meta:
        model = Product
        fields = [
            "p_sku",
            "description",
            "quantity",
            "action",
            "location",
            # "date_created",
        ]
