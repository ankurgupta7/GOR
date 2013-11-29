'''
    storing words in a trie with EOW pointing to the count of word ending at this node
    adding to trie : O(length(word))
    retrieving a word : (O(length(word)))

    ** I did not choose hash tables because:
    0. no space optimisation possible
    1. multiple strings can have same hashValue. Collision handling removes the O(1) charm of hashes
    2. for displaying the result, the whole hash table had to be traversed, which is O(noOfWords) >> O(length(word))
    
'''
import re
EOW='~'
fin=open(u'input.txt','r')
fout=open(u'output_1.txt','w')
class Trie:
    def __init__(self):
        self.T = dict()
    def add(self, word):
        trieRoot = self.T
        current_dict = trieRoot
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        try:
            current_dict[EOW]=current_dict[EOW]+1
        except KeyError:
            current_dict=current_dict.setdefault(EOW,1)
        return trieRoot

    def traverse(self,_T_,word):
        curKey=_T_
        for key in curKey.viewkeys():
            if(key==EOW):
                fout.write(word+ str(curKey[EOW])+' ')
                return
            self.traverse(curKey[key],word+key)

if __name__=='__main__':
    
    wordLines=fin.readlines() 
    Trie_object=Trie()
    for line in wordLines:
        words = re.split('''[ ' \t \n , . ! @ # $ % ^ & * ( ) ;  " : ? \ / > < - + ]''', line) #used to split on the tokens specified
        for word in words:
            T=Trie_object.add(word.lower())
    Trie_object.traverse(Trie_object.T,'')
    fin.close()
    fout.close()

    
