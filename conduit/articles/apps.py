from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'conduit.articles'
    def ready(self):                        # new
        import conduit.articles.signals  