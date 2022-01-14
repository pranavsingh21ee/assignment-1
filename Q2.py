gi=int(input("Enter Gross Income : "))
dep=int(input("Enter No. Of Dependents : "))
sd=10000
print("Standard Deduction : ",sd)
dd=3000
print("Dependent Deduction : ",dd)
op=dd*dep
ti=gi-sd-op
print("Taxable income=Gross income-Standard Deduction-(Dependent deduction*No. of dependents : ",ti)
tr=0.2
print("Tax=Taxable Income*Tax Rate : ",ti*tr)
