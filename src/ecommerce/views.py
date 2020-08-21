# authentication imports
from django.contrib.auth import authenticate, login

from django.http import HttpResponse
from django.shortcuts import render, redirect


# my custom modules import
from .forms import ContactForm, LoginForm


def home_page(request):
    context = {
        "title": "Hello World!",
        "content": "Welcome to the home page."
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {
        "title": "About Page!",
        "content": "Welcome to the about page."
    }
    return render(request, 'home_page.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Page!",
        "content": "Welcome to the contact page.",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     # print(request.POST)
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))
    #     print(request.POST.get("content"))
    return render(request, 'contact/view.html', context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form
    }
    print(request.user.is_authenticated())
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        login_user = authenticate(
            request, username=username, password=password)
        print(request.user.is_authenticated())
        if login_user is not None:
            login(request, login_user)
            # context['form'] = LoginForm()
            return redirect("/login")
        else:
            print("Error")

    return render(request, "auth/login.html", context)

# def register_page(request):
#     register_form = RegisterForm(request.POST or None)
#     if register_form.is_valid():
#         print(register_form.cleaned_data)
#     return render(request, "auth/register.html", {})
