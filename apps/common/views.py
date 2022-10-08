from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm

class HomeView(TemplateView):
    template_name = 'templates\common\home.html'
class DashboardView(TemplateView):
    template_name = 'templates\common\dashboard.html'

class SignUpView(CreateView):
    form_class= SignUpForm
    success_url = reverse_lazy('home')
    template_name = r'templates\common\register.html'
    
def sign_up(request):
  if 'code_user' in request.session:
    return redirect('home')
  elif request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        request.session['code_user'] = user.code
        request.session['username'] = user.username
        return redirect('home')
    else:
        for field in form:
            if field.errors:
                form.fields[field.name].widget.attrs['class'] = 'form-control is-invalid'
        return render(request, 'blog/signup.html', {'form': form})

  else:
    form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})
