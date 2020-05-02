# rprover9
A client to wrap a prover9 to be used for NLTK without installing prover9.

## Why do you need this?

If you cannot build or install Prover9/Mace4, you can use this remote access to prover9 and mace4.

It is highly recommended to use the original program here:
https://www.cs.unm.edu/~mccune/prover9/

## What?

This is a web client that imitates prover9 and mace4 that is suitable for using with NLTK. 
To secure the server the maxtime of prover and the search size of the model builder is fixed.

## Requirements

* aiohttp

## How?

```
import nltk
from nltk.sem import Expression
read_expr = Expression.fromstring
p1 = read_expr('man(socrates)')
p2 = read_expr('all x.(man(x) -> mortal(x))')
c1 = read_expr('mortal(socrates)')
c2 = read_expr('-mortal(socrates)')

prover = nltk.Prover9()
prover.config_prover9('./prover9_bin')
print(prover.prove(c1, [p1, p2])) # True
print(prover.prove(c2, [p1, p2])) # False

mace = nltk.Mace()
mace._mace4_bin = './prover9_bin/mace4'
print(mace.build_model(None, [p1, p2, c1])) # True
print(mace.build_model(None, [p1, p2, c2])) # False
```

