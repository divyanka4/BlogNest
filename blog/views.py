from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm  # Use Django's built-in form
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.db.models import Q
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserProfileForm

def post_list(request):
    query = request.GET.get('q', '')
    posts = Post.objects.all().order_by('-published_date')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    return render(request, 'blog/post_list.html', {'posts': posts})

# def post_list(request):
#     posts = Post.objects.all().order_by('-published_date')  # newest first
#     return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Auto-fill author
            post.save()
            return redirect('post_detail', pk=post.pk)  # Redirect to the created post
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user.username:
        messages.error(request, "You cannot edit this post. Only the author can edit it.")
        return redirect('post_detail', pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.author = post.author  # <-- THIS FIX
            updated_post.save()
            messages.success(request, "Your post was updated successfully!")
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Change forbidden to message + redirect for non-authors
    if post.author != request.user.username:
        messages.error(request, "You cannot delete this post. Only the author can delete it.")
        return redirect('post_detail', pk=pk)
    
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})


def signup_view(request):  # Renamed from 'signup' to 'signup_view'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Use Django's built-in form
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect('home')  # Redirect to home page as planned
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def home(request):
    recent_posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')[:3]
    return render(request, 'blog/home.html', {'recent_posts': recent_posts})


def about(request):
    return render(request, 'blog/about.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent! We will get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('home')


def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            send_mail(
                subject="Subscription Confirmation - BlogNest",
                message="Thank you for subscribing to BlogNest. Have a great reading and writing experience!",
                from_email=None,   # or settings.DEFAULT_FROM_EMAIL
                recipient_list=[email],
                fail_silently=False,
            )
            messages.success(request, "Thank you for subscribing! Please check your inbox.")
            return redirect('home')
    return render(request, 'blog/home.html')

@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})