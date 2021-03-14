from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import CustomUser
from contacts.models import Contact
# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, 'You are successfuly logged in.')
            if request.POST['next'] != '/':
                print(request.POST['next'])
                return redirect(request.POST['next'])
            return redirect('account:dashboard')
        else:
            messages.error(request, 'Invalid credentials supplied.')
            return redirect('account:login')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('account:register')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('account:register')
                else:
                    user = CustomUser.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                            email=email, password=password1)
                    auth.login(request, user)
                    messages.success(request, 'Successfuly logged in')
                    return redirect('account:dashboard')
                    print('After return redirect')
                    user.save()
                    messages.success(request, 'Account created successfuly')

                    return redirect('account:login')
        else:
            messages.error(request,'Password does not match.')
            return redirect('account:register')
    return render(request, 'accounts/register.html')

@login_required
def dashboard(request):
    user_inquiries = Contact.objects.order_by('created_date').filter(user_id=request.user.id)
    paginator = Paginator(user_inquiries, 10)
    page = request.GET.get('page')
    paged_inquiries = paginator.get_page(page)

    return render(request, 'accounts/dashboard.html', {'user_inquiries':paged_inquiries})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('pages:home')
    return redirect('pages:home')
