from flask import Flask ,jsonify ,request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend

# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://Wann:(((PASS)))@Wann.mysql.pythonanywhere-services.com/Wann$default'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow

# defino la tabla
class Libro(db.Model):   # la clase Producto hereda de db.Model
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    titulo=db.Column(db.String(100))
    autor=db.Column(db.String(50))
    idioma=db.Column(db.String(10))
    anio=db.Column(db.Integer)
    genero=db.Column(db.String(50))
    stock=db.Column(db.Integer)
    imagen=db.Column(db.String(400))
    prestamo=db.Column(db.Boolean)
    def __init__(self,titulo,autor,idioma,anio,genero,stock,imagen,prestamo):   #crea el  constructor de la clase
        self.titulo=titulo   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.autor=autor
        self.idioma=idioma
        self.anio=anio
        self.genero=genero
        self.stock=stock
        self.imagen=imagen
        self.prestamo=prestamo


    #  si hay que crear mas tablas , se hace aqui


with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
class LibroSchema(ma.Schema):
    class Meta:
        fields=('id','titulo','autor','idioma','anio','genero','stock','imagen','prestamo')


libro_schema=LibroSchema()            # El objeto producto_schema es para traer un producto
libros_schema=LibroSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto


# crea los endpoint o rutas (json)
@app.route('/libros',methods=['GET'])
def get_Libros():
    all_libros=Libro.query.all()         # el metodo query.all() lo hereda de db.Model
    result=libros_schema.dump(all_libros)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla


@app.route('/libros/<id>',methods=['GET'])
def get_libro(id):
    libro=Libro.query.get(id)
    return libro_schema.jsonify(libro)   # retorna el JSON de un producto recibido como parametro


@app.route('/libros/<id>',methods=['DELETE'])
def delete_libro(id):
    libro=Libro.query.get(id)
    db.session.delete(libro)
    db.session.commit()
    return libro_schema.jsonify(libro)   # me devuelve un json con el registro eliminado

@app.route('/libros', methods=['POST']) # crea ruta o endpoint
def create_libro():
    #print(request.json)  # request.json contiene el json que envio el cliente
    titulo=request.json['titulo']
    autor=request.json['autor']
    idioma=request.json['idioma']
    anio=request.json['anio']
    genero=request.json['genero']
    stock=request.json['stock']
    imagen=request.json['imagen']
    prestamo=request.json['prestamo']
    new_libro=Libro(titulo,autor,idioma,anio,genero,stock,imagen,prestamo)
    db.session.add(new_libro)
    db.session.commit()
    return libro_schema.jsonify(new_libro)

@app.route('/libros/<id>' ,methods=['PUT'])
def update_libro(id):
    libro=Libro.query.get(id)

    libro.titulo=request.json['titulo']
    libro.autor=request.json['autor']
    libro.idioma=request.json['idioma']
    libro.anio=request.json['anio']
    libro.genero=request.json['genero']
    libro.stock=request.json['stock']
    libro.imagen=request.json['imagen']
    libro.prestamo=request.json['prestamo']

    db.session.commit()
    return libro_schema.jsonify(libro)

@app.route('/')
def hello_world():
    return 'Hello Wannmi!'