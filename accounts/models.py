from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from .managers import UserManager
from django.conf import settings



class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=20,null=True)
    contact_number = models.CharField(max_length=10,null=True)
    about = models.TextField(null=True)
    email    = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    date_of_birth = models.DateField(null=True)
    company_name = models.CharField(max_length=30, null=True)
    designation = models.CharField(max_length=50, null=True)
    last_login_time = models.DateTimeField(null=True,blank=True)
    last_logout_time = models.DateTimeField(null=True,blank=True)
    is_active       = models.BooleanField(default=True)
    email_verified  = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
    

class question_model(models.Model):
    auto_question_id = models.AutoField(primary_key= True)
    question_title = models.CharField(max_length=100)
    question_description = models.TextField()
    technology_name = models.CharField (max_length=20)
    status_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)    
    user_question = models.ForeignKey(User, on_delete=models.CASCADE)
    

    class Meta:
        ordering = ('auto_question_id',)

    def get_questions(self):
        return ",".join([str(u) for u in self.user_question.all()])

    def __str__(self):
        return str(self.auto_question_id) + ',' + str(self.question_title)

class answer_model(models.Model):
    auto_answer_id = models.AutoField(primary_key= True)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
    like_and_dislike = models.IntegerField(null=True)
    technology_name = models.CharField (max_length=20)
    status_name = models.CharField(max_length=20)
    user_answer = models.ForeignKey(User, on_delete=models.CASCADE)
    questions_answers = models.ForeignKey(question_model,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.answer) 

    class Meta:
        ordering = ('auto_answer_id',)     

    def get_answers(self):
        return ",".join([str(q) for q in self.questions_answers.all()])


    def __str__(self):
        return str(self.answer)