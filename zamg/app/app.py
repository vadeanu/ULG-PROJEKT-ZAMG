from typing import List, Dict
from flask import Flask
import logging
from flask_mysqldb import MySQL
from crawler import Crawler
from xmlparser import XmlParser

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

app.config['MYSQL_HOST'] = 'mysql_database'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'zamg'
app.config['MYSQL_DB'] = 'zamg'

mysql = MySQL(app)

def getThesis():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT urn, title, author, university FROM thesis')
    results = cursor.fetchall()
    cursor.close()

    return results

def deletethesis():
    cursor = mysql.connection.cursor()
    cursor.execute('delete from thesis')
    mysql.connection.commit()

def crawlthesis():
    cursor = mysql.connection.cursor()

    serverurls = { 'http://apache_uni1', 'http://apache_uni2', 'http://apache_uni3'}

    c = Crawler()
    parser = XmlParser()

    for url in serverurls:
        app.logger.info('crawling ' + url)
        c.crawl(url + "/thesis.txt")
        if c.wasSuccessful():
            for filename in c.getText().splitlines():
                thesisurl = url + "/" + filename
                app.logger.info('crawling ' + thesisurl)
                c.crawl(thesisurl)
                if c.wasSuccessful():
                    thesis = parser.readXML(c.getText())
                    print(thesis.inspect())

                    # die folgenden set methoden befüllen das Objekt technisch korrekt, damit es abgespeichert werden kann. Diese Zeilen müssen natürlich wieder raus
                    thesis.setUrn("urn1")
                    thesis.setTitle("titel1")
                    thesis.setAuthor("author1")
                    thesis.setLanguage("language1")
                    thesis.setSupervisor("Supervisor1")
                    thesis.setGenre("genre1")
                    thesis.setUniversity("uni1")
                    thesis.setProduction("1980")

                    if thesis.isValid():
                        # check ob thesis schon eingefuegt
                        sql = "select count(*) from thesis where urn = '" + thesis.getUrn() + "'";
                        cursor.execute(sql)
                        result = cursor.fetchone()
                        numberOfRows = result[0]
                        if numberOfRows > 0:
                            app.logger.info("Thesis " + thesis.getUrn() + " befindet sich schon in der Datenbank")
                            continue

                        sql = "insert into thesis (urn, title, subtitle, author, language, supervisor, sec_supervisor, genre, university, production, abstract) values (" \
                              "'" + thesis.getUrn() + "', " \
                              "'" + thesis.getTitle() + "', " \
                              "'" + thesis.getSubtitle() + "', " \
                              "'" + thesis.getAuthor() + "', " \
                              "'" + thesis.getLanguage() + "', " \
                              "'" + thesis.getSupervisor() + "', " \
                              "'" + thesis.getSec_supervisor() + "', " \
                              "'" + thesis.getGenre() + "', " \
                              "'" + thesis.getUniversity() + "', " \
                              "'" + thesis.getProduction() + "', " \
                              "'" + thesis.getAbstract() + "'" \
                              ")"

                        cursor.execute(sql)
                        mysql.connection.commit()
                        app.logger.info("Thesis " + thesis.getUrn() + " in der Datenbank gespeichert.")
                    else:
                        app.logger.info("Thesis kann nicht importiert werden. Nicht valide.")
                else:
                    app.logger.info("crawl von " + thesisurl + " war nicht erfolgreich.")


def generateHtml():
    list = getThesis()
    html = '<h1>Thesis</h1>'
    html = html + '<a href="/">Home</a> | <a href="/crawlthesis">crawl thesis</a> | <a href="/deletethesis">delete thesis</a><p/>'

    if len(list) > 0:
        html = html + '<table border="1">'
        html = html + '<tr><th>urn</th><th>title</th><th>author</th><th>university</th></tr>'
        for item in list:
            html = html + '<tr><td>' + item[0] + '</td><td>' + item[1] + '</td><td>' + item[2] + '</td><td>' + item[3] + '</td></tr>'
        html = html + '</table>'
    else:
        html = html + '<p>keine Daten</p>' 

    return html

@app.route('/')
def index():
    return generateHtml()

@app.route('/deletethesis')
def delete():
    deletethesis()
    return generateHtml()

@app.route('/crawlthesis')
def crawl():
    crawlthesis()
    return generateHtml()

if __name__ == '__main__':
    app.run(host='0.0.0.0')