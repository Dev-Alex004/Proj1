from src.view.song_register_view import SongRegisterView
from src.controllers.song_register_controler import SongRegisterControler

# SongRegisterView -> Pascal Case (Classes)
# song_regiser_view -> Snake Case (Funções, métodos, variaveis)

def song_register_process():
    song_register_view = SongRegisterView()
    song_register_controler = SongRegisterControler()
    

    new_song_informations = song_register_view.registry_song_initial()
    response = song_register_controler.insert(new_song_informations)

    if response["success"]:
        song_register_view.registre_song_success(response)
    else:
        song_register_view.registry_song_fail(response)

