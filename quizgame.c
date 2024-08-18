#include <stdio.h>

int main() {
    int score = 0;

    printf("Science Quiz\n");
    printf("-----------\n");

    // Question 1
    printf("What is the largest planet in our solar system?\n");
    printf("A) Earth\n");
    printf("B) Saturn\n");
    printf("C) Jupiter\n");
    printf("D) Uranus\n");

    char answer1;
    scanf(" %c", &answer1);

    if (answer1 == 'C' || answer1 == 'c') {
        score++;
        printf("Correct!\n");
    } else {
        printf("Incorrect. The correct answer is C) Jupiter.\n");
    }

    // Question 2
    printf("What is the process by which plants make their own food?\n");
    printf("A) Respiration\n");
    printf("B) Photosynthesis\n");
    printf("C) Decomposition\n");
    printf("D) Fermentation\n");

    char answer2;
    scanf(" %c", &answer2);

    if (answer2 == 'B' || answer2 == 'b') {
        score++;
        printf("Correct!\n");
    } else {
        printf("Incorrect. The correct answer is B) Photosynthesis.\n");
    }

    // Question 3
    printf("What is the largest living species of lizard?\n");
    printf("A) Komodo dragon\n");
    printf("B) Saltwater crocodile\n");
    printf("C) Black mamba\n");
    printf("D) African elephant\n");

    char answer3;
    scanf(" %c", &answer3);

    if (answer3 == 'A' || answer3 == 'a') {
        score++;
        printf("Correct!\n");
    } else {
        printf("Incorrect. The correct answer is A) Komodo dragon.\n");
    }

    // Question 4
    printf("What is the scientific term for the 'building blocks of life'?\n");
    printf("A) Cells\n");
    printf("B) Molecules\n");
    printf("C) Tissues\n");
    printf("D) Organs\n");

    char answer4;
    scanf(" %c", &answer4);

    if (answer4 == 'A' || answer4 == 'a') {
        score++;
        printf("Correct!\n");
    } else {
        printf("Incorrect. The correct answer is A) Cells.\n");
    }

    // Question 5
    printf("What is the process by which water moves through a plant, from the roots to the leaves?\n");
    printf("A) Respiration\n");
    printf("B) Photosynthesis\n");
    printf("C) Transpiration\n");
    printf("D) Evaporation\n");

    char answer5;
    scanf(" %c", &answer5);

    if (answer5 == 'C' || answer5 == 'c') {
        score++;
        printf("Correct!\n");
    } else {
        printf("Incorrect. The correct answer is C) Transpiration.\n");
    }

    printf("Your final score is %d/5.\n", score);

    return 0;
}