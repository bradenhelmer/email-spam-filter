class hashCheck:
    def __init__(self, hash):
        self.hash = hash

    def hashCheck(self):
        file = open('myfile.txt', 'r')
        Lines = file.readlines()
        if self.hash in Lines:
            return True
        return False