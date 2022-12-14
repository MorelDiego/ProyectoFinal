from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.

def index(request):

    # if request.user.is_authenticated():    

    #     images = Avatar.objects.filter(user=request.user.id)

    #     return render(request, 'index.html', {'url': images[0].image.url})

    # else:
        return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    
    if request.method == "POST":

        contact_form = CreateContact(request.POST)

        if contact_form.is_valid():

            formulario_contacto = contact_form.cleaned_data

            contacto = Contact(name=formulario_contacto["name"], email=formulario_contacto["email"], message=formulario_contacto["message"])

            contacto.save()

            return render(request, "CinemaRevs/templates/index.html")
    else:
        contact_form = CreateContact()
        
    return render(request, "contact.html", {"contact_form": contact_form})

def reviews(request):

    review_list = Reviews.objects.all()

    context = {'reviews_list': review_list}

    return render(request, 'reviews.html', context=context)

def search(request):
     if request.GET.get('film', False):
        film = request.GET['film']

        found = Reviews.objects.filter(film__icontains=film)

        return render(request, "search.html", {"found":found})
     else:
        respuesta = "No results found"
    
     return render(request, 'search.html', {'respuesta': respuesta})


def editProfile(request):

    user = request.user

    if request.method == 'POST':
        editprofile_form = UserEditForm(request.POST)

        if editprofile_form.is_valid():

            information = editprofile_form.cleaned_data

            user.username = information['username']
            user.email = information['email']
            user.password1 = information['password']
            user.password2 = information['password2']
            user.save()

            return render(request, 'index.html')

    else:

        editprofile_form = UserEditForm(initial={'username': user.username, 'email': user.email})

    return render(request, 'Profile/editprofile.html', {'form': editprofile_form, 'user': user})

def addAvatar(request):
    if request.method == 'POST':

        avatar_form = AvatarForm(request.POST, request.FILES)
        
        if avatar_form.is_valid():

            currentUser = User.objects.get(username=request.user)
            avatar = Avatar(user=currentUser, image=avatar_form.cleaned_data['image'])
            avatar.save()
            return render(request, 'index.html')

    else:

        avatar_form = AvatarForm()

        return render(request, 'Profile/addAvatar.html', {'avatar_form': avatar_form})

class ProfileView(DetailView):
    model = User
    template_name = 'Profile/profile.html'

# class UserList(ListView):
#     model = User
#     template_name = 'userlist.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('Index')
    template_name = 'register.html'

class AdminLoginView(LoginView):
    template_name = 'login.html'

class AdminLogoutView(LogoutView):
    template_name = 'logout.html'

class ReviewsListView(ListView):
    model = Reviews
    template_name ='Reviews/reviews_list.html'

class ReviewsDetailView(DetailView):
    model = Reviews
    template_name ='Reviews/reviews_detail.html'

class ReviewsDeleteView(DeleteView):
    model = Reviews
    success_url = '/reviews_list'
    template_name = 'Reviews/reviews_delete.html'

class ReviewsCreateView(LoginRequiredMixin, CreateView):
    model = Reviews
    success_url = reverse_lazy('ReviewsList')
    template_name = 'Reviews/reviews_create.html'
    fields = ['title', 'body', 'film', 'image']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, **kwargs):         
        if  kwargs != None:
            return reverse_lazy('ReviewsList')
        else:
            return reverse_lazy('ReviewsList')

class ReviewsUpdateView(UpdateView):
    model = Reviews
    success_url = '/reviews_list'
    template_name = 'Reviews/reviews_update.html'
    fields = ['title', 'body', 'film', 'image']

