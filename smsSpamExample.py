import pandas as pd


raw_data = open('SMSSpamCollection').read()
#print (raw_data[0:500])

parsed_data = raw_data.replace('\t','\n').split('\n')
#print(parsed_data[0:10])

label_list = parsed_data[0::2]
msg_list = parsed_data[1::2]
#print(label_list[0:5])
#print(msg_list[0:5])

combined_df = pd.DataFrame({
    'label' : label_list[:-1],
    'sms' : msg_list
})

print(combined_df.head())

print("==================================  reading the csv data using pandas =================================")
dataset = pd.read_csv('SMSSpamCollection', sep="\t", header=None)
dataset.columns = ['label','sms']
print(dataset.head())

print(f" input dataset has {len(dataset)} rows, {len(dataset.columns)} columns")
print(f"ham = {len(dataset[dataset['label'] == 'ham'])}")
print(f"spam = {len(dataset[dataset['label'] == 'spam'])}")

print()
print("=================================== missing data ===========================================")
print(f"missing labels = {dataset['label'].isnull().sum()}")
print(f"missing msgs = {dataset['sms'].isnull().sum()}")