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

See, I had looked at arguments for the countability of the rationals (mirrored in [my "intervals" argument](/infinity-trees#intervals)) that seemed to function by simply looking at the numbers in a different way, and so I became convinced that my tree could be a way of looking at the numbers in a different way that allowed them to be counted.

However, fortunately for his diagonal argument, Cantor cares not from whence the sequence comes. In my example I said to pick from the reals in a random order, but that is by no means required. You could pick from the reals in *any* order (and a random order could generate any order). The actual diagonal argument (and not my failing mimicry) very deliberately does not prescribe the order in which you try to write out the rationals. There *are* more reals than integers, and no new way of looking at it I invent is going to change that.

## Bijections

Additionally, as if that wasn't enough, I want to extend on something I touched on last time, but clearly didn't understand fully: bijections.

I clearly had some sense that only being able to go from integers to "reals", and not the other way was a problem:

> Unfortunately though it is only one way. It only goes from non-negative integers to reals, not the other way around. This argument would be much more conclusive if it could go the other way.

Though I clearly didn't understand why, or how to articulate it, what I seem to have been trying to argue last time was that I had found a bijection from the integers to the reals. [Wikipedia](https://en.wikipedia.org/wiki/Bijection) will explain it better, but essentially a bijection is just a mapping that goes from any element in a set $A$ uniquely to exactly one particular element in a set $B$, and hence allows the mapping to be followed back the other way, from $B$ to $A$ uniquely and exactly as well.

And whilst finding a bijection is a valid method of showing that two sets are the same size, by no means did I do that. My function, as I said, couldn't be inverted to go the other way and so clearly wasn't a bijection, leaving the grain of truth behind my idea that "finding a mapping" would mean the sets were the same size unsupported.

## Distance Down the Tree

And thirdly I want to discuss a rather short, and more high-level issue with what I was claiming. Essentially, the irrationals are all infinitely far down the tree.

One of my claims was that because all the rows were finite, I could just count along every row, and as I wouldn't "run out" of integers, I could count all the reals because, I figured, they were all on there somewhere.

But there is at least one substantial issue with this, which is that you clearly cannot get infinite digits (and hence irrationals) in the tree until you have gone infinitely many rows down the tree, and by that time you have already "run out" of integers, whatever that means.

## And Another Thing

The lasts thing I would like to touch on here is that I spent a decent chunk of the post trying to come up with a way to express the function implied by the tree as a construct of elementary functions that I already knew, like logarithms and floors and ceilings.

Whilst I could now pretend that the motivation for doing that was to try to find an inverse function (that is, a way of going back from the reals to the integers to justify having a bijection) if that was the case I would have given up the instant I tried to use a floor or ceiling function (as you lose information in them, you can't take your answer and go back to a unique input in the set you original came from). In reality I was doing it because I thought that it wasn't a real function until I had expressed it in a form that I recognised.

What I didn't realise, and what I now think it is important to realise, is that "take the infinity tree diagram and your input, count up from zero to your input across the rows on the diagram, moving to the next row when you run out of nodes, and then take the number at the location you land as your output" is a function. All I have to do to define a function is to give a way of taking some input, and finding some output in such a way that the same input always gives the same output. Writing it out in the symbols that we all know is just building functions out of agreed upon elementary functions, and all combinations of them do not exhaust all possible functions (for one, functions are not restricted to only mapping from numbers to numbers).

## Hopefully Slightly More Conclusive Conclusion

So, I hope that at least partially absolves the mistakes in my previous post. That said, finding where I fail is why I'm here, and I expect to still be wrong somewhere above as well, or at least to have missed some ways in which I was also wrong before. As always, if I am wrong, feel free to let me know.
