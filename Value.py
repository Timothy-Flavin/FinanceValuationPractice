import numpy as np

def netPresentValue(assetLife, cashflow, discountRate):
  value=0
  if(hasattr(cashflow, '__len__')):
    for i in range(assetLife):
      value+=cashflow[i]/((1+discountRate)**(i+1))
  else:
    for i in range(assetLife):
      value+=cashflow/((1+discountRate)**(i+1))
  return value


if __name__ == "__main__":
  assetLife = int(input("expected life of asset: "))
  variableCashflow = bool(input("Constant cashflow? 'True' or 'False'"))
  if variableCashflow:
    cashflow = list()
    for i in range(assetLife):
      cashflow.append(float(input("Enter cashflow for year " + str(i+1) + ": ")))
  else:
    cashflow=float(input("Enter cashflow: "))
  discountRate = float(input("Enter discount rate ex(0.01) for 1%: "))
  print("Net present value: "+ str(netPresentValue(assetLife, cashflow, discountRate)))

