from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def RegistrationValidator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Sorry I just can't accept 1 character as a first name unless you're Prince "
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Sorry I just can't accept 1 character as a last name unless you're Prince "
        UserRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not UserRegex.match(postData['email']):
            errors['email'] = "Must use a valid email"
        EmailCheck = User.objects.filter(email=postData['email'])
        if len(EmailCheck) > 0:
            errors['emailExists'] = "Already a user with this email in our database"
        if postData['password'] != postData['passwordC']:
            errors['passwordC'] = "Your password and confirm password do not match"
        return errors 

    def LoginValidator(self, postData):
        errors = {}
        LoginUser = User.objects.filter(email=postData['email'])
        if len(LoginUser) > 0:
            if bcrypt.checkpw(postData['password'].encode(), LoginUser[0].password.encode()):
                print("Password matches")
            else:
                errors['password'] = "Password does not match!"
        else:
            errors['email'] = "There is no user with that email"
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# Create your models here.
