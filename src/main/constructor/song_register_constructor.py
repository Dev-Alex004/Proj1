from src.view.song_register_view import SongRegisterView

# SongRegisterView -> Pascal Case (Classes)
# song_regiser_view -> Snake Case (Funções, métodos, variaveis)

def song_register_process():
    song_register_view = SongRegisterView()
    # Instancia do controller

    new_song_informations = song_register_view.registry_song_initial()
    # enviar para new_song_informations para controller