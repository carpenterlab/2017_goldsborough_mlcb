#!/bin/bash

python3 -m cytogan.train.bbbc021                        \
  --epochs 10                                           \
  --model vae                                           \
  --lr 0.001                                            \
  --lr-decay 0.996                                      \
  --lr-decay-steps 100                                  \
  --batch-size 128                                      \
  --workspace /data1/peter/runs                         \
  --checkpoint-freq '1min'                              \
  --summary-freq '1min'                                 \
  --reconstruction-samples 20                           \
  --latent-samples 1000                                 \
  --generative-samples 10                               \
  --gpus 2 3                                            \
  --metadata /data1/peter/metadata/BBBC021_v1_image.csv \
  --labels /data1/peter/metadata/BBBC021_v1_moa.csv     \
  --images /data1/peter/segmented                       \
  --cell-count-file /data1/peter/cell_counts.csv        \
  --latent-compounds                                    \
  --latent-moa                                          \
  --confusion-matrix                                    \
  --restore-from /data1/peter/runs/vae_30-08-2017_23-12-04/checkpoints \
  $1
