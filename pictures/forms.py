from django.forms import ModelForm
from pictures.models import Picture, Category


class PictureForm(ModelForm):
    class Meta():
        model = Picture
        fields = ['title', 'picture', 'category', 'description']

    def __init__(self, *args, **kwargs):
        super(PictureForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({'class': 'form-control'})
        
        self.fields['category'].widget.attrs.update({'class': 'form-select'})
        self.fields['description'].widget.attrs.update({'style': 'height: 200px'})


class CategoryForm(ModelForm):
    class Meta():
        model = Category
        fields = ['category']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({'class': 'form-control'})
