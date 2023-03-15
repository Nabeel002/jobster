from pyexpat import model
from models import UserProfile,Post


def extra(request,pk):
    profile = UserProfile.objects.get(pk=pk)
    user = profile.user
    return {
        'user': user,
        'profile': profile
    }