from nltk.corpus import wordnet
import numpy as np
import pandas as pd

#similarity function
#http://www.nltk.org/howto/wordnet.html
#w1,w2: string ; wordtype: wordnet.VERB, wordnet.NOUN, wordnet.ADJ, wordnet.ADV
#method: "path":  path_similarity, "lch": Leacock-Chodorow Similarity, "wup", Wu-Palmer Similarity
def similarity(w1,w2, method = "path", wordtype=None):
    #select similarity scheme
    fn = wordnet.path_similarity
    
    if method == "lch":
        #Leacock-Chodorow Similarity: The relationship is given as -log(p/2d) (not [0-1])
        fn = wordnet.lch_similarity
        #lch similarity requires same part of speech
        if wordtype == None:
            #Noun by default
            wordtype = wordnet.NOUN
    elif method == "wup":
        #Wu-Palmer Similarity
        fn = wordnet.wup_similarity
        
    if wordtype == None:
        w1syn = wordnet.synsets(w1)
        w2syn = wordnet.synsets(w2)
    else:
        w1syn = wordnet.synsets(w1, wordtype)
        w2syn = wordnet.synsets(w2, wordtype)
    max_similarity = 0
    for i in w1syn:
        for j in w2syn:
            similarity = fn(i,j)
            if similarity == None:
                continue
            if similarity > max_similarity:
                max_similarity = similarity
    return max_similarity







##build relationship_table class
#
##assume we have data
#tweets_data = ["Please call our Contact Centre on 02392441234 and we will be able to assist you", 
#          "We don't like to keep our lovely customers waiting for long! We hope you enjoy! Happy Friday!",
#         "Stats for the day have arrived. 1 new follower and NO unfollowers"]
##assume we get the following from using textblob on tweets_data
#noun_list = ["Contact Centre", "we", "you", "we", "customers", "Friday", "Stats", "follower","you"]
#noun_index = [0,0,0,1,1,1,2,2,2]
#verb_list = ["call", "able", "assist", "like", "keep", "hope", "have","able"]
#verb_index = [0,0,0,1,1,1,2,2]
#
##usage:
#table = relationship_table(noun_list, noun_index, verb_list, verb_index)
#table.getDistribution("have",1)
#Output: 
#Friday            0.000000
#Contact Centre    0.000000
#customers         0.000000
#we                0.000000
#follower          0.333333
#you               0.333333
#Stats             0.333333
#Name: have, dtype: float64

#table.getDistribution("have",1)["follower"]
#Output: 0.33333333333333


class relationship_table:
    
    def __init__(self, list1, list1_index, list2, list2_index):
        
        n1_set = list(set(list1))
        n1_dict = dict(zip(n1_set, range(len(n1_set))))
        n2_set = list(set(list2))
        n2_dict = dict(zip(n2_set, range(len(n2_set))))
        n1 = len(n1_set)
        n2 = len(n2_set)
        self.array = np.zeros((n1,n2))
        self.graph = None
        for i in range(len(list1)):
            #get what tweet n1 item comes from
            n1tweetidx = list1_index[i]
            #get index in array
            n1idx = n1_dict[list1[i]]
            for j in range(len(list2)):
                #get what tweet the n2 item comes from
                n2tweetidx = list2_index[j]
                if n1tweetidx == n2tweetidx:
                    #get index in array
                    n2idx = n2_dict[list2[j]]
                    self.array[n1idx, n2idx] += 1
        self.array = pd.DataFrame(self.array, index=n1_set, columns=n2_set)
    def toArray(self):
        return self.array
    def toGraph(self):
        if self.graph != None:
            return self.graph.view()
        #
        from graphviz import Graph
        
        #construct graph
        e = Graph('G', filename='graph.gv')
        #nodes
        #elements in list1 shown as box
        e.attr('node', shape='box')
        for i in self.array.index:
            e.node(i)
        #elements in list2 shown as ellipse
        e.attr('node', shape='ellipse')
        for i in self.array.columns:
            e.node(i)
        
        #edges
        for i in self.array.index: 
            for j in self.array.columns:
                count = self.array.loc[i,j]
                if count > 0:
                    e.edge(i, j, label=str(count))
        #store graph
        self.graph = e
        return e.view()
    #get n1_set and n2_set
    def getLists(self):
        return [self.array.index, self.array.columns]
    #get probability distribution of all words in other list 
    #when keyword in the list specified by listnumber appears
    def getDistribution(self, keyword, listnumber):
        if(listnumber == 0):
            #list1
            if keyword not in self.array.index:
                return None
            return self.array.loc[keyword] / np.sum(self.array.loc[keyword])
        else:
            #list2
            if keyword not in self.array.columns:
                return None
            return self.array[keyword] / np.sum(self.array[keyword])
    #get count (similar to getDistribution but no normalization)
    def getCount(self, keyword, listnumber):
        if(listnumber == 0):
            #list1
            if keyword not in self.array.index:
                return None
            return self.array.loc[keyword]
        else:
            #list2
            if keyword not in self.array.columns:
                return None
            return self.array[keyword]
    #get sum of words in other list appears together with keyword in list specified by listnumber
    def getDistCumSum(self, keyword, listnumber):
        
        if(listnumber == 0):
            cumsum = (self.array.T).cumsum()
            #list1
            if keyword not in self.array.index:
                return None
            return (cumsum[keyword]/cumsum[keyword][-1])
        else:
            cumsum = self.array.cumsum()
            #list2
            if keyword not in self.array.columns:
                return None
            return (cumsum[keyword]/cumsum[keyword][-1])
