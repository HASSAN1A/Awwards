from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page,name='home_page'),
    path('project/new',views.submit_project,name='submit_project'),
    path('search/projects',views.search_projects,name='search_projects'),
    path('view/project/<prj_id>',views.view_project,name='view_project'),
    path('view/my-profile',views.my_profile,name='my_profile'),
    path('api/profiles', views.ProfileList.as_view()),
    path('api/projects', views.ProjectsList.as_view()),
]