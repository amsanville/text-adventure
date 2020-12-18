#from termcolor import colored
my_house = {
    # Front Hallway
    'front_hallway' :
    {
        'room_name' : 'Front Hallway',
        'initial_message' : 'PLACEHOLDER: initial front hallway',
        'visited_message' : 'You return to the entrance of the house.',
        'neighboring_rooms' : ['living_room', 'bedroom', 'upstairs_hallway'],
        'room_objects' : [],
        'hints' : []
    },
    # Living Room
    'living_room' :
    {
        'room_name' : 'Living Room',
        'initial_message' : 'PLACEHOLDER: initial living room',
        'visited_message' : 'You return to the living room.',
        'neighboring_rooms' : ['front_hallway', 'shower_closet', 'back_hallway'],
        'room_objects' : [],
        'hints' : []
    },
    # Shower Closet
    'shower_closet' : 
    {
        'room_name' : 'Shower Closet',
        'initial_message' : 'PLACEHOLDER: initial shower closet',
        'visited_message' : 'You return to the shower closet.',
        'neighboring_rooms' : ['living_room'],
        'room_objects' : [],
        'hints' : []
    },
    # Back hallway
    'back_hallway' :
    {
        'room_name' : 'Back Hallway',
        'initial_message' : 'PLACEHOLDER: initial back hallway',
        'visited_message' : 'You return to the back hallway.',
        'neighboring_rooms' : ['living_room', 'bathroom', 'kitchen', 'basement'],
        'room_objects' : [],
        'hints' : []
    },
    # First floor bathroom
    'bathroom' :
    {
        'room_name' : 'Bathroom',
        'initial_message' : 'PLACEHOLDER: initial bathroom',
        'visited_message' : 'You return to the bathroom.',
        'neighboring_rooms' : ['back_hallway'],
        'room_objects' : [],
        'hints' : []
    },
    # Kitchen
    'kitchen' :
    {
        'room_name' : 'Kitchen',
        'initial_message' : 'PLACEHOLDER: initial kitchen',
        'visited_message' : 'You return to the kitchen.',
        'neighboring_rooms' : ['back_hallway', 'bedroom'],
        'room_objects' : [],
        'hints' : []
    },
    # Bedroom
    'bedroom' :
    {
        'room_name' : 'Bedroom',
        'initial_message' : 'PLACEHOLDER: initial bedroom',
        'visited_message' : 'You return to the bedroom.',
        'neighboring_rooms' : ['front_hallway', 'kitchen'],
        'room_objects' : [],
        'hints' : []
    },
    # Basement
    'basement' :
    {
        'room_name' : 'Basement',
        'initial_message' : 'PLACEHOLDER: initial basement',
        'visited_message' : 'You return to the basement.',
        'neighboring_rooms' : ['back_hallway'],
        'room_objects' : [],
        'hints' : []
    },
    # Upstairs Hallway
    'upstairs_hallway' :
    {
        'room_name' : 'Upstairs Hallway',
        'initial_message' : 'PLACEHOLDER: initial upstairs hallway.',
        'visited_message' : 'You return to the upstairs hallway.',
        'neighboring_rooms' : ['front_hallway', 'upstairs_bathroom', 'red_room', 'blue_room', 'yellow_room', 'green_room'],
        'room_objects' : [],
        'hints' : []
    },
    # Upstairs Bathroom
    'upstairs_bathroom' :
    {
        'room_name' : 'Upstairs Bathroom',
        'initial_message' : 'PLACEHOLDER: initial upstairs hallway.',
        'visited_message' : 'You return to the upstairs bathroom.',
        'neighboring_rooms' : ['upstairs_hallway'],
        'room_objects' : [],
        'hints' : []
    },
    # Red Room
    'red_room' :
    {
        'room_name' : 'Red Room',
        'initial_message' : 'PLACEHOLDER: initial red room.',
        'visited_message' : 'You return to the red room.',
        'neighboring_rooms' : ['upstairs_hallway'],
        'room_objects' : [],
        'hints' : []
    },
    # Blue Room
    'blue_room' :
    {
        'room_name' : 'Blue Room',
        'initial_message' : 'PLACEHOLDER: initial blue room.',
        'visited_message' : 'You return to the blue room.',
        'neighboring_rooms' : ['upstairs_hallway'],
        'room_objects' : [],
        'hints' : []
    },
    # Yellow Room
    'yellow_room' :
    {
        'room_name' : 'Yellow Room',
        'initial_message' : 'PLACEHOLDER: initial yellow room.',
        'visited_message' : 'You return to the yellow room.',
        'neighboring_rooms' : ['upstairs_hallway'],
        'room_objects' : [],
        'hints' : []
    },
    # Green Room
    'green_room' :
    {
        'room_name' : 'Green Room',
        'initial_message' : 'PLACEHOLDER: initial green room.',
        'visited_message' : 'You return to the green room.',
        'neighboring_rooms' : ['upstairs_hallway'],
        'room_objects' : [],
        'hints' : []
    }
}

def wrap_message(curr_str, wrap_len=80):
    '''
    Wraps the string provided to the line wrap length by inserting a new line character in for the first white space character found up to the wrap length.
    curr_str - the string to be wrapped, assumes no new lines in the text
    wrap_len - the maximum length before a new line
    '''
    index = wrap_len
    while index < len(curr_str):
        # Search for white space
        temp_index = index - 1
        counter = 0
        while not curr_str[temp_index].isspace() and counter < wrap_len:
            counter += 1
            temp_index -= 1
        if counter < wrap_len:
            # If white space, replace with new-line character
            curr_str = curr_str[0:temp_index] + '\n' + curr_str[temp_index + 1:]
            index = temp_index + wrap_len + 1
        else:
            # If no white space, insert white space
            curr_str = curr_str[0:index] + '\n' + curr_str[index:]
            index += wrap_len + 1


    return curr_str

def test_wrap_message():
    '''
    Test the wrap message function.
    '''
    # No white space
    str1 = '01234567890'
    print('Expected Result:\n01234\n56789\n0')
    print('Actual Result:')
    print(wrap_message(str1, 5))

    str2 = 'A whole bunch of text that is more than 80 character. We will see if it can split the string correctly or not. Maybe across multiple lines. Maybe not. Who knows, I thought I did a good enough job...'
    print(wrap_message(str2))

class House:
    def __init__(self, new_house):
        self.__all_rooms = {}
        for key, value in new_house.items():
            self.__all_rooms[key] = Room(
                value['room_name'],
                wrap_message(value['initial_message']),
                wrap_message(value['visited_message']),
                value['neighboring_rooms'],
                value['room_objects'],
                value['hints'])

    def play_game(self):
        # Welcome message:
        print('Welcome!\n')
        print(wrap_message('This is the start of a text adventure through a home. Your goal is to collect all of the colored keys and open the lock box that you have. Try exploring the house and interacting with different things. If you ever get stuck or need help, enter the command \'help\' when prompted. Good luck!'))
        
        # Main game loop
        next_room = 'front_hallway'
        while(not next_room == 'quit'):
            # Update the current room
            curr_room = self.__all_rooms[next_room]
            curr_room.enter_room()
            curr_room.list_interactions()
            next_room = curr_room.do_input()

        # Check how game loop terminated
        if(next_room == 'quit'):
            print('Thanks for playing!')

class Room:
    # Help message for all rooms
    __help_message = 'Commands:\n* go x - replace x with the room number you want to go to\n* take x - replace x with the object you want to take\n* examine - examines the room\n* examine x - replace x with the object you want to examine\n* use x - replace x with the objet you want to use\n* use x y - replace x and y with the objects you want to use on each other\n* help - displays this message\n* hint - gives a hint of what to do next in the given room'

    def __init__(self, room_name, initial_message, visited_message, neighboring_rooms, room_objects, hints):
        # __room_name - the name of the room
        self.__room_name = room_name
        # __initial_message - the intial message played when entering the room
        self.__initial_message = initial_message
        # __visited_message - the message played after the room has been visited and the player comes back
        self.__visited_message = visited_message
        # __visisted - has the room been visited
        self.__visited = False
        # __neighboring_rooms - the names of the neighboring rooms, given as a list of strings
        self.__neighboring_rooms = neighboring_rooms
        # __room_objects - the names of the objects in the room, given as a list of strings
        self.__room_objects = room_objects
        # __hints - the hints for the room, given as a list of strings
        self.__hints = hints
        # __hint_count - the counter that tracks which hint should be given for the room. Certain events will change the state of the room. By incrementing the __hint_counter the room can keep track of which hint to give
        self.__hint_count = 0

    def enter_room(self):
        '''
        Displays the message to the player upon entering the room
        '''
        print('\n' + self.__room_name)
        # If the room has not been visited
        if not self.__visited:
            print('\n' + self.__initial_message)
            self.__visited = True
        else:
            print(self.__visited_message)
    
    def list_interactions(self):
        '''
        Displays what the player can interact with in the room
        '''
        print('\nPlaces you can go:')
        for count, room in enumerate(self.__neighboring_rooms, 1):
            print(str(count) + '.', room.replace('_', ' '))
        # List objects of interest
        print('\nObjects of interest in the room:')
        if(len(self.__room_objects) == 0):
            print('* No objects of interest here.')
        else:
            for item in self.__room_objects:
                print('*', item)

    def __examine_room(self):
        '''
        Prints the initial message
        '''
        print(self.__initial_message)

    def __go(self, where):
        '''
        Attempts to go where the user requested, returning the key of the next room. If unable to go to the next room, returns 'here'
        '''
        # Process the where input
        if(where.isdigit()):
            # Confirmed to be an integer so cast
            where = int(where)
            # Make sure it's in the correct range
            if(where > len(self.__neighboring_rooms) or where < 1):
                print('go usage error: Please enter a valid location number.')
                return 'here'
            else:
                return self.__neighboring_rooms[where - 1]
        else:
            print('\nError: Please enter an integer corresponding to the room you would like to go to')
            return 'here'
            

    def __help(self):
        '''
        Displays the help message
        '''
        print(self.__help_message)

    def __hint(self):
        '''
        Displays the appropriate hint
        '''
        if self.__hint_count < len(self.__hints):
            print('\nHint:', self.__hints[self.__hint_count])
        else:
            print('\nHint: No more hints for this room (try exploring the others)')

    def do_input(self):
        '''
        Asks the user for input and processes that input. Returns a string of what the user wants to do next upon leaving the room (either the key of the next room or 'quit')
        '''
        # Loop on user input
        done = False
        next_room = ''
        while(not done):
            user_input = input('\nWhat do you do?\n').split()
            # Validate the input
            if(user_input[0] == 'go' and len(user_input) == 2):
                # Attempt to go to the next location
                next_room = self.__go(user_input[1])
                if(not next_room == 'here'):
                    done = True
            elif(user_input[0] == 'examine' and len(user_input) == 1):
                # Examine the room
                self.__examine_room()
            elif(user_input[0] == 'help' and len(user_input) == 1):
                # Help message
                self.__help() 
            elif(user_input[0] == 'hint' and len(user_input) == 1):
                # Hint message
                self.__hint()
            elif(user_input[0] == 'quit' and len(user_input) == 1):
                # Quit the game
                done = True
                next_room = 'quit'
            else:
                print('\nError: unrecognized command for a list of valid commands')
        return next_room

def main():
    the_house = House(my_house)
    the_house.play_game()

if __name__ == '__main__':
    main()

