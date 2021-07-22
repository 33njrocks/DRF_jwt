from django.contrib.auth.base_user import BaseUserManager

# To manage our custom user django needs a manager. Since our user is not default user of django , so our manager
# has to be defined seperately.

class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user    

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(("Superuser must have is_staff True"))

        return self.create_user(email,password,**extra_fields) 
