Algorithm

The variable lastSpaceIndex stores the index of space character last found. Initialize its value to -1.

Traverse over each character of the string from 0th index to nth index using strindex

As strIndex points to a space character, mark the start and end index of the current word in the variables startIndex and endIndex as,

The startIndex of the current word is the value of lastSpaceIndex + 1.
The endIndex of the current word is the value of strIndex - 1.
Reverse the characters in the current word using two pointer approach.

Update the lastSpaceIndex to the value of strIndex i.e the index of current space character. The next iteration will refer to this variable to identify the start position of the next word.