use std::fs::File;
use std::io::{self, BufRead};

fn matches(word:&String) -> bool {
    let mut prev = ' ';
    for c in word.to_lowercase().chars() {
        match prev {
            ' ' => match c {
                'b'|'c'|'e'|'g'|'h'|'l'|'n'|'o'|'r'|'s'|'t'|'w'|'y' => (),
                _ => return false
            },
            'b' => match c {
                'r'|'l'|'o'|'t'|'y' => (),
                _ => return false
            },
            'r' => match c {
                'c'|'e'|'o'|'l'|'b' => (),
                _ => return false
            },
            'c' => match c {
                'h'|'g'|'o'|'e'|'r' => (),
                _ => return false
            },
            'h' => match c {
                's'|'w'|'o'|'g'|'c' => (),
                _ => return false
            },
            's' => match c {
                'y'|'n'|'o'|'w'|'h' => (),
                _ => return false
            },
            'y' => match c {
                'b'|'t'|'o'|'n'|'s' => (),
                _ => return false
            },
            'l' => match c {
                'b'|'r'|'e'|'o'|'t' => (),
                _ => return false
            },
            'e' => match c {
                'r'|'c'|'g'|'o'|'l' => (),
                _ => return false
            },
            'g' => match c {
                'e'|'c'|'h'|'w'|'o' => (),
                _ => return false
            },
            'w' => match c {
                'o'|'g'|'h'|'s'|'n' => (),
                _ => return false
            },
            'n' => match c {
                't'|'o'|'w'|'s'|'y' => (),
                _ => return false
            },
            't' => match c {
                'b'|'l'|'o'|'n'|'y' => (),
                _ => return false
            },
            'o' => match c {
                'b'|'l'|'r'|'e'|'c'|'g'|'h'|'w'|'s'|'n'|'y'|'t' => (),
                _ => return false
            },
            _ => return false
        }
        prev = c
    }
    return true
}

fn main() {
    let file = File::open("/usr/share/dict/words").unwrap();
    let lines = io::BufReader::new(file).lines();
    for line in lines {
        if let Ok(word) = line {
            if matches(&word) {
                println!("{}", word);
            }
        }
    }
}
