import os
from django.shortcuts import render
from django.conf import settings
from main.utils import predict_quality
from main.forms import RegistrationForm 
from django.views import View
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST' and 'file' in request.FILES:
        image_file = request.FILES['file']
        image_path = os.path.join(settings.MEDIA_ROOT, 'tmp_img.jpg')
        with open(image_path, 'wb+') as destionatoin:
            for chunk in image_file.chunks():
                destionatoin.write(chunk)
        prediction = predict_quality(image_path)
        return render(request, 'result.html', {'predicted_class': prediction['predicted_class']})
                   
    return render(request, 'predict.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations! Registered Successfully')
            form.save()
            form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})