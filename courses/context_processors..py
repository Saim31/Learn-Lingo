from .models import Language

def languages_processor(request):
    return {
        'languages': Language.objects.all()
    }
