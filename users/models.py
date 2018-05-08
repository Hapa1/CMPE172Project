from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Departments(models.Model):
    dept_no = models.CharField(primary_key=True, max_length=4)
    dept_name = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        app_label = "users"

class Dept(models.Model):
    dept_no = models.CharField(primary_key=True, max_length=4)
    dept_name = models.CharField(unique=True, max_length=40)

class DeptEmp(models.Model):
    emp_no = models.ForeignKey('Employees', models.DO_NOTHING, db_column='emp_no', primary_key=True)
    dept_no = models.ForeignKey(Departments, models.DO_NOTHING, db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        managed = False
        unique_together = (('emp_no', 'dept_no'),)
        app_label = "users"


class DeptManager(models.Model):
    emp_no = models.ForeignKey('Employees', models.DO_NOTHING, db_column='emp_no', primary_key=True)
    dept_no = models.ForeignKey(Departments, models.DO_NOTHING, db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        managed = False
        app_label = "users"
        unique_together = (('emp_no', 'dept_no'),)


#class Employees(models.Model):
#    emp_no = models.IntegerField(primary_key=True)
#    birth_date = models.DateField()
#    first_name = models.CharField(max_length=14)
#    last_name = models.CharField(max_length=16)
#    gender = models.TextField()  # This field type is a guess.
#    hire_date = models.DateField()
#
#    class Meta:
#        app_label = "users"
#        managed = False

class Lift(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField(primary_key=True, default=False)

    def __str__(self):
        return self.name

class Employees(models.Model):
    emp_id = models.IntegerField(primary_key=True, default=False)
    birth_date = models.DateField(default=timezone.now)
    first_name = models.CharField(max_length=14, blank=True)
    last_name = models.CharField(max_length=16, blank=True)
    gender = models.TextField(blank=True) 
    hire_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.first_name

class Profiles(models.Model):
    emp_id = models.IntegerField(primary_key=True, default=False)
    birth_date = models.DateField(default=timezone.now)
    first_name = models.CharField(max_length=14, blank=True)
    last_name = models.CharField(max_length=16, blank=True)
    gender = models.TextField(blank=True) 
    hire_date = models.DateField(default=timezone.now)

    class Meta:
        app_label = "users"

class Salaries(models.Model):
    emp_no = models.ForeignKey(Employees, models.DO_NOTHING, db_column='emp_no', primary_key=True)
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        app_label = "users"
        managed = False
        unique_together = (('emp_no', 'from_date'),)


class Titles(models.Model):
    emp_no = models.ForeignKey(Employees, models.DO_NOTHING, db_column='emp_no', primary_key=True)
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        app_label = "users"
        managed = False
        unique_together = (('emp_no', 'title', 'from_date'),)

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.BooleanField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    token = models.CharField(max_length=32)
    next_step = models.SmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)