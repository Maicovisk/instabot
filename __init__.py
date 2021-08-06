from instaLogin import sistem_auto_instagram as Instagram
from getWorlds import Pensador
from createImage import CreateImage
from createTags import createTags

def postFrase(num=1, post=False):
    insta = Instagram(
        user="videos2018pg@gmail.com",
        password="maicon2018",
    )

    pensador = Pensador()
    for c in range(1):
        autor = pensador.getAleatoriousAutor()
        frase = pensador.aleatoriesFrase(autor=autor)

        if (frase):
            img = CreateImage('@maicon_st001')
            img.create(text=frase['frase'], name=f'_{c}.jpg')
            if post:
                insta.login()
                insta.post_image(f'_instagram_post/image/new/_{c}.jpg', description='')