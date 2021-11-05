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
$ python manage.py migrate
```
4. Working with QuerySet in Django
refs: https://docs.djangoproject.com/en/3.2/ref/models/querysets/

## Custom Dashboard page
