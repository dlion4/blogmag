from django.shortcuts import render, get_object_or_404
from django.views import generic
from accounts.models import Profile
from django.shortcuts import redirect
from posts.models import Post
from django.db.models import Sum
from writer.forms.posts.forms import PostForm
from django.utils.text import slugify
from paginator.paginators import Paginator

def post_view_count(request, field):
    return Post.objects.filter(writer=request).all().aggregate(total_views=Sum(field))

def post_object(queryset, **kwargs):
    return get_object_or_404(queryset, pk=kwargs.get("pk"), slug=kwargs.get("slug"))



class EditorListView(Paginator, generic.TemplateView):
    template_name = "editor/posts/posts.html"
    queryset = Post
    context_object_name = "posts"
    paginate_by = 5
    
    
    def get_profile(self):
        return get_object_or_404(Profile,user=self.request.user)
    
    def gq_queryset(self,**kwargs):
        return self.queryset.objects.filter(writer=self.get_profile()).all().order_by("-createdAt")
    
    
    def get_context_data(self, **kwargs):
        context = super(EditorListView, self).get_context_data(**kwargs)
        if self.get_profile() is not None:
            context['profile'] = self.get_profile()
        context['total_views'] = post_view_count(self.get_profile(), "views")
        return context
    
            
    
    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("posts:home")
        print(self.get_context_data(**kwargs))
        return render(request, self.template_name, self.get_context_data(**kwargs))

class EditorCreatePostView(Paginator, generic.TemplateView):
    template_name = "editor/posts/create.html"
    form_class = PostForm
    queryset = Post
    context_object_name = "posts"
    paginate_by = 10
    
    
    def get_profile(self):
        return get_object_or_404(Profile,user=self.request.user)
    
    
    def gq_queryset(self,**kwargs):
        return self.queryset.objects.filter(writer=self.get_profile()).all().order_by("-createdAt")
    
    
    def get_context_data(self, **kwargs):
        context = super(EditorCreatePostView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        context['total_views'] = post_view_count(self.get_profile(), "views")
        context['profile'] = self.get_profile()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.writer = self.get_profile()
            instance.slug = slugify(form.cleaned_data.get("title"))
            instance.save()
            print(form.cleaned_data)
            form.save()
            return redirect("writer:posts_list")
        self.get_context_data(**kwargs).update({
            "form": form
        })
        return render(request, self.template_name, self.get_context_data(**kwargs))

class EditPostView(generic.TemplateView):
    template_name = "editor/posts/edit.html"
    form_class = PostForm
    queryset = Post
    
    def get_profile(self):
        return get_object_or_404(Profile,user=self.request.user)
    
    def get_context_data(self, **kwargs):
        instance = post_object(queryset=self.queryset, **kwargs)
        context = super(EditPostView, self).get_context_data(**kwargs)
        context['form'] = self.form_class(instance=instance)
        context['post'] = post_object(queryset=self.queryset, **kwargs)
        context['profile'] = self.get_profile()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
                instance = form.save(commit=False)
                instance.writer = self.request.user.user_profile
                instance.slug = slugify(form.cleaned_data.get("title"))
                instance.save()
                print(form.cleaned_data)
                form.save()
                return redirect("writer:posts_list")
        self.get_context_data(**kwargs).update({
            "form": form
        })
        print(form.errors)
        return render(request, self.template_name, self.get_context_data(**kwargs))     


class DeletePostView(generic.TemplateView):
    pass
