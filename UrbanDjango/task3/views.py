from django.shortcuts import render


def ind(request):
    return render(request, 'third_task/index.html')


def shop(request):
    context = {
        "text1": "Отправиться в прошлое",
        "text2": "Отправиться в будущее",
        "text3": "Посетить параллельный мир",
    }
    return render(request, 'third_task/shop.html', context)


def basket(request):
    return render(request, 'third_task/basket.html')
