# Narisma and Del Mundo
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('LoanDataRaw.csv')

df['default'] = pd.to_numeric(df['default'].astype(str).str.replace(r'\D', '', regex=True), errors='coerce')

# Separate features and target
features = df.drop('default', axis=1)
target = df['default']

# Impute features
imputer = SimpleImputer(strategy='mean')
features = pd.DataFrame(imputer.fit_transform(features), columns=features.columns)

# Scale features
scaler = StandardScaler()
features = pd.DataFrame(scaler.fit_transform(features), columns=features.columns)

# Recombine
df = pd.concat([features, target], axis=1)

print("Missing values after cleaning:")
print(df.isnull().sum())
print("\nFirst 5 rows after cleaning:")
print(df.head())

df.to_csv('LoanDataClean.csv', index=False)


