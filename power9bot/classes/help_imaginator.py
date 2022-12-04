from classes.default_imaginator import DefaultImaginator


class HelpImaginator(DefaultImaginator):
    def imagination(self):
        for command in self.value:
            print(command)
