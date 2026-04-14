import pickle
import pandas as pd
from transformers import AutoTokenizer, AutoModel
import torch
from config.details import class_labels

Model_Version = "1.0.0"

with open("models/security_alert.pkl", "rb") as f:
    model = pickle.load(f)

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
bert_model = AutoModel.from_pretrained("bert-base-uncased")

def get_embedding(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = bert_model(**inputs)
    emb = outputs.last_hidden_state[:, 0, :]
    return emb.squeeze().numpy()

def predict_risk(alert):
    try:
        emb = get_embedding(alert.Status)

        if len(emb) != 768:
            raise ValueError(f"Embedding size mismatch: {len(emb)}")

        emb_dict = {f"emb_{i}": float(emb[i]) for i in range(768)}

        expected_columns = model.feature_names_in_.tolist()

        input_data = {
            "Category": alert.category_input,
            "Impact": alert.impact_input,
            "Priority": alert.priority_input,
            "Type": alert.type_input,
            "time_to_close": alert.time_to_close_seconds,
            "Sub_Category": alert.sub_category_input,
            **emb_dict
        }

        input_df = pd.DataFrame([input_data])
        input_df = input_df.fillna(0)
        input_df = input_df.reindex(columns=expected_columns, fill_value=0)

        prediction_idx = int(model.predict(input_df)[0])
        prediction_label = class_labels[prediction_idx]
        probabilities = model.predict_proba(input_df)[0]

        return {
            "predicted_category": prediction_label,   # ✅ FIXED
            "confidence": float(max(probabilities)),
            "class_probabilities": dict(
            zip(class_labels, [round(float(p), 4) for p in probabilities])
        )
    }
        

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e
    
print(class_labels)