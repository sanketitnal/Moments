from django.shortcuts import render
from django.views.generic import CreateView
from pictures.models import Category, Picture
from pictures.forms import PictureForm, CategoryForm
from django.urls import reverse_lazy

# Create your views here.


def landing_page(request):
    categories = Category.objects.all()

    req_category = request.GET.get('category')
    if (req_category is not None):
        pictures = Picture.objects.all().filter(category__category=req_category)
        message = "Result: category = {}, {} pictures".format(
            req_category, pictures.count())
    else:
        pictures = Picture.objects.all()
        message = "Result: category = all categories, {} pictures".format(
            pictures.count())

    ctx = {
        'categories': categories,
        'pictures': pictures,
        'message': message
    }
    return render(request, 'pictures/index.html', context=ctx)


class PictureCreateView(CreateView):
    form_class = PictureForm
    model = Picture
    success_url = reverse_lazy('pictures:pictures-landing-page')
    # looks for modelname_form.html -> picture_form.html


class CategoryCreateView(CreateView):
    form_class = CategoryForm
    success_url = reverse_lazy('pictures:pictures-landing-page')
    template_name = 'pictures/category-form.html'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)
