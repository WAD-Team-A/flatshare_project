import os 
import uuid
os.environ.setdefault('DJANGO_SETTINGS_MODULE','flatshare_project.settings')
import django
django.setup()

from flatshare.models import Flat, Address

def populate():
    addresses = [
        {'flat_no':'0/1', 'house_no':1, 'street': 'lorem ipsudem str', 'city':'Glasgow', 'province': 'Lanarkshire', 'postcode':'G200TH', 'country':'United Kingdom'},
      {'flat_no':'0/2', 'house_no':1, 'street': 'lorem ipsum str', 'city':'Glasgow', 'province': 'Lanarkshire', 'postcode':'G200TH', 'country':'United Kingdom'}]
    
    addr_objects=[]
    for p in addresses:
        addr_objects.append(add_address(p['flat_no'], p['house_no'], p['street'], p['city'], p['province'], p['postcode'], p['country']))
    
    flats = {'flat1': {'address':addr_objects[0],'rent': 100, 'description':'Lorem ipsum dolor sit amet, \
        consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.' },
	'flat2':{'address':addr_objects[1],'rent': 200, 'description':'Lorem ipsum dolor sit amet, \
        consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.' }}
   
    for flat_name, flat_data in flats.items():
        f = add_flat(flat_name, flat_data['address'], flat_data['rent'], flat_data['description'])

    for c in Flat.objects.all():
        print(c)

def add_address(flat_no, house_no, street, city, province, postcode, country):
    a = Address.objects.create()
    a.flat_no=flat_no
    a.house_no=house_no
    a.street=street
    a.city=city
    a.postcode=postcode
    a.country=country
    a.save()
    return a

def add_flat(name, address, rent, description):
    f = Flat.objects.create()
    f.name = name
    f.address = address
    f.rent=rent
    f.description=description
    f.save()
    return f

if __name__ =='__main__':
        print('Starting flatshare population script...')
        populate()


