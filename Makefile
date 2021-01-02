all: puzzlerrs puzzlerc
.PHONY : all clean

puzzlerrs: puzzler.rs
	rustc -C opt-level=3 puzzler.rs -o puzzlerrs

puzzlerc: puzzler.c
	gcc -O3 puzzler.c -o puzzlerc

clean:
	rm -f puzzlerc puzzlerrs
