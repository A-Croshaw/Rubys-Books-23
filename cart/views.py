from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from books.models import Book


def shopping_cart(request):
    """ View that renders the shopping cart """

    return render(request, 'cart/cart.html')
