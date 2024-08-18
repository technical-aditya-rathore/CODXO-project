#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STUDENTS 100
#define MAX_NAME_LENGTH 50

typedef struct {
    int rollNo;
    char name[MAX_NAME_LENGTH];
    int age;
    float marks;
} Student;

Student students[MAX_STUDENTS];
int studentCount = 0;

void addStudent() {
    if (studentCount < MAX_STUDENTS) {
        printf("Enter roll number: ");
        scanf("%d", &students[studentCount].rollNo);
        printf("Enter name: ");
        scanf("%49s", students[studentCount].name);
        printf("Enter age: ");
        scanf("%d", &students[studentCount].age);
        printf("Enter marks: ");
        scanf("%f", &students[studentCount].marks);
        studentCount++;
        printf("Student added successfully!\n");
    } else {
        printf("Maximum number of students reached!\n");
    }
}

void displayStudents() {
    if (studentCount == 0) {
        printf("No students in the record!\n");
    } else {
        printf("Student Record:\n");
        for (int i = 0; i < studentCount; i++) {
            printf("Roll No: %d\n", students[i].rollNo);
            printf("Name: %s\n", students[i].name);
            printf("Age: %d\n", students[i].age);
            printf("Marks: %.2f\n", students[i].marks);
            printf("\n");
        }
    }
}

void searchStudent() {
    int rollNo;
    printf("Enter roll number to search: ");
    scanf("%d", &rollNo);
    for (int i = 0; i < studentCount; i++) {
        if (students[i].rollNo == rollNo) {
            printf("Student found!\n");
            printf("Roll No: %d\n", students[i].rollNo);
            printf("Name: %s\n", students[i].name);
            printf("Age: %d\n", students[i].age);
            printf("Marks: %.2f\n", students[i].marks);
            return;
        }
    }
    printf("Student not found!\n");
}

void updateStudent() {
    int rollNo;
    printf("Enter roll number to update: ");
    scanf("%d", &rollNo);
    for (int i = 0; i < studentCount; i++) {
        if (students[i].rollNo == rollNo) {
            printf("Enter new name: ");
            scanf("%49s", students[i].name);
            printf("Enter new age: ");
            scanf("%d", &students[i].age);
            printf("Enter new marks: ");
            scanf("%f", &students[i].marks);
            printf("Student updated successfully!\n");
            return;
        }
    }
    printf("Student not found!\n");
}

void deleteStudent() {
    int rollNo;
    printf("Enter roll number to delete: ");
    scanf("%d", &rollNo);
    for (int i = 0; i < studentCount; i++) {
        if (students[i].rollNo == rollNo) {
            for (int j = i; j < studentCount - 1; j++) {
                students[j] = students[j + 1];
            }
            studentCount--;
            printf("Student deleted successfully!\n");
            return;
        }
    }
    printf("Student not found!\n");
}

int main() {
    int choice;
    while (1) {
        printf("Student Record System\n");
        printf("1. Add Student\n");
        printf("2. Display Students\n");
        printf("3. Search Student\n");
        printf("4. Update Student\n");
        printf("5. Delete Student\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                addStudent();
                break;
            case 2:
                displayStudents();
                break;
            case 3:
                searchStudent();
                break;
            case 4:
                updateStudent();
                break;
            case 5:
                deleteStudent();
                break;
            case 6:
                printf("Exiting...\n");
                return 0;
            default:
                printf("Invalid choice!\n");
        }
    }
    return 0;
}