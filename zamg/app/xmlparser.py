import xml.etree.ElementTree as ET
from thesis import Thesis

class XmlParser:

    def readXML(self, xmldata):

        obj = Thesis()
        root = ET.fromstring(xmldata)

        family = ""
        given = ""

        for element in root:
            if element.tag == "identifier":
                URN = element.text
                obj.setUrn(URN)
            if str(element.attrib) == "{'type': 'thesis'}":
                # print('yesssssss')
                thesis = element.text
                genre = thesis.split(' -- ')[0]
                obj.setGenre(genre)
                year = thesis.split(' -- ', )[1]
                university = year.split(',')[0]
                obj.setUniversity(university)
            for subelement in element:
                if subelement.tag == "title":
                    title = subelement.text
                    obj.setTitle(title)
                if subelement.tag == "subTitle":
                    subTitle = subelement.text
                    obj.setSubtitle(subTitle)
                if str(subelement.attrib) == "{'type': 'family'}":
                    print("treffer")
                    family = subelement.text
                if str(subelement.attrib) == "{'type': 'given'}":
                    given = subelement.text
                if subelement.tag == 'dateIssued':
                    production = subelement.text
                    obj.setProduction(production)
            # for subelement in element:
            if str(element.attrib) == "{'type': 'Betreuer'}":
                Betreuer = element.text
                obj.setSupervisor(Betreuer)
            if str(element.attrib) == "{'type': 'Betreuer2'}":
                Betreuer2 = element.text
                obj.setSec_supervisor(Betreuer2)
            if element.tag == 'language':
                language = element.text
                obj.setLanguage(language)
            if element.tag == 'abstract':
                abstract = element.text
                obj.setAbstract(abstract)

            autor = family + ", " + given
            obj.setAuthor(autor)

            return obj
