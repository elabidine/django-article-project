from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
from .models import Article,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Home(ListView):
    """
    View for the home page, displaying a list of articles ordered by creation date.
    """
    template_name = 'home.html'
    queryset = Article.objects.order_by('-created_at')
    context_object_name = "articles"

class ArticleDetailView(DetailView):
    """
    View for displaying detailed information about a specific article.
    """
    model = Article
    template_name = "article_detail.html"

    def get_object(self):
        """
        Retrieve the article object based on the slug from the URL.
        """ 
        slug = self.kwargs.get("slug")                                          
        return get_object_or_404(Article, slug=slug)
    
    def get_context_data(self, **kwargs):
        """
        Add additional context to the template, including a comment form.
        """           
        context = super().get_context_data(**kwargs)            
        context["form"] = CommentCreateView().get_form_class()  
        return context    
    
class EditorCreateView(LoginRequiredMixin,CreateView):                                 
    """ View for creating articles."""                               
                                                                    
    model = Article                                                 
    fields = ['title', 'description', 'body']                       
    template_name = "editor.html"  

    def form_valid(self, form):
        """
        Assign the current user as the author of the article before saving.
        """
        self.object = form.save(commit=False)           
        self.object.author = self.request.user.profile
        self.object.save()                              
        return super().form_valid(form)
  

class EditorUpdateView(LoginRequiredMixin,UpdateView):
    """
    View for authenticated users to edit an existing article.
    """
    model = Article
    fields = ["title", "description", "body"]
    template_name = "editor.html"
    def get_object(self):
        """
        Retrieve the article object to be edited based on the slug.
        """                 
        slug = self.kwargs.get("slug")                
        return get_object_or_404(Article, slug=slug)
    
    def post(self, request, *args, **kwargs):
        """
        Allow editing only if the current user is the author of the article.
        """
        if request.user == self.get_object().author.user:
            return super().post(request, *args, **kwargs)
        return redirect(self.get_object().get_absolute_url())
    
class EditorDeleteView(LoginRequiredMixin,DeleteView):             
    """
    View for authenticated users to delete their articles.
    """         
                                                
    model = Article                             
    template_name = "article_detail.html"       
    success_url = reverse_lazy("home")   

    def get_object(self):    
        """
        Retrieve the article object to be deleted based on the slug.
        """                                   
        slug = self.kwargs.get("slug")                
        return get_object_or_404(Article, slug=slug) 
    
    def post(self, request, *args, **kwargs):
        """
        Allow deletion only if the current user is the author of the article.
        """
        if request.user == self.get_object().author.user:
            return super().post(request, *args, **kwargs)
        return redirect(self.get_object().get_absolute_url())

class CommentCreateView(LoginRequiredMixin,CreateView):
    """
    View for authenticated users to create a comment on an article.
    """
    model = Comment
    fields = ["body"]
    template_name = "article_detail.html"
    def form_valid(self, form):
        """
        Assign the current user and the corresponding article to the comment before saving.
        """
        form.instance.author = self.request.user.profile
        form.instance.article = get_object_or_404(Article, slug=self.kwargs.get("slug"))
        return super().form_valid(form)
    
    def get_success_url(self):
        """
        Redirect to the article detail page after successfully posting a comment.
        """
        return reverse(
            "article_detail", kwargs={"slug": self.object.article.slug}
        )
class ArticleCommentView(LoginRequiredMixin,View):
    """View for viewing articles and posting comments."""

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests by rendering the article detail view.
        """
        view = ArticleDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests by delegating to the comment creation view.
        """
        view = CommentCreateView.as_view()
        return view(request, *args, **kwargs)

class CommentDeleteView(LoginRequiredMixin,DeleteView):
    """
    View for authenticated users to delete their comments.
    """

    model = Comment
    template_name = "article_detail.html"

    def get_success_url(self):
        """
        Redirect to the article detail page after successfully deleting a comment.
        """
        return reverse("article_detail", kwargs={"slug": self.object.article.slug})