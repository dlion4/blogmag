from django.shortcuts import render
from django.views import generic
from .models import SubCategory
from posts.models import Post
# Create your views here.


class SubCategoryListView(generic.TemplateView):
    template_name = "pages/category.html"
    posts = Post
    queryset = SubCategory
    
    def get_object(self,**kwargs):
        return self.queryset.objects.get(category__name__icontains=kwargs.get("category_slug"),id=kwargs.get("pk"))
    
    def get_related_posts(self,**kwargs):
        return self.posts.objects.filter(topic__sub_category__name__icontains=self.get_object(**kwargs).name).all()
    
    
    def get_context_data(self, **kwargs):
        context = super(SubCategoryListView, self).get_context_data(**kwargs)
        context['sub'] = self.get_object(**kwargs)
        context['posts'] = self.get_related_posts(**kwargs).order_by("?").order_by("-createdAt")[:10]
        return context
    