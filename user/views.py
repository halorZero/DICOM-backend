from django.http import JsonResponse
from django.views import View
from .models import User


class Users(View):
    mode = 0

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        if self.mode == 0:  # login
            try:
                user = User.objects.get(username=username)
            except:
                return JsonResponse({'errno': 1001, 'msg': "用户不存在"})
            password = request.POST.get('password')
            if user.password == password:
                return JsonResponse({'errno': 0, 'msg': "登录成功"})
            else:
                return JsonResponse({'errno': 1002, 'msg': "密码错误"})
        elif self.mode == 1:  # register
            users = User.objects.filter(username=username)
            if len(users) != 0:
                return JsonResponse({'errno': 1003, 'msg': "用户名已被占用"})
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password2 != password1:
                return JsonResponse({'errno': 1004, 'msg': "两次输入的密码不相同"})
            name = request.POST.get('name')
            sex = request.POST.get('sex')
            profile = request.POST.get('profile')
            new_user = User(username=username, password=password1, name=name, sex=sex, profile=profile)
            new_user.save()
            return JsonResponse({'errno': 0, 'msg': "注册成功"})



