import pandas as pd


data = {'name': ['nick', 'david', 'joe', 'ross','root'],
		'age': ['5', '10', '7', '6','11']}
new = pd.DataFrame.from_dict(data)

print(new)
