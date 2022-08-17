from django.shortcuts import render


def sign_up(request):
    return render(request, 'sign_up.html')


def userpage(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    print(email)
    print(password)
    return render(request, 'userpage.html')


def send_email(request):
    print("sending email")
    print("sent successfully")
    return render(request, 'index.html')


def automate(request):
    return render(request, 'automate.html')


def autoresponder(request):
    return render(request, 'autoresponder.html')


def ecommerce(request):
    return render(request, 'ec_mktn.html')


def blank(request):
    return render(request, 'blank.html')
