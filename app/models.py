from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from . import db, login_manager



class Owner(db.Model):
    __tablename__='own'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, default='Deilmann s.r.o.')
    email1 = db.Column(db.String(128), default='karavan@deilmann.sk')
    email2 = db.Column(db.String(128))
    email3 = db.Column(db.String(128))
    phone1 = db.Column(db.String(24), unique=True, default='+421-950-764-554')
    phone2 = db.Column(db.String(24), unique=True)
    phone3 = db.Column(db.String(24), unique=True)
    icho = db.Column(db.Integer, unique=True)
    ulica_dom = db.Column(db.String(128))
    index = db.Column(db.String(24))
    text = db.Column(db.Text)

    def getOwn(self):
        own = Owner.query.all()


    def setOwn(self, name, email1, email2='', email3=''):
        own = Owner(name=name, email1=email1, email2=email2,email3=email3)
        db.session.add(own)
        db.session.commit()


    def __repr__(self):
        return self.name, self.email1, self.phone1, self.ulica_dom, self.index, self.icho


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    mess = db.relationship('Messages', backref='messages')



    def user_insert(self, name):
        user = User(name=name)
        db.session.add(user)
        db.session.commit()

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            return True

    def getUserId(self, mail):
        id_user = User.query.filter_by(email=mail).first().id
        return id_user

    def __repr__(self):
        return self.first_name


class Messages(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    subject = db.Column(db.String(128))
    message = db.Column(db.Text)

    def __repr__(self):
        return self.message


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(128), unique=True)

    def __repr__(self):
        return self.role


class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16


class Menu(db.Model):
    __tablename__='menu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    url = db.Column(db.String(128), unique=True)

    def set_menu(self, name, url):
        name_menu = Menu(name=name, url=url)
        db.session.add(name_menu)
        db.session.commit()


    def __repr__(self):
        return self.name



class FotoAlbum(db.Model):
    __tablename__ = 'foto_album'
    foto_album_id = db.Column(db.Integer, primary_key=True)
    foto_album_name = db.Column(db.String(80), unique=True)
    foto = db.relationship('Foto', backref='foto')
    coating = db.relationship('Coating', backref='album')
    warming = db.relationship('Warming', backref='album')
    dors = db.relationship('Dors', backref='album')
    seal = db.relationship('Seal', backref='album')
    windows = db.relationship('Windows', backref='album')
    ventilation = db.relationship('Ventilation', backref='album')
    boxes = db.relationship('BoxesCollections', backref='album')
    runduk = db.relationship('Runduk', backref='album')
    fittings = db.relationship('Fittings', backref='album')
    # mattress = db.relationship('mattress', backref='album')
    sinck = db.relationship('Sinck', backref='album')
    pump = db.relationship('Pump', backref='album')
    tank = db.relationship('Tank', backref='album')
    light = db.relationship('LightCollection', backref='album')
    socket = db.relationship('SocketCollection', backref='album')
    solar_panel = db.relationship('SolarPanel', backref='album')
    akb = db.relationship('Akb', backref='album')
    roof_rack = db.relationship('RoofRack', backref='album')
    cooking_stove = db.relationship('CookingStove', backref='album')
    mosquito_net = db.relationship('MosquitoNet', backref='album')
    heater = db.relationship('Heater', backref='album')
    model = db.relationship('Models', backref='album')

    def __repr__(self):
        return self.foto_album_name


class Foto(db.Model):
    __tablename__ = 'foto'
    foto_id = db.Column(db.Integer, primary_key=True)
    foto_name = db.Column(db.String(80))
    foto_url = db.Column(db.String(80), unique=True)
    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))
    color = db.relationship('Color', backref='color')

    def __repr__(self):
        return self.foto_name


class Color(db.Model):
    __tablename__ = 'color'
    color_id = db.Column(db.Integer, primary_key=True)
    color_name = db.Column(db.String(80), unique=True)
    foto_id = db.Column(db.Integer, db.ForeignKey('foto.foto_id'))

    def __repr__(self):
        return self.color_name


# покрытие

class Coating(db.Model):
    __tablename__ = 'coating'
    coating_id = db.Column(db.Integer, primary_key=True)
    coating_name = db.Column(db.String(80))
    coating_description = db.Column(db.Text)
    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.coating_name


# Утепление
class Warming(db.Model):
    __tablename__ = 'warming'
    warming_id = db.Column(db.Integer, primary_key=True)
    warming_name = db.Column(db.String(80))
    warming_description = db.Column(db.Text)
    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.warming_name


# двери

class Dors(db.Model):
    __tablename__ = 'dors'
    dors_id = db.Column(db.Integer, primary_key=True)
    dors_name = db.Column(db.String(80))
    dors_description = db.Column(db.Text)
    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.dors_name


# Уплотнение

class Seal(db.Model):
    __tablename__ = 'seal'
    seal_id = db.Column(db.Integer, primary_key=True)
    seal_name = db.Column(db.String(80))
    seal_description = db.Column(db.Text)
    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.seal_name


# окна
class Windows(db.Model):
    __tablename__ = 'windows'
    windows_id = db.Column(db.Integer, primary_key=True)
    windows_name = db.Column(db.String(80))
    windows_description = db.Column(db.Text)
    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.windows_name


# Вентиляция

class Ventilation(db.Model):
    __tablename_ = 'ventilation'
    ventilation_id = db.Column(db.Integer, primary_key=True)
    ventilation_name = db.Column(db.String(80))
    ventilation_description = db.Column(db.Text)
    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.ventilation_name


# коллекция ящиков

class BoxesCollections(db.Model):
    __tablename__ = 'boxes_collections'
    boxes_collections_id = db.Column(db.Integer, primary_key=True)
    boxes_collections_name = db.Column(db.String(80))
    boxes_collections_descriptions = db.Column(db.Text)
    box = db.relationship('Boxes', backref='box')
    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.boxes_collections_name


class Boxes(db.Model):
    __tablename__ = 'boxes'
    boxes_id = db.Column(db.Integer, primary_key=True)
    boxes_name = db.Column(db.String(80))
    boxes_description = db.Column(db.Text)
    boxes_collect_id = db.Column(db.Integer, db.ForeignKey('boxes_collections.boxes_collections_id'))

    def __repr__(self):
        return self.boxes_name


# Рундук

class Runduk(db.Model):
    __tablename__ = 'runduk'
    runduk_id = db.Column(db.Integer, primary_key=True)
    runduk_name = db.Column(db.String(80))
    runduk_description = db.Column(db.Text)
    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.runduk_name


class Fittings(db.Model):
    __tablename__ = 'fittings'
    fittings_id = db.Column(db.Integer, primary_key=True)
    fittings_name = db.Column(db.String(80))
    fittings_description = db.Column(db.Text)
    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.fittings_name


# матрас
class Mattress(db.Model):
    __tablename__ = 'mattress'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    # album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.name


# раковина

class Sinck(db.Model):
    __tablename__ = 'sinck'
    sinck_id = db.Column(db.Integer, primary_key=True)
    sinck_name = db.Column(db.String(80))
    sinck_description = db.Column(db.Text)
    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.sinck_name


# насос

class Pump(db.Model):
    __tablename__ = 'pump'
    pump_id = db.Column(db.Integer, primary_key=True)
    pump_name = db.Column(db.String(80))
    pump_description = db.Column(db.Text)
    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))
    pump_power = db.Column(db.String(80))
    pump_volt = db.Column(db.Float)

    def __repr__(self):
        return self.pump_name


# бак

class Tank(db.Model):
    __tablename__ = 'tank'
    tank_id = db.Column(db.Integer, primary_key=True)
    tank_name = db.Column(db.String(80))
    tank_description = db.Column(db.Text)
    tank_volume = db.Column(db.Integer)
    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))
    model = db.relationship('ModelSettings', backref='model')

    def __repr__(self):
        return self.tank_name


# освещение коллекции
class LightCollection(db.Model):
    __tablename__ = 'light_collection'
    light_coll_id = db.Column(db.Integer, primary_key=True)
    light_coll_name = db.Column(db.String())
    light_coll_description = db.Column(db.Text)
    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))
    light = db.relationship('Light', backref='light collections')
    #models = db.relationship('ModelSettings', backref='light')

    def __repr__(self):
        return self.light_coll_name


# освещение
class Light(db.Model):
    __tablename__ = 'light'
    light_id = db.Column(db.Integer, primary_key=True)
    light_name = db.Column(db.String(80))
    light_description = db.Column(db.Text)
    foto_id = db.Column(db.Integer, db.ForeignKey('foto.foto_id'))
    foto = db.relationship('Foto', backref='foto light')
    light_coll = db.Column(db.Integer, db.ForeignKey('light_collection.light_coll_id'))

    def __repr__(self):
        return self.light_name


# розетки коллекция
class SocketCollection(db.Model):
    __tablename__ = 'socket_collection'
    socket_coll_id = db.Column(db.Integer, primary_key=True)
    socket_coll_name = db.Column(db.String(80))
    socket_coll_description = db.Column(db.Text)
    socket = db.relationship('Socket', backref='socket')

    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.socket_coll_name


class Socket(db.Model):
    __tablrname__ = 'socket'
    socket_id = db.Column(db.Integer, primary_key=True)
    socket_name = db.Column(db.String(80))
    socket_description = db.Column(db.Text)
    socket_coll = db.Column(db.Integer, db.ForeignKey('socket_collection.socket_coll_id'))


class SolarPanel(db.Model):
    __tablename__ = 'solar_panel'
    solar_panel_id = db.Column(db.Integer, primary_key=True)
    solar_panel_name = db.Column(db.String(80))
    solar_panel_description = db.Column(db.Text)

    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.solar_panel_name


class Akb(db.Model):
    __tablename__ = 'akb'
    akb_id = db.Column(db.Integer, primary_key=True)
    akb_name = db.Column(db.String(80))
    akb_description = db.Column(db.Text)
    akb_volt = db.Column(db.Integer)
    akb_amp_hour = db.Column(db.Integer)

    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.akb_name


# багажник на крышу
class RoofRack(db.Model):
    __tablename__ = 'roof_rack'
    roof_rack_id = db.Column(db.Integer, primary_key=True)
    roof_rack_name = db.Column(db.String(80))
    roof_rack_description = db.Column(db.Text)

    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.roof_rack_name


# варочная плита

class CookingStove(db.Model):
    __tablename__ = 'stove'
    stove_id = db.Column(db.Integer, primary_key=True)
    stove_name = db.Column(db.String(80))
    stove_description = db.Column(db.Text)
    stove_price = db.Column(db.Float)

    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.stove_name


# москитные сетки
class MosquitoNet(db.Model):
    __tablename__ = 'mosquito_net'
    mosquito_net_id = db.Column(db.Integer, primary_key=True)
    mosquito_net_name = db.Column(db.String(80))
    mosquito_net_description = db.Column(db.Text)
    mosquito_net_price = db.Column(db.Float)

    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.mosquito_net_name


# отопитель

class Heater(db.Model):
    __tablename__ = 'heater'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.Text)
    price = db.Column(db.Float)



    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))

    def __repr__(self):
        return self.heater_name


# модели
class Models(db.Model):
    __tablename__ = 'models'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)

    settings = db.relationship('ModelSettings', backref='model settings')

    album_id = db.Column(db.Integer, db.ForeignKey('foto_album.foto_album_id'))
    css_class = db.Column(db.String(256))

    def __repr__(self):
        return self.models_name


class ModelSettings(db.Model):
    __tablename__ = 'model_settings'
    model_settings_id = db.Column(db.Integer, primary_key=True)

    model_id = db.Column(db.Integer, db.ForeignKey('models.id'))

    heater_id = db.Column(db.Integer, db.ForeignKey('heater.id'))
    heater = db.relationship('Heater', backref='heater')

    mosquito_net_id = db.Column(db.Integer, db.ForeignKey('mosquito_net.mosquito_net_id'))
    mosquito_net = db.relationship('MosquitoNet', backref='mosquito')

    stove_id = db.Column(db.Integer, db.ForeignKey('stove.stove_id'))
    stove = db.relationship('CookingStove', backref='stove')

    roof_rack_id = db.Column(db.Integer, db.ForeignKey('roof_rack.roof_rack_id'))
    roof_rack = db.relationship('RoofRack', backref='roof rack')

    akb_id = db.Column(db.Integer, db.ForeignKey('akb.akb_id'))
    akb = db.relationship('Akb', backref='akb')

    solar_panel_id = db.Column(db.Integer, db.ForeignKey('solar_panel.solar_panel_id'))
    solar_panel = db.relationship('SolarPanel', backref='solar panel')

    socket_collection_id = db.Column(db.Integer, db.ForeignKey('socket_collection.socket_coll_id'))
    socket = db.relationship('SocketCollection', backref='socket collection')

    light_collection_id = db.Column(db.Integer, db.ForeignKey('light_collection.light_coll_id'))
    #light_collection = db.relationship('LightCollection', backref='light collection')

    tank_id = db.Column(db.Integer, db.ForeignKey('tank.tank_id'))

    pump_id = db.Column(db.Integer, db.ForeignKey('pump.pump_id'))
    pump = db.relationship('Pump', backref='pumps')

    sinck_id = db.Column(db.Integer, db.ForeignKey('sinck.sinck_id'))
    sinck = db.relationship('Sinck', backref='sincks')

    # mattress_id = db.Column(db.Integer, db.ForeignKey('mattress.id'))
    # mattress = db.relationship('Mattress', backref='mattresss')

    fittings_id = db.Column(db.Integer, db.ForeignKey('fittings.fittings_id'))
    fittings = db.relationship('Fittings', backref='fitting')

    runduk_id = db.Column(db.Integer, db.ForeignKey('runduk.runduk_id'))
    runduk = db.relationship('Runduk', backref='runduks')

    boxes_collections_id = db.Column(db.Integer, db.ForeignKey('boxes_collections.boxes_collections_id'))
    boxes = db.relationship('BoxesCollections', backref='boxes_coll')

    ventilation_id = db.Column(db.Integer, db.ForeignKey('ventilation.ventilation_id'))
    ventilation = db.relationship('Ventilation', backref='ventilations')

    windows_id = db.Column(db.Integer, db.ForeignKey('windows.windows_id'))
    windows = db.relationship('Windows', backref='windowss')

    seal_id = db.Column(db.Integer, db.ForeignKey('seal.seal_id'))
    seal = db.relationship('Seal', backref='seals')

    dors_id = db.Column(db.Integer, db.ForeignKey('dors.dors_id'))
    dors = db.relationship('Dors', backref='dorss')

    warming_id = db.Column(db.Integer, db.ForeignKey('warming.warming_id'))
    warming = db.relationship('Warming', backref='warmings')

    def __repr__(self):
        return self.model_settings_id


# заказ
class Orders(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)

    model_settings_id = db.Column(db.Integer, db.ForeignKey('model_settings.model_settings_id'))
    model_settings = db.relationship('ModelSettings', backref='model-settings')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='user')

    def __repr__(self):
        return self.id


dict_models = {'foto_album':FotoAlbum,
               'foto':Foto,
               'user':User,
               'role':Role,
               'color':Color,
               'coating':Coating,
               'warming':Warming,
               'dors':Dors,
               'seal':Seal,
               'windows':Windows,
               'ventilation':Ventilation,
               'boxes_collections':BoxesCollections,
               'boxes':Boxes,
               'runduk':Runduk,
               'fittings':Fittings,
               #'mattress':Mattress,
               'sinc':Sinck,
               'pump':Pump,
               'tank':Tank,
               'light_collection':LightCollection,
               'light':Light,
               'socket_collection':SocketCollection,
               'socket':Socket,
               'solar_panel':SolarPanel,
               'akb':Akb,
               'roof_rack':RoofRack,
               'cooking_stove':CookingStove,
               'mosquito_net':MosquitoNet,
               'heater':Heater,
               'models':Models,
               'models_settings':ModelSettings}

