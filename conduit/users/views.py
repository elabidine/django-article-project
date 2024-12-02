from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect,get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView

from conduit.users.models import User


class Login(LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.next_page)
        return super().get(request, *args, **kwargs)


class Logout(LogoutView):
    next_page = reverse_lazy("home")
    
    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)
    


class SignUpView(CreateView):
    model = get_user_model()
    fields = ["username", "email", "password"]
    template_name = "signup.html"
    success_url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)
    def form_valid(self, form):  # new
        # create the User object
        user = form.save(commit=False)  # new
        # set password manually
        # as otherwise the User will be saved with unhashed password
        password = form.cleaned_data.get("password")  # new
        user.set_password(password)  # new
        # save the User object to the database
        user.save()  # new
        # authenticate your user with unhashed password
        # (`authenticate` expects unhashed passwords)
        email = form.cleaned_data.get("email")  # new
        authenticated_user = authenticate(email=email, password=password)  # new
        # log in
        login(self.request, authenticated_user)  # new
        return redirect(self.success_url)  # new

class ProfileDetailView(DetailView):
    model = User
    template_name = "profile_detail.html"
    def get_object(self, queryset=None):                                  # new
        username = self.kwargs.get("username", None)                    # new
        profile = get_object_or_404(User, username=username).profile    # new
        return profile 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["my_articles"] = self.object.articles.order_by('-created_at')
        return context