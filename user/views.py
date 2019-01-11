from django.views import generic
from .models import User

# Create your views here.


class IndexView(generic.ListView):
    model = User


class DetailView(generic.DetailView):
    model = User


class CreateView(generic.edit.CreateView):
    model = User
    fields = '__all__'


class UpdateView(generic.edit.UpdateView):
    model = User
    fields = '__all__' 