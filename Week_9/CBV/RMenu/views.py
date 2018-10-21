from django.shortcuts import render,reverse
from django.views.generic import TemplateView,ListView,DeleteView,CreateView,UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import RestaurantForm
from .models import Restau

class HomeView(TemplateView):
    template_name = "home.html"

class RestaurantListView(ListView):
    model = Restau
    template_name = "restaurant.html"

@method_decorator(login_required, name='dispatch')
class DeleteRestaurantView(DeleteView):
    login_required = True
    model = Restau

@method_decorator(login_required, name='dispatch')
class RestaurantCreateView(CreateView):
    login_required = True
    model = Restau
    form_class = RestaurantForm
    template_name = "add_res.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

@method_decorator(login_required, name='dispatch')
class RestaurantUpdateView(UpdateView):
    login_required=True
    model = Restau
    fields = ['name', 'telephone', 'city']
    template_name = "update_res.html"