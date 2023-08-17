python train.py \
--weights 'weights/yolov5m.pt' \
--data 'data/yolov5comp_split.yaml' \
--hyp 'data/hyps/obb/hyp.finetune_comp.yaml' \
--epoch 10 \
--batch-size 2 \
--img 640 \
--device 0
