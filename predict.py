import time
import config as cf
from code import csv_processor as csv
from code.clustering import Clustering
from code.make_rule import Rule
from code.predict import Predict

if __name__ == "__main__":

    # read data
    data = csv.read_file(cf.train_path, 'float')
    clusters = csv.read_file(cf.clusters_path, 'float')
    rules = csv.read_file(cf.rule_path, 'float')
    
    # Predict and save data
    now = time.time()
    x = Predict(data, clusters, rules)

    corrects = 0
    edit = []
    editCollection = []

    for ix, record in enumerate(data):
        if int(record[0]) == x.predict(record, rules)["predict"]:
            corrects += 1
        else:
            pr_rules = x.predict(record, rules)["rule"]
            cr_rules = x.get_rule_truth(record)["rule"]
            edit += x.detect_cluster(pr_rules, cr_rules, record[1: len(record) ])
    print('\n  __Predict time: {:.2f}s'.format(time.time() - now))
    print("  __Correct: {}, Total: {}, Accuracy: {:.2f}%\n".format(corrects, len(data), 100*corrects / len(data)))
    
