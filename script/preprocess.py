import re
import pandas as pd

def clean_amharic_text(text):
  text = re.sub(r'http\S+|@\w+|[^\w\s\u1200-\u137F]', '',str(text))
  text = re.sub(r'\s+', ' ', text).strip()
  return text

df = pd.read_csv('/content/drive/MyDrive/10Acadamy/data/raw_messages.csv')
df['clean_text'] = df['text'].apply(clean_amharic_text)

df.to_csv('/content/drive/MyDrive/10Acadamy/data/cleaned_messages.csv', index=False)
print("Preprocessed data saved to '/content/drive/MyDrive/10Acadamy/data/cleaned_messages.csv'")