
from multiprocessing import context
from django.shortcuts import render, HttpResponseRedirect, redirect,get_object_or_404
from django.views import View
from .models import *
from .forms import CommentForm, JobUpload, PostForm, RequestForm, ResumeUpload
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models import Q


# Create your views here.


class PostListView(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        current_user=request.user
        profile=UserProfile.objects.get(user=current_user.id)
        posts = Post.objects.filter(author=current_user)
        form=PostForm()
        suggested_user = UserProfile.objects.exclude(user_id=request.user.id)
        context={
            'post_list':posts,
            'form':form,
            'profile':profile,
            'suggested_user':suggested_user
        }
        return render(request,'global/post_list.html',context=context)

    def post(self, request, *args, **kwargs):
        current_user=request.user
        posts=Post.objects.filter(author=current_user)
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return HttpResponseRedirect('/global')
            
        

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'global/post_list.html', context)

class PostDetailView(View):
    def get(self,request,pk,*args, **kwargs):
        profile = UserProfile.objects.all()
        # user=request.user
        post=Post.objects.get(pk=pk)
        comment_form=CommentForm()
        comments=Comment.objects.filter(post=post).order_by('-created_date')
        profile = UserProfile.objects.get(user=post.author)
        context={
            'form':comment_form,
            'post':post,
            'comments':comments,
            'profile':profile
        }

        return render(request,'global/post_detail.html',context)


    def post(self,request,pk,*args, **kwargs):
        post=Post.objects.get(pk=pk)
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.author=request.user
            new_comment.post=post
            new_comment.save()
        comments=Comment.objects.filter(post=post).order_by('-created_date')
        context={
            'form':comment_form,
            'post':post,
            'comments': comments,
            }

        
        return render(request, 'global/post_detail.html', context)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    


        


        





class DeletePost(DeleteView,UserPassesTestMixin,LoginRequiredMixin):
    model=Post
    success_url='/global'
    template_name='global/confirm_delete.html'


    def test_func(self):
        post=self.get_object()
        return reverse_lazy('post-list')






class UpdatePost(UpdateView,UserPassesTestMixin,LoginRequiredMixin):
    model=Post
    fields=["body",
    
    ]
    success_url='/'
    def test_func(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post_details', kwargs={'pk': pk})

 


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'global/comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post_details', kwargs={'pk': pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')
        followers = profile.followers.all()
        
            

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        number_of_followers = len(followers)
        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'number_of_followers':number_of_followers,
            'is_following':is_following
        }

    
        
        return render(request, 'global/profile.html', context)


class FeedView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        followers = profile.followers.all()
        posts = Post.objects.filter(author__in=followers)
      
            

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        number_of_followers = len(followers)
        context = {
            'profile': profile,
            'posts': posts,
            'number_of_followers':number_of_followers,
            'is_following':is_following,
            'follower':followers
        }

    
        
        return render(request, 'global/followers_feed.html', context)

        

    

   

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['name', 'proffession', 'birth_date', 'location', 'picture','resume']
    template_name = 'global/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


class ResumeCreation(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['resume','video_resume']
    template_name = 'global/resume.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user)

        return redirect('profile', pk=profile.pk)


class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect('profile', pk=profile.pk)


class ViewJobs(ListView):
    model=Jobs
    template_name='global/job_view.html'
 



class JobDeleteView(DeleteView):
    model = Jobs 
    template_name='global/job_delete.html'


class PostJob(CreateView):
    def get(self,request,*args, **kwargs):
        form=JobUpload()
        context={
            'form':form
        }

        return render(request,'global/job_creation.html',context=context)

    def post(self,request,*args, **kwargs):
        form = JobUpload(request.POST)
        if form.is_valid():
            new_job = form.save(commit=False)
            new_job.save()
            return HttpResponseRedirect('/global/jobs')
            
        

        context = {
            'form': form,
        }
        return render(request, 'global/job_creation.html', context=context)






class JobDetails(View):
    def get(self,request,pk,*args, **kwargs):
        profile = UserProfile.objects.all()
        job=Jobs.objects.get(pk=pk)
        print(job.pk)
        requests_form=RequestForm()
        requests=JobRequest.objects.filter(job=job)
        profile = UserProfile.objects.get(user=job.author)
        context={
            'form':requests_form,
            'jobs':job,
            'comments':requests,
            'profile':profile
        }

        return render(request,'global/job_detail.html',context)


    def post(self,request,pk,*args, **kwargs):
        job=Jobs.objects.get(pk=pk)
        requests_form = RequestForm(request.POST)
        if requests_form.is_valid():
            new_request=requests_form.save(commit=False)
            new_request.author=request.user
            new_request.job = job
            new_request.save()
            return redirect('/global/jobs',pk=job.pk)
        requests = JobRequest.objects.filter(
            job=job)
        context={
            'form':requests_form,
            'jobs':job,
            'requests': requests,
            }

        
        return render(request, 'global/job_detail.html', context)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author




class RequestViewer(View):
    def get(self,request,pk,*args, **kwargs):
        try:
            particular_job=Jobs.objects.get(pk=pk)
            job=Jobs.objects.filter(author=request.user)
            requests=JobRequest.objects.filter(pk=particular_job.pk).first()
        except ObjectDoesNotExist:
            return HttpResponse('<h1 class="is-size-2 has-text-centered">No jobs posted by you</h1>')
            


        context={
            'job':job,
            'requests':requests
        }

        return render(request,'global/job_request.html',context=context)



class RequestDetail(View):
    def get(self,request,pk,*args, **kwargs):
        job = Jobs.objects.get(pk=pk)
        requests = JobRequest.objects.filter(job=job)

       
        


        context={
            'requests':requests
        }

        return render(request,'global/request_view.html',context=context)



class UserSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = UserProfile.objects.filter(
            Q(user__username__icontains=query)
        )

        context = {
            'profile_list': profile_list,
        }

        return render(request, 'global/search.html', context)
