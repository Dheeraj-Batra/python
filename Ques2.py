print("enter your gross income= ")
gross_income=int(input())
print("number of dependents= ")
dependent=int(input())
taxable_income=gross_income-10000-(dependent*3000)
"""Taxable income = Gross Income - Standard deduction - (Dependent deduction * No. of dependents)"""
print(taxable_income*0.2)    #tax to be paid = taxable income*tax rate