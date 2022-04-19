from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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


