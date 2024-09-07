from django.urls import path
from .views import (
    course, course_detail, trainer, edit_comment
)


app_name = "course"

urlpatterns = [
    path("", course, name="courses"),
    path("category/<str:catname>", course, name="courses_category"),
    path("trainer/<str:tr>", course, name="courses_trainer"),
    path("price/<str:pr>", course, name="course_price"),
    path("detail/<int:id>", course_detail, name="course_detail"),
    path("trainer", trainer, name="trainers"),
    path("comment/<int:id>", edit_comment, name="edit-comment"),
    
]