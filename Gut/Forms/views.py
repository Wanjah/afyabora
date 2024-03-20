from django.shortcuts import render, redirect
from .userForm import Form
from django.http import HttpResponse

# Create your views here.

def userForm(request):
    return HttpResponse('<h1>Forms<h1>')
    '''
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = Form()
    return render(request, '<h1>Pge not Found</h1>', {'form': form})
    '''