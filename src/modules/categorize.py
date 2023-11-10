import torch
from torch.nn.functional import softmax
from transformers import BertForSequenceClassification, BertJapaneseTokenizer
from transformers import BertForSequenceClassification, BertJapaneseTokenizer
from ..models.message.request import AnalyzeRequest
from ..models.message.result import AnalyzeResult, Result

path = "/app/bert"
loaded_model = BertForSequenceClassification.from_pretrained(path)
loaded_tokenizer = BertJapaneseTokenizer.from_pretrained(path)


def categorize(analyze_request: AnalyzeRequest):
    results = []
    for msg in analyze_request.messages:
        try:
            max_length = 512
            words = loaded_tokenizer.tokenize(msg.text)
            word_ids = loaded_tokenizer.convert_tokens_to_ids(words)  # 単語をインデックスに変換

            x = torch.tensor([word_ids[:max_length]])  # テンソルに変換
            y = loaded_model(x)  # 予測

            probabilities = torch.softmax(y[0], dim=-1)
            probabilities = probabilities.detach().numpy()  # 確率をnumpy配列に変換

            probabilities = {
                "response_present": float(probabilities[0][0]),
                "not_needed": float(probabilities[0][1]),
                "no_sales": float(probabilities[0][2]),
                "newsletter": float(probabilities[0][3]),
                "auto_reply": float(probabilities[0][4]),
            }
            result = Result(id=msg.id, probabilities=probabilities)
            results.append(result)
        except Exception as e:
            print(e)
    return AnalyzeResult(messages=results)
