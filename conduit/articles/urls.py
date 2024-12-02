from django.urls import path
from .views import Home,ArticleDetailView,EditorCreateView,EditorUpdateView,EditorDeleteView,ArticleCommentView


urlpatterns = [
    path("",Home.as_view(),name="home"),
    path(                                                                                           # to this
        "article/<slug:slug>-<uuid:uuid>",                                                          #
        ArticleDetailView.as_view(),                                                                #
        name="article_detail",                                                                      #
    ),
    #path("article/<slug:slug>", ArticleCommentView.as_view(), name="article_detail"),     # to this
    path("editor", EditorCreateView.as_view(), name="editor_create"),      
    
    path("editor/<slug:slug>", EditorUpdateView.as_view(), name="editor_update"),
    path(                                       # new
        "editor/<slug:slug>/delete",       #
        EditorDeleteView.as_view(),             #
        name="editor_delete",                   #
    ), 
      # new
]
