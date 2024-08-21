num1,num2,num3 = int(input()),float(input()),int(input())
res_a = str((f"{num3:0>16b}")[::-1])
print(f"{num1:0=+10}\n{num2:#>10.2f}",
      '_'.join(res_a[i:i+4] for i in range(0, len(res_a), 4))[::-1],
      sep='\n')