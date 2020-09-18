from django.contrib.auth.mixins import LoginRequiredMixin #New
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Client
from .models import Computer
from. models import Comment
from django.urls import reverse_lazy

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'

class ClientDetailView(LoginRequiredMixin ,DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ComputerUpdateView(LoginRequiredMixin, UpdateView):
    model = Computer
    fields = ('type', 'manufacturer', 'model', 'date_of_purchase', 'last_serviced')
    template_name = 'computer_edit.html'

class ComputerDeleteView(LoginRequiredMixin, DeleteView):
    model = Computer
    template_name = 'computer_delete.html'
    success_url = reverse_lazy('client_list')

class ComputerCreateView(LoginRequiredMixin, CreateView):
    model = Computer
    template_name = 'computer_new.html'
    fields = ('client', 'type', 'manufacturer', 'model', 'date_of_purchase', 'last_serviced','author')
    login_url = 'login'

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ('client', 'comment','author')
    login_url = 'login'

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('client_list')

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ('client','comment','author')
    template_name = 'comment_edit.html'