# knights_path
Sample pathfinding command line program that remembers and returns the most efficient path taken.


### environment
```
python 3.9
```

### dependencies
```
no external libraries used
```
### input
Program takes two user inputs as strings in chess notation format ('[A-Z][a-z]{1}[0-9]{1}'), validating that they correspond to a legal position on the board. Suggested options are shown to the user as prompts, with invalid inputs highlighted and ignored.

### output
Prints the shortest path found using the available moves of a knight as a space-separated string.

### notes
Program uses chess board size of 8, this can be modified with range of 6-26 by a global variable but increasing this is not advisable due to algorithmic complexity of O(n^8). 

Assumed user is not malicious, validation could alternately be performed by regex pattern matching - this could be a more secure option but is less immediately readable.

Used queue from built-ins instead of simple list to handle move queueing, though could be accomplished without any imports.

Pathfinding is done using breadth-first search, for larger boards more efficient algorithm such as Dijkstra could be implemented to improve runtime.

Mapping of chess notation to matrix position done by using ASCII index position. Dict could be populated using char list for key, value lookup as alternate method.