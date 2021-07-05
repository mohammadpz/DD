import numpy as np

hours = 23
list_num_classes = [1, 10]
list_label_noise = [0.0, 0.2]
list_lambda_log = [8]
list_seed = range(10)
save_indivs = 1
save_epochs = 0
compute_ntk = 0
exp_name = 'kmeans'

# hours = 23
# list_num_classes = [10]
# list_label_noise = [0.2]
# list_lambda_log = np.linspace(0.1, 8, 100)
# list_seed = range(1)
# save_indivs = 0
# save_epochs = 0
# compute_ntk = 0
# exp_name = 'regwise'

# hours = 23
# list_num_classes = [1]
# list_label_noise = [0.0, 0.2]
# list_lambda_log = [8]
# list_seed = range(5)
# save_indivs = 0
# save_epochs = 0
# compute_ntk = 1
# exp_name = 'ntk'

names = []
sh_number = 0
for num_classes in list_num_classes:
    for label_noise in list_label_noise:
        for lambda_log in list_lambda_log:
            for seed in list_seed:

                sh_number += 1
                args = (str(label_noise) + ' ' +
                        str(num_classes) + ' ' +
                        str(lambda_log) + ' ' +
                        str(seed) + ' ' +
                        str(save_indivs) + ' ' +
                        str(save_epochs) + ' ' +
                        str(compute_ntk) + ' ' +
                        exp_name)

                print(exp_name + str(sh_number) + ': ' + args)

                names += [exp_name + str(sh_number)]
                run_file = open('shs/' + exp_name + str(sh_number) + ".sh", "w")
                run_file.write('#!/bin/bash\n')
                run_file.write('~/miniconda/bin/python /home/pezeshki/scratch/dd/DD/train.py ' + args)

                run_file.flush()

run_all = open("shs/" + exp_name + ".sh", "w")
run_all.write('#!/bin/bash\n')
for name in names:
    run_all.write('sbatch --time=' + str(hours) + ':00:0 --gres=gpu:1 --mem=12G --account=rrg-bengioy-ad_gpu '
                  '--cpus-per-task=4 --output=/home/pezeshki/scratch/logs/slurm-%j.out '
                  '/home/pezeshki/scratch/dd/DD/shs/' +
                  name + ".sh\n")
run_all.write('watch -n 0.1 squeue -u pezeshki')
run_all.flush()
