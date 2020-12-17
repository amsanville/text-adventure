#from termcolor import colored
class Room:

    __help = 'This is the help message. Nothing here right now. Will be universal help message'

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
    
    # Enter the room: print the appropriate message
    def enter_room(self):
        print(self.__room_name)
        # If the room has not been visited
        if not self.__visited:
            print(self.__initial_message)
            self.__visited = True
        else:
            print(self.__visited_message)
    
    def list_interactions(self):
        # List the neighboring rooms
        print('Places you can go:')
        for count, room in enumerate(self.__neighboring_rooms, 1):
            print(str(count) + '.', room)
        # List objects of interest
        print('Objects of interest in the room:')
        if(len(self.__room_objects) == 0):
            print('* No objects of interest here.')
        else:
            for item in self.__room_objects:
                print('*', item)

    # Examine the room: prints the initial message
    def examine_room(self):
        print(self.__initial_message)

    # Go - leave for next room, returns the name of the next room (or here for staying here)
    def go(self, where):
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
            print('go usage error: Please enter an integer corresponding to the room you would like to go to')
            

    # Help - display the help method
    def help(self):
        print(self.__help)

    # Hints - display the appropriate hint
    def hint(self):
        if self.__hint_count < len(self.__hints):
            print('Hint:', self.__hints[self.__hint_count])
        else:
            print('No more hints for this room (try exploring the others)')


def test_room():
    # Testing the room class
    init_room = Room('Initial Room', 'Initial Message', 'Visited Message', ['Second Room'], ['Light switch'], ['Try going to another room', 'Yeah def go to another room'])
    # Should be: Initial Room\nInitial Message
    init_room.enter_room()
    # Should list Second Room and light switch appropriately
    init_room.list_interactions()
    # Should be: Initial Message
    init_room.examine_room()
    # Should be: generic help message that isn't finished
    init_room.help()
    # Should be the first hint
    init_room.hint()



if __name__ == '__main__':
    test_room()