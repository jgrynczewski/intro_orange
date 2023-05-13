from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout

User = get_user_model()


# Create your views here.
def index(request):
    users = User.objects.all()
    print(users)

    # Tworzenie użytkownika
    # nie możemy użyć metody create menadżera modelu, bo create nie hashuje hasła. Zamiast tego używamy metody
    # create_user
    # User.objects.create_user(username='test4', password='tajne')

    # Uwierzytelnienie użytkownika
    # metoda filter i get ma ten sam problem co metoda create, bo hasło jest zahashowane.
    # Jeżeli uwierzytelnienie się nie powiedzie
    result = authenticate(username='admin', password='błędne hasło')
    print(result)  # to metoda authenticate zwróci None

    # a w przypadku pomyślnego uwierzytlenienia
    user = authenticate(username='admin', password='admin')
    print(user)  # metoda authenticate zwróci obiekty klasy User, będący uwierzytelnionym użytkownikiem

    # uwierzytelnionego użytkownika możemy zalogować
    if user:
        login(request, user=user)  # logowanie to: utworzenie sesji, wygenerowanie klucza sesji, wprowadzenie user_id
        # do danych sesji (tzw. sesja uwierzytelniona) i żądanie ustawienia ciasteczka z kluczem sesji (sessionid)

    # wylogowanie
    logout(request)

    return render(
        request,
        'auth_app/index.html',
    )


def login_view(request):
    if request.method == 'GET':
        print(request.user)

        return render(
            request,
            'auth_app/login.html',
        )
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user=user)

        return redirect('auth_app:login')


def logout_view(request):
    logout(request)

    return redirect('auth_app:login')