from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        # this part
        else:
            if user.check_password(password):
                return user
        return None

# from django.contrib.auth import get_user_model  # gets the user_model django  default or your own custom
# from django.contrib.auth.backends import ModelBackend
# from django.db.models import Q


# # Class to permit the athentication using email or username
# class CustomBackend(ModelBackend):  # requires to define two functions authenticate and get_user

#     def authenticate(self, username=None, password=None, **kwargs):
#         UserModel = get_user_model()

#         try:
#             # below line gives query set,you can change the queryset as per your requirement
#             user = UserModel.objects.filter(
#                 Q(username__iexact=username) |
#                 Q(email__iexact=username)
#             ).distinct()

#         except UserModel.DoesNotExist:
#             return None

#         if user.exists():
#             ''' get the user object from the underlying query set,
#             there will only be one object since username and email
#             should be unique fields in your models.'''
#             user_obj = user.first()
#             if user_obj.check_password(password):
#                 return user_obj
#             return None
#         else:
#             return None

#     def get_user(self, user_id):
#         UserModel = get_user_model()
#         try:
#             return UserModel.objects.get(pk=user_id)
#         except UserModel.DoesNotExist:
#             return None



# from django.contrib.auth.backends import ModelBackend, UserModel
# from django.db.models import Q

# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try: #to allow authentication through phone number or any other field, modify the below statement
#             user = UserModel.objects.get(Q(email__iexact=username))
#         except UserModel.DoesNotExist:
#             UserModel().set_password(password)
#         except MultipleObjectsReturned:
#             return User.objects.filter(email=username).order_by('id').first()
#         else:
#             if user.check_password(password) and self.user_can_authenticate(user):
#                 return user

#     def get_user(self, user_id):
#         try:
#             user = UserModel.objects.get(pk=user_id)
#         except UserModel.DoesNotExist:
#             return None

#         return user if self.user_can_authenticate(user) else None
