class Thesis:
    urn = ""
    title = ""
    subtitle = ""
    author = ""
    language = ""
    supervisor = ""
    sec_supervisor = ""
    genre = ""
    university = ""
    production = -1
    abstract = ""

    def getUrn(self):
        return self.urn

    def setUrn(self, urn):
        self.urn = urn

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getSubtitle(self):
        return self.subtitle

    def setSubtitle(self, subtitle):
        self.subtitle = subtitle

    def getAuthor(self):
        return self.author

    def setAuthor(self, author):
        self.author = author

    def getLanguage(self):
        return self.language

    def setLanguage(self, language):
        self.language = language

    def getSupervisor(self):
        return self.supervisor

    def setSupervisor(self, supervisor):
        self.supervisor = supervisor

    def getSec_supervisor(self):
        return self.sec_supervisor

    def setSec_supervisor(self, sec_supervisor):
        self.sec_supervisor = sec_supervisor

    def getGenre(self):
        return self.genre

    def setGenre(self, genre):
        self.genre = genre

    def getUniversity(self):
        return self.university

    def setUniversity(self, university):
        self.university = university

    def getProduction(self):
        return self.production

    def setProduction(self, production):
        self.production = production

    def getAbstract(self):
        return self.abstract

    def setAbstract(self, abstract):
        self.abstract = abstract

    def isValid(self):
        if self.urn == "" or \
           self.title == "" or \
           self.author == "" or \
           self.language == "" or \
           self.supervisor == "" or \
           self.genre == "" or \
           self.university == "" or \
           self.production == -1:
            return False
        else:
            return True

    def inspect(self):
        print("urn: " + self.urn)
        print("title: " + self.title)
        print("subtitle: " + self.subtitle)
        print("author: " + self.author)
        print("supervisor: " + self.supervisor)
        print("sec_supervisor: " + self.sec_supervisor)
        print("language: " + self.language)
        print("production: " + repr(self.production))
        print("abstract: " + self.abstract)
        print("genre: " + self.genre)
        print("university: " + self.university)
        print("is valid: " + str(self.isValid()))

