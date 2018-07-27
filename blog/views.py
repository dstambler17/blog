from django.shortcuts import get_object_or_404, render, redirect
#from django.urls import reverse
from django.views import generic

from .forms import ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
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
    return render(request, 'blog/about.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['dstambl2@jhu.edu'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('http://127.0.0.1:8000/contact/')
    return render(request, "blog/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Thank you for your message! You will recieve a reply soon')

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
