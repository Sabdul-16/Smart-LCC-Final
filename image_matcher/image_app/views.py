from .models import ImageModel
from .forms import ImageUploadForm
from django.shortcuts import render
from .compare_images import compare_images


def home(request):
    images = ImageModel.objects.all()  # fetch images outside the if condition
    context = {'images': images}  # include images in context

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            index = compare_images(image)
            context['index'] = index  # add index to context

    else:
        form = ImageUploadForm()

    context['form'] = form  # include the form in the context

    return render(request, 'home.html', context)  # render with context
