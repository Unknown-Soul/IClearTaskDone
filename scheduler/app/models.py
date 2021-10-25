from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password

class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name,
                    dateOfBirth, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have an first name")
        if not last_name:
            raise ValueError("Users must have an last name")
        if not dateOfBirth:
            raise ValueError("Users must have an date of birth")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            dateOfBirth=dateOfBirth,
        )
        user.password = make_password(password)
        user.save(using=self._db)
        print("created user")
        return user

    def create_superuser(self, email, first_name, last_name,
                         dateOfBirth, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            dateOfBirth=dateOfBirth,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        print('my user manager')
        return user


# Create your models here.
class MyUser(AbstractBaseUser):
    user_identification = models.CharField(
        max_length=6, primary_key=True, editable=False, unique=True)
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    dateOfBirth = models.DateField(verbose_name='Date Of Birth')
    image = models.FileField(blank=True, null=True,
                             default='NO_CONTRACT_UPLOADED', upload_to='images/')
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'dateOfBirth']

    objects = MyAccountManager()

    def save(self, *args, **kwargs):
        if not self.user_identification:
            self.user_identification = get_random_string(6)
        return super(MyUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    # if user is admin, can chenge
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def staff(self):
        return self.is_staff

    @property
    def active(self):
        return self.is_active



class IP(models.Model):
    Id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=100)
    hour = models.CharField(max_length=2)
    minute = models.CharField(max_length=2)
    second = models.CharField(max_length=2)
    status = models.CharField(default="Down",max_length=10)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.ip
