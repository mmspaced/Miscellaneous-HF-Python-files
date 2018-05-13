import pprint

people = {}

people['Ford'] = {'Name': 'Ford Prefect',
                  'Gender' : 'Male',
                  'Occupation': 'Researcher',
                  'Home Planet': 'Betelgeuse Seven'}

people['Arthur'] = {'Name': 'Arthur Dent',
                    'Gender': 'Male',
                    'Occupation': 'Sandwich-Maker',
                    'Home Planet': 'Earth'}

people['Trillian'] = {'Name': 'Tricia McMillian',
                      'Gender': 'Female',
                      'Occupation': 'Mathematician',
                      'Home Planet': 'Earth'}

people['Robot'] = {'Name': 'Marvin',
                   'Gender': 'Unknown',
                   'Occupation': 'Paranoid Android',
                   'Home Planet': 'Unknown'}

pprint.pprint(people)

print()
print("Ford's name is", people['Ford']['Name'])
print()
print('Arthur is a', people['Arthur']['Gender'])
print()
print('Trillian works as a', people['Trillian']['Occupation'])
print()
print('Robot hails from', people['Robot']['Home Planet'])

