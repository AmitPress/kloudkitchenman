from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from stakeholders.models import Owner

# class CommonAuthBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         email = kwargs.get('email')
#         print(email)
#         try:
#             user = Owner.objects.get(email=email)
#             print(password, user.password)
#             if check_password(password=password, encoded=user.password):
#                 return user
#         except User.DoesNotExist:
#             return None
#         return None
