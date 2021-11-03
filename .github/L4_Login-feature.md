## 1. Update form in file `login.html`

## 2. Init model
refs: https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#custom-users-and-proxy-models
1. Go to file _app_name/models.py_
```python
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Define model here

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
```


2. Go to file _settings.py_
```python
AUTH_USER_MODEL = 'app_name.MyUser'
```

3. Apply the change of Database
- Create migrations: creating new migrations based on the changes you have made to your models.
```
$ python manage.py makemigrations
```
- Apply migration: applying and unapplying migrations
```
$ python manage.py migrate
```
- Other:
```cmd
# displays the SQL statements for a migration
$ python manage.py sqlmigrate

# lists a project’s migrations and their status
$ python manage.py showmigrations
```
