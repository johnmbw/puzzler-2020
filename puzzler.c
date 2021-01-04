#include <ctype.h>
#include <stdio.h>
#include <string.h>

char *ALL_LETTERS = "brchsylegwnto";
char *FOLLOWING_LETTERS[13] = {
    "rloty",
    "ceolb",
    "hgoer",
    "swogc",
    "ynowh",
    "btons",
    "breot",
    "rcgol",
    "echwo",
    "oghsn",
    "towsy",
    "blony",
    "blrecghwsnyt"
};


int match(char *line) {
    char *allowed = ALL_LETTERS;
    int c;
    int index;

    while((c = *line) != '\n') {
        c = tolower(c);
        if (strchr(allowed, c) == NULL) {
            return 0;
        }
        index = strchr(ALL_LETTERS, c) - ALL_LETTERS;
        allowed = FOLLOWING_LETTERS[index];
        line++;
    }
    return 1;
}

int main() {
    FILE *f;
    char line[100];

    f = fopen("/usr/share/dict/words", "r");
    if (f == NULL) {
        return -1;
    }

    while (fgets(line, 100, f) != NULL) {
        if (match(line)) {
            printf("%s", line);
        }
    }

    fclose(f);
    return 0;
}
