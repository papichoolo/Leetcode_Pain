### Minimum Length of a String after deleiting Similar Ends

So this is a string based problem, and it is fairly easy to implement once you know how to use the two pointers and their condition:
```
 while(s[prefptr]==s[sufptr]&&prefptr<sufptr) for string s
```
The prefix and suffix pointer value must be same and prefix should be ahead of suffix.
We iteratively push prefix and suffix closer and return the minimun no of string after simiar ends are deleted. 
```
 return sufptr-prefptr+1;
```