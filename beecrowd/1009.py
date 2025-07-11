vendedor=input('')
salario=float(input())
vendas=float(input())
comissao=vendas*15/100
total=salario+comissao
print(f"TOTAL = R$ {total:.2f}")