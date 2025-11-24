from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Contact
from .forms import ContactForm, SignUpForm



# --- SIGNUP ---
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('contact_list')

    def form_valid(self, form):
        user = form.save()
        # auto-login after successful signup
        login(self.request, user)
        return redirect(self.success_url)

# --- CRUD ---
@login_required
def contact_list(request):
    """List + simple search across multiple fields."""
    q = request.GET.get('q', '').strip()
    contacts = Contact.objects.all()
    if q:
        contacts = contacts.filter(
            Q(name__icontains=q) |
            Q(address__icontains=q) |
            Q(profession__icontains=q) |
            Q(tel_number__icontains=q) |
            Q(email__icontains=q)
        ).distinct()
    return render(request, 'contacts/list.html', {'contacts': contacts, 'q': q})

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/form.html', {'form': form, 'title': 'Add Contact'})

@login_required
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/form.html', {'form': form, 'title': 'Edit Contact'})

@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/confirm_delete.html', {'contact': contact})


# Create your views here.
