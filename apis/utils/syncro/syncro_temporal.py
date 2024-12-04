import os
import shutil

def Archivo_temporal(suministro):
    if suministro.endswith('.pdf'):
        # lista = os.getcwd().split('/')
        # ots = lista[1:-1]
        # print(os.path.join(*ots,'pdf'))
        # paths = os.path.join(*ots,'pdf')

        paths = os.path.join(os.getcwd(),'pdf') 
        os.makedirs(paths, exist_ok=True)
        shutil.move(suministro, os.path.join(paths,suministro))

        # linea para vps
        os.remove(suministro.replace('.pdf', '.TIF'))

    if suministro.endswith('.png'):
        paths = os.path.join(os.getcwd(),'png') 
        os.makedirs(paths, exist_ok=True)
        shutil.move(suministro, os.path.join(paths,suministro))

        # os.remove(suministro.replace('.pdf', '.TIF'))

    else:
        return False
    
    return True
