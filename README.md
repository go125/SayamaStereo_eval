# MINATOView

## How to use

## 1 Use ReadMovie.ipynb

## 2 Use GenData.py (crop images)

### Input example

```script
nohup python GenData.py --base_path ../all_video/ \
--ROOT_DIR ../Mask_RCNN \
--WIDTH 416 \
--HEIGHT 128 \
--OUTPUT_DIR ../out \
--TEMP_DIR ../tmpdir &
```
