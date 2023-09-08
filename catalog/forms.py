from django import forms

from catalog.models import Product, Version, Category


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'image', 'purchase_price')

    def clean_title(self):
        cleaned_data = self.cleaned_data['title']

        for word in self.forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'В продукте нельзя использовать слова: {", ".join(self.forbidden_words)}')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in self.forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'В продукте нельзя использовать слова: {", ".join(self.forbidden_words)}.')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class CategoryForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'description',)
