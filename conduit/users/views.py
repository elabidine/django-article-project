from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect,get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView

from conduit.users.models import User


class Login(LoginView):
    """
    View to handle user login.
    If the user is already authenticated, they are redirected to the home page.
    """
    template_name = "login.html"
    next_page = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        """
        Redirect authenticated users to the next page (home) to avoid redundant login.
        """
        if request.user.is_authenticated:
            return redirect(self.next_page)
        return super().get(request, *args, **kwargs)


class Logout(LogoutView):
    """
    View to handle user logout.
    Redirects users to the home page after logout.
    """
    next_page = reverse_lazy("home")
    
    def dispatch(self, request, *args, **kwargs):
        """
        Ensure GET requests for logout behave like POST for consistency.
        """
        if request.method == "GET":
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)
    


class SignUpView(CreateView):
    """
    View to handle user registration (sign-up).
    """
    model = get_user_model()   # Reference the custom user model
    fields = ["username", "email", "password"]    # Fields included in the registration form
    template_name = "signup.html"    # Template used for rendering the sign-up page
    success_url = reverse_lazy("home")    # Redirect URL after successful registration

    def get(self, request, *args, **kwargs):
        """
        Redirect authenticated users to the home page to prevent unnecessary sign-up.
        """
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)
    def form_valid(self, form):  
        """
        Custom form handling to ensure the password is hashed and the user is authenticated after sign-up.
        """
        # Create the User object
        user = form.save(commit=False)  
        # Set and hash the password
        password = form.cleaned_data.get("password")  
        user.set_password(password)  
        # save the User object to the database
        user.save()  
        # Authenticate the user with the provided credentials
        email = form.cleaned_data.get("email")  
        authenticated_user = authenticate(email=email, password=password)  
        # Log in the authenticated user
        login(self.request, authenticated_user)  
        return redirect(self.success_url)  

class ProfileDetailView(DetailView):
    """
    View to display user profile details, including their articles.
    """
    model = User   # Reference the User model
    template_name = "profile_detail.html"   # Template used for rendering the profile page
    def get_object(self, queryset=None):
        """
        Retrieve the profile object based on the username in the URL.
        """                          
        username = self.kwargs.get("username", None)                    
        profile = get_object_or_404(User, username=username).profile   
        return profile 
    def get_context_data(self, **kwargs):
        """
        Add additional context to the template, including the user's articles.
        """
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:  # Check if the user is logged in
            context["my_articles"] = self.object.articles.order_by('-created_at')    # User's articles sorted by creation date
        return context