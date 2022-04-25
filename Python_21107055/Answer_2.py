Gross_income = int(input("Enter your Gross income: "))

Dependents_in_family = int(input("Enter number of dependents in your family: "))

Standard_deduction = 10000     # to be charged on all taxpayers in $

tax_rate = 0.2     #20% tax rate charged on all taxpayers

deductionn_per_dependent = 3000   

Taxable_income = Gross_income - Standard_deduction - (deductionn_per_dependent*Dependents_in_family)

Tax = Taxable_income*tax_rate

print("Tax:", Tax)
