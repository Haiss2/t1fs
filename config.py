# data
train_path = 'data/TrainingData.csv'
test_path = 'data/TestData.csv'
full_path = 'data/FullData.csv'
clusters_path = 'export/Clusters.csv'
rule_path = 'export/Rules.csv'
fmc_path = 'export/Fmc.csv'
editFmc_path = 'export/Edit.csv'
num_classes = 6

# clustering
k_mean = 5
m_fuzzy = 2
e_fcm = 0.001

# make rule
e_rule = 0.01
num_rules = 300

# fixed 4 gia tu: V, M, P, L
ha_tree_deep = 3

# cross validation iterators
k_fold = 3
shuffle = False
   