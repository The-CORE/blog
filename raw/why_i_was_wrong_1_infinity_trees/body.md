## The Diagonal Argument

As I said last time, the diagonal argument goes a little like this...

> Let $s$ be the set of all real numbers between zero and one.  
> For each of the positive integers, pick a random member of $s$, and never
> repeat.  
> Write these out, in binary, with all the infinite digits of each real.  
> <br>
> For example:  
> $s_1$: $0.100111010...$  
> $s_2$: $0.011111110...$  
> $s_3$: $0.100111000...$  
> $s_4$: $0.110101000...$  
> $s_5$: $0.010100000...$  
> $s_6$: $0.000010011...$  
> $s_7$: $0.110001101...$  
> $s_8$: $0.100100011...$  
> $s_9$: $0.111100111...$  
> $...$  
> <br>
> Then, you take the first digit of the first number, the second digit of the
> second number, the third of the third, and so on, and make a new number by
> inverting these digits (turning $0$s to $1$s and $1$s to $0$s).  
> <br>
> i.e.  
> $s_1$: $0.\color{rgb(0, 255, 51)}{\mathbf{1}}00111010...$  
> $s_2$: $0.0\color{rgb(0, 255, 51)}{\mathbf{1}}1111110...$  
> $s_3$: $0.10\color{rgb(0, 255, 51)}{\mathbf{0}}111000...$  
> $s_4$: $0.110\color{rgb(0, 255, 51)}{\mathbf{1}}01000...$  
> $s_5$: $0.0101\color{rgb(0, 255, 51)}{\mathbf{0}}0000...$  
> $s_6$: $0.00001\color{rgb(0, 255, 51)}{\mathbf{0}}011...$  
> $s_7$: $0.110001\color{rgb(0, 255, 51)}{\mathbf{1}}01...$  
> $s_8$: $0.1001000\color{rgb(0, 255, 51)}{\mathbf{1}}1...$  
> $s_9$: $0.11110011\color{rgb(0, 255, 51)}{\mathbf{1}}...$  
> $\color{rgb(0, 255, 51)}{...}$  
> Highlighted digits: $\color{rgb(0, 255, 51)}{110100111...}$  
> $\therefore$ the new numbers is: $0.001011000...$  
> <br>
> However, this number is different from every number in the list above in at
> least one way.  
> <br>
> So, we have not indexed every item in $s$, despite using all the positive
> integers.  
> <br>
> And therefore, as there are the same number of integers as there are
> positive integers, there are more numbers between zero and one, than there
> are integers.

Now this looks rather conclusive. And as it turns out, perhaps unfortunately for my past self, it is.

See, I had looked at arguments for the countability of the rationals (mirrored in [my "intervals" argument](/infinity-trees#intervals) that seemed to function by simply looking at the numbers in a different way, and so I became convinced that my tree could be a way of looking at the numbers in a different way that allowed them to be counted.

However, fortunately for his diagonal argument, Cantor cares not from whence the sequence comes. In my example I said to pick from the reals in a random order, but that is by no means required. You could pick from the reals in *any* order. The actual diagonal argument (and not my failing mimicry) very delibrately does not prescribe the order in which you try to write out the rationals. There *are* more reals than integers, and no new way of looking at it I invent is going to change that.

## Bijections

Additionally, as if that wasn't enough, I want to extend on something I touched on last time, but clearly didn't understand fully: bijections.

I clearly had some sense that only being able to go from integers to "reals", and not the other way was a problem:

> Unfortunately though it is only one way. It only goes from non-negative integers to reals, not the other way around. This argument would be much more conclusive if it could go the other way.

Though I clearly didn't understand why, or how to articulate it, what I seem to have been trying to argue last time was that I had found a bijection from the integers to the reals. To delve into what these means exactly we will have to deal a little with how we formalise functions.

So, if we have a function $f: A \rightarrow B$, where $A$ is a set called the "domain" and $B$ is a set called the "codomain"

## Distance Down the Tree

And thirdly I want to discuss a rather short, and more high-level issue with what I was claiming. Essentially, the irrationals are all infinitely far down the tree.

One of my claims was that because all the rows were finite, I could just count along every row, and as I wouldn't "run out" of integers, I could count all the reals because, I figured, they were all on there somewhere.

But there is at least one substantial issue with this

## And Another Thing

Me assuming that I had to build functions out of well known elementary functions
