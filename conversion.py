import csv
import re
import pandas as pd

class DissertationModule:
    def __init__(self):
        self.sem2syns_active = {
            'theme': 'obj',
            'agent': 'nsubj',
            'recipient': 'iobj',
            'location': 'obl'
        }

        self.sem2syns_passive = {
            'theme': 'nsubj:pass',
            'agent': 'obl:agent',
            'recipient': 'iobj',
            'location': 'obl'
        }
        self.verbs_lemmas = {
            'ate':'eat', 'painted':'paint', 'drew':'draw', 'cleaned':'clean',
            'cooked':'cook', 'dusted':'dust', 'hunted':'hunt', 'nursed':'nurse',
            'sketched':'sketch', 'washed':'wash', 'juggled':'juggle', 'called':'call',
            'eaten':'eat', 'drawn':'draw', 'baked':'bake', 'liked':'like', 'knew':'know',
            'helped':'help', 'saw':'see', 'found':'find', 'heard':'hear', 'noticed':'notice',
            'loved':'love', 'admired':'admire', 'adored':'adore', 'appreciated':'appreciate',
            'missed':'miss', 'respected':'respect', 'tolerated':'tolerate', 'valued':'value',
            'worshipped':'worship', 'observed':'observe', 'discovered':'discover', 'held':'hold',
            'stabbed':'stab', 'touched':'touch', 'pierced':'pierce', 'poked':'poke',
            'known':'know', 'seen':'see', 'hit':'hit', 'hoped':'hope', 'said':'say',
            'believed':'believe', 'confessed':'confess', 'declared':'declare', 'proved':'prove',
            'thought':'think', 'supported':'support', 'wished':'wish', 'dreamed':'dream',
            'expected':'expect', 'imagined':'imagine', 'envied':'envy', 'wanted':'want',
            'preferred':'prefer', 'needed':'need', 'intended':'intend', 'tried':'try',
            'attempted':'attempt', 'planned':'plan','craved':'crave','hated':'hate',
            'enjoyed':'enjoy', 'rolled':'roll', 'froze':'freeze', 'burned':'burn', 'shortened':'shorten',
            'floated':'float', 'grew':'grow', 'slid':'slide', 'broke':'break', 'crumpled':'crumple',
            'split':'split', 'changed':'change', 'snapped':'snap', 'tore':'tear', 'collapsed':'collapse',
            'decomposed':'decompose', 'doubled':'double', 'improved':'improve', 'inflated':'inflate',
            'enlarged':'enlarge', 'reddened':'redden', 'popped':'pop', 'disintegrated':'disintegrate',
            'expanded':'expand', 'cooled':'cool', 'soaked':'soak', 'frozen':'freeze', 'grown':'grow',
            'broken':'break', 'torn':'tear', 'slept':'sleep', 'smiled':'smile', 'laughed':'laugh',
            'sneezed':'sneeze', 'cried':'cry', 'talked':'talk', 'danced':'dance', 'jogged':'jog',
            'walked':'walk', 'ran':'run', 'napped':'nap', 'snoozed':'snooze', 'screamed':'scream',
            'stuttered':'stutter', 'frowned':'frown', 'giggled':'giggle', 'scoffed':'scoff',
            'snored':'snore', 'snorted':'snort', 'smirked':'smirk', 'gasped':'gasp',
            'gave':'give', 'lent':'lend', 'sold':'sell', 'offered':'offer', 'fed':'feed',
            'passed':'pass', 'rented':'rent', 'served':'serve','awarded':'award', 'promised':'promise',
            'brought':'bring', 'sent':'send', 'handed':'hand', 'forwarded':'forward', 'mailed':'mail',
            'posted':'post','given':'give', 'shipped':'ship', 'packed':'pack', 'studied':'study',
            'examined':'examine', 'investigated':'investigate', 'thrown':'throw', 'threw':'throw',
            'tossed':'toss', 'meant':'mean', 'longed':'long', 'yearned':'yearn', 'itched':'itch',
            'loaned':'loan', 'returned':'return', 'slipped':'slip', 'wired':'wire', 'crawled':'crawl',
            'shattered':'shatter', 'bought':'buy', 'squeezed':'squeeze', 'teleported':'teleport',
            'melted':'melt', 'blessed':'bless'
        } 

        self.verbs = list(self.verbs_lemmas.values())

        self.articles = ['a', 'the']
        self.prepositions = ['on', 'in', 'beside', 'by']
        self.output = {}
        self.gen = {}
        self.worddata = None

        self.pos = {
            'a': 'DET',
            'the': 'DET',
            'on': 'ADP',
            'in': 'ADP',
            'beside': 'ADP',
            'that': 'SCONJ',
            'was': 'AUX',
            'by': 'ADP', 
            'did': 'AUX', 
            'what': 'PRON',
            'who': 'PRON'
        }

        self.proper_nouns = {
            'Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'William', 'Isabella', 'James', 'Sophia', 'Oliver',
            'Charlotte', 'Benjamin', 'Mia', 'Elijah', 'Amelia', 'Lucas', 'Harper', 'Mason', 'Evelyn', 'Logan',
            'Abigail', 'Alexander', 'Emily', 'Ethan', 'Elizabeth', 'Jacob', 'Mila', 'Michael', 'Ella', 'Daniel',
            'Avery', 'Henry', 'Sofia', 'Jackson', 'Camila', 'Sebastian', 'Aria', 'Aiden', 'Scarlett', 'Matthew',
            'Victoria', 'Samuel', 'Madison', 'David', 'Luna', 'Joseph', 'Grace', 'Carter', 'Chloe', 'Owen',
            'Penelope', 'Wyatt', 'Layla', 'John', 'Riley', 'Jack', 'Zoey', 'Luke', 'Nora', 'Jayden',
            'Lily', 'Dylan', 'Eleanor', 'Grayson', 'Hannah', 'Levi', 'Lillian', 'Isaac', 'Addison', 'Gabriel',
            'Aubrey', 'Julian', 'Ellie', 'Mateo', 'Stella', 'Anthony', 'Natalie', 'Jaxon', 'Zoe', 'Lincoln',
            'Leah', 'Joshua', 'Hazel', 'Christopher', 'Violet', 'Andrew', 'Aurora', 'Theodore', 'Savannah', 'Caleb',
            'Audrey', 'Ryan', 'Brooklyn', 'Asher', 'Bella', 'Nathan', 'Claire', 'Thomas', 'Skylar', 'Leo', 'Lina', 'Charlie'
        }

        self.length = 0

    def load_data(self, filename):
        with open(filename, 'r') as tsvfile:
            reader = csv.reader(tsvfile, delimiter='\t')
            sentence_id = 1
            for row in reader:
                if row:
                    sentence = row[0]
                    semantics = row[1]
                    distribution = row[2]
                    self.output[sentence_id] = {'sentence': sentence, 'semantics': semantics, 'distribution': distribution}
                    sentence_id += 1
                    self.length += 1

    def process_sentence(self, sentence_id):
        sentence = self.output.get(sentence_id)

        # ---------------------- Add the words to the dataframe ---------------------- #
        if sentence:
            words = sentence['sentence'].split(' ')
            proper_words = []
            for word in words:
                if word not in self.proper_nouns:
                    proper_words.append(word.lower())
                else:
                    proper_words.append(word)
            self.worddata = pd.DataFrame(proper_words, columns=['form'])

        # ---------------------- Add the lemmas to the dataframe --------------------- #
            lemmas = []
            for index, row in self.worddata.iterrows():
                if row['form'] in self.verbs_lemmas:
                    lemmas.append(self.verbs_lemmas[row['form']])
                elif row['form'] == 'did':
                    lemmas.append('do')
                elif row['form'] == 'was':
                    lemmas.append('be')
                elif row['form'] in self.proper_nouns:
                    lemmas.append(row['form'])
                else:
                    lemmas.append(row['form'])
            self.worddata['lemma'] = lemmas

        # ---------------------- Setting up the dataframe ------------ #

            heads = [0 for i in range(len(words))] # this might need to be set to a dicionary as well to deal with multiple relations
            deprel = {k: ['root'] for k in range(len(words))} # sets the default to 'root'
            pos = [0 for i in range(len(words))]

            single = re.compile(r'(\w+ \( x _ \d \))')
            double = re.compile(r'(\w+ \. \w+ (\. \w+ )?\( x _ \d+ , (?:x _ \d+|\w+|\?) \))') 
            finder = re.compile(r'(?P<word>\w+) \. (?P<relationname>\w+)(?: \. )?(?P<preposition>\w+)? (?: )?(?P<relationship>\( x _ (?P<head>\d+) , (x _ (?P<number>\d+)|(?P<name>\w+)|(?P<question>\?)) \))')

            relations = re.findall(double, sentence['semantics'])            

        # --------------------------- Dealing with passives -------------------------- #
            relationships = []
            for relation in relations:
                relation = relation[0]
                relationship = re.search(finder, relation).group('relationname')
                relationships.append(relationship)
    
            if 'theme' in relationships and 'agent' in relationships:
                theme_index = relationships.index('theme')
                agent_index = relationships.index('agent')
                if theme_index < agent_index:
                    # 'theme' comes before 'agent' in the relation
                    passive = True
                else:
                    passive = False
            elif 'theme' in relationships and 'agent' not in relationships:
                passive = True
            else:
                passive = False

        # ------------------------- Dealing with passives v2 ------------------------- #
            
    

        # ----------------------------- Dealing with 'to' ---------------------------- #
            
            if 'to' in self.worddata['form'].values and 'recipient' in relationships:
                dative = True
            else:
                dative = False
        # -------------------- Check if the sentence is a question ------------------- #
            if '?' in sentence['sentence']:
                _question = True
            else:
                _question = False

        # ------------------------- Identifying the main verb ------------------------ #

            dependents = []
            for relation in relations:
                relation = relation[0]
                number = re.search(finder, relation).group('number')
                if number is not None:
                    number = int(number)
                    dependents.append(number)


            for index, row in self.worddata.iterrows():
                    if index not in dependents:
                        if row['form'] in self.verbs_lemmas or row['form'] in self.verbs:

                            main_verb = row['form']
                
        # --------------------------- Heads and Deprels ---------------------------  #
            for i, relation in enumerate(relations):
                relation = relation[0]

                number = re.search(finder, relation).group('number')
                if number is not None:
                    number = int(number)

                name = re.search(finder, relation).group('name')

                question = re.search(finder, relation).group('question')

                for index, row in self.worddata.iterrows():
                    # if index not in dependents:
                    #     if row['form'] in self.verbs_lemmas or row['form'] in self.verbs:

                    #         main_verb = row['form']

                    if index == number or row['form'] == name or row['form'] == question:
                        heads[index] = int(re.search(finder, relation).group('head'))
                        if re.search(finder, relation).group('relationname') == 'nmod':
                            if self.worddata.iloc[number]['form'] in self.verbs_lemmas:
                                deprel[index].append('acl:relcl')
                            preposition = re.search(finder, relation).group('preposition')
                            deprel[index].append(f'nmod:{preposition}') 
                        else:
                            deprel[index].append(re.search(finder, relation).group('relationname'))
                    
                    elif row['form'] in self.prepositions:
                        heads[index] = index + 1
                        deprel[index].append('case')

                    elif row['form'] == '.':
                        main_verb_index = self.worddata[self.worddata['form'] == main_verb].index[0]
                        heads[index] = main_verb_index
                        deprel[index].append('punct')

                    elif row['form'] == 'was':
                        heads[index] = index + 1
                        deprel[index].append('aux:pass')

                    elif row['form'] == 'that':
                        heads[index] = int(re.search(finder, relation).group('head'))
                        deprel[index].append('mark')

                    elif row['form'] == 'to':
                        if dative == True:
                            heads[index] = index + 1
                            deprel[index].append('case')
                        else:
                            heads[index] = index + 1
                            deprel[index].append('mark')

                    elif row['form'] == 'did': 
                        main_verb_index = self.worddata[self.worddata['form'] == main_verb].index[0]
                        heads[index] = main_verb_index
                        deprel[index].append('aux')

                    elif row['form'] in self.articles:
                        heads[index] = index + 1
                        deprel[index].append('det')
                        if self.worddata.iloc[index-1]['form'] in self.prepositions or self.worddata.iloc[index-1]['form'] == 'to':
                            heads[index-1] = index + 1

                    elif heads[index] == 0:
                        heads[index] = 0

            # --------------------------- Dealing the POS tags --------------------------- #
                    if row['form'] == 'to':
                        if dative == False:
                            pos[index] = 'PART'
                        else:
                            pos[index] = 'ADP'
                    elif row['form'] in self.pos:
                        pos[index] = self.pos[row['form']]
                    elif row['form'] in self.verbs or row['form'] in self.verbs_lemmas:
                        pos[index] = 'VERB'
                    elif row['form'] in self.proper_nouns:
                        pos[index] = 'PROPN'
                    elif row['form'] == '.' or row['form'] == '?':
                        pos[index] = 'PUNCT'
                    else:
                        pos[index] = 'NOUN'


            if _question:
                heads[0] = heads[-1]
                deprel[0] = deprel[list(deprel)[-1]]
                deprel[list(deprel)[-1]] = ['punct']


            for key in deprel.keys():
                if len(deprel[key]) == 1:
                    deprel[key] = deprel[key][0]
                else:
                    deprel[key] = deprel[key][1]

            for k, v in deprel.items():
                if passive:
                    if v in self.sem2syns_passive.keys():
                        deprel[k] = self.sem2syns_passive[v]
                else:
                    if v in self.sem2syns_active.keys():
                        deprel[k] = self.sem2syns_active[v]

            # print(heads)
            

            self.worddata['pos'] = pos
            self.worddata['head'] = heads
            self.worddata['deprel'] = deprel.values()

            return self.worddata
        else:
            return None
        


# Example usage:
# module = DissertationModule()
# module.load_data('gen_cogsLF.tsv')
# worddata = module.process_sentence(16001)
# print(worddata)

# ---------------------------------------------------------------------------- #
#                                  Main runner                                 #
# ---------------------------------------------------------------------------- #

# module = DissertationModule()
# module.load_data('train.tsv')

# for i in range(module.length):
#     worddata = module.process_sentence(i)
#     if worddata is not None:
#         print(worddata)
#         print('\n')
#     else:
#         print('No data found for sentence', i)
#         print('\n')




