
from pykospacing import spacing
from tqdm import trange

def merge_text(result):    
    qst = ' '.join([result['question_text']])
    ast = ' '.join(result['answers_text'])
    tit = result['title']
    txt = ' '.join([tit, qst, ast])
    txt = txt.replace('\u200b', ' ')
    txt = txt.replace(u'\xa0', ' ')
    txt = txt.replace('\t', ' ')
    result['text_all'] = txt
    return result

def phrase_split(tags):
    tags2 = []
    for x in tags:
        sep = []
        for y in x:
            sep.extend(y.split('+'))
        tags2.append(sep)
    return tags2

def tag_split(tags2):
    tags3 = []
    for x in tags2:
        tup = []
        for y in x:
            tup.append(tuple(y.split('/')))
        tags3.append(tup)
    return tags3



def pos_select(tags3, pos):
    tags4 = []
    for x in tags3:
        select = []
        for y in x:
            if y[-1] in pos:
                select.append(y[0])
        tags4.append(select)
    return tags4
    

def __check(tags4):
    tags5 = []
    for x in tags4:
        select = []
        for y in x:
            if '__' in y:
                y= y.split('__')[0]
            select.append(y)
        tags5.append(select)    
    return tags5

def space_check(tags5):
    checks = []
    for x in trange(len(tags5)):
      check = spacing(tags5[x])
      checks.append(check)
      #print(check)
    return checks


###############################################################################
if __name__ == '__main__':
    import pickle
    with open(r'.\keyword_results.txt', 'rb') as f:
        results = pickle.load(f)
    
    results = [merge_text(x) for x in results]

    txt_all = [x['text_all'] for x in results]
    with open(r'./keyword_texts_all.txt', 'w', encoding = 'utf-8') as f:
        f.writelines([x+'\n' for x in txt_all])

#Here we use the "Utagger": an effective Korean pos tagging program.
#More details to see: http://nlplab.ulsan.ac.kr/doku.php?id=utagger
#You can use  the "KoNlpy" module as well.
#But please take care of the tagging sets applied in different pos tagging tools.
       
    with open(r'./keyword_tags_all.txt', 'r', encoding = 'utf-8') as f: # read the utagger tagging file
         tags_all = [x.strip() for x in f.readlines()]
         
    tags = [x.split(' ') for x in tags_all]
    tags2 =  phrase_split(tags)
    tags3 = tag_split(tags2)
    # Here we only choose nouns, verbs, adjetives, and verbs to save for the next experiment.
    # You can select what you think are important through changing the list of "pos".
    tags4 = pos_select(tags3, pos=['NP','NNP', 'VV', 'VA', 'VX', 'MM', 'MAG', 'SL', 'SH', 'NF', 'NV'])
    tags5 =  __check(tags4)
    #if needed, !pip install git+https://github.com/haven-jeon/PyKoSpacing.git
    checks = space_check(tags5)




