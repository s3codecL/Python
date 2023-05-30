usuarios = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
id_usuario = '004'

try:
    print(usuarios[id_usuario])
except KeyError:
    print('La clave {} no está en el diccionario. \nAgregando clave... \nCargando...'.format(id_usuario))
    usuarios[id_usuario] = 'Ninguno'
    print(usuarios)