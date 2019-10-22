# python

started = False
while True:
 command = input('> ').lower()
 if command == 'start':
        if not started:
            print('car started ...')
            started = True
        else:
            print('car already started !!')
 elif command == 'stop':
        if not started:
            print('car already stopped!!')
        else:
            print('car stopped')
            started = False
 elif command == 'help':
        print('''
 start -> start the car 
 stop -> stop the car 
 quit -> to quit
               ''')
 elif command == 'quit':
        break
 else:
  print('dont understand that !!')
