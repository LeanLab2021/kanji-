from .views import Bloglist,BlogCreate,BlogDetail,BlogDelete,BlogUpdate
from django.urls import path



urlpatterns = [
    path('create/',BlogCreate.as_view(),name='create')
    
]    

urlpatterns.append(path('list/',Bloglist.as_view(),name='list'))
urlpatterns.append(path('detail/<int:pk>',BlogDetail.as_view(),name='detail'))    
urlpatterns.append(path('delete/<int:pk>',BlogDelete.as_view(),name='delete'))   
urlpatterns.append(path('update/<int:pk>',BlogUpdate.as_view(),name='update'))
 
    


