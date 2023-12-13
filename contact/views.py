from django.shortcuts import render
import os

def contact(request):
    """ A view to return the contact page """
    if 'Send' in request.POST:
         messages.success(request, 'The Book was successfully added')

    return render(request, 'contact/contact.html', context={
        'EMAILJS': os.environ.get('EMAILJS')
    })
