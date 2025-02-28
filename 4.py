# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

fat = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(fat.values())

percentual = {}
for estado, valor in fat.items():
    percentual[estado] = (valor / total) * 100


print("Percentual de representação por estado:")
for estado, percentual in percentual.items():
    print(f"{estado}: {percentual:.2f}%")
