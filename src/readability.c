#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

float liau(int letters, int words, int sentences)
{
    // letters / words = letters (per 100 words) / 100
    // therefore: (letters / words) * 100 = letters (per 100 words)
    // same applys for sentences / words

    // typecasting
    // letters per 100 words
    float L = (letters / (float)words) * 100;
    // sentences per 100 words
    float S = (sentences / (float)words) * 100;


    float index = 0.0588 * L - 0.296 * S - 15.8;

    return index;
}

int main()
{
    // string text
    char text[1000] = "";
    // get text
    printf("Text: ");
    fgets(text, sizeof text, stdin);

    // counts
    int sentences = 0;
    int words = 1; // include the first word
    int letters = 0; // doesn't include digits

    // store length
    int length = strlen(text);

    // interate through chars
    for (int i = 0; i < length; i++)
    {
        // current char
        char ch = text[i];

        // add sentence
        if (ch == '.' || ch == '!' || ch == '?')
        {
            sentences++; // log sentence
        }
        // add word
        else if (ch == ' ')
        {
            words++; // log word
        }
        // given char is a letter
        else if (isalpha(ch))
        {
            letters++; // log letter
        }
    }

    float index = liau(letters, words, sentences);

    // over sixteen
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %.0f\n", round(index));
    }
}
