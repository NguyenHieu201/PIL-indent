from pathlib import Path
import json

DATA_ROOT_PATH = "/home/hieu/PIL-indent/pii-detection-removal-from-educational-data"
OUTPUT_PATH = "./data/PIL_sample/test"
train_path = Path(DATA_ROOT_PATH) / "train.json"
train_datas = json.load(open(train_path, "r"))

seq_in_writer = open(Path(OUTPUT_PATH) / "seq.in", "w")
seq_out_writer = open(Path(OUTPUT_PATH) / "seq.out", "w")
label_writer = open(Path(OUTPUT_PATH) / "label", "w")

def is_whitespace(token: str):
    cond = ("\xa0" in token) | ("\n" in token) | (" " in token)
    return cond

for data in train_datas[:10]:
    tokens = data["tokens"]
    slots = data["labels"]
    idxs = [idx for idx in range(len(data["tokens"]))
            if not is_whitespace(tokens[idx])]
    tokens = [tokens[idx] for idx in idxs]
    slots  = [slots[idx] for idx in idxs]
    
    token_seq = " ".join(tokens)
    slot_seq = " ".join(slots)
    
    seq_in_writer.write(f"{token_seq}\n")
    seq_out_writer.write(f"{slot_seq}\n")
    label_writer.write(f"docs\n")
    
seq_in_writer.close()
seq_out_writer.close()
label_writer.close()
    



