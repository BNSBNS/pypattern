from library import Base

# assert hasattr(Base,'foo'), "broken"

class Derived(Base):
    # if only this is created, bad user class is raised
    def eee(self):
        return 'eee'

    # def bar(self):
    #     return self.foo()

    def bar(self):
        return 'bar'
        

