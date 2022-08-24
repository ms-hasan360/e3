from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from homepage import forms
from django.views.decorators.csrf import csrf_exempt
import pyfiglet


@csrf_exempt
def homepage(request):
    form_data = forms.UserForm(request.POST)
    data = {
        'form': form_data,
        'name_ascii': ''
    }
    
    if request.method == 'POST':
        if form_data.is_valid():
            name = form_data.cleaned_data['user_name']
            mail = form_data.cleaned_data['user_email']
            
            
            
            ascii_name = []
            font_list = ["standard", "slant", "3-d", "3x5", "5lineoblique", "alphabet", "banner3-D",
                         "doh", "isometric1", "letters", "alligator", "dotmatrix", "bubble", "bulbhead", "digital"]
            for i in font_list:
                name_ascii = pyfiglet.figlet_format(
                    name, font=i, justify='center')
                ascii_name.append(name_ascii)

            
            data.update({'user_name': name})
            data.update({'user_email': mail})
            data.update({'name_ascii': ascii_name})
            
    
    
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context=data))

def aboutPage(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
