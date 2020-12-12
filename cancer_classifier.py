#Samantha Murray Tuesta
#June 2, 2020
#write a program that takes the id of a patient and returns the
#records for that patient and whether or not that patient has
#a malignant or benign tumor
#add to the function sin order to help you achieve that
#follow the pseudocode and descriptions of functions

###############################################################################
# GLOBAL CONSTANT
# For use as dictionary keys
# You can use this list throughout the program without passing it to a function
# DO NOT MODIFY
ATTRS = []
ATTRS.append("ID")
ATTRS.append("radius")
ATTRS.append("texture")
ATTRS.append("perimeter")
ATTRS.append("area")
ATTRS.append("smoothness")
ATTRS.append("compactness")
ATTRS.append("concavity")
ATTRS.append("concave")
ATTRS.append("symmetry")
ATTRS.append("fractal")
ATTRS.append("class")
###############################################################################


def make_training_set(filename):
    """ Read training data from the file whose path is filename.
        Return a list of records, where each record is a dictionary
        containing a value for each of the 12 keys in ATTRS.
    """
    training_records = []
    # Read in file
    for line in open(filename,'r'):
        if '#' in line:
            continue
        line = line.strip('\n')
        line_list = line.split(',')
        
        # Create a dictionary for the line and map the attributes in
        # ATTRS to the corresponding values in the line of the file
        record = {}
        
        # read patient ID as an int:
        record[ATTRS[0]] = int(line_list[0].strip())
        
        # read attributes 1 through 10 as floats:
        for i in range(1,11):
            record[ATTRS[i]] = float(line_list[i])
        
        # read the class (label), which is "M", or "B" as a string:
        record[ATTRS[11]] = line_list[31].strip() 

        # Add the dictionary to a list
        training_records.append(record)        

    return training_records


def make_test_set(filename):
    """ Read test data from the file whose path is filename.
        Return a list with the same form as the training
        set, except that each dictionary has an additional
        key "prediction" initialized to "none" that will be
        used to store the label predicted by the classifier. 
    """
    test_records = make_training_set(filename)

    for record in test_records:
        record["prediction"] = "none"

    return test_records

def make_dict(lst):
    """ returns a dictionary that utilizes the global keys
        precondition: ATTRS act as the global keys in this case,
        if used in other cases you would have to create global keys.
        parameters: name of list of keys that you would like to utilize
        return: dictionary that utilizes keys 1-10
        purpose of this function: helper function because it's required lol :)
    """
    #makes a dictionary that utilizes keys 1-10
    dictionary = {lst[1]: 0, lst[2]: 0, lst[3]: 0, lst[4]: 0, lst[5]: 0, lst[6]: 0, lst[7]: 0, lst[8]: 0, lst[9]: 0, lst[10]: 0}
    #returns that dictionary
    return dictionary
        
def train_classifier(training_records):
    """ Return a dict containing the midpoint between averages
        among each class (malignant and benign) of each attribute.
        (See the A5 writeup for a more complete description)
        Precondition: training_records is a list of patient record
        dictionaries, each of which has the keys
        in the global variable ATTRS
        Postcondition: the returned dict has midpoint values calculated
        from the training set for all 10 attributes except
        "ID" and"class".
    """
    #create dictionaries for malignant and benign averages as well as midpoint (classifier)
    maverages = make_dict(ATTRS)
    baverages = make_dict(ATTRS)
    classifier = make_dict(ATTRS)
    #these keep track of how many of each kind
    b_record = 0
    m_record = 0
    for record in training_records:
        #if tumor in test benign
        if record["class"] == "B":
            #adds to total of benign
            b_record += 1
            for i in baverages:
                #adds all them up
                baverages[i] += record[i]
        #if the tumor in the test malignant    
        if record["class"] == "M":
            #adds to total of malignant
            m_record += 1
            for i in maverages:
                #adds them all up
                maverages[i] += record[i]
    #gives average b       
    for i in baverages:
        baverages[i] = baverages[i]/b_record
    #gives average m
    for i in maverages:
        maverages[i] = maverages[i]/m_record
    #gives midpoints between the attributes
    for i in classifier:
        classifier[i] = (baverages[i] + maverages[i])/2
    
    return(classifier)            

def classify(test_records, classifier):
    """ Use the given classifier to make a prediction for each record in
        test_records, a list of dictionary patient records with the keys in
        the global variable ATTRS. A record is classified as malignant
        it has more attribute values are above the classifier's
        threshold then below.
        Precondition: classifier is a dict with midpoint values for all
        keys in ATTRS except "ID" and "class"
        Postcondition: each record in test_records has the "prediction" key
        filled in with the predicted class, either "M" or "B"
    """
    for record in test_records:
        #malignant count
        votem = 0
        #benign count
        voteb = 0
        #for each attribute compare values
        for i in classifier:
            #if greater, it is malignant
            if record[i] >= classifier[i]:
                votem += 1
            #else benign
            else:
                voteb += 1
            #if the majority of the attributes fit malignant
            #the prediction is malignant
            if votem >= voteb:
                record["prediction"] = "M"
            #else benign
            else:
                record["prediction"] = "B"
    
def print_table(record, classifier):
    """ Given a patient record and the classifier, print a table 
        comparing the two; the table has four columns: Attribute,
        Patient, Classifier, and Vote"""
    
    # column headers:
    print("Attribute".rjust(16),
          "Patient".rjust(12),
          "Classifier".rjust(12),
          "Vote".rjust(12), sep="")
    
   
    # print rows:
    for key in ATTRS[1:11]:
        if record[key] > classifier[key]:
            vote = "Malignant"
        else:
            vote = "Benign"                       
        print(f"{key:>16}", end="")
        print(f"{record[key]:12.4f}", end="")
        print(f"{classifier[key]:12.4f}", end="")
        print(f"{vote:>12}")

def report_accuracy(test_records):
    """ Print the accuracy of the predictions made by the classifier
        on the test set as a percentage of correct predictions.
        Precondition: each record in the test set has a "prediction"
        key that maps to the predicted class label ("M" or "B"), as well
        as a "class" key that maps to the true class label. """
    accurate = 0
    #total number of records
    total = 0
    for record in test_records:
        #adds to record count
        total += 1
        #if the prediction matches the actual it is accurate
        if record["prediction"] == record["class"]:
            accurate += 1
    #percentage of accuracy    
    total_accuracy = (accurate/total)*100
    print("Classifier accuracy:", total_accuracy)    

def check_patients(test_records, classifier):
    """ Repeatedly prompt the user for a Patient ID until the user
        enters "quit". For each patient ID entered, search the test
        set for the record with that ID, print a message and prompt
        the user again. If the patient is in the test set, print a
        table: for each attribute, list the name, the patient's value,
        the classifier's midpoint value, and the vote cast by the
        classifier. After the table, output the final prediction made
        by the classifier.
        If the patient ID is not in the test set, print a message and
        repeat the prompt. Assume the user enters an integer or quit
        when prompted for the patient ID.
    """
    # prompt user for an ID
    ID = input("Enter a patient ID to see classification details:")
    # while the user has not entered "quit":
    while ID.lower() != "quit":
        #check if user enters a number
        if ID.isdigit():
            for record in test_records:
                # determine whether the entered patient ID is in the test set
                if int(ID) == record["ID"]:
                    # print a table of results using print_table()
                    print_table(record, classifier)
                    # then print the overall diagnosis. See handout for sample output
                    if record["prediction"] == "B":
                        print("Classifier's diagnosis: Benign")
                    elif record["prediction"] == "M":
                        print("Classifier's diagnosis: Malignant")
                    break
            else:
                # print a message saying the patient ID wasn't found
                print("Patient ID not found")
        #if not ask them to enter a valid ID
        else:
            print("Please enter a valid patient ID")
        # prompt the user for another ID
        ID = input("Enter a patient ID to see classification details:")

if __name__ == "__main__": 
    # Main program
    
    # load the training set
    print("Reading in training data...")
    training_data_file = "cancerTrainingData.txt"
    training_set = make_training_set(training_data_file)
    print("Done reading training data.")
    
    # load the test set 
    print("Reading in test data...")
    test_file = "cancerTestingData.txt"
    test_set = make_test_set(test_file)
    print("Done reading test data.\n")

    # train the classifier: uncomment this block once you've
    # implemented train_classifier
    print("Training classifier..."    )
    classifier = train_classifier(training_set)
    print("Classifier cutoffs:")
    for key in ATTRS[1:11]:
        print("    ", key, ": ", classifier[key], sep="")
    print("Done training classifier.\n")

    # use the classifier to make predictions on the test set:
    print("Making predictions and reporting accuracy")
    classify(test_set, classifier)
    report_accuracy(test_set)
    print("Done classifying.\n")

    # prompt the user for patient IDs and provide details on
    # the diagnosis: 
    check_patients(test_set, classifier)
