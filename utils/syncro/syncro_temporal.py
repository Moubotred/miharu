import os
import shutil

def Archivo_temporal(suministro,pwd):
    if suministro.endswith('.pdf'):

        paths = os.path.join(pwd,'pdf') 
        os.makedirs(paths, exist_ok=True)
        shutil.move(suministro, os.path.join(paths,suministro))

        # linea para vps
        # os.remove(suministro.replace('.pdf', '.TIF'))

    if suministro.endswith('.png'):
        paths = os.path.join(pwd,'png') 
        os.makedirs(paths, exist_ok=True)
        shutil.move(suministro, os.path.join(paths,suministro))

        # os.remove(suministro.replace('.pdf', '.TIF'))

    else:
        return False
    
    return True
