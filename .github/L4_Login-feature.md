## 1. Init model
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


2. Go to file _settings.py_: specify the custom model as the default user model for projec in setting file
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
# For all
$ python manage.py migrate

# For app
$ python manage.py migrate [app_name]
```
- Other:
```cmd
# displays the SQL statements for a migration
$ python manage.py sqlmigrate [app_name] [migration_name]

#ex: python manage.py sqlmigrate management 0001


# lists a project’s migrations and their status
$ python manage.py showmigrations
```
- Create supperuser
```cmd
$ python manage.py createsuperuser
> Email: admin@test.com
> Password: ******
> Password confirmation: ******
```

## 2. Custom form login in file _app_name/templates/layouts/login.html_
```python
<form class="user" method="POST" action="{% url 'login' %}">
    {% csrf_token %}
    <div class="form-group">
        <input type="email" name="email" class="form-control form-control-user"
            id="exampleInputEmail" aria-describedby="emailHelp"
            placeholder="Enter Email Address...">
    </div>
    <div class="form-group">
        <input type="password" name="password" class="form-control form-control-user"
            id="exampleInputPassword" placeholder="Password">
    </div>
    <div class="form-group">
        <div class="custom-control custom-checkbox small">
            <input type="checkbox" class="custom-control-input" id="customCheck">
            <label class="custom-control-label" for="customCheck">Remember Me</label>
        </div>
    </div>
    <button class="btn btn-primary btn-user btn-block">
        Login
    </button>
</form>
```

## 3. Implement LOGIN feature
1. Custom views _app_name/views.py_
```python
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, authenticate

def user_login(request, method="POST"):
    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        user = authenticate(email=email, password=password)

        if user is None:
            my_message = (
                "Your email address or password is incorrect. Please login again!"
            )

            return render(request, "layouts/login.html")

        login(request, user)
        return HttpResponseRedirect("dashboard/")

    return render(request, "layouts/login.html")
```

2. Update login url _app_name/urls.py_
```python
urlpatterns = [
    path("", views.user_login, name="login"),
    #something ...
]
```

3. Handle display message when login failure
- _app_name/views.py_
```python
# something
from django.contrib import messages


def user_login(request, method="POST"):
    if request.method == "POST":
        # something ...

        if user is None:
            my_message = (
                "Your email address or password is incorrect. Please login again!"
            )
            messages.error(request, my_message)

            return render(request, "layouts/login.html")

        # something ...
```
- Create new file in _app_name/templates/layouts/_ folder: __message.html_
```python
{% if messages %}
    <ul>
        {% for message in messages %}
            <p style="color: red;"> {{ message }} </p>
        {% endfor %}
    </ul>
{% endif %}
```
- In file _app_name/templates/layouts/login.html_
```python
<div>
    {% include "layouts/_message.html" %}
</div>
<form class="user" method="POST" action="{% url 'login' %}">
# something
</form>
```
## 4. Implement LOGOUT feature
1. _app_name/views.py_
```python
# something
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
```
2. Add logout url in _app_name/urls.py_
```python
urlpatterns = [
    # something... ,
    path("logout/", views.user_logout, name="logout"),
]
```
4. Go to file _app_name/templates/dashboard/index.html_, replace logout url
