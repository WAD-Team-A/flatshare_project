import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','flatshare_project.settings')
import django
django.setup()

from flatshare.models import Flat, Address

def populate():
    address1 = [
        {'flat_no':1, 'house_no':1, 'street': 'lorem ipsudem str', 'city':'Glasgow', 'province': 'Lanarkshire', 'postcode':'G200TH', 'country':'United Kingdom'},
       ]
    flats = {'flat1':{'address':address1,'rent': 100, 'description':'Lorem ipsum dolor sit amet, \
        consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.' }}
    for flat, flat_data in flats.items():
        f = add_flat(flat, flat_data['rent'], flat_data['description'])
        for p in flat_data['address']:
            add_address(f, p['flat_no'], p['house_no'], p['street'], p['city'], p['province'], p['postcode'], p['country'])

    for c in Flat.objects.all():
        for p in Address.objects.filter(flat=c):
            print(f'- {c}: {p}')

def add_address(flat,flat_no, house_no, street, city, province, postcode, country):
    a,created= Address.objects.get_or_create(flat=flat,city =city, postcode= postcode, country = country)
    a.flat_no =flat_no
    a.house_no=house_no
    a.street = street
    a.province = province
    a.save()
    return a

def add_flat(name, rent, description):
    f, created = Flat.objects.get_or_create(name =name, rent = rent,description=description)
    f.save()
    return f
    


if __name__ =='__main__':
        print('Starting flatshare population script...')
        populate()


