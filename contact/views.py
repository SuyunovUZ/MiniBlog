from django.shortcuts import render
from .models import Contact


def contact_page(request):
    articles = Contact.objects.all().order_by('-id')
    context = {'articles': articles}
    return render(request, 'contact.html', context)
