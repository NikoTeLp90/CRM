from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (home, 
                    createUser,
                    userCreationSuccess, 
                    login, 
                    userList,
                    userEdit,
                    userDelete,
                    SearchUser,
                    SearchResults,
                    suspenderHabilitarUsuario,
                    createCompany,
                    companyIndex,
                    CompanyIndexView)

urlpatterns = [
    path('', login_required(companyIndex.as_view()), name='index'),
    path('createuser/', createUser.as_view(), name = 'createuser'),
    path('usercreationsuccess/', userCreationSuccess.as_view(), name = 'usercreationsuccess'),
    path('login/', login.as_view(), name ="login"),
    path('userList/', userList.as_view(), name ="userList"),
    path('edituser/<int:pk>/',userEdit.as_view(),name="edituser"),
    path('userdelete/<int:pk>/',userDelete.as_view(),name="userDelete"),
    path('search/', SearchUser.as_view(), name='search_user'),
    path('searchresult/', SearchResults.as_view(), name='search_results'),
    path('suspenderHabilitarUsuario/<int:pk>',suspenderHabilitarUsuario.as_view(),name="suspenderHabilitarUsuario"),


    #Compañias
    path('createcompany/',login_required(createCompany.as_view()),name="createcompany"),
    path('company/<int:company_id>/', login_required(CompanyIndexView.as_view()), name='company_index'),
]
