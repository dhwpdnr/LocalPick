from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, phone_number, password, is_staff, is_superuser, **extra_fields):
        if not phone_number:
            raise ValueError("user must have phone number")
        now = timezone.now()
        user = self.model(
            phone_number=phone_number,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields,
        )
        if password:
            user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        user = self._create_user(phone_number, password, False, False, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        user = self._create_user(phone_number, password, True, True, **extra_fields)
        user.username = f"admin-{user.id}"
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, phone_number):
        return self.get(phone_number=phone_number)


class User(AbstractUser):
    username = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=20, unique=True)
    birth = models.DateField(null=True)
    gender = models.CharField(max_length=1, null=True)
    nickname = models.CharField(max_length=15, unique=True, null=True)
    
    objects = UserManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self):
        return "<%d %s>" % (self.pk, self.phone_number)

    class Meta:
        # 테이블 명 정하기 가능
        db_table = "User"
