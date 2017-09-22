# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# parameter_optimization.py
# Copyright (C) 2015 Fracpete (pythonwekawrapper at gmail dot com)

import weka.core.jvm as jvm
import weka.core.serialization as serialization
from weka.core.converters import Loader
from weka.classifiers import Classifier
from weka.classifiers import PredictionOutput, KernelClassifier, Kernel
from weka.core.classes import Random
from weka.classifiers import Evaluation

def SimpleLogistic():
 
    # load a dataset
    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file("First_trial_classification.arff")
    data.class_is_last()  # set class attribute

    cls = Classifier(classname="weka.classifiers.functions.SimpleLogistic")
    pout = PredictionOutput(classname="weka.classifiers.evaluation.output.prediction.PlainText")
    evl = Evaluation(data)
    evl.crossvalidate_model(cls, data, 10, Random(486), pout)

    print(evl.summary())
    print(pout.buffer_content())

    # save model
    serialization.write_all("SimpleLogistic2.model", cls)

    # load model
    # classifier = Classifier(jobject=serialization.read("SimpleLogistic.model"))

def SMOreg():

    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file("First_trial_regression.arff")
    data.class_is_last()

    cls = KernelClassifier(classname="weka.classifiers.functions.SMOreg", options=["-N", "0"])
    kernel = Kernel(classname="weka.classifiers.functions.supportVector.RBFKernel", options=["-G", "0.2"])
    cls.kernel = kernel
    pout = PredictionOutput(classname="weka.classifiers.evaluation.output.prediction.PlainText")
    evl = Evaluation(data)
    evl.crossvalidate_model(cls, data, 10, Random(486), pout)

    print(evl.summary())
    print(pout.buffer_content())

    # save model
    serialization.write_all("SMOreg.model2", cls)

    # load model
    # classifier = Classifier(jobject=serialization.read("SMOreg.model"))    
    

   # train, test = data.train_test_split(66.0, Random(1))
   # evl.test_model(cls,test)

def main():

    if False:
        SMOreg()
    else:
        SimpleLogistic()

if __name__ == "__main__":
    try:
        jvm.start(packages=True)
        main()

    finally:
        jvm.stop()