from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import  User,question_model, answer_model
from .forms import UserForm, RegisterUserForm,answer_form, question_form
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import viewsets
from . serializers import UserSerializer, answer_serializer, question_serializer,Questio_serializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.db.models import Q

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    def get_instance(self):
        return self.request.user

    def user_profile(self, request, pk):
        obj = self.get_object()
        serializer = self.UserSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return redirect('index')
        return render(request, 'register1.html')


def profile(request):
    form = RegisterUserForm()
    print(1)
    if request.method == 'POST':
        
        pro = RegisterUserForm(request.POST,instance=request.user)
        
        if pro.is_valid():
            pro.save()
            return redirect('index')
           

    context = {
        'form': form
    }
    return render(request, 'detail.html', context)

def view_profile(request):
    profile = request.user 
    return render(request, 'View_profile.html', {'profile':profile})

def homePage(request):
    User1 = User.objects.all()
    return render(request, 'homepage.html')

#Question Answer
class questionViewSet(viewsets.ModelViewSet):
    queryset = question_model.objects.all()
    serializer_class = Questio_serializer
    permission_classes = [AllowAny]
    #http_method_names = ['get','post','put']

    def get_instance(self):
        return self.request.user
    
    def user_profile(self, request, pk):
        obj = self.get_object()
        serializer = self.Questio_serializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return redirect('index')
        return render(request, 'register1.html')

class answerViewSet(viewsets.ModelViewSet):
    queryset = answer_model.objects.all()
    serializer_class = answer_serializer
    permission_classes = [AllowAny]
    def get_instance(self):
        return self.request.user

    def user_profile(self, request, pk):
        obj = self.get_object()
        serializer = self.answer_serializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return redirect('index')
        return render(request, 'register1.html')



def base_view(request):
    ques = question_model.objects.all()
    usr = User.objects.all()
    ans = answer_model.objects.all()
    return render(request, 'question_template/question_home.html', {'questions': ques, 'users': usr, 'answers':ans})

def all_questions(request):
    ques = question_model.objects.all()
    ans = answer_model.objects.all()
    return render (request, 'question_template/view_question.html', {'questions': ques, 'answers':ans})


def detailed_view_of_individual_question(request, pk):
    ques = question_model.objects.get(auto_question_id = pk)
    return render(request, 'question_template/individual_detailed_question_template.html', {'question': ques})


def all_answers(request, pk):
    ans = answer_model.objects.filter(questions_answers = pk)
    ques = question_model.objects.filter(auto_question_id = pk)
    #ans1 = answer_model.objects.all()
    print('ans',ans)
    return render(request, 'answer_template/answer_template.html', {'answers': ans,'questions': ques})


def searched_vlaue(request):
    if request.method == "POST":
        searched = request.POST['searched']
        detail = User.objects.filter(Q(auto_user_id = searched))
        return render(request, 'search_template/search_template.html', {'search': searched, 'user_detail': detail} )
    else:
        return render(request, 'search_template/search_template.html', {})


def ask_question(request):
    new_question_form = question_form()
    if request.method == 'POST':
        new_question_form = question_form(request.POST)
        if new_question_form.is_valid():
            new_question_form.save()
        return redirect(base_view)
    return render(request, 'form_template/ask_question_form.html', {'form': new_question_form} )


def provide_your_answer(request):
    new_answer_form = answer_form()
    if request.method == 'POST':
        new_answer_form = answer_form(request.POST)
        if new_answer_form.is_valid():
            new_answer_form.save()
        return redirect(base_view)
    return render(request, 'form_template/create_your_answer_form.html', {'form': new_answer_form})