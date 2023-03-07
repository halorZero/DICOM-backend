from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views import View

from .models import MyUser as User


class Users(View):
    name = ''

    def post(self, request):
        username = request.POST.get('username')
        if self.name == 'register':
            user_filter = User.objects.filter(username=username)
            if len(user_filter) >= 1:
                return JsonResponse({'errno': 1000, 'msg': "username has been used"})
            pwd1 = request.POST.get('pwd1')
            pwd2 = request.POST.get('pwd2')
            if pwd1 != pwd2:
                return JsonResponse({'errno': 1001, 'msg': "password unmatch"})
            User.objects.create_user(username=username, password=pwd1)
            return JsonResponse({'errno': 0, 'msg': "register success"})
        elif self.name == 'login':
            pwd = request.POST.get('pwd')
            user = authenticate(username=username, password=pwd)
            if not user:
                return JsonResponse({'errno': 1002, 'msg': "wrong password"})
            login(request, user)
            return JsonResponse({'errno': 0, 'msg': "login success"})

    def get(self, request):
        if self.name == 'logout':
            logout(request)
            return JsonResponse({'errno': 0, 'msg': "logout success"})


class Update(View):
    name = ''

    def post(self, request):
        if self.name == 'avatar':
            session_store = request.session
            if len(session_store.items()) == 0:
                return JsonResponse({'errno': 1003, 'msg': "please login first"})
            user = User.objects.get(id=session_store.get('_auth_user_id'))
            avatar = request.FILES.get('avatar')
            user.avatar = avatar
            user.save()
            return JsonResponse({'errno': 0, 'msg': "update avatar success"})
        elif self.name == 'info':
            session_store = request.session
            if len(session_store.items()) == 0:
                return JsonResponse({'errno': 1003, 'msg': "please login first"})
            user = User.objects.get(id=session_store.get('_auth_user_id'))
            email = request.POST.get('email')
            bio = request.POST.get('bio')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            user.email = email
            user.bio = bio
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return JsonResponse({'errno': 0, 'msg': "update info success"})
        elif self.name == 'pwd':
            session_store = request.session
            if len(session_store.items()) == 0:
                return JsonResponse({'errno': 1003, 'msg': "please login first"})
            user = User.objects.get(id=session_store.get('_auth_user_id'))
            pwd = request.POST.get('pwd')
            new_pwd = request.POST.get('new_pwd')
            auth_user = authenticate(username=user.username, password=pwd)
            if not auth_user:
                return JsonResponse({'errno': 1002, 'msg': "wrong password"})
            user.set_password(new_pwd)
            user.save()
            return JsonResponse({'errno': 0, 'msg': 'change password success'})
