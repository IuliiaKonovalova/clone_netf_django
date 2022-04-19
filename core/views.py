from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Profile, Movie


class HomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(
                request,
                'profile_list.html',
                {'profiles': request.user.profile.all()}
            )
        return render(request, 'home.html')


@method_decorator(login_required, name='dispatch')
class ProfileListView(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profile.all()
        return render(
            request,
            'profile_list.html',
            {'profiles': profiles}
        )


@method_decorator(login_required,name='dispatch')
class ProfileCreate(View):
    def get(self,request,*args, **kwargs):
        form=ProfileForm()

        return render(
            request,
            'profile_create.html',
            {"form": form}
        )

    def post(self,request,*args, **kwargs):
        form=ProfileForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profile.add(profile)
                return redirect(f'/watch/{profile.uuid}')

        return render(request,'profile_create.html',{
            'form':form
        })


@method_decorator(login_required,name='dispatch')
class WatchView(View):
    def get(self,request,profile_id,*args, **kwargs):
        try:
            profile=Profile.objects.get(uuid=profile_id)

            movies=Movie.objects.filter(age_limit=profile.age_limit)

            try:
                showcase=movies[0]
            except :
                showcase=None
            

            if profile not in request.user.profile.all():
                return redirect(to='core:profile_list')
            return render(
                request,
                'movie_list.html',{
                'movies':movies,
                'show_case':showcase,
                'profile':profile
                }
            )
        except Profile.DoesNotExist:
            return redirect(to='core:profile_list')