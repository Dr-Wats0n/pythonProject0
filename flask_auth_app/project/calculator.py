base = int(input('Enter the amount of funds allocated for the award: '))
print('\n')


print('Section A: quantitative(measurable) KPI: ' + '\n')

print('a1: ')

plan_a1 = int(input("Enter the target sales figure: "))
fact_a1 = int(input('Enter the actual sales figure: '))
kpi_a1 = fact_a1 / plan_a1 * 100
weight_a1 = 0.25

if fact_a1 > plan_a1 * 1.1:
    a1 = 0
elif plan_a1 * 1.02 < fact_a1 <= plan_a1 * 1.1:
    a1 = weight_a1 * 0.8 / kpi_a1
elif plan_a1 * 0.97 < fact_a1 <= plan_a1 * 1.02:
    a1 = weight_a1 * 1.05 / kpi_a1
else:
    a1 = weight_a1 * 1.2 / kpi_a1
# print(str(round(a1, 3)) + "\n")

print('a2: ')

plan_a2 = int(input('Enter a profit target: '))
fact_a2 = int(input('Enter the actual profit figure: '))
kpi_a2 = fact_a2 / plan_a2 * 100
weight_a2 = 0.4

if fact_a2 <= plan_a2 * 0.7:
    a2 = 0
elif plan_a2 * 0.7 < fact_a2 <= plan_a2 * 0.96:
    a2 = weight_a2 * 0.90 / kpi_a2
elif plan_a2 * 0.96 < fact_a2 <= plan_a2 * 1.0:
    a2 = weight_a2 * 1.05 / kpi_a2
else:
    a2 = weight_a2 * 1.1 / kpi_a2
# print(str(round(a2, 3)) + "\n")

print('a3: ')

plan_a3 = int(input('Enter the planned annual indicator of general household expenses: '))
fact_a3 = int(input('Enter the actual annual general household expenses: '))
kpi_a3 = fact_a3 / plan_a3 * 100
weight_a3 = 0.15

if fact_a3 > plan_a3 * 0.2:
    a3 = 0
elif plan_a3 * 0.1 < fact_a3 <= plan_a3 * 0.2:
    a3 = weight_a3 * 0.80 / kpi_a3
elif plan_a3 * 0.03 < fact_a3 <= plan_a3 * 0.1:
    a3 = weight_a3 * 1.05 / kpi_a3
else:
    a3 = 0
# print(str(round(a3, 3)) + "\n")

print('a4: ')

plan_a4 = int(input('Enter the planned turnover ratio for receivables: '))
fact_a4 = int(input('Enter the actual accounts receivable turnover ratio: '))
kpi_a4 = fact_a4 / plan_a4 * 100
weight_a4 = 0.2

if fact_a4 > plan_a4 * 0.2:
    a4 = 0
elif plan_a4 * 0.1 < fact_a4 <= plan_a4 * 0.2:
    a4 = weight_a4 * 0.80 / kpi_a4
elif plan_a4 * 0.03 < fact_a4 <= plan_a4 * 0.1:
    a4 = weight_a4 * 1.05 / kpi_a4
else:
    a4 = weight_a4 * 1.2 / kpi_a4
# print(str(round(a4, 3)) + "\n" + "\n")

A = a1 + a2 + a3 + a4
print('A = ' + str(round(A, 3)) + "\n" + "\n")


print('Section B: quality(evaluative) KPI: ' + "\n")

print('b1: ')

weight_b1 = int(input("Enter the weight in %: "))
kpi_b1 = int(input("Enter an assessment of the quality of the work performed: "))

b1 = (weight_b1 / 100) * kpi_b1 / 3
# print(str(round(b1, 3)) + "\n")

print('b2: ')

weight_b2 = int(input("Enter the weight in %: "))
kpi_b2 = int(input("Enter an assessment of the quality of the work performed: "))

b2 = (weight_b2 / 100) * kpi_b2 / 3
# print(str(round(b2, 3)) + "\n" + "\n")

B = b1 + b2
print('B = ' + str(round(B, 3)) + "\n" + "\n")


print('Section C: design tasks: ' + "\n")

print('c1: ')

weight_c1 = int(input("Enter the weight in %: "))
kpi_c1 = int(input("Enter an assessment of the quality of the work performed: "))

c1 = (weight_c1 / 100) * kpi_c1 / 3
# print(str(round(c1, 3)) + "\n" + "\n")

C = c1
print('C = ' + str(round(C, 3)) + "\n" + "\n")


k = A * 0.4 + B * 0.4 + C * 0.2
premiya = base * k
print('' + str(round(premiya, 3)))