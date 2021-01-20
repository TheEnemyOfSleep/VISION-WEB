from django.views.generic import (
    ListView,
    FormView
    )
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from page.models import Block
from page.forms import ContactForm

def index_page(request):
    block_list = Block.objects.exclude(root__isnull=False).order_by('sorting')

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Test subject"
            from_email = "landing@vision_web.com"
            message = form.cleaned_data['name']
            try:
                send_mail(subject, message, from_email, ['zedavis2011@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Succes')

    context = {
        'form': form,
        'block_list': block_list
    }

    return render(request, "index.html", context=context)