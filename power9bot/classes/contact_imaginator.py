from classes.default_imaginator import DefaultImaginator


class ContactImaginator(DefaultImaginator):
    def imagination(self):
        return self.value
