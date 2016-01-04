# Test project for a possible Django 1.8.7/1.9.1 bug

This project defines a model app.MyModel which has a CharField.

- The initial migration for the app defines the CharField with db_index=True set.
- Migration 0002 alters the CharField to also set unique=True as well as `db_index=True.

When migration 0002 is run on postgresql the following error occurs:

```
django.db.utils.ProgrammingError: relation "app_mymodel_my_field_3922656f_like" already exists
```

The SQLite and MySQL backends work though.
