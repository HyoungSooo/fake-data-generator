from ninja import Router
from faker import Faker
import json
from django.http import JsonResponse
from api.utils import get_random_seed

router = Router()

@router.get('/names')
def create_names(request, country:str = "", count:int = "", split:bool = False):
    num = get_random_seed()
    res = {}
    if country:
      fake = Faker(country)
    else:
      fake = Faker()
    Faker.seed(num)
    if not count:
       count = 1
    try:
      if split:
        res = {i : {'first': fake.first_name(), 'last' : fake.last_name()} for i in range(count)}
      else:
        res = res = {i : fake.name() for i in range(count)}
    except:
      return JsonResponse({'msg' : 'something error'})
    

    return JsonResponse(res)

@router.get('/address')
def create_random_address(request, category:str='', count:int = ''):
    '''
    category = ['city', 'city__suffix', 'country', 'country__code', 'street_name']
    '''
    num = get_random_seed()

    fake = Faker()
    Faker.seed(num)

    if not count:
       count = 1
    try:
      if category == 'city':
        return JsonResponse({i: fake.city() for i in range(count)})
      elif category == 'city__suffix':
        return JsonResponse({i: fake.city_suffix() for i in range(count)})
      elif category == 'country':
        return JsonResponse({i: fake.country() for i in range(count)})
      elif category == 'country__code':
        return JsonResponse({i: fake.country_code() for i in range(count)})
      elif category == 'street_name':
        return JsonResponse({i: fake.street_name() for i in range(count)})
      else:
        return JsonResponse({i: fake.address() for i in range(count)})
    except:
      return JsonResponse({'msg' : 'unvalid tag in category'})
    

@router.get('/licenseplate')
def get_random_license_plate(request, count:int = ''):

    num = get_random_seed()

    fake = Faker()
    Faker.seed(num)

    if not count:
      count = 1
    
    return JsonResponse({i: fake.license_plate() for i in range(count)})


