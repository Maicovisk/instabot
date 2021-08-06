from bs4 import BeautifulSoup as bs
from requests import get
import json

params = {
    'cookie': 'ig_did=4E43D784-8CC9-48AF-B632-04F7A4B49C45; ig_nrcb=1; mid=YQX_pAALAAFuapi41AQbKJilJTGr; fbm_124024574287414=base_domain=.instagram.com; shbid="17600\05413224583011\0541659319349:01f753e4b794374b48f59132f5a34c328fed484e59817078cacd329914137807fcccb358"; shbts="1627783349\05413224583011\0541659319349:01f7b494b0caaca9966a2280e4cd9ffb94bad622025279881ac63613923d58b1131798db"; csrftoken=kr22IM0mZsil6lhvp9b5xPQB0CGxCY37; ds_user_id=13224583011; sessionid=13224583011%3AL2I2x7zgyOESEK%3A28; rur="ATN\05413224583011\0541659460820:01f7344ca8c70183b16da3d9b7a9c8b5bc80971f60799c8c2c2b10b4941d4b1c6f497eb6"',
}


class createTags:

    def __init__(self: str) -> None:
        pass


    def Hashtags(self, text) -> json:
        return get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query=%23{text}', cookies=params).json()['hashtags']
    

    def Persons(self, text: str) -> dict:
        return {}


    def __repr__(self) -> dict:
        return params
