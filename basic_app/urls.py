from django.urls import path
from . import views

urlpatterns = [
                path('',views.new,name='new'),
                path('',views.index, name='index'),
                path('<int:question_id>',views.details,name='details'),
                path('<int:question_id>',views.results,name='results'),
                path('<int:question_id>',views.vote,name='vote'),
]


# list ka synatx is []
#tuple ka syntax is ()
