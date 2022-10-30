from PIL import Image


def pixel_non_blanc():

    """Fonction qui traite l'ensemble des données en transformant le fichier dans une liste
    de position de ce format (x,y)"""

    with open('Data/non_blanc.txt', 'r') as filout:
        liste_pixel = []
        for taille in range(800):
            ligne = filout.readline()
            traitement_ligne = list(ligne)
            for elem in traitement_ligne:
                if elem == '\n':
                    traitement_ligne.remove('\n')
            x = True
            coord_x, coord_y = '', ''
            coord = []
            for element in traitement_ligne:
                if element == ' ':
                    coord.append((int(coord_x), int(coord_y)))
                    coord_x, coord_y = '', ''
                    x = not x
                if element == ',':
                    x = not x
                if x == True and element != ',' and element !=' ':
                    coord_x += element
                elif x == False and element != ',' and element !=' ':
                    coord_y += element
            liste_pixel.append(coord)
        return liste_pixel

def dessin():

    """Fonction qui trace un fond blanc en 800x800 et qui noirci les pixels dans la liste
    avec la position : pos qui est de ce format (x,y)
    Elle sauvegarde aussi l'image qui vient d'être faite"""

    image = Image.new('RGB', (800, 800))

    for x in range(800):
        for y in range(800):
            image.putpixel((x, y), (255, 255, 255))

    liste_pixel = pixel_non_blanc()

    cpt_pix = 0
    for elem in liste_pixel:
        for pos in elem:
           #  cpt_pix += 1 pour GIF
            image.putpixel(pos, (0, 0, 0))
            # if cpt_pix % 1000 == 0 : pour GIF
            #    image.save(f'GIF/test_gif_{cpt_pix}.png') pour GIF
    image.save('Résultats/test.png')
    image.show()

dessin()