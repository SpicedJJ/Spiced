from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request,'pages/home.html', {'navbar': 'homePage'})

def about_page(request):
    return render(request, 'pages/aboutus.html', {'navbar': 'aboutPage'})

def services_page(request):
    return render(request, 'pages/services.html', {'navbar': 'servicesPage'})

def contact_page(request):
    return render(request, 'pages/contact.html', {'navbar': 'contactPage'})

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Inquiry
from .forms import InquiryForm

class InquiryListView(ListView):
    model = Inquiry
    template_name = 'pages/inquiry_list.html'

class InquiryCreateView(CreateView):
    model = Inquiry
    form_class = InquiryForm
    template_name = 'pages/inquiry_form.html'
    success_url = reverse_lazy('homePage')

class InquiryUpdateView(UpdateView):
    model = Inquiry
    form_class = InquiryForm
    template_name = 'pages/inquiry_form.html'
    success_url = reverse_lazy('inquiry_list')

class InquiryDeleteView(DeleteView):
    model = Inquiry
    template_name = 'pages/inquiry_confirm_delete.html'
    success_url = reverse_lazy('inquiry_list')

from .models import Inquiry
from .forms import InquiryForm

def create_inquiry(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inquiry_list')
    else:
        form = InquiryForm()
    return render(request, 'inquiry_form.html', {'form': form})

def update_inquiry(request, pk):
    inquiry = Inquiry.objects.get(pk=pk)
    if request.method == 'POST':
        form = InquiryForm(request.POST, instance=inquiry)
        if form.is_valid():
            form.save()
            return redirect('inquiry_list')
    else:
        form = InquiryForm(instance=inquiry)
    return render(request, 'inquiry_form.html', {'form': form})

def delete_inquiry(request, pk):
    inquiry = Inquiry.objects.get(pk=pk)
    inquiry.delete()
    return redirect('inquiry_list')

from django.shortcuts import render, redirect
from .forms import InquiryForm

def create_or_update_inquiry(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the home page
            return redirect('homePage')
    else:
        form = InquiryForm()
    return render(request, 'inquiry_form.html', {'form': form})