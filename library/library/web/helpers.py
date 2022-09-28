from library.web.models import Profile


def get_profile():
    profiles=Profile.objects.all()

    if profiles:
        return profiles[0]
    return None
