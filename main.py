#import requests
#from requests.exceptions import ConnectionError

URL = 'http://sabertech.com/'

def get_domain():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print('El nombre de dominio no está disponible')
    except ConnectionError:
        print('El nombre de dominio está disponible')
if __name__ == '__main__':
    delta = []
    my_char = ord('a')
    while my_char <= ord('z'):
        delta.append(('Q5',chr(my_char),'Q5'))
        my_char +=1
    print(delta)
    delta_num = []
    for i in range(10):
        delta_num.append(('Q5',i,'Q5'))
    print(delta_num)