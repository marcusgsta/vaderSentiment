

def getPrecision(truePositives, trueNegatives, trueNeutrals):
    """
    Calculate accuracy score from result
    """
    precisionScore = truePositives / (truePositives + trueNegatives + trueNeutrals)
    
    return precisionScore
    
def getRecall(truePositives, falseNegatives):
    """
    Calculate recall from result
    """
    recall = truePositives / (truePositives + falseNegatives)
    
    return recall
    
def getF1Score(precision, recall):
    """
    Calculate F1 Score
    """
    
    F1Score = 2 * ( precision * recall / (precision + recall) )
    
    return F1Score
    
    
def printMetricsTable(arr):
    """
    Print a nice table of the evaluation metrics
    """
    import termtables as tt
    strategy, precision, recall, F1Score = arr
    precision, recall, F1Score = round(precision, 2), round(recall, 2), round(F1Score, 2)
    string = tt.to_string(
        [[strategy, precision, recall, F1Score]], header=["Strategy", "Precision", "Recall", "F1Score"], style=tt.styles.ascii_thin_double
    )
    print(string)
    













