#!/bin/bash
#SBATCH --nodes=1
#SBATCH --partition=nltmp
#SBATCH --cpus-per-task=128
#SBATCH --gres=gpu:A100-SXM4:1
#SBATCH --time=160:00:00
#SBATCH --exclude=scn42-10g
#SBATCH --error=job.%J.err
#SBATCH --output=job.%J.out
echo "Starting at `date`"
echo "Running on hosts: $SLURM_NODELIST"
echo "Running on $SLURM_NNODES nodes"
echo "Running $SLURM_NTASKS tasks"
echo "Job id is $SLURM_JOBID"
echo "Job submission directory is : $SLURM_SUBMIT_DIR"

source /nlsasfs/home/nltm-pilot/jordanf/espnet/tools/activate_python.sh
#after scp to tsv conv

# 1. pass parameters of dump_hubert_features.py
# srun python file_path of  dump_hubert_features.py in fairseq --tsv_dir-folder path of tsv --split-train/vaild --ckpt_path- /nlsasfs/home/nltm-pilot/vasistal/superb_ckpts/30k_pt/hub_large/best.pt --layer-21 for large 9 for small (layer from which embeddings are taken) --nshard 4-valid, 8-train --rank (0-7) --feat_dir- new folder path for feats_hubert

# 2. pass parameters of learn_kmeans.py
srun python /nlsasfs/home/nltm-pilot/malavika/Sowmithaa/fairseq/examples/hubert/simple_kmeans/learn_kmeans.py /nlsasfs/home/nltm-pilot/malavika/Sowmithaa/Tamil_Units/data/feats_hubert train 8 /nlsasfs/home/nltm-pilot/malavika/Sowmithaa/Tamil_Units/data/Kmeans/km_500.pkl 500 --percent 0.05

# 3. pass parameters of dump_km_label.py
#srun python /nlsasfs/home/nltm-pilot/malavika/Sowmithaa/fairseq/examples/hubert/simple_kmeans/dump_km_label.py /--feat_dir:nlsasfs/home/nltm-pilot/malavika/Sowmithaa/Tamil_Units/data/Kmeans --split:train --km_path:/nlsasfs/home/nltm-pilot/malavika/Sowmithaa/Tamil_Units/data/Kmeans/km_500.pkl --nshard:8 --rank:(0-7) --lab_dir: /nlsasfs/home/nltm-pilot/malavika/Sowmithaa/Hindi_Units/data/Units_500_clusters

#4. To combine all km_files
#source /nlsasfs/home/nltm-pilot/jordanf/espnet/tools/activate_python.sh
#for rank in $(seq 0 7); do 
#    cat /nlsasfs/home/nltm-pilot/malavika/Sowmithaa/Hindi_Units/all_units/500_clus/train_${rank}_8.km 
#done > /nlsasfs/home/nltm-pilot/malavika/Sowmithaa/Hindi_Units/all_units/500_clus/train.km
