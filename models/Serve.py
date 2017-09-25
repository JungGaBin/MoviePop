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
    # 분류이기 때문에 예측 데이터 타입이 nominal이라 numpy로 받을 수 없음.

    data.class_is_last()
    for index, inst in enumerate(data):
        pred = cls.classify_instance(inst)
        # print("predicted : %d " % inst.get_string_value(inst.class_index),)

    # index가 0부터라 +1
    return pred + 1;

def SMOreg():
    # load model
    cls = Classifier(jobject=serialization.read("SMOreg.model"))
    input = np.array([[8148,42066,44011723316,5712639,1,1,7,1,8.64,8.48,15,3,0]])
    instance = ndarray_to_instances(input,relation="input")

    for index, inst in enumerate(instance):
        pred = cls.classify_instance(inst)

    return pred;


def main():


    if True:
        predict = SMOreg()
    else:
        predict = SimpleLogistic()

    print(predict)

if __name__ == "__main__":
    try:
        jvm.start(packages=True)
        main()

    finally:
        jvm.stop()
