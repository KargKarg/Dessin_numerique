from Module import tab_donne

TABLEAU = tab_donne.tab_data('../Data/info_img.png.txt')
MASQUE_BOOL = TABLEAU<100

def pixel_non_blanc():

    """Fonction qui conserve tout les pixels qui ne sont pas blancs dans un fichier txt"""

    with open('../Data/non_blanc.txt', 'w') as filout:
        for i in range(len(MASQUE_BOOL)):
            cpt = 0
            liste_trans = []
            for j in range(len(MASQUE_BOOL) * 3):
                cpt += 1
                if len(liste_trans) == 3:
                    for elem in liste_trans:
                        if elem == True:
                            filout.write(f"{str(i)},{str(j // 3)} ")
                            break
                if cpt <= 3:
                    liste_trans.append(MASQUE_BOOL[i][j])
                else:
                    liste_trans = []
                    liste_trans.append(MASQUE_BOOL[i][j])
                    cpt = 1
            filout.write('\n')

pixel_non_blanc()