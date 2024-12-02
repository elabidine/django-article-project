from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
from .models import Article,Comment
# Create your views here.

class Home(ListView):
    
    template_name = 'home.html'
    queryset = Article.objects.order_by('-created_at')
    context_object_name = "articles"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"
    def get_object(self):                                                       
        slug = self.kwargs.get("slug")                                          
        uuid_field = self.kwargs.get("uuid")                                    
        return get_object_or_404(Article, slug=slug, uuid_field=uuid_field)
    
    def get_context_data(self, **kwargs):                       # new
        context = super().get_context_data(**kwargs)            # new
        context["form"] = CommentCreateView().get_form_class()  # new
        return context    
    
class EditorCreateView(CreateView):                                 # new
    """ View for creating articles."""                               #
                                                                    #
    model = Article                                                 #
    fields = ['title', 'description', 'body']                       #
    template_name = "editor.html"  
    #def form_valid(self, form):                         # new
    #    self.object.author = self.request.user.profile  #
    #    return super().form_valid(form)  

class EditorUpdateView(UpdateView):
    """View for editing articles."""
    model = Article
    fields = ["title", "description", "body"]
    template_name = "editor.html"
    def get_object(self):                                       # new
        slug = self.kwargs.get("slug")                #
        return get_object_or_404(Article, slug=slug)
    
class EditorDeleteView(DeleteView):             # new
    """View for deleting articles."""           #
                                                #
    model = Article                             #
    template_name = "article_detail.html"       #
    success_url = reverse_lazy("home")   

    def get_object(self):                                       # new
        slug = self.kwargs.get("slug")                #
        return get_object_or_404(Article, slug=slug)  #

class CommentCreateView(CreateView):
    """View for creating comments."""

    model = Comment
    fields = ["body"]
    template_name = "article_detail.html"

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.instance.article = Article.objects.filter(
            slug_uuid=self.kwargs.get("slug")
        ).first()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "article_detail", kwargs={"slug": self.object.article.slug}
        )
    
class ArticleCommentView(View):
    """View for viewing articles and posting comments."""

    def get(self, request, *args, **kwargs):
        view = ArticleDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentCreateView.as_view()
        return view(request, *args, **kwargs)