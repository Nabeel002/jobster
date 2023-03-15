from cProfile import label
from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Comment, JobRequest, Jobs, Post, UserProfile

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'name':'body', 
            'rows': '7',
            'placeholder': 'Say Something...'
        }))

    
    class Meta:
        model=Post
        fields=['body']
      

class CommentForm(forms.ModelForm):
    text=forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'input',
            'name':'body', 
            'rows': '2',
            'placeholder': 'Add a comment...'
        }))

    class Meta:
        model=Comment
        fields=["text"]

class ResumeUpload(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['resume','video_resume']

  


class JobUpload(forms.ModelForm):
    class Meta:
        model=Jobs
        fields=['description','company_name','job_title','salary','location']



class RequestForm(forms.ModelForm):
    class Meta:
        model=JobRequest
        fields=['request']

        

