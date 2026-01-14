# inference_utils.py
import re
import pandas as pd

SLANG_DICT = {
    "yg": "yang",
    "dgn": "dengan",
    "ga": "tidak",
    "gak": "tidak",
    "udah": "sudah",
    "bgt": "banget",
    "aja": "saja",
    "kmu": "kamu",
    "km": "kamu"
}

EMOJI_PATTERN = re.compile("[" 
    u"\U0001F600-\U0001F64F"
    u"\U0001F300-\U0001F5FF"
    u"\U0001F680-\U0001F6FF"
    u"\U0001F1E0-\U0001F1FF"
    u"\U00002700-\U000027BF"
    u"\U0001F900-\U0001F9FF"
    u"\U00002600-\U000026FF"
"]+", flags=re.UNICODE)

def preprocess_text(text, model_type="indobert"):
    if text is None or str(text).strip() == "":
        return ""

    t = str(text)

    # cleaning dasar
    t = re.sub(r"http\S+|www\.\S+", " ", t)
    t = re.sub(r"@\w+", " ", t)
    t = t.replace("#", " ")
    t = EMOJI_PATTERN.sub(" ", t)

    # lowercase
    t = t.lower()

    # slang normalization HANYA untuk SVM
    if model_type == "svm":
        for slang, formal in SLANG_DICT.items():
            t = re.sub(rf"\b{slang}\b", formal, t)

    # angka: simpan untuk IndoBERT
    if model_type == "svm":
        t = re.sub(r"\d+", " ", t)

    # karakter
    t = re.sub(r"[^a-zA-Z0-9\s!?.,]", " ", t)

    # spasi
    t = re.sub(r"\s+", " ", t).strip()

    return t
