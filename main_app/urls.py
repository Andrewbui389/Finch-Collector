from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finches_index, name='Finches'),
  path('finches/<int:finch_id>', views.detail , name='detail'),
  path('finches/create', views.CreateFinch.as_view() , name='new_finch'),
  path('finches/<int:pk>/delete/', views.DeleteFinch.as_view(), name='delete_finch'),
  path('finches/<int:pk>/edit/', views.EditFinch.as_view(), name='edit_finch'),
  path('finches/<int:finch_id>/feed/', views.feed_finch , name='feed_finch'),
  path('blades/', views.BladeList.as_view(), name='blade_index'),
  path('blades/create/', views.BladeCreate.as_view(), name='blade_create'),
  path('blades/<int:pk>/', views.BladeDetail.as_view(), name='blade_details'),
  path('blades/<int:pk>/delete/', views.BladeDelete.as_view(), name='blade_delete'),
  path('blades/<int:pk>/update/', views.BladeUpdate.as_view(), name='blade_update'),


]