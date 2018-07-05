r 
Dataset Used: Alon (1999), retrieved from:
https://github.com/ramhiser/datamicroarray/wiki/Alon-%281999%29
2000 genes sampled from 62 different people, screening for cancer (yes/no)

Data was imported to R-studio, then written out into a CSV file.  Quotation marks around patient numbers were removed, and “T” or ”N” categories were converted to “1” or “0”, respectively, to allow processing by numpy (version 1.14.5), a scientific python (2.7.4) package with a C backend.

Data was loaded into the program using numpy’s readtxt method, where commas are used as the sole delimiter delimiter and the first and last columns are excluded.  This is the feature space to be analyzed, and it has dimensions of 62x2000.  The last column was also read in, and this is the target classification list, or as it will be referred to in this document and attached code, the target.

The features of the data were then normalized using maxabs scale from sklearn.  Sklearn (0.19.1) is a scientific/statistical machine learning package for python, from which several different methods can be imported and utilized. Maxabs converts the largest datapoint in a sample to a 1, and the smallest (or most negative) to a -1, scaling all of the values in between accordingly.

After normalization, the next step was to trim down the number features to be used.  This was done using Recursive Feature Elimination (RFE), and by using linear correlation as a metric.  Recursive feature elimination uses a simple, user defined metric to determine which features are most relevant to the prediction of a target, scoring each feature, and eliminating non-relevant features until a user-defined number of features is reached. The features that are retained, or the selected features, are then split into training (in this case, ~25% of the available data) and testing sets (~75%), along with their corresponding targets.

The training set is then given to a support vector machine using a linear kernel to classify which provided approximately 90% accuracy. Note that other SVM kernels were used, but only predicted one class, likely due to a lack of data.

Of interest is that when different numbers of features are selected, accuracy doesn’t appear to suffer greatly. When sampling 200 features (10% of the available features) the accuracy is generally around 90%, but when sampling only 20 features (1%), similar accuracy is obtained.

This illustrates why removing irrelevant data is important, especially when using difficult to train machine learning models. This is because a large number of features will take a longer time to train, and introduce a lot of noisy data to the training.
