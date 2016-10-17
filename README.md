# FutoshikiGame
A futoshiki game built in Python for a workclass in USP - Universidade de São Paulo
I decided to built it in Python because I really wanted to learn Python, and the awesome way to do that is in a workclass with a small deadline in a language I didn't knew a thing, because well, I'm suicidal.
But it worked! And now I know some things in Pyhton!

#How To Use It
My teacher asked for this data structure of inputs and outputs:
The input will have a line for the number of cases to solve,
	the next line will be the size of the game and the number of restrictions,
	then we'll receive the initial game setting and then the restrictions.
The restrictions are like:
1 2 3 4
That represents that the cell (1,2) should be minor than (3, 4), like (1,2) < (3, 4)
That's a restriction.
The output will be the number of the case solved and the solution.

#Input
1              <- Number of test cases
4 4	       <- Game size and number of restrictions
0 0 0 0	       <- Game initial setting
0 0 0 0
0 0 0 0
0 0 0 0
2 1 1 1	       <- Restrictions like (2,1) < (1, 1)
2 4 1 4
2 2 2 1
4 2 4 3

#Output
1
4 3 1 2 
3 2 4 1 
1 4 2 3 
2 1 3 4 
