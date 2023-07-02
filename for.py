'''
for element in range(20):
    print(element) # Va de 0 a 19
    
for element in range(1,20):
    print(element) # Va de 1 a 19
'''

my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)
    
my_tuple = ('Nico', 'Nahuel', 'Meli', 'Jose')
for element in my_tuple:
    print(element)
    
product = {
    'name': "Camisa",
    'price': 100,
    'stock': True
}

for element in product:
    print(element, ' => ', product[element])
    
for key, value in product.items():
    print(key, ' => ', value)
    
people = [
    {
        'name': 'Nico',
        'age': 30
    },
    {
        'name': 'Nahuel',
        'age': 28
    },
    {
        'name': 'Meli',
        'age': 25
    }
]

for person in people:
    print('name => ', person['name'])