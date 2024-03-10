import re
import argparse
import json
import pandas as pd

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_file", type=str, required=True)
    parser.add_argument("--pred_file", type=str, required=True)
    parser.add_argument("--submit_file", type=str, required=True)
    opt = parser.parse_args()
    return opt
    
def convert_to_submit_file(data_file, pred_file, submit_file):
    datas = json.load(open(data_file, "r"))
    pred_file = open(pred_file, "r").readlines()
    submit_data = []
    row_id = 0
    for pred, data in zip(pred_file, datas):
        pred.replace("\n", "")
        slots = re.findall("\[([^\]]*)\]", pred)
        tokens = data["tokens"]
        start_idx = 0
        for slot in slots:
            token, label = slot.split(":")
            token_id = tokens[start_idx:].index(token)
            
            submit_data.append({
                "row_id": row_id,
                "document": data["document"],
                "token": token_id + start_idx,
                "label": label
            })
            print(f"{token} - {label} - {token_id + start_idx} - {tokens[token_id + start_idx]}")
            start_idx = token_id + start_idx + 1
            row_id += 1
    submit_df = pd.DataFrame(submit_data)
    submit_df.to_csv(submit_file, index=False)
    
if __name__ == "__main__":
    opt = parse_opt()
    convert_to_submit_file(opt.data_file, opt.pred_file, opt.submit_file)
    