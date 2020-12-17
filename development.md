# Development Plan
## Basic Design
Some of the basics of the design:
* The house is an undirected graph of connected rooms. Each room connects to a minimum of one other room and has a description of the room as well as what's inside the room.
* Inside the rooms are objects. Some objects the player can take with him/her, some cannot be taken. What makes an object distinct is that it can be used, taken, or examined.
* The player interacts with the game with a set of basic commands: go, take, examine, use, help, hint, quit.
  * go - go only interacts with other rooms. Upon entering the room, the other rooms the player can travel to are numbered. So 'go 1' will go to the first room, etc.
  * take - takes the object and puts it in the player inventory if possible
  * examine - examines the room, objects in the room, objects in inventory, or self to get a list of objects in the inventory
  * use - player uses items with other items or individually. So 'use item' will attempt to use whatever item individually, like 'use couch' might display a message, 'you sit on the couch, it is comfy'. Also, players can use items with other items. Example, 'use batteries flashlight' will attempt to put the batteries in the flashlight.
  * help - shows a menu of different commands (i.e. this summary list)
  * hint - gives a hint of what to do in the room/what can still be done

## Features
Itemized list of intended features:
[ ] Build basic house and player can travel from room to room
[ ] Make basic UI with help
[ ] Build out each room with objects for the player to interact with (following is a list of rooms)
    [ ] Front Hallway
    [ ] Living Room
    [ ] Back Hallway
    [ ] Shower closet
    [ ] First floor bathroom
    [ ] Kitchen
    [ ] First floor bedroom
    [ ] Basement
    [ ] Upstairs Hallway
    [ ] Upstairs bathroom
    [ ] Red room
    [ ] Blue room
    [ ] Yellow room
    [ ] Green room
    [ ] Basement
[ ] Time passes and certain events happen after a certain amount of time. For example, if a player spends a lot of time in a room, the game will ask if they want a hint/all hints
[ ] Use colored text to highlight items