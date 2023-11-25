from django.shortcuts import render
from .models import Comment

MENU = {"Персонажи": "/", "О блоге": "/about", "Комментарии": '/comments'}


def comment_page(request):
    fullName = request.POST.get('fullName')
    email = request.POST.get('email')
    text = request.POST.get('text')

    if fullName and email and text:
        Comment.objects.create(fullName=fullName, email=email, text=text)
    comments = Comment.objects.filter(checked=True)
    data = {"menu": MENU, "comments": comments}
    return render(request, './comments.html', context=data)