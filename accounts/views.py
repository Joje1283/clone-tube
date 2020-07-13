from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('password')

    return render(request, 'accounts/login.html')