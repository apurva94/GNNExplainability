#!/usr/bin/env python
# coding: utf-8

# # Replication experiment
#
# This is the main notebook required to obtain the results of our replication study. The notebook is build around the concepts of predefined configuration files. These configuration files can be found within the codebase. The configuration files for different datasets and different explainers can be chosen by changing the parameters in the second codeblock.
#
# When loaded, the configuration for a replication experiment is passed to the replication function. This function is responsible for running all parts of the evaluation; quantitative, qualitative and efficiency. The results for the quantitative and efficiency studies are returned by the replication method and also stored in the `results` folder. The results of the qualitative study are stored in the folder name `qualitative`.
#
# **Be aware that the replication function can take very long to completed**. This is caused by the method averaging all scores over ten runs. If speed is required over accuracy the last line of the 2nd codeblock can be uncommented. This will make the evaluation run over one run only.
#

# In[1]:


from ExplanationEvaluation.configs.selector import Selector
from ExplanationEvaluation.tasks.replication import replication


# In[2]:


_dataset = 'ba2motifs' # One of: bashapes, bacommunity, treecycles, treegrids, ba2motifs, mutag
_explainer = 'pgexplainer' # One of: pgexplainer, gnnexplainer

# Parameters below should only be changed if you want to run any of the experiments in the supplementary
_folder = 'replication' # One of: replication, extension

# PGExplainer
config_path = f"./ExplanationEvaluation/configs/{_folder}/explainers/{_explainer}/{_dataset}.json"

config = Selector(config_path)
extension = (_folder == 'extension')

#todo generate dataset and use batch size for training for mutag

# config.args.explainer.seeds = [0]


# In[ ]:


(auc, auc_std), inf_time = replication(config.args.explainer, extension)


# In[ ]:


print((auc, auc_std), inf_time)
