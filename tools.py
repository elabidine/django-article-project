import random
from django.contrib.auth import get_user_model
from conduit.articles.models import Article


User = get_user_model()

# Vérifier si des utilisateurs existent
users = User.objects.all()
if not users.exists():
    print("No users found! Please create users first.")
else:
    titles = [
        "Django Tips and Tricks",
        "How to Learn Python Fast",
        "Understanding PostgreSQL",
        "A Guide to Web Development",
        "Mastering JavaScript",
        "The Art of Debugging",
    ]
    descriptions = [
        "This article explains key concepts.",
        "Learn how to get started quickly.",
        "A deep dive into the best practices.",
        "An ultimate guide for beginners and pros.",
        "The must-know tips for web developers.",
        "Essential strategies for clean debugging.",
    ]
    
    
    for i in range(6):  # Générer 20 articles
          user = random.choice(users)
          article = Article.objects.create(
              title=random.choice(titles),
              description=random.choice(descriptions),
              body="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
              author=user.profile,
          )
          print(f"Created article '{article.title}' for user {user.username}")
