import weka.core.jvm as jvm
import weka.core.serialization as serialization
from weka.core.converters import Loader
from weka.classifiers import Classifier
from weka.core.converters import ndarray_to_instances
import numpy as np


def SimpleLogistic(obj):
    jvm.start(packages=True)

    # TODO: First_trial_classification.arff First_trial_regression.arff 데이터 셋에 피쳐로 Date 있는데 최신걸로 다 수정좀 (new_models 폴더 전체)
    # TODO: obj의 내용을 바탕으로 input_classification.arff을 작성하는 코드 생성하기

    # load model
    cls = Classifier(jobject=serialization.read("new_models/SimpleLogistic.model"))
    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file("new_models/input_classification.arff")
    # 분류이기 때문에 예측 데이터 타입이 nominal이라 numpy로 받을 수 없음.

    data.class_is_last()
    for index, inst in enumerate(data):
        audience_class = cls.classify_instance(inst)

    jvm.stop()
    return audience_class + 1  # index가 0부터라 +1


def SMOreg(obj):
    jvm.start(packages=True)

    # load model
    cls = Classifier(jobject=serialization.read("new_models/SMOreg.model"))
    input = np.array([[obj.screen_num_7, obj.show_num_7, obj.money_num_7, obj.audience_num_7, obj.director_effect,
                       obj.distributor_effect, obj.month, obj.nationality, obj.before_grade, obj.after_grade, obj.age,
                       obj.actor_effect, 0]])
    instance = ndarray_to_instances(input, relation="input")

    for index, inst in enumerate(instance):
        audience_num = cls.classify_instance(inst)

    jvm.stop()
    return audience_num
