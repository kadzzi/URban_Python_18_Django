from django.shortcuts import render
from .forms import UserRegister


users_bank = [
    "Vasya",
    "Petya",
    "Belka99"
]


def is_valid_user_data(username_, password_, repeat_password_, age_):
    if (username_ not in users_bank) and (password_ == repeat_password_) and (int(age_) >= 18):
        return [True]
    elif password_ != repeat_password_:
        return [False, 'Пароли не совпадают!']
    elif int(age_) < 18:
        return [False, 'Вы должны быть старше 18!']
    elif username_ in users_bank:
        return [False, f'Пользователь {username_} уже существует!']


# Create your views here.
def sign_up_by_html(request):
    info = dict()
    if request.method == 'POST':
        # Получаем данные:
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Проверяем данные:
        valid_result = is_valid_user_data(username, password, repeat_password, age)

        if valid_result[0]:
            info['success'] = f"Приветствуем, {username}!"
            users_bank.append(username)
            print(f'Новый пользователь: {username}\tВсе пользователи: {sorted(users_bank)}')
        else:
            info['error'] = valid_result[1]

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    info = dict()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        info['form'] = form

        if form.is_valid():
            # Получаем данные:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверяем данные:
            valid_result = is_valid_user_data(username, password, repeat_password, age)

            if valid_result[0]:
                info['success'] = f"Приветствуем, {username}!"
                users_bank.append(username)
                print(f'Новый пользователь: {username}\tВсе пользователи: {sorted(users_bank)}')
            else:
                info['error'] = valid_result[1]

    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'fifth_task/registration_page.html', info)
