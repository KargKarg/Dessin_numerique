from PIL import Image

def info_image(nom):

    """Fonction qui renvoie les données de tout les pixels en RGB dans un fichier txt
    en forçant l'image à se mettre en 800x800"""

    image = Image.open(nom)
    image = image.resize((800, 800))
    ligne = []
    with open(f"../Data/info_{nom}.txt", 'w') as filout:
        for i in range(800):
            for j in range(800):
                r, v, b = image.getpixel((i, j))
                liste_transitoire = [r,v,b]
                ligne.append(liste_transitoire)
            for elem in ligne:
                for element in elem:
                    filout.write(str(element) + ' ')
            filout.write("\n")
            ligne = []
info_image('../Image/img.png')