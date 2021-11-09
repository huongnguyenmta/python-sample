## Complete the Login and Logout feature
refs: https://github.com/huongnguyenmta/python-sample/blob/main/.github/L4_Login-feature.md

## Setup tool connect MySQL
refs: https://computingforgeeks.com/install-and-configure-dbeaver-on-ubuntu-debian/

## Init all models
1. Reference to Group's requirement (created google sheet file for each group)
2. Define:
refs: https://docs.djangoproject.com/en/3.2/topics/db/models/
- Model name (class model name)
- Field name
- Field types (refs: https://docs.djangoproject.com/en/3.2/ref/models/fields/#module-django.db.models.fields)
- Relationship with another model (refs: https://docs.djangoproject.com/en/3.2/topics/db/models/#relationships)
3. Apply the changes
- Create file migrations:
```
$ python manage.py makemigrations
```
- Apply changes to DB
```
# Apply for all
$ python manage.py migrate

# Apply for project app
$ python manage.py migrate app_name
```
4. Working with QuerySet in Django
refs: https://docs.djangoproject.com/en/3.2/ref/models/querysets/
- Working with django shell
```cmd
$ python manage.py shell
```
- Interact with DB with shell
```cmd
> from app_name.models import MyUser

# Get all objects in a table. ex: list all of users (model: MyUser)
> MyUser.objects.all()

# Check the exist of any user in users: return `True/False`
> MyUser.objects.exists()

# Get an object by id: return object
> MyUser.get(id=1)

# Filter objects are matched by condition: return QuerySet
> MyUser.objects.filter(id=1)
> MyUser.objects.filter(first_name__contains="H")
> MyUser.objects.filter(first_name__contains="h")
> MyUser.objects.filter(first_name__startswith="H")
...

# Create an object and save it
> MyUser.objects.create(email="user1@test.com")

# Returns a tuple of (object, created): if found: get and created='False', if not: create and created=`True`
> MyUser.objects.get_or_create(email="user1@test.com")
...

# `Field lookups`
> MyUser.objects.filter(id_exact=1)

# Filter objects are not match by condition: return QuerySet
> MyUser.objects.exclude(id=1)
```

## Custom Dashboard page
