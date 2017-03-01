## Generalized Sandpiles

Sandpiles are a very interesting construct to play with. Guided by 2 simple rules, they make _for fun_ (noticed the alliteration?) visualizations. 

Here are the vanilla sandpile rules:

 1.  You have a grid of blocks (may or may not be a square). Each square in the grid can hold maximum of 3 sand particles.

 2.  When any grid exceeds 3 sand particles, they topple


<img src="https://github.com/darshanime/sandpiles/blob/master/images/sandpiles_1.png" width="250" height="250">
<img src="https://github.com/darshanime/sandpiles/blob/master/images/sandpiles_2.png" width="250" height="250">
<img src="https://github.com/darshanime/sandpiles/blob/master/images/sandpiles_3.png" width="250" height="250">

This happens forever until we have a stable sandpile. Pretty neat eh?

## Generalized sandpiles

In this project, I have generalized the maximum that any square can hold. 

So, you can choose the maximum for any one square to be say, 10 while everone else is at 3. 

This can make for some pretty graphics when done on a large sandpile.

## Interactive script

Try the `interactive.py` script for a flavor of the sandpile simulation (and to tire your fingers)

```
    $ python interactive.py
    Enter dimensions of grid (eg, 4x4):
    2x2
    Max for row 1, col 1:
    3
    Initial for row 1, col 1:
    5
    Max for row 1, col 2:
    3
    Initial for row 1, col 2:
    6
    Max for row 2, col 1:
    3
    Initial for row 2, col 1:
    4
    Max for row 2, col 2:
    3
    Initial for row 2, col 2:
    7
    
    Ran for 4 iterations
```
The script will produce this image

![img](https://github.com/darshanime/sandpiles/blob/master/images/sandpiles_4.png)

Inspired by this amazing video - <https://www.youtube.com/watch?v=1MtEUErz7Gg>
