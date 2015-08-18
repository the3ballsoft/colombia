import json
from pprint import pprint

with open('colombia_json.json') as data_file:
    data = json.load(data_file)

id_department = 1
id_city = 1

#print(data.__class__)
#print(data['Santander'])

f = open('colombia_sql.sql','w')

f.write('/* Table Deparments */\n')
f.write('DROP TABLE IF EXISTS departments;\n')
f.write('CREATE TABLE IF NOT EXISTS departments( `id` int(11) NOT NULL AUTO_INCREMENT, `name` varchar(255) NOT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1;\n\n') 
id_department = 0
for r in data:
    id_department = id_department+1
    f.write('INSERT INTO departments(`id`, `name`) VALUES ('+str(id_department)+', "'+r+'");\n') # python will convert \n to os.linesep
    
f.write('\n/* Table Cities */\n')
f.write('DROP TABLE IF EXISTS cities;\n')
f.write('CREATE TABLE IF NOT EXISTS cities( `id` int(11) NOT NULL AUTO_INCREMENT, `name` varchar(255) NOT NULL, `department_id` int(11) NOT NULL, PRIMARY KEY (`id`), FOREIGN KEY (`department_id`) REFERENCES departments(`id`)) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;;\n\n')
id_department = 0
id_city = 0
for r in data:
    id_department = id_department+1
    for city in data[r]:
        id_city = id_city+1
        f.write('INSERT INTO cities(`id`, `name`, `department_id`) VALUES ('+str(id_city)+', "'+city+'", '+str(id_department)+' );\n') # python will convert \n to os.linesep

f.close() # you can omit in most cases as the destructor will call it
