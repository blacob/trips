# Trips
A python program to track driving history for people.

## Dependencies
Python3

## Usage
On command line, run
```bash
python3 trips.py input.txt
```
where input.txt can be any path to a valid input file, as described in
the problem spec.  

## Thought Process

The heart of this implementation revolves around the Driver class.
I decided to create a class for Drivers because the operation which I needed to do seemed aligned with the operations that I new python supported.
For example, I knew that I would have to sort the driver reports at the end of my program, and I knew that python list built in sort method takes a key parameter that can sort objects based on, in this case, a chosen attribute of that object. Additionally, I knew that my job of formatting the output would be easier once I could implement a general __repr__ method that applied to all Drivers.

As for the implementation of the main function, there were a few decisions to be made.
In fact, even in manipulating the input from a filename into a usable form, I ran into a question of how to clean the data. I felt that it was reasonable to assume that line of input should internally contain "\n", and so I scrubbed that from input.

Now, onto the handling of commmands. In the case of a Driver command, I simply needed to create a new driver object. But I also needed to keep track of my existing drivers, for which I used a python dictionary because I wanted quick search time from names to driver objects for my Trip commands.

Once I had processed the various commands, my necesarry data was stored properly, and form there it was just a matter of processing it for output, much of which I discussed in the first section. 
