from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django import forms
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Entry, Category

#Homepage, lists the most recent blogs and all categories below
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'newest_entry_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Entry.objects.order_by('pub_date')[:5]

#about page (with links to personal site)
def about(request):
    return HttpResponse('about me')

def contact(forms.Form):
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        cc_myself = form.cleaned_data['cc_myself']

        recipients = ['dstambl2@jhu.edu']
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, sender, recipients)
        return HttpResponseRedirect('Thank you. I will contact you soon')


#Lists the archive of all blog posts
class BlogArchiveView(generic.ListView):
    template_name = 'blog/archive.html'
    context_object_name = 'entry_list'

    def get_queryset(self):
        return Entry.objects.all()

#Lists all blogs in a given category
class CategoryView(generic.DetailView):
    model = Category
    template_name = 'blog/category.html'


#Lists all posts from a given date
#class DateView(generic.DetailView): TODO


class EntryView(generic.DetailView):
    model = Entry
    template_name = 'blog/entry.html'
