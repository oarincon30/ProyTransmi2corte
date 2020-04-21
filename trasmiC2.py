
# Oswaldo Rincón
# 67000530

from math import radians, cos, sin, asin, sqrt

import json

class Item():
  def __init__(self, obj1, obj2, obj3, obj4, obj5,obj6,obj7):
    self.item = obj1
    #self.nombre = obj
    self.geoLat = obj2
    self.geoLong = obj3
    self.tipo = obj4
    self.nombreTroncal = obj5
    self.alimentadores=obj6
    self.upz=obj7
    self.nxt = None
    self.prv = None

class Item_upz():
  def __init__(self, obj1, obj2, obj3, obj4, obj5, obj6):
    self.nombre = obj1
    self.numero = obj2
    self.localidad = obj3
    self.cantHabitantes = obj4
    self.latitudUpz = obj5
    self.longitudUpz = obj6

class ListDynamic(object):
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
    self.head2 = None
    self.tail2 = None
    self.size2 = 0

  def add_element(self, a, b, c, d, e,f,g):
    new_item = Item(a, b, c, d, e,f,g)
    if new_item.nombreTroncal=="AV CARACAS":
        if self.size == 0:
          self.head = new_item
          self.tail=new_item
          self.head.nxt=self.tail
          self.tail.prv=self.head
        elif self.size == 1:
          self.tail = new_item
          aux=self.head
          aux2=self.tail
          aux.nxt=self.tail
          aux2.prv=self.head
        else:
          aux3 = self.head
          while(aux3.nxt != None):
            aux3 = aux3.nxt
          self.tail = new_item
          aux3.nxt = self.tail
          aux2=self.tail
          aux2.prv=aux3
        self.size += 1
    elif new_item.nombreTroncal=="Calle 80":
        if self.size2 == 0:
          self.head2 = new_item
          self.tail2=new_item
          aux = self.head2
          aux.nxt=self.tail2
          aux2 = self.tail2
          aux2.prv=self.head2
        elif self.size2 == 1:
          self.tail2 = new_item
          aux=self.head2
          aux2=self.tail2
          aux.nxt=self.tail2
          aux2.prv=self.head2
        else:
          aux3 = self.head2
          while(aux3.nxt != None):
            aux3 = aux3.nxt
          self.tail2 = new_item
          aux3.nxt = self.tail2
          aux2=self.tail2
          aux2.prv=aux3
        self.size2 += 1



  def print_list(self):
    item = self.head
    g=0
    if self.size > 0:
        g=self.size
    for i in range(g):
      print(item.item)
      print(item.geoLat)
      print(item.geoLong)
      print(item.tipo)
      print(item.alimentadores)
      print(item.upz)
      print("--")
      item =  item.nxt
    print("-------------------\n")



  def print_list2(self):
      item = self.head2
      g=0
      if self.size2 > 0:
          g=self.size2
      for i in range(g):
        print(item.item)
        print(item.geoLat)
        print(item.geoLong)
        print(item.tipo)
        print(item.alimentadores)
        print(item.upz)
        print("")
        item =  item.nxt
      print("-------------------\n")



  def calcular(self, ori, des):
      origen=ori
      destino=des
      lat1=0.0
      lon1=0.0
      lat2=0.0
      lon2=0.0
      aux4 = self.head
      aux5=self.head2
      aux6 = self.head
      aux7=self.head2
      m=self.size
      n=self.size2
      for i in range(m):
          if aux4.item==origen:
              lat1=aux4.geoLat
              lon1=aux4.geoLong
              break
          else:
              aux4=aux4.nxt

      for i in range(n):
          if aux5.item==origen:
              lat1=aux5.geoLat
              lon1=aux5.geoLong
              break
          else:
              aux5=aux5.nxt


      for i in range(m):
          if aux6.item==destino:
              lat2=aux6.geoLat
              lon2=aux6.geoLong
              break
          else:
              aux6=aux6.nxt

      for i in range(n):
          if aux7.item==destino:
              lat2=aux7.geoLat
              lon2=aux7.geoLong
              break
          else:
              aux7=aux7.nxt
      print(lista.haversine(lon1,lat1,lon2,lat2))


  def haversine(self,lon1, lat1, lon2, lat2):

    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r




lista = ListDynamic()
hash_table = [[] for _ in range(60)]


def cargar_datos(ruta):
    with open(ruta) as contenido:
        troncales=json.load(contenido)
        for troncal in troncales:
            estaciones=troncal.get('estaciones')
            e=troncal.get('nombreTroncal')
            for estacion in estaciones:
                a = estacion.get('nombreEstacion')
                b = estacion.get('latitud')
                c = estacion.get('longitud')
                b=float(b)
                c=float(c)
                d = estacion.get('tipoEstacion')
                f = estacion.get('alimentadores')
                g = estacion.get('UPZ')
                lista.add_element(a, b, c, d, e,f,g)


def hashing_func(key):
    return key % len(hash_table)


def insert(hash_table, key, object):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, object))
    else:
        bucket.append((key, object))

def cargar_datosUpz(ruta2):
    with open(ruta2) as contenido:
        upzs=json.load(contenido)
        for upz in upzs:
            a = upz.get('nombre')
            b = upz.get('numero')
            c = upz.get('localidad')
            d = upz.get('cantHabitantes')
            e = upz.get('latitudUpz')
            f = upz.get('longitudUpz')
            e=float(e)
            f=float(f)
            new_item_upz=Item_upz(a,b,c,d,e,f)
            insert(hash_table, b, new_item_upz)

def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        #print(i,k,v)
        if key == k:
            print("Upz: "+v.nombre)
            print("Localidad: "+v.localidad)
            print("Población: "+str(v.cantHabitantes))
            print("Latitud: "+str(v.latitudUpz))
            print("Longitud: "+str(v.longitudUpz))

if __name__=='__main__':
    ruta='transmi.json'
    cargar_datos(ruta)
    ruta2='upz.json'
    cargar_datosUpz(ruta2)

op=0
while ((op < 1) or (op > 6)):
    print("\n 1) Mostrar Estaciones\n 2) Calcular distancia\n 3) Buscar UPZ\n 4) Salir")
    op=int(input("\n --Elija una opcion: "))
    if op==1:
        lista.print_list()
        lista.print_list2()
        op=0
    if op==2:
        origen =input("\n Escriba la estación de origen: ")
        destino=input("\n Escriba la estación de destino: ")
        print("\nLa distancia entre las dos estaciones es:")
        lista.calcular(origen, destino)
        op=0
    if op==3:
        num=int(input("\n Número de Upz a buscar: "))
        search(hash_table, num)
        op=0
