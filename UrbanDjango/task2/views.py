from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def func(request):
    return render(request, 'second_task/func_template.html')


def test(request):
    return render(request, 'third_task/index.html')


def shop(request):
    text1 = "Отправиться в прошлое"
    text2 = "Отправиться в будущее"
    text3 = "Посетить параллельный мир"
    context = {
        "text1": text1,
        "text2": text2,
        "text3": text3,
    }
    return render(request, 'third_task/shop.html', context)


def basket(request):
    return render(request, 'third_task/basket.html')


class class_template(TemplateView):
    template_name = 'second_task/class_template.html'
