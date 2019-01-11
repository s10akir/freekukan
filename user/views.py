from django.views import generic
from .models import User

# Create your views here.


class IndexView(generic.ListView):
    model = User


class DetailView(generic.DetailView):
    model = User
