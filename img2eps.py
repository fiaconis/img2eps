from PIL import Image
import glob
import os
import numpy as np

def img2esp(parent_dir):
    ''' Esta funcion transforma todas las imagenes que estan en el parent_dir 
    a formato EPS y las guarda en un subdirectorio "EPS_images"'''
    
    '''This function transforms all the images that are in the parent_dir 
    to EPS format and saves them in a subdirectory "EPS_images"'''
    
    lista = glob.glob(parent_dir+'/*')
    lista_png = filt_list(lista,'.jpg','.bmp','.JPEG','jpeg','.png',method = 'or') #filtro la lista para quedarme con archivos de imagenes
    directory = "EPS_images"
    path = os.path.join(parent_dir, directory) 
    try:
        os.mkdir(path) # Creo la carpeta EPS_images. Si ya esta creada no hago nada.
    except:
        pass
    print("Directory '% s' created" % directory) 
    print(path)  
    for imagen in lista_png:
        conv_im(imagen,path) # Esta funcion hace la conversion imagen por imagen
        
def conv_im (image_png,path):
    # Esta funcion es la que convierte una imagen a la vez y la guarda en el directorio "path"
    from PIL import Image
    im = Image.open(image_png)
    fig = im.convert('RGB')
    num = image_png[::-1].find('\\')
    nombre = image_png[-num:-4]
    fig.save(path+'/'+nombre+'.eps', lossless = True)

def filt_list(lista, *arg,**method):
    #Esta funcion filtra una lista de strings con el filtro del segundo argumento. puede utilizar el metodo "and, para indicar que necesita contener todos los argumentos o el metodo 'or' que implica que tenga algunos de los argumentos. Por defecto esta el metodo 'and'.
    return_lst = []
    lista_temp = lista.copy()
    if not method:
        method = {'method' : 'and'}
    if method['method'] == 'and':
        for f in arg:
            lista_temp = [ k for k in lista_temp if f in k]
        return(lista_temp)
    elif method['method'] == 'or':
        for f in arg:
            lista_temp = [ k for k in lista if f in k]
        return lista_temp
    else:
        print("Method not especified. it has to be 'method = 'and' or 'or'")