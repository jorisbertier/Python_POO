class ToolBox:
    def __init__(self, tools = []):
        self.tools = tools

    def add_outils(self, name):
        self.tools.push(name)
        return self.tools
    
    def delete_outils(self, name):
        self.tools.remove(name)
        return self.tools
    

class Hammer:
    def __init__(self, color = 'red'):
        self.color = color

    def paint(self, color):
        self.color = color

    def hammer_in(self):
        print('Enfonce clou')
        
    def remove(self):
        print("Retire le clou")

class Screwdriver:
    def __init__(self, size):
        self.size = size

    def tighten(self, screw):
        """Serrer une vis."""
        pass

    def loosen(self, screw):
        """Desserre une vis."""
        pass