# Puzzler 2020

Find all words in this bi-directional graph:

![](graph.png)

## Python

There are two Python implementations of this in the repo.  The initial version is
about 60 lines long, but has generally the good performance.  The other version
was written to see how little code could be used and is 3 lines long and contains
240 characters.

```
$ time ./puzzler.py | wc -l
     484

real	0m0.607s
user	0m0.399s
sys	0m0.081s
```

```
$ time python3 pzr.py /usr/share/dict/words | wc -l
     484

real	0m1.528s
user	0m1.183s
sys	0m0.094s
```

Both of these programs use the same approach and use sets to check if each (overlapping)
pair of characters in the string are valid for the graph.

## Bash/shell

After writing the short version in Python I was curious to see if I could write
a still shorter program using bash.  In the end it was possible to implement
this via a single `grep` command (totally 166 characters):

```
$ cat /usr/share/dict/words | time ./puzzler.sh | wc -l
        0.26 real         0.25 user         0.00 sys
     484
```

Performance of this is surprisingly good and the regex used while long is not
actually very complicated.  The main trick to using the regex was to rely on
matching words not in the graph and then negate that match with `-v` in `grep`.

## Rust

As the grep command was faster than the Python code I was then intrigued to see
if using Rust would be faster still.  When compiled in release mode it is
faster than the grep command:

```
$ rustc -C opt-level=3 puzzler.rs 
$ time ./puzzler | wc -l
     484

real	0m0.193s
user	0m0.147s
sys	0m0.012s
```

This one relies on using Rust's match statement, which should compile to
pretty efficient code.
