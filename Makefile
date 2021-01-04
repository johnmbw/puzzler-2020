all: puzzlerrs puzzlerc
.PHONY : all benchmark clean

puzzlerrs: puzzler.rs
	rustc -C opt-level=3 puzzler.rs -o puzzlerrs

puzzlerc: puzzler.c
	gcc -O3 puzzler.c -o puzzlerc

benchmark: puzzlerc puzzlerrs
	hyperfine --warmup 3 './puzzler.py' 'python3 pzr.py /usr/share/dict/words' 'cat /usr/share/dict/words | ./puzzler.sh' './puzzlerrs' './puzzlerc'

clean:
	rm -f puzzlerc puzzlerrs
