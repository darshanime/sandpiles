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

```
$ pip install sandpiles
```

## Demo visualization

Use it like so:

```python

In [1]: from sandpiles.visualize import sandpile, run_pile

# creating an empty 30x100 grid
In [2]: pile = sandpile(size="30x100", initial_max=0, initial_min=0)

# adding 10,000 grains at bottom center square
In [3]: pile[(30, 50)]["#"] = 10000

# simulating the pile
In [4]: run_pile(pile, save=True)
Ran for 3644 iterations

In [5]: !ls sandpile.png
sandpile.png

```

The script will produce this image

![img](https://github.com/darshanime/sandpiles/blob/master/images/sandpiles_4.png)


## Implementation details

### `pile` structure
- The primary data structure used is the `pile` hashtable (python dict). It is *1-indexed*, and has the following structure:

```python

In [1]: pile = sandpile(size="2x2")

In [2]: pile
Out[2]:
defaultdict(dict,
            {'c': 2,
             'r': 2,
             (1, 1): {'#': 10, 'max': 3},
             (1, 2): {'#': 10, 'max': 3},
             (2, 1): {'#': 10, 'max': 3},
             (2, 2): {'#': 10, 'max': 3}})
```

So, each square in the grid has 2 parameters -
 - # --> the number of sand grains on that square
 - max --> the maximum number of grains that square can hold, after which it topples


### Toppling order

Since the maximum for any square is not 3 but can be decided by the user, I have defined a clockwise toppling order for each square. 

That means, if any square has a "max" of 2, and "#" is 3; it will topple the first grain to the square on it's left, then the one above it, next to the one to it's right. It cannot topple to the one below it because it has no more grains left now.

______

Inspired by this amazing video - <https://www.youtube.com/watch?v=1MtEUErz7Gg>
