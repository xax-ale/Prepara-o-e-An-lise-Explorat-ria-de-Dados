import pandas as pd
import numpy as np

df = pd.read_csv(
    r'dados-somativa.csv',
    sep=',',
    quotechar='"',
    decimal=','
)

for col in ['Idade', 'Salario', 'Tempo_empresa', 'Satisfacao']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("Colunas:", df.columns.tolist())
print("Tipos:\n", df.dtypes)
print("\nPrimeiras linhas:\n", df.head(3))

df['Idade']         = df['Idade'].fillna(df['Idade'].median())
df['Salario']       = df['Salario'].fillna(df['Salario'].median())
df['Tempo_empresa'] = df['Tempo_empresa'].fillna(df['Tempo_empresa'].median())
df['Satisfacao']    = df['Satisfacao'].fillna(df['Satisfacao'].median())

df['Faixa_Idade'] = pd.cut(df['Idade'], bins=3,
    labels=['Jovem (18-33)', 'Adulto (34-49)', 'Sênior (50-64)'])

df['Faixa_Salario'] = pd.cut(df['Salario'], bins=3,
    labels=['Baixo', 'Médio', 'Alto'])

df['Faixa_Satisfacao'] = pd.cut(df['Satisfacao'], bins=3,
    labels=['Baixa (1-4)', 'Média (5-7)', 'Alta (8-10)'])

print("\n=== ESTATÍSTICAS DESCRITIVAS ===")
print(df[['Idade','Salario','Tempo_empresa','Satisfacao']].describe().round(2))

print("\n=== SALÁRIO MÉDIO POR DEPARTAMENTO ===")
print(df.groupby('Departamento')['Salario'].mean().round(2))

print("\n=== SATISFAÇÃO MÉDIA POR DEPARTAMENTO ===")
print(df.groupby('Departamento')['Satisfacao'].mean().round(2))

print("\n=== CONTAGEM: DEPARTAMENTO x FAIXA DE SATISFAÇÃO ===")
print(pd.crosstab(df['Departamento'], df['Faixa_Satisfacao']))

print("\n=== CORRELAÇÃO ===")
print(df[['Idade','Salario','Tempo_empresa','Satisfacao']].corr().round(3))

df.to_excel('resultado_analise.xlsx', index=False)
print("\nArquivo resultado_analise.xlsx gerado!")
