python3 main.py --no_cuda --task PIL_sample \
                --model_type bert \
                --model_dir atis_model \
                --do_train --do_eval \
                --save_steps 10 \
                --num_train_epochs 100 \
                --logging_steps 20