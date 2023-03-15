from django import views
from . import views
from django.urls import path
from .views import *


urlpatterns = [
    path('',PostListView.as_view(),name='post-list'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post_details'),
    path('<pk>/delete/', DeletePost.as_view(),name='post_remove'),
    path('<int:pk>', JobDeleteView.as_view(),name='delete'),
    path('<pk>/edit',UpdatePost.as_view(),name='edit'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/',CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/<int:pk>/',ProfileView.as_view(), name='profile'),
    path('feed/<int:pk>/',FeedView.as_view(), name='feed'),
    path('profile/edit/<int:pk>',ProfileEditView.as_view(),name='profile_edit'),
    path('profile/upload/<int:pk>', ResumeCreation.as_view(), name='resume_upload'),
    path('profile/<int:pk>/followers/add',AddFollower.as_view(),name='follow'),
    path('profile/<int:pk>/followers/remove',RemoveFollower.as_view(),name='remove'),
    path('jobs/create',PostJob.as_view(),name='create_job'),
    path('jobs',ViewJobs.as_view(),name='jobs'),
    path('job/<int:pk>', JobDetails.as_view(), name='job_details'),
    path('job/posted/<int:pk>', RequestViewer.as_view(), name='request'),
    path('job/requests/<int:pk>', RequestDetail.as_view(), name='posters'),
    path('search/', UserSearch.as_view(), name='profile-search'),





]
