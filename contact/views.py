from django.shortcuts import render
import os

def contact(request):
    """ A view to return the contact page """
    if request.method == 'SUBMIT':
        if form.is_valid():
            messages.success(request, 'The Book was successfully added')
        else:
            messages.error(request, 'failed to add the book. Please ensure the details are correct and all fields that are required are entered.')
    return render(request, 'contact/contact.html', context={
        'EMAILJS': os.environ.get('EMAILJS')
    })

def thank_you(request):
    """ A view to return the thank you page """

    return render(request, 'thank_you.html')
