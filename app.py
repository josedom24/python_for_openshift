from flask import Flask, request,url_for,render_template,abort
from lxml import etree
import requests
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
	doc=etree.parse("sevilla.xml")
	municipios=doc.findall("municipio")
	return render_template("inicio.html",municipios=municipios)

@app.route('/<code>')
def temperatura(code):
	#try:
	response = requests.get("http://www.aemet.es/xml/municipios/localidad_"+code+".xml")
	xml = response.content
	doc=etree.fromstring(xml)

	#except:
	#	abort(404)
	name=doc.find("nombre").text
	max=doc.find("prediccion/dia/temperatura").find("maxima").text
	min=doc.find("prediccion/dia/temperatura").find("minima").text
	return render_template("temperaturas.html",name=name,max=max,min=min)

if __name__ == '__main__':
	app.run('0.0.0.0',8080,debug=True)
