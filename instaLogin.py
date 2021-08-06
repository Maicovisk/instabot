from logging import fatal
from instabot import Bot
from modules import delCookie


class sistem_auto_instagram:


    def __init__(self, user, password):
        self.bot = Bot()
        self.user = user
        self.password = password


    def login(self):
        delCookie()
        self.bot.login(username=f"{self.user}", password=f"{self.password}")


    def post_image(self, url, description):
        self.bot.upload_photo(url, caption=description)

