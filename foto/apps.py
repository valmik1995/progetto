from django.apps import AppConfig


class FotoConfig(AppConfig):
    name = 'foto'
    
    def ready (self): 
        import foto.signals
