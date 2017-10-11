## Different sizes of infinity

To begin, it is important to note one interesting thing about infinity: that
there are different sizes of it. I am going to reference certain sets of
numbers being the same size (integers, positive integers, negative integers,
odd numbers, even numbers, rational numbers, etc. (I may also refer to sets of
this size as countable)) and more importantly some perhaps not being the same
size. The core idea about these sets being, or not being, the same size is
quite simple though (at least to my understanding): if you can match one set up
one for one with the other, without ever running out of either set, then they
are the same size. If you can't match them one-to-one, then, the set that
didn't 'run out' is larger.  

<br>

For example, you can match all the positive integers up with a positive even
integer ($1$ goes with $2$, $2$ goes with $4$, $3$ goes with...), and you will
never run out of either. And, as you will see, the argument for there being
more numbers between zero and one that I will focus on centres around not
being able to do this one-to-one mapping. So, without further ado, lets get
onto that.  

## The Diagonal Argument

A typical argument given for there being more numbers between zero and one is a
specific application of part of Cantor's Diagonal Argument. It is no doubt
put much better by <a
href='https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument'
target='_blank_'>Wikipedia</a>, <a
href='https://www.youtube.com/watch?v=elvOZm0d4H0' target='_blank_'>
Numberphile</a>, and <a href='https://www.youtube.com/watch?v=s86-Z-CbaHA'
target='_blank_'>Vsauce</a>, but below I shall attempt to describe a simplified
(and slightly modified to my specific case) version of the argument as well.

<br>

It goes something like this:

<br>

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

<br>

This argument certainly seems quite conclusive to me, but, is it enough?.
Because, I think I have another way of looking at the real numbers that allows
them to be 'counted', mapped one to one with the integers (or some other set of
equivalent size), and (for reasons you will see below) I don't think that
looking at them another way is necessarily an unreasonable way of going about
doing this.

## Intervals

One of the first things to deal with is the fact that the argument above and my
argument below simply deal with the real numbers within an interval (in both
cases between zero and one). Now, in the case of the former it certainly seems
fine, because proving there are more members in a subset of set $a$ than there
are members in all of set $b$, means that there are more members in set $a$
than there are in set $b$. But, with my contrarian case, it is not so clear.
Even if I showed that I could map one to one all the integers to all the real
numbers between zero and one, would that mean that I could map an integer to
all the real numbers?

<br>

And supposing that we could give every real number in a given interval a
corresponding positive integer (which we could do if we could map them to
another set of the same size), what would that mean? Well, we could then create
a set for the reals between every pair of adjacent integers (including the
integer below, and not including the one above to make them tessellate nicely),
and we would have a range that covered all the reals. And, as it turns out, we
could actually map integers one-to-one with this, using the diagram below. We
can place the positive integer index within each set across the axis at the
top, and the integer that is the lower bound of the range across the axis on
the left (covering the negatives by alternating, e.g. $[0, 1, -1, 2, -2, 3,
...]$).   

![Grid counting diagram](
    ..\static\infinity_trees\grid_counting.svg
    "I got this idea from the Numberphile video I linked above. It was used
    for the positive rationals there."
)

Now, after that, we are left with an integer grid, extending off both right and
down forever, with as many coordinates on each axis as there are integers. We
clearly can't count it by counting rows or columns, as we could never finish
them, there are as many in each as we have integers to count with. But we can
still count it. We can count the diagonals as given by the numbers in the
squares. Each diagonal is of finite length, so, we will always finish all of
them, and we will never run out of integers.  

<br>

I should probably say that I got this idea from the <a
href='https://www.youtube.com/watch?v=elvOZm0d4H0' target='_blank_'>
Numberphile video</a> that I referenced at the top of the post, though it was
used for the positive rationals there.  

<br>

There is an additional benefit to considering this. It reveals that the way we
arrange the numbers influences our ability to count them. Simply 'looking' at a
set a certain way can make it clear that it is countable, where looking at
it in other ways would have it appear that it wasn't. This is fundamental to my
notion of the tree, as all it is is a different way of arranging the numbers,
and I think that it does allow us to count them.

## Infinity Trees

And so, we finally come to the namesake of this post...

### Reals Representation

I have chosen to deal with the reals in much the same way as I did in my
description of the diagonal argument, in binary, as infinite stings of
digits. I was initially worried that this may not be an adequate description,
as it may not, for instance, include irrational numbers (are infinite digits of
$\pi$ actually equivalent to $\pi$?), and issues relating to this will come up
[later](#the-issue-with-irrationals). But, as the definition I am using is
basically the same as that used for the diagonal argument, even if it didn't
fully encapsulate the reals, it seems to fully encapsulate some set that seems
to contain more members than the set of integers, so, the question is
interesting anyway.  

### The Structure

![Infinity trees diagram](
    ..\static\infinity_trees\infinity_trees.svg
    "I will still get to the duplicates. Eventually."
)

The arrangement that I believe allows the reals to be counted is the tree graph
depicted above. Each node is a number (written in binary), and each number is
connected to two other numbers below it, and, one above it. The two numbers
below it are both itself, and a number a specific power of two (depending on
how far down the tree it is) greater than itself.  

<br>

All of the numbers represent unending decimals, but, some of the trailing zeros
(and only zeros) have been removed for simplicity. The number of significant
figures displayed is to represent the relevant power of two to be changed at
that particular depth down the tree.  

<br>

Also, you may have noticed the duplicates. Each number appearing infinitely
many times in fact, with every left branch of the tree being the number above
it. While this may be a strange way of counting something, it was necessary to
continue to subdivide the numbers.  

<br>

Most importantly though: the diagram shows that each row can quite easily be
counted. This tree halves reals between zero and one, over and over again, and
goes on forever, but, as each row is clearly finite, you won't run out of
integers to count with. As this tree never ends, every combination of digits
that was expressed in the [diagonal argument](#the-diagonal-argument) should
appear. This hand-waving argument seems fine to me, it seems to me that we can
in fact list, or count, all of the real numbers, mapping them to integers just
by counting along the rows.  

<br>

However, if we look into this a little further, we may see at least one
particular issue arise.  

### The issue with irrationals

While I will go into the details of actually making a set out of the tree
below, one thing is easier to see when looking at the tree itself.  

![Infinity trees diagram](
    ..\static\infinity_trees\infinity_trees.svg
    "If you are still waiting for the duplicates thing. You missed it."
)

Where are the irrationals?  

<br>

There is no one point on the tree that I can point to and say "there's $\pi$".
And I can't work out if that means that this doesn't contain them, because the
tree won't ever stop, and each row is finite, so, I won't ever run out of
integers to count with either.  

<br>

Additionally, if I was to write $pi$ out in binary, and round it to any
precision, I would be able to find that value in the tree, and give it a
corresponding number. And then I could go to the next digit, and the next
digit, and the next, etc. So I think the question becomes: is infinitely
approaching $\pi$ equivalent to $\pi$?  

<br>

I am not sure what the answer to this question is. If the answer is no, then
this is just an inefficient way to show that we can match the rationals
one-to-one with the integers. But I _feel_ like this _might_ not be the case
(very dubious). You can create irrationals with infinite series that don't
have more terms than there are integers, and the diagonal argument seems to
imply that the numbers it deals with can have their digits mapped one-to-one
with the positive integers.  

<br>

These things make it feel like while I can't tell you where on the tree an
irrational is, that the tree extends as infinitely far into the reals as the
irrationals do. But, I don't even know what that sentence really means.

### Flattening the tree

But, despite that potentially fatal wound, I would like to try to formalise
this rather unwieldy tree into a function, that given an integer spits out a
real (though, as mentioned above, no particular integer will be able to coax
into spitting out an irrational).  

So, what do we want? We want some function, lets call it $s(n)$, that takes an
integer and gives back a real.  

<br>

So, if we just let $n$ correspond to counting across one row, and then across
the next row down, and then across the next row down, and so one, we can start
to write out what this function must look like, reading off the tree.  

<br>

| $n$    | $0$ | $1$ | $2$   | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $...$ |
|:------:| ---:| ---:| -----:| ---:| ---:| ---:| ---:| ---:| ---:|:-----:|
| $s(n)$ | $0$ | $0$ | $0.1$ |     |     |     |     |     |     | $...$ |

<br>


$$ \left \lceil{\frac{5}{2}}\right \rceil = 3$$

<br><br>

## I Expect to be Wrong

Despite the fact that this seems to make sense to me, this is also something
that it looks like a lot of smart people have spent quite a while thinking
about, and all seem to agree on, and even I can see at least one potentially
serious problem with it. So, I certainly expect to be wrong about this.  

<br>

However, I do look forward to finding out where, and why. And if you want to
let me know, there are details just below.
