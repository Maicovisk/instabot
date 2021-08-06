from requests import get
from bs4 import BeautifulSoup as bs
from random import choice, randint
from time import sleep

class Pensador:
    
    
    def __init__(self):
        self.autores = ''


    def getAutors(self):
        text = get('https://www.pensador.com/autores/').text.encode(encoding='UTF-8',errors='strict')
        bs_arg = bs(text, 'html.parser')
        autors = bs_arg.find('ul', {'class': 'custom'})
        autors_names = [c.text for c in autors.find_all('a')]
        self.autores = autors_names
        
        return autors_names


    def getAleatoriousAutor(self):
        try:
            text = get('https://www.pensador.com/autores/').text.encode(encoding='UTF-8',errors='strict')
            bs_arg = bs(text, 'html.parser')
            autors = bs_arg.find('ul', {'class': 'custom'})
            autors_names = [c.text for c in autors.find_all('a')]
            self.autores = autors_names
            choice(autors_names)
        except: return False
            
        return choice(autors_names)


    def getAllFrases(self, autor):
        _autor = get(f'https://www.pensador.com/autor/{autor.replace(" ", "_")}/')       
        _bs = bs(_autor.text, 'html.parser')
        frasesp1 = _bs.find_all('div', {'class': 'thought-card'})
        frasesp2 = [{'autor': autor, 'frase': c.find('p', {'class': 'frase'}).text} for c in frasesp1]
        
        return frasesp2


    def aleatoriesFrase(self, autor: str) -> dict:
        autor = autor.lower()
        autor = autor.replace('.', '')
        autor = autor.replace('ó', 'o')
        autor = autor.replace('ú', 'u')
        autor = autor.replace('á', 'a')
        autor = autor.replace('í', 'i')
        autor = autor.replace('-', '_')
        autor = autor.replace('ã', 'a')
        autor = autor.replace('ô', 'o')
        autor = autor.replace('ê', 'e')
        autor = autor.replace('é', 'e')
        autor = autor.replace('õ', 'o')
        number = 0
        while True:
            try:
                print(autor)
                print(f'https://www.pensador.com/autor/{autor.replace(" ", "_")}/')
                _autor = get(f'https://www.pensador.com/autor/{autor.replace(" ", "_")}/')       
                _bs = bs(_autor.text, 'html.parser')
                try:
                    number_pages = _bs.find('div', {'class': 'paginacao'}).find_all('a')[-2].text
                except:
                    number_pages = 0
                _autor = get(f'https://www.pensador.com/autor/{autor.replace(" ", "_")}/{randint(0, int(number_pages))}/')       
                _bs = bs(_autor.text, 'html.parser')


                frasesp1 = _bs.find_all('div', {'class': 'thought-card'})
                frasesp2 = [c.find('p', {'class': 'frase'}).text for c in frasesp1]
                


                fz = choice(frasesp2)
                if (len(fz) > 350):
                    print('...frase grande...')
                    raise
            except:
                print('new trying')
                number += 1
            else:              
                return {
                    'autor': autor,
                    'frase': fz
                }
            if number >= 4:
                break
        

    def __str__(self) -> str:
        return '''
        esse modulo é focado em crowlear o site
        Pensador.com.br 
        '''




