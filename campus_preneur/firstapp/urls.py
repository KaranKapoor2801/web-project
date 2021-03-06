from django.urls import path
from firstapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name="firstapp"

urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path("login/",views.login_user, name="login"),
    path("register/",views.register_user, name="register"),
    path("dashboard/<int:current_level>/<int:rank>/",views.go_to_dashboard, name="dashboard"),
    path("logout/",views.logout_user, name="logout"),
    path("thanks/",views.thanks_for_logging, name="thanks"),
    path('question/<int:q_no>/',views.go_to_question,name='question_current'),
    path('complete/task/',views.complete_task,name="complete_task"),
    path('leaderboard/',views.get_leaderboard,name="leaderboard"),
    path('developers/',views.go_to_developers,name='developers'),
    path('commingsoon/', views.comming_soon, name="commingsoon"),
    path('contact/', views.contact, name="contact"),
    path('rules/', views.rules, name="rules"),
]
