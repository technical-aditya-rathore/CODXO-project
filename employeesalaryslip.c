 #include <stdio.h>
#include <string.h>

struct Employee {
    char name[50];
    int emp_id;
    float basic_salary;
    float da;
    float hra;
    float pf;
    float net_salary;
};

void generate_salary_slip(struct Employee emp) {
    printf("\n\n");
    printf("EMPLOYEE SALARY SLIP\n");
    printf("-------------------------------\n");
    printf("Employee Name: %s\n", emp.name);
    printf("Employee ID: %d\n", emp.emp_id);
    printf("-------------------------------\n");
    printf("Earnings:\n");
    printf("Basic Salary: %.2f\n", emp.basic_salary);
    printf("Dearness Allowance (DA): %.2f\n", emp.da);
    printf("House Rent Allowance (HRA): %.2f\n", emp.hra);
    printf("-------------------------------\n");
    printf("Deductions:\n");
    printf("Provident Fund (PF): %.2f\n", emp.pf);
    printf("-------------------------------\n");
    printf("Net Salary: %.2f\n", emp.net_salary);
    printf("-------------------------------\n");
}

int main() {
    struct Employee emp;
    printf("Enter Employee Details:\n");
    printf("Name: ");
    fgets(emp.name, sizeof(emp.name), stdin);
    emp.name[strlen(emp.name) - 1] = '\0'; // remove newline character
    printf("Employee ID: ");
    scanf("%d", &emp.emp_id);
    printf("Basic Salary: ");
    scanf("%f", &emp.basic_salary);
    printf("DA (as a percentage of basic salary): ");
    float da_percentage;
    scanf("%f", &da_percentage);
    emp.da = (emp.basic_salary * da_percentage) / 100;
    printf("HRA (as a percentage of basic salary): ");
    float hra_percentage;
    scanf("%f", &hra_percentage);
    emp.hra = (emp.basic_salary * hra_percentage) / 100;
    printf("PF (as a percentage of basic salary): ");
    float pf_percentage;
    scanf("%f", &pf_percentage);
    emp.pf = (emp.basic_salary * pf_percentage) / 100;
    emp.net_salary = emp.basic_salary + emp.da + emp.hra - emp.pf;
    generate_salary_slip(emp);
    return 0;
}