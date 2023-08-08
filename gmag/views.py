from category.models import (
Category,
SubCategory,
Topic,
Tag
)
from django.http import JsonResponse
from django.views import generic
from posts.models import Post
from pages.forms.forms import ContactForm


class CategoryListView(generic.TemplateView):
    template_name = "pages/category.html"


class AboutUs(generic.TemplateView):
    template_name = "pages/about.html"


class ContactUs(generic.TemplateView):
    template_name = "pages/contact.html"
    
    def get_context_data(self, **kwargs):
        context = super(ContactUs, self).get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        return context
    
    def post(self, *args,**kwargs):
        form  = ContactForm(self.request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Your Comment Was posted successfully"})
        return JsonResponse({"message": "Something went wrong"})

