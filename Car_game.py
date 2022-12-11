command = ''
started= False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car already started')
        else:
            started = True
            print('The Car Started...')
    elif command == 'stop':
        if not started:
            print('Car already stopped')
        else:
            started = False
            print('The Car Stopped..')
    elif command == 'help':
        print("""
Start-to start car
Stop- to stop car
Quit- to exit
        """)
    elif command == 'quit':
        break
    else:
        print('I do not understand this')











