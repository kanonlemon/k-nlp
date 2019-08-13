import sys, os, csv
from knlp.preprocess.TextConverter import TextConverter
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import joblib

class BondChatTextRFClassifier(object):

    def __init__(self, model_path=None, load_model_on_init=False, padding=200, *args, **kwargs):
        self.converter = TextConverter()
        self.clf = None
        self.padding = padding
        if model_path:
            self.model_path=model_path
        else:
            self.model_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "models/skl_bcc_rf.m") 
        if load_model_on_init:
            self.clf = joblib.load(self.model_path)
        return super().__init__(*args, **kwargs)

    def train(self, filepath, *args, **kwargs):
        
        mapping = {
            "first": 1,
            "second" : 2,
            "fund": 3,
            "other": 4 
        }
        X = []
        y = []
        with open(filepath, encoding="utf8") as fi:
            csv_reader = csv.reader(fi)
            for row in csv_reader:
                X.append( self.preprocessText(row[0]) )
                y.append( mapping[row[1]] )
        clf = RandomForestClassifier(*args, **kwargs)
        scores = cross_val_score(clf, X, y, cv=5)
        print(scores.mean())

        self.clf = clf.fit(X, y)
        joblib.dump(clf, self.model_path)
    
    def predict(self, textes):
        if self.clf == None:
            return None
        else:
            textes = [ self.preprocessText(text) for text in textes]
            return self.clf.predict( textes )

    def preprocessText(self, text):
        return self.converter.text2number(text, padding=self.padding, dropIfNotExist=False) 


if __name__=="__main__":
    bctc = BondChatTextRFClassifier(load_model_on_init=True, padding=200)
    #bctc.train("C:/Users/Administrator/git/knlp/train_data/bond_chat_msg.csv",n_estimators=80)
    print(bctc.predict(["""bid 万科"""]))
