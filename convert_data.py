import os
import argparse

from pathlib import Path
import json

def check_valid_convert(tokens):
    n_tokens = len(tokens)
    token_string = " ".join(tokens)
    split_tokens = token_string.split()
    n_split_tokens = len(split_tokens)
    
    if n_tokens != n_split_tokens:
        print(tokens)
        for idx in range(n_tokens):
            if tokens[idx] != split_tokens[idx]:
                print(tokens[idx])
                break

def is_whitespace(token: str):
    cond = ("\xa0" in token) | ("\n" in token) | (" " in token) | ("\t" in token) | (token.isspace())
    return cond

def convert_data(data_path: str, output_path):
    print(f"Converting data from {data_path} -> {output_path}")
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    datas = json.load(open(data_path, "r"))
    seq_in_writer = open(Path(output_path) / "seq.in", "w")
    seq_out_writer = open(Path(output_path) / "seq.out", "w")
    label_writer = open(Path(output_path) / "label", "w")

    for data in datas:
        tokens = data["tokens"]
        # slots = data["labels"]
        slots = data.get("labels", ["O"] * len(tokens))
        idxs = [idx for idx in range(len(data["tokens"]))
                if not is_whitespace(tokens[idx])]
        tokens = [tokens[idx] for idx in idxs]
        slots  = [slots[idx] for idx in idxs]
        
        check_valid_convert(tokens)
        
        token_seq = " ".join(tokens)
        slot_seq = " ".join(slots)
        
        seq_in_writer.write(f"{token_seq}\n")
        seq_out_writer.write(f"{slot_seq}\n")
        label_writer.write(f"docs\n")
    
    seq_in_writer.close()
    seq_out_writer.close()
    label_writer.close()
    
def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    convert_data(opt.data_path, opt.output_path)
    



