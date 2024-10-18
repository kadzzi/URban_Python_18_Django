from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'third_task/0_mp_template.html')


def herbs_page(request):
    return render(request, 'third_task/1_page_template.html')


def status_page(request):
    return render(request, 'third_task/2_page_template.html')
