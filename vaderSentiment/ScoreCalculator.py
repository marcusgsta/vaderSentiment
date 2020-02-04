# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import seaborn as sn
import pandas as pd


class ScoreCalculator():
    """
    Perform calculations on tweets for different evaluation metrics.
    Print table of metrics.
    """
    
    def __init__(self, tweets, analyzer):
        self.tweets = tweets
        self.analyzer = analyzer
    
    
    def confusionMatrix(self):
        """
        Create a confusion matrix
        """
        
        cn_matrix = confusion_matrix(self.y_Actual, self.y_Predicted, labels=["Positive", "Neutral", "Negative"])
        print(cn_matrix)
        print("Accuracy Score:", accuracy_score(self.y_Actual, self.y_Predicted))
        print(classification_report(self.y_Actual, self.y_Predicted))
        
    
    def getScores(self):
        self.y_Actual = []
        self.y_Predicted = []
        
        for tweet in self.tweets:
            # append actual class
            self.y_Actual.append(tweet[1])
            
            # count += 1
            vs = self.analyzer.polarity_scores(tweet[0])
            compound = vs['compound']
            
            predicted = ""
            # Predicted class:
            if compound > 0.05:
                predicted = "Positive"
            elif compound < -0.05:
                predicted = "Negative"
            elif -0.05 <= compound <= 0.05:
                predicted = "Neutral" 
                
            # append predicted class
            self.y_Predicted.append(predicted)
            