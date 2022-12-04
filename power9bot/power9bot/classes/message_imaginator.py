from power9bot.classes.default_imaginator import DefaultImaginator


class MessageImaginator(DefaultImaginator):
    def imagination(self):
        print(self.value)
