To reproduce the experiments,

1. Install a Python 3.6 environment
2. Install the package with "pip install -e ."
3. pip install git+https://github.com/automl/HPOlib2 
4. pip install git+https://github.com/befelix/SafeOpt.git


To run the experiments, replace "{experiment_name}" in the instructions below by any of:

* camelback
* camelback_sub10
* hartmann6
* hartmann6_sub14
* gaussian10
* camelback_constraint
* hartmann6_constraint
* camelback_sub10_constraint

Instructions to run experiments and create plots:

1. febo create {experiment_name} --config config/{experiment_name}.yaml
2. febo run {experiment_name}
                (this will take a while, you can set the number of repetitions in the yaml file)
3. febo plot {experiment_name} --plots febo.plots.InferenceRegret
