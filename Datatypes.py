# Создать переменную типа String: 

   Name = 'Kristina'

# Создать переменную типа Integer:

   i_1 = 5
 
# Создать переменную типа Float:

   N_2 = 2.8

# Создать переменную типа Bytes: 

   empty_bytes = bytes (4)     
   print(empty_bytes)
   print(type (empty_bytes))
   Результат в консоли:
   b'\x00\x00\x00\x00'
   <class 'bytes'>

   data_bytes = bytes(b'\xFF\xFF')
   print(data_bytes)
   Результат в консоли: b'\xff\xff'

# Создать переменную типа List:

   t2 = [1,2,'Kristina','Tur']
   print(t2)
   Результат:[1,2,'Kristina','Tur']

# Создать переменную типа Tuple:

   t_3 = (1,2,'Kristina','Tur')
   print(t_3)
   Результат:(1,2,'Kristina','Tur')


# Создать переменную типа Set:

# Создание пустого сета
   s = set()
   print(s)
   Результат в консоли:set()

   s = set('hello')
   print(s)
   Результат в консоли:{'h', 'l', 'e', 'o'}

   f_set = {"Alex","John", "Mike","Alex"}
   print (f_set)
   Результат в консоли: {'John', 'Mike', 'Alex'}

# Создать переменную типа Frozen set: к данной функции нельзя ничего добавить

   s_set = set ("Hello")
   f_set = frozenset ("Qwerty")
   s_set.add(22)
   print(s_set)
   Результат в консоли:{'l', 'H', 'e', 22, 'o'}

   f_set.add(22)
   print(f_set)
   Результат в консоли:AttributeError: 'frozenset' object has no attribute 'add'


# Создать переменную типа Dict:
   my_dict = { } 
   my_dict["country"] = "Mexico" 
   print(my_dict)
   Результат в консоли:{'country': 'Mexico'}

# Вывести в консоль все выше перечисленные переменные с добавлением типа данных:

   print (( Name ,type(Name)), ( i_1,type(i_1)), (N_2,type (N_2)), (empty_bytes, type(empty_bytes)),(t2, type(t2)),(t_3 type(t_3)),(s, type(s)),(f_set,type(f_set)), (my_dickt, type(my_dict)) )

# Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
   a = 'Kristina'
   b = 'Tur'
   result = a+b
   print(result)


# Вывести в одну строку переменные типа String и Integer используя “,” (Запятую):    
      a = '5'
      b = "elok"
      print(a,b)

# Вывести в одну строку переменные типа String и Integer используя “+” (Плюс):      
      a = '3'
      b = 'porosenka'
      print(a+b)
