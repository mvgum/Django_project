from django.shortcuts import render


def ind(request):
    return render(request, 'fourth_task/index.html')


def shop(request):
    context = {'text': ["Отправиться в прошлое", "Отправиться в будущее", "Посетить параллельный мир"]}
    return render(request, 'fourth_task/shop.html', context)


def basket(request):
    return render(request, 'fourth_task/basket.html')
