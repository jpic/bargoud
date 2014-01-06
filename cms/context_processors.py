from .models import Photo


def home_photos(request):
    return {'home_photos': Photo.objects.filter(on_home=True)}
