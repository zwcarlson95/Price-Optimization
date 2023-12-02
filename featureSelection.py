import pandas as pd
import statsmodels.api as sm

dataset = pd.read_csv('/Users/zachcarlson/Downloads/retail_price.csv')
selected_features = ['qty', 'total_price', 'freight_price', 'unit_price', 'product_name_lenght',
                     'product_description_lenght', 'product_photos_qty', 'product_weight_g',
                     'product_score', 'customers', 'weekday', 'weekend', 'holiday', 'month', 'year', 's', 'volume',
                     'comp_1', 'ps1', 'fp1', 'comp_2', 'ps2', 'fp2', 'comp_3', 'ps3', 'fp3', 'lag_price']

# Features (X) and target variable (y)
X = dataset[selected_features]
y = dataset['unit_price']

def forward_selection(data, target, significance_level=0.05):
    initial_features = data.columns.tolist()
    best_features = []
    while (len(initial_features)>0):
        remaining_features = list(set(initial_features)-set(best_features))
        new_pval = pd.Series(index=remaining_features)
        for new_column in remaining_features:
            model = sm.OLS(target, sm.add_constant(data[best_features+[new_column]])).fit()
            new_pval[new_column] = model.pvalues[new_column]
        min_p_value = new_pval.min()
        if(min_p_value<significance_level):
            best_features.append(new_pval.idxmin())
        else:
            break
    return best_features

print(forward_selection(X,y))