from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost

class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/list.html"

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/detail.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save()
        return obj

class BlogCreateView(CreateView):
    model = BlogPost
    fields = ["title", "content", "preview_image", "is_published"]
    success_url = reverse_lazy("blog:blog_list")

class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "content", "preview_image", "is_published"]

    def get_success_url(self):
        return reverse_lazy("blog:blog_detail", kwargs={"pk": self.object.pk})

class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog:blog_list")
