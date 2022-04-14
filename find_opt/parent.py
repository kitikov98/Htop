import psutil

class Parent:
    info = {}
    template =""

    def get(self):
        pass


    def prepare(self):
        pass

    def show(self):
        print(self.template.format(**self.info))


