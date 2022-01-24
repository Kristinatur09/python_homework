# Создать переменную count со значением 0:

    count = 0

# Создать переменную range_count со значением 10:

    range_count = 10

# Создать переменную for_count со значением 0:

    for_count = 0
 
# Создать переменную run  со значением True:

    run = True

# Сделать цикл while который будет работать пока run:
Тело цикла:
	5.1 Выводить в консоль “Hello Cycle”
    while = run:
      print('hello Cycle')
# Сделать цикл while который будет работать пока run:

    while run:

Тело цикла:
	# 6.1 Выводить в консоль (“Step =”, count):
    
      print('Step =', count)

	# 6.2 Переменной count прибавлять 1 с присвоением:
    count += 1
  
# Сделать цикл while который будет работать пока count < range_count:

       while count < range_count:
    
Тело цикла:
	# 7.1 Выводить в консоль (“Step =”, count):
  
     
            print('Step =', count)
   
  
	# 7.2 Переменной count прибавлять 1 с присвоением:
      
        count += 1

# Сделать цикл while который будет работать пока count < range_count:

    while count < range_count:

Тело цикла:
	# 8.1 Выводить в консоль (“Step =”, count)
  
      print('Step=', count)
  
	# 8.2 Переменной count прибавлять 1 с присвоением:
   
      count +=1
   
	# 8.3 Сделать if с условием, если count равен 3 то выводить в консоль (“Step =”, count, ‘If body’)
  
        if count == 3:
            print ('Step =', count, 'If body')

# Сделать цикл while который будет работать пока run:
      
    while run:
      
Тело цикла:
	# 9.1 Выводить в консоль (“Step =”, count):
  
      print('Step=',count)
  
	# 9.2 Переменной count прибавлять 1 с присвоением:
  
        count +=1
  
	# 9.2 Сделать if с условием, если count равен range_count то цикл остановится.
  
            if count == range_count:
   
	# 9.3 В теле if вывести в консоль (“STOP”, count)
            
                  print('Stop',count)


Цилы For
# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от for_count  до range_count:
  
        for item in range (for_count, range_count):
  
Тело цикла:
# 10.1 Вывести в консоль (‘Step =’, item)

        print('Step =', item)

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 30:

      for item in range (30)
  
Тело цикла:
# 11.1 Вывести в консоль (‘Step =’, item):

  print('Step=',item)
  
# 11.2 Сделать if с условием, если item равен  5, то вывести в консоль (‘Item =’, item):
    if item == 5:
        print('Item=',item)
# 11.3 Сделать if с условием, если item равен  10, то вывести в консоль (‘Item =’, item):

    if item == 10:
        print("Item=', item)

# 11.4 Сделать if с условием, если item меньше 4, то вывести в консоль (‘Item <’, item):
    
    if item < 4:
        print('Item <', item)
    
# 11.5 Сделать if с условием, если item больше или равно 27, то вывести в консоль (‘Item >=’, item):

    if item >=27:
        print('Item >=', item)
    

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до range_count +1

    for item in range (0, range_count+1):
    
Тело цикла:
# 12.1 Вывести в консоль (‘Step =’, item)
              
              print('Step =', item)
              
# 12.2 Сделать if с условием, если item равен  7:
              
     if item == 7:
      inner_count = 0
      print('-- inner_count =', inner_count)
        for inner_item in range(0, item):
              print('-------- Inner_Step =', inner_item)
                if inner_item == 5:
                inner_count = inner_item
                print('-- inner_count =', inner_count)
	 

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 20
              for item in range (0, 20)
Тело цикла:
# 13.1 Вывести в консоль (‘Step =’, item)
              print('Step = ', item)
# 13.2 Сделать if с условием, если item больше  7 и item меньше 12.
               if item > 7 and item < 12
	# В теле if вывести (‘If_item =’, item)
              print('If_item =', item)
	# В теле if поставить continue
              continue

# 13.3 Выйти з if. Вывести в консоль (‘End_iteration =’, item)
              print('End_iteration =', item)




	



