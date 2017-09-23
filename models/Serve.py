import weka.core.jvm as jvm
import weka.core.serialization as serialization
from weka.core.converters import Loader
from weka.core.dataset import Instances
from weka.core.dataset import Instance
from weka.classifiers import Classifier
from weka.core.converters import ndarray_to_instances
import numpy as np

def SimpleLogistic():
    # load model
    cls = Classifier(jobject=serialization.read("SimpleLogistic.model"))
    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file("./input_classification.arff")
    input = np.array([[8148, 42066, 44011723316, 5712639, 1, 1, 7, 30, 1, 8.64, 8.48, 15, 3, 0]])
    instance = ndarray_to_instances(input, relation="input")
    print(data)
    print(instance)
    instance.class_is_last()
    for index, inst in enumerate(instance):
        pred = cls.classify_instance(inst)
        print("predicted : %d " % inst.get_string_value(inst.class_index),)

    return pred;

def SMOreg():
    # load model
    cls = Classifier(jobject=serialization.read("SMOreg.model"))
    input = np.array([[8148,42066,44011723316,5712639,1,1,7,30,1,8.64,8.48,15,3,0]])
    instance = ndarray_to_instances(input,relation="input")

    for index, inst in enumerate(instance):
        pred = cls.classify_instance(inst)
        print("predicted : %f " %pred)

    return pred;


def main():


    if False:
        predict = SMOreg()
    else:
        predict = SimpleLogistic()



if __name__ == "__main__":
    try:
        jvm.start(packages=True)
        main()

    finally:
        jvm.stop()
