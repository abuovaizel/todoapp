from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (
    Login,
    Register,
    TaskCreate,
    TaskDelete,
    TaskDetail,
    TaskList,
    TaskUpdate
)

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", Register.as_view(), name="register"),
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(), name="task-delete"),
]
