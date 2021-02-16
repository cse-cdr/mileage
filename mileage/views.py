from django.shortcuts import render
from django.views import View
from .apps import *
from .models import *
from django.views.generic.list import ListView
from django.http import HttpResponse
# Create your views here.

class MainView(View):
    def get(self, request):
        if 'login_id' in request.session:
            user = User.objects.get(user_id=request.session['login_id'])
            mileage_history= Mileage.objects.filter(user=user.id)
            template_name = 'main.html'
            template_path = MileageConfig.name + '/' + template_name
            context={
                'user_id': request.session['login_id'],
                'object_list':mileage_history,
            }

            return render(request,template_path,context)

        else:
            template_name = 'login.html'
            template_path = MileageConfig.name + '/' + template_name
            context = {'mode': 'login', 'loginstate': False}

            return render(request,template_path,context)


class SignupView(View):
    def get(self,request):
        template_name = 'signup.html'
        template_path = MileageConfig.name + '/' + template_name

        return render(request, self.template_path, {})



class RegisterAccount(View):
    template_name = 'signup_result.html'
    template_path = MileageConfig.name + '/' + template_name

    def post(self,request):
        user_id = request.POST['user_id']
        pw = request.POST['pw']
        pw_repeat= request.POST['pw_repeat']

        isPwSame = False
        isSuccess = False
        isUserIdAlreadyExists=False

        if User.objects.filter(user_id=user_id).exists():
            isUserIdAlreadyExists = True
        elif (pw == pw_repeat):
                isPwSame = True
                user_info = User(user_id=user_id, password=pw)
                user_info.save()
                isSuccess = True

        
        context = {
            'isPwSame': isPwSame,
            'isSuccess': isSuccess,
            'isUserIdAlreadyExists': isUserIdAlreadyExists,
        }
        
        return render(request,self.template_path,context)

class LoginView(View):
    template_name = 'login.html'
    template_path = MileageConfig.name + '/' + template_name

    def get(self, request):
        context = {'mode':'login', 'loginstate':False}
        if 'store_name' in request.GET and 'point' in request.GET:
            StoreName = request.GET['store_name']
            point = request.GET['point']
            context['mode']='register_mileage'
            context |={
                'store_name': StoreName,
                'point': point,
            }
        if 'login_id' in request.session:
            context['user_id_login_'] = request.session['login_id']
            context['loginstate'] = True

        return render(request, self.template_path, context)

class LoginValidateView(View):
    template_name = 'login_validate.html'
    template_path = MileageConfig.name + '/' + template_name

    def post(self, request):
        user_id = request.POST['user_id']
        password = request.POST['password']

        isIdExist = False
        isPWCorrect = False
        isSuccess = False
        if User.objects.filter(user_id=user_id).exists():
            isIdExist = True
            user = User.objects.get(user_id=user_id)

            if user.password == password:
                isPWCorrect = True
                isSuccess =True
                request.session['login_id'] = user.user_id

        context = {
            'isIdExist': isIdExist,
            'isPWCorrect': isPWCorrect,
            'isSuccess': isSuccess,
        }
        return render(request, self.template_path, context)

class RegisterMileageView(View):
    def post(self, request):
        template_name = 'register_mileage.html'
        template_path = MileageConfig.name + '/' + template_name
        user_id = request.POST['user_id']
        password = request.POST['password']

        store_name =request.GET['store_name']
        point = request.GET['point']

        isIdExist = False
        isPWCorrect = False
        isSuccess = False
        if User.objects.filter(user_id=user_id).exists():
            isIdExist = True
            user = User.objects.get(user_id=user_id)

            if user.password == password:
                isPWCorrect = True
                if not Store.objects.filter(name=store_name).exists():
                    store=Store(name=store_name)
                    store.save()
                store = Store.objects.get(name=store_name)

                mileage = Mileage(store=store, user=user,point=point)
                mileage.save()

                isSuccess = True



        context = {
            'isIdExist': isIdExist,
            'isPWCorrect': isPWCorrect,
            'isSuccess': isSuccess,
            'userid': user_id,
            'point': point,
        }
        return render(request, template_path, context)

class MileageHistoryView(ListView):
    model = Mileage
    template_name = "mileage/mileage_history.html"

