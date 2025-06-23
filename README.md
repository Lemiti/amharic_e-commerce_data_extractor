# Amharic E-commerce Data Extractor for EthioMart

![NLP](https://img.shields.io/badge/NLP-Amharic-green) 
![ML](https://img.shields.io/badge/Model-XLM_Roberta-blue) 
![Task](https://img.shields.io/badge/Task-NER-orange)

A Named Entity Recognition (NER) system to extract product, price, and location data from Ethiopian Telegram e-commerce channels. This project powers **EthioMart**'s centralized platform and supports micro-lending decisions via a **Vendor Scorecard**.

---

## 📌 Project Overview
**Business Goal:**  
EthioMart aims to consolidate decentralized Telegram-based e-commerce in Ethiopia by extracting structured data (products, prices, locations) from Amharic messages. The extracted data will:
1. Populate a unified e-commerce hub.  
2. Generate **Vendor Scorecards** to identify loan-worthy sellers.  

**Technical Goal:**  
Fine-tune multilingual LLMs (e.g., XLM-Roberta) for Amharic NER, compare model performance, and explain predictions using SHAP/LIME.

---

## 🛠️ Tasks Breakdown
1. **Data Ingestion**  
   - Scrape messages/images from ≥5 Ethiopian Telegram channels.  
   - Preprocess Amharic text (tokenization, normalization).  

2. **Data Labeling**  
   - Label 30–50 messages in CoNLL format (`B-Product`, `I-PRICE`, `B-LOC`).  

3. **Model Fine-Tuning**  
   - Fine-tune XLM-Roberta/mBERT on labeled data using Hugging Face.  

4. **Model Comparison**  
   - Evaluate models (F1-score, precision/recall) and select the best performer.  

5. **Interpretability**  
   - Use SHAP/LIME to explain model predictions.  

6. **Vendor Scorecard**  
   - Calculate metrics (post frequency, avg. views, price points) to rank vendors for loans.  

---

## 📂 Repository Structure
```
.
├── data/ # Raw and processed datasets
├── notebooks/ # Jupyter/Colab notebooks for tasks
│ ├── 1_data_ingestion.ipynb
│ ├── 2_data_labeling.ipynb
│ └── 3_model_training.ipynb
├── models/ # Saved model weights
├── scripts/ # Scripts for scraping, preprocessing, etc.
└── README.md
