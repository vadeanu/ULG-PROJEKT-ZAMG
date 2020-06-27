from crawler import Crawler
from xmlparser import XmlParser
from thesis import Thesis

c = Crawler()
c.crawl("http://localhost:8081/thesis.txt")
if c.wasSuccessful():
    for line in c.getText().splitlines():
        print(line)

c.crawl("http://localhost:8081/BergLauben.xml")
if c.wasSuccessful():
    print(c.getText())

parser = XmlParser()
thesis = parser.readXML(c.getText())

print(thesis.inspect())


thesis = Thesis()

thesis.setUrn("urn1")
thesis.setTitle("titel1")
thesis.setAuthor("author1")
thesis.setLanguage("language1")
thesis.setSupervisor("Supervisor1")
thesis.setGenre("genre1")
thesis.setUniversity("uni1")
thesis.setProduction("1980")

print(thesis.inspect())


