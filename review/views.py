# from .serializers import CommentSerializer, RatingSerializer
# from .models import Comment, RatingUser
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import AllowAny
# from .permissions import IsAuthorOrReadOnly


# class PermissionMixin:
#     def get_permissions(self):
#         if self.action == 'create':
#             permissions = [IsAuthorOrReadOnly]
#         elif self.action in ['update', 'partial_update', 'destroy']:
#             permissions = [IsAuthorOrReadOnly]
#         else:
#             permissions = [AllowAny]
#         return [permission() for permission in permissions]



# class CommentViewSet(PermissionMixin ,ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [PermissionMixin]

    
# class RatingViewSet(PermissionMixin, ModelViewSet):
#     queryset = RatingUser.objects.all()
#     serializer_class = RatingSerializer
#     permission_classes = [PermissionMixin]

from .serializers import CommentSerializer, RatingSerializer
from .models import Comment, RatingUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .permissions import IsAuthorOrReadOnly

class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthorOrReadOnly]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorOrReadOnly]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]

class CommentViewSet(PermissionMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthorOrReadOnly]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorOrReadOnly]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]
    
class RatingViewSet(PermissionMixin, ModelViewSet):
    queryset = RatingUser.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthorOrReadOnly]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorOrReadOnly]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]

# [Unit]
# Description=gunicorn daemon
# Requires=gunicorn.socket
# After=network.target

# [Service]
# User=sultanhoja228
# Group=www-data
# WorkingDirectory=/home/sultanhoja228/jetkir
# ExecStart=/home/sultanhoja228/jetkir/venv/bin/gunicorn \
#           --access-logfile - \
#           --workers 3 \
#           --bind unix:/run/gunicorn.sock \
#           main.wsgi:application

# [Install]
# WantedBy=multi-user.target


# ALTER ROLE sultanhoja228 SET client_encoding TO 'utf8';
# ALTER ROLE sultanhoja228 SET default_transaction_isolation TO 'read committed';
# ALTER ROLE sultanhoja228 SET timezone TO 'UTC';

# GRANT ALL PRIVILEGES ON DATABASE jetkir TO sultanhoja228;