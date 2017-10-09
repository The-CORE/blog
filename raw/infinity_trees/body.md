## Different sizes of infinity

One interesting thing about infinity is that there are different sizes of it. I
am going to reference certain sets of numbers being the same size (integers,
positive integers, negative integers, odd numbers, even numbers, rational
numbers, etc.) and more importantly some perhaps not being the same size. The
core idea about these sets being, or not being, the same size is quite simple
though (at least to my understanding): if you can match one set up one for one
with the other, without ever running out of either set, then they are the same
size. If you can't match them one-to-one, then, the set that didn't 'run out'
is larger.  

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
put much better by
[Wikipedia](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument),
[Numberphile](https://www.youtube.com/watch?v=elvOZm0d4H0), and
[Vsauce](https://www.youtube.com/watch?v=s86-Z-CbaHA), but below I shall attempt
to describe a simplified (and slightly modified to my specific case) version of
the argument as well.

<br>

It goes something like this:

<br>

> Let $r$ be the set of all real numbers between zero and one.  
> For each of the positive integers, pick a random member of $r$, and never
> repeat.  
> Write these out, in binary, with all the infinite digits of each real.  
> <br>
> For example:  
> $r_1$: $0.100111010...$  
> $r_2$: $0.011111110...$  
> $r_3$: $0.100111000...$  
> $r_4$: $0.110101000...$  
> $r_5$: $0.010100000...$  
> $r_6$: $0.000010011...$  
> $r_7$: $0.110001101...$  
> $r_8$: $0.100100011...$  
> $r_9$: $0.111100111...$  
> $...$  
> <br>
> Then, you take the first digit of the first number, the second digit of the
> second number, the third of the third, and so on, and make a new number by
> inverting these digits (turning $0$s to $1$s and $1$s to $0$s).  
> <br>
> i.e.  
> $r_1$: $0.\color{rgb(0, 255, 51)}{\mathbf{1}}00111010...$  
> $r_2$: $0.0\color{rgb(0, 255, 51)}{\mathbf{1}}1111110...$  
> $r_3$: $0.10\color{rgb(0, 255, 51)}{\mathbf{0}}111000...$  
> $r_4$: $0.110\color{rgb(0, 255, 51)}{\mathbf{1}}01000...$  
> $r_5$: $0.0101\color{rgb(0, 255, 51)}{\mathbf{0}}0000...$  
> $r_6$: $0.00001\color{rgb(0, 255, 51)}{\mathbf{0}}011...$  
> $r_7$: $0.110001\color{rgb(0, 255, 51)}{\mathbf{1}}01...$  
> $r_8$: $0.1001000\color{rgb(0, 255, 51)}{\mathbf{1}}1...$  
> $r_9$: $0.11110011\color{rgb(0, 255, 51)}{\mathbf{1}}...$  
> $\color{rgb(0, 255, 51)}{...}$  
> Highlighted digits: $\color{rgb(0, 255, 51)}{110100111...}$  
> $\therefore$ the new numbers is: $0.001011000...$  
> <br>
> However, this number is different from every number in the list above in at
> least one way.  
> So, we have not indexed every item in $r$, despite using all the positive
> integers.  
> And therefore, as there are the same number of integers as there are
> positive integers, there are more numbers between zero and one, than there
> are integers.  

<br>

This argument certainly seems quite conclusive to me, but, is it enough?.
Because, I think I have another way of looking at the real numbers that allows
them to be 'counted', mapped one to one with the integers (or some other set of
equivalent size), and I don't think that looking at them another way is
necessarily an unreasonable way of going about doing this.

## Intervals

One of the first things to deal with is the fact that the argument above and my
argument below simply deal with the real numbers within an interval, in both
cases, between zero and one. Now, in the case of the former it certainly seems
fine, because proving there are more members in a subset of, say, set $a$ than
set there are members in set $b$, means that there are more members in set $a$
than there are in set $b$. But, with my contrarian case, it is not so clear.
Even if I showed that I could map one to one all the integers to all the real
numbers between zero and one, would that mean that I could map an integer to
all the real numbers? Well, it doesn't sound like it, but, using the same
method used to map the rationals to integers.  

<br>

Well, what will we actually have a set for the reals between each pair of
adjacent integers (each of these sets includes the integer at the bottom of
the range, but not at the top, if it is set out like my tree diagram, so no
integers counted multiple times or missed). But, as it turns out, we can
actually count this. Supposing that we have shown that we could give a
corresponding positive integer for every real number in a given interval, then
we could use these integers as coordinates across the top of the diagram below.
And we could then use, say, the integer that is the lower bound of the range as
a coordinate down the right hand side (covering the negatives by alternating
$0$, $1$, $-1$, $2$, $-2$, $3$, etc.).  

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
them, and we will never run out of integers. I should probably say that I got
this idea from the
[Numberphile video](https://www.youtube.com/watch?v=elvOZm0d4H0) that I
referenced at the top of the post, though it was used for the positive
rationals there.  

<br>

There is an additional benefit to considering this. It reveals that the way we
arrange the numbers influences our ability to count them. This is fundamental
to my notion of the tree, as all it is is a different way of arranging the
numbers, and I think that it does allow us to count them.

## Infinity Trees

### Reals Representation

I have chosen to deal with the reals in much the same way as I did in my
description of the diagonal argument, in binary, as infinite stings of
digits. I was initially worried that this may not be an adequate description,
as it may not, for instance, include irrational numbers (are infinite digits of
$\pi$ actually equivalent to $\pi$?). But, as the definition I am using is
basically the same as that used for the diagonal argument, even if it does not
fully encapsulate the reals, it does fully encapsulate some set that seems to
contain more members than the set of integers.

### The Structure

![Infinity trees diagram](
    ..\static\infinity_trees\infinity_trees.svg
    "I will still get to the duplicates. Eventually."
)

The arrangement that I believe allows the reals to be counted is the tree graph
depicted above. Each node is a number (written in binary), and each number is
connected to two other numbers below it, and, one above it. The two numbers
below it are both itself, and a number a specific power of two greater than
itself.  

<br>

All of the numbers represent unending decimals, but, some of the trailing zeros
(and only zeros) have been removed for simplicity. The number of significant
figures displayed is to represent the relevant power of two to be changed at
that particular depth down the tree.  

<br>

Most importantly though: the diagram shows that each row can quite easily be
counted. This tree halves reals between zero and one, over and over again, and
goes on forever, but, as each row is clearly finite, you won't run out of
integers to count with. As this tree never ends, every combination of digits
that was expressed in the [diagonal argument](#the-diagonal-argument) should
appear. This hand-waving argument seems fine to me, it seems to me that we can
in fact list, or count, all of the real numbers, mapping them to integers just
by counting along the rows. However, I will go into the actual processes of
doing this mapping below.

<br>

You may have noticed the duplicates. Each number appearing infinitely many
times in fact, with every left branch of the tree being the number above it.
While this may be a strange way of counting something, it was necessary to
continue to subdivided the numbers.

### Coordinates

To formalise this further, we can give each position on the tree a pair of
coordinates, one for its row, and another for its position in its row.




## I Expect to be Wrong

This is something that it looks like a lot of smart people have spent quite a
while thinking about, and, it appears, all seem to agree on. So, I certainly
expect to be wrong about this, but I do look forward to finding out where, and
why.
