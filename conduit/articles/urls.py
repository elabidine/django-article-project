from django.urls import path
from .views import Home,EditorCreateView,EditorUpdateView,EditorDeleteView,ArticleCommentView,CommentDeleteView,ArticleDetailView


urlpatterns = [
    path("",Home.as_view(),name="home"),
   
    path("article/<slug:slug>", ArticleCommentView.as_view(), name="article_detail"),     # to this
    path("editor", EditorCreateView.as_view(), name="editor_create"),      
    
    path("editor/<slug:slug>", EditorUpdateView.as_view(), name="editor_update"),
    path(                                       # new
        "editor/<slug:slug>/delete",       #
        EditorDeleteView.as_view(),             #
        name="editor_delete",                   #
    ), 
    path(
        "article/<slug:slug>/comment/<int:pk>/delete",
        CommentDeleteView.as_view(),
        name="comment_delete",
    ),
      # new
]
