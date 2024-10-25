from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'fourth_task/0_mp_template.html')


def herbs_page(request):
    context = {
        'herbs': [
            ('Зеленоцвет', "Снимает усталость"),
            ('Цветущий зеленоцвет', "Лечит переутомление"),
            ('Пурпурный мох', "Лечит отравление"),
            ('Цветущий пурпурный мох', "Выводит яды и токсины")
        ]

    }
    return render(request, 'fourth_task/1_page_template.html', context)


def status_page(request):
    return render(request, 'fourth_task/2_page_template.html')