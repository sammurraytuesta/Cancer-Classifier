# CancerClassifier
Parses data files containing hundreds of patient records to implement a machine learning framework and develop a rule-based classifier that can be used to predict the malignancy of a tumor.

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![python-version](https://img.shields.io/badge/Python-3.7-blue.svg)](https://shields.io/) [![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg) [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/sammurraytuesta)

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
      <li><a href="#Machine-Learning-Framework">Machine Learning Framework</a></li>
      <ul>
        <li><a href="#Training">Training</a></li>
        <li><a href="#Testing">Testing</a></li>
      </ul>
    </li>
    <li><a href="#Program-Specification">Program Specification</a></li>
    <li><a href="#Thank-You">Thank You!</a></li>
  </ol>
</details>

## Machine Learning Framework 
The algorithm for CancerClassifier uses previously observed data to make predictions about new data, this can also be referred to as a machine learning framework where two phases occur to correctly compute or predict the malignancy of a tumor. This rule-based classifier is split into two phases: Training and Testing. 

### Training
In the training phase, the program will “learn” the average value each attribute (e.g. area, smoothness, etc.) among the malignant tumors as well as “learn” the average value of each attribute among benign tumors. It will then compute the midpoint for each attribute and add it to a collection. This collection of midpoints, one for each attribute, is our classifier.

The following displays the resulting data as computed by the training phase:

```
Reading in training data...
Done reading training data.
Reading in test data...
Done reading test data.

Training classifier...
Classifier cutoffs:
    radius: 14.545393772893773
    texture: 19.279093406593404
    perimeter: 94.91928571428579
    area: 693.337728937729
    smoothness: 0.09783294871794869
    compactness: 0.1104729532967033
    concavity: 0.09963735815018318
    concave: 0.054678068681318664
    symmetry: 0.18456510989010982
    fractal: 0.06286657967032966
Done training classifier.
```
The "cutoffs" displayed above are the midpoints computed during the training phase. These "cutoffs" will determine whether a tumor is benign or malignant.

### Testing 
In the testing phase, the program will be used to make an educated guess about the label of a new tumor given the measurements of all of its attributes. The educated guess will be based on the following criteria:

- If the tumor’s value for an attribute is greater than or equal to the midpoint value for that attribute, cast one vote for the tumor being malignant.
- If the tumor’s attribute value is less than the midpoint, cast one vote for the tumor being benign.
- Tally up the votes cast according to these rules for each of the ten attributes. If the malignant votes are greater than or equal to the benign votes, teh resulting prediction is malignant.

Before using this classifier to predict diagnoses, the algorithm will first have to undergo tests using the 20% of data that has been held out as the test set (data not used in the training phase the classifier). The rate of accuracy on this data should be indicative of how well the classifier will do on new, unlabeled tumors.

The following displays the resulting accuracy as calculated in the testing phase:
```
Making predictions and reporting accuracy
Classifier accuracy: 92.20779220779221
Done classifying.
```

## Program Specification
After compiling and running the program, the program will prompt you for a patient ID to see classification details. 

```
Enter a patient ID to see classification details: 9010258
```

The votes and resulting diagnosis from the training data for the corresponding patient ID will then be displayed on the page in the following format:

```
       Attribute     Patient  Classifier        Vote
          radius     12.5600     14.5454      Benign
         texture     19.0700     19.2791      Benign
       perimeter     81.9200     94.9193      Benign
            area    485.8000    693.3377      Benign
      smoothness      0.0876      0.0978      Benign
     compactness      0.1038      0.1105      Benign
       concavity      0.1030      0.0996   Malignant
         concave      0.0439      0.0547      Benign
        symmetry      0.1533      0.1846      Benign
         fractal      0.0618      0.0629      Benign
Classifier's diagnosis: Benign
```

The above example details the voting process for a benign tumor. Below is the patient ID for a different patient:

```
Enter a patient ID to see classification details: 899987
```

The results depicted below are derived from the voting process for a malignant tumor:

```
       Attribute     Patient  Classifier        Vote
          radius     25.7300     14.5454   Malignant
         texture     17.4600     19.2791      Benign
       perimeter    174.2000     94.9193   Malignant
            area   2010.0000    693.3377   Malignant
      smoothness      0.1149      0.0978   Malignant
     compactness      0.2363      0.1105   Malignant
       concavity      0.3368      0.0996   Malignant
         concave      0.1913      0.0547   Malignant
        symmetry      0.1956      0.1846   Malignant
         fractal      0.0612      0.0629      Benign
Classifier's diagnosis: Malignant
```

To terminate the program, enter quit as the patient ID. The following is a sample termination:

```
Enter a patient ID to see classification details: quit
```

## Thank You!
Thank you for reading about CancerClassifier!
