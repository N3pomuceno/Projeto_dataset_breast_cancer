
def salva_modelo_pkl(model, filename):
    import pickle
    import datetime
    
    suffixe = datetime.datetime.today().strftime("_%d%m%y")  
    nome_arquivo = filename+suffixe
    path = './models/'
    verifica_diretorio(path)
    
    with open(path+nome_arquivo, 'wb') as file:
        pickle.dump(model, file)


def verifica_diretorio(path, cria_dir = True):
    import os
    if not os.path.isdir(path):
        os.mkdir(path)