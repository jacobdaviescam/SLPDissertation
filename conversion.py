import csv
import re
import pandas as pd

class DissertationModule:
    def __init__(self):
        self.sem2syns_active = {
            'theme': 'obj',
            'agent': 'nsubj',
            'recipient': 'iobj',
            'location': 'obl',
            'xcomp': 'xcomp'
        }

        self.sem2syns_passive = {
            'theme': 'nsubj:pass',
            'agent': 'obl:agent',
            'recipient': 'nsubj:pass',
            'location': 'obl',
            'xcomp': 'xcomp'
        }

        self.sem2syns_unaccusative = {
            'theme': 'nsubj',
            'agent': 'nsubj',
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

        self.V_unacc = [
        'rolled', 'froze', 'burned', 'shortened', 'floated',
        'grew', 'slid', 'broke', 'crumpled', 'split',
        'changed', 'snapped', 'disintegrated', 'collapsed', 'decomposed',
        'doubled', 'improved', 'inflated', 'enlarged', 'reddened', 'shattered'
        ]

        self.verbs = list(self.verbs_lemmas.keys())
        self.verbs.extend(self.verbs_lemmas.values())

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

            heads = {k: [(0, 'root')] for k in range(len(words))} 
            deprel = {k: ['root'] for k in range(len(words))} # sets the default to 'root'
            pos = [0 for i in range(len(words))]

            single = re.compile(r'(\w+ \( x _ \d \))')
            double = re.compile(r'(\w+ \. \w+ (\. \w+ )?\( x _ \d+ , (?:x _ \d+|\w+|\?) \))') 
            finder = re.compile(r'(?P<word>\w+) \. (?P<relationname>\w+)(?: \. )?(?P<preposition>\w+)? (?: )?(?P<relationship>\( x _ (?P<head>\d+) , (x _ (?P<number>\d+)|(?P<name>\w+)|(?P<question>\?)) \))')

            relations = re.findall(double, sentence['semantics'])            

        # --------------------------- Dealing with passives -------------------------- #
        # ----------------- Another version of this for unaccusatives ---------------- #
            relationships = []
            verbs = {}
            for relation in relations:
                relation = relation[0]

                if verbs.get(re.search(finder, relation).group('word')) is None:
                    if re.search(finder, relation).group('number') is not None:
                        verbs[re.search(finder, relation).group('word')] = [(re.search(finder, relation).group('relationname'), re.search(finder, relation).group('number'))]
                    elif re.search(finder, relation).group('name') is not None:
                        verbs[re.search(finder, relation).group('word')] = [(re.search(finder, relation).group('relationname'), re.search(finder, relation).group('name'))]
                    else:
                        verbs[re.search(finder, relation).group('word')] = [(re.search(finder, relation).group('relationname'), re.search(finder, relation).group('question'))]
                else:
                    if re.search(finder, relation).group('number') is not None:
                        verbs[re.search(finder, relation).group('word')].append((re.search(finder, relation).group('relationname'), re.search(finder, relation).group('number')))
                    elif re.search(finder, relation).group('name') is not None:
                        verbs[re.search(finder, relation).group('word')].append((re.search(finder, relation).group('relationname'), re.search(finder, relation).group('name')))
                    else:
                        verbs[re.search(finder, relation).group('word')].append((re.search(finder, relation).group('relationname'), re.search(finder, relation).group('question')))


                relationship = re.search(finder, relation).group('relationname')
                relationships.append(relationship)

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

            passive = False
                
        # --------------------------- Heads and Deprels ---------------------------  #
            for i, relation in enumerate(relations):
                relation = relation[0]
                # print(relation)

                number = re.search(finder, relation).group('number')
                if number is not None:
                    number = int(number)

                name = re.search(finder, relation).group('name')

                question = re.search(finder, relation).group('question')

                for index, row in self.worddata.iterrows():

                    # if row['form'] in self.verbs:
                    #     if self.worddata[index-1]['form'] == 'was':
                    #         passive = True

                    if index == number or row['form'] == name or row['form'] == question:
                            head_verb = self.worddata.iloc[int(re.search(finder, relation).group('head'))]['form']
                            if self.worddata.iloc[int(re.search(finder, relation).group('head'))]['form'] in self.verbs_lemmas:
                                if self.worddata.iloc[int(re.search(finder, relation).group('head'))-1]['form'] == 'was':
                                    passive = True
                            heads[index].append((int(re.search(finder, relation).group('head')), re.search(finder, relation).group('relationname')))

                    # ----------------------- Dealing with relative clauses ---------------------- #
                            if re.search(finder, relation).group('relationname') == 'nmod':
                                if self.worddata.iloc[number]['form'] in self.verbs_lemmas:
                                    that_index = int(re.search(finder, relation).group('head')) + 1
                    # ---------------------------- Dealing with 'that' --------------------------- #
                                    if self.worddata.iloc[that_index]['form'] == 'that':
                                        heads[that_index].append((number, 'that'))
                                    deprel[index].append('acl:relcl')
                    # -------------------- Dealing with deps for prepositions -------------------- #
                                preposition = re.search(finder, relation).group('preposition')
                                deprel[index].append(f'nmod:{preposition}') 
                    # ----------------- Dealing with 'that' in subordinate clause ---------------- #
                            elif re.search(finder, relation).group('relationname') == 'ccomp':
                                that_index = int(re.search(finder, relation).group('head')) + 1
                                heads[that_index].append((number, 'that'))
                                deprel[index].append('ccomp')
                            else:
                    # ------------------ Dealing with passives and unaccusatives ----------------- #
                                if passive:
                                    verbs_list = [verb[0] for verb in verbs[re.search(finder, relation).group('word')]]
                                    # if the relationname is recipient it should be given 'nsubj:pass' and 
                                    if re.search(finder, relation).group('relationname') == 'theme':
                                        # print(verbs_list)
                                        if 'recipient' in verbs_list and verbs_list.index('recipient') < verbs_list.index('theme'):
                                            deprel[index].append('obj')
                                        else:
                                            deprel[index].append('nsubj:pass')
                                    elif re.search(finder, relation).group('relationname') == 'recipient':
                                        if 'recipient' in verbs_list and verbs_list.index('recipient') > verbs_list.index('theme'):
                                            deprel[index].append('iobj')
                                        else:
                                            deprel[index].append('nsubj:pass')
                                        
                                    else:
                                        deprel[index].append(self.sem2syns_passive[re.search(finder, relation).group('relationname')])
                                elif self.worddata.iloc[int(re.search(finder, relation).group('head'))]['form'] in self.V_unacc:
                                    if re.search(finder, relation).group('relationname') == 'theme' and len(verbs[re.search(finder, relation).group('word')]) < 2:
                                        deprel[index].append('nsubj')
                                    else:
                                        deprel[index].append(self.sem2syns_active[re.search(finder, relation).group('relationname')])
                                else:
                                    deprel[index].append(self.sem2syns_active[re.search(finder, relation).group('relationname')])

                                # print(deprel[index])
                    
                    elif row['form'] in self.prepositions:
                        heads[index].append(((index + 1), 'preposition'))
                        deprel[index].append('case')

                    elif row['form'] == '.':
                        main_verb_index = self.worddata[self.worddata['form'] == main_verb].index[0]
                        heads[index].append(((main_verb_index), 'punct'))
                        deprel[index].append('punct')

                    elif row['form'] == 'was':
                        heads[index].append(((index + 1), 'aux:pass'))
                        deprel[index].append('aux:pass')

                    elif row['form'] == 'that':
                        deprel[index].append('mark')

                    elif re.search(finder, relation).group('relationname') == 'recipient':
                        if row['form'] == 'to':
                            if name:
                                heads[index].append((self.worddata.index[[self.worddata['form'] == name]].to_list()[0], 'preposition'))
                                deprel[index].append('case')
                            elif number:
                                heads[index].append((number, 'preposition'))
                                deprel[index].append('case')
                            elif question:
                                heads[index].append((0, 'preposition'))
                                deprel[index].append('case')

                    elif row['form'] == 'to':
                        if dative == False:
                            heads[index].append(((index + 1), 'mark'))
                            deprel[index].append('mark')

                    elif row['form'] == 'did': 
                        main_verb_index = self.worddata[self.worddata['form'] == main_verb].index[0]
                        heads[index].append(((main_verb_index), 'aux'))
                        deprel[index].append('aux')

                    elif row['form'] in self.articles:
                        heads[index].append(((index + 1), 'det'))
                        deprel[index].append('det')
                        if self.worddata.iloc[index-1]['form'] in self.prepositions or self.worddata.iloc[index-1]['form'] == 'to':
                            heads[index-1].append(((index + 1), 'case'))

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
                heads[0] = heads[list(heads)[-1]]
                deprel[0] = deprel[list(deprel)[-1]]
                deprel[list(deprel)[-1]] = ['punct']

            # print(deprel)
            # print(heads)

            for k, v in deprel.items():
                if len(v) == 1:
                    deprel[k] = v[0]
                elif 'nsubj' in v:
                    deprel[k] = 'nsubj'
                elif 'iobj' in v and 'nsubj:pass' in v:
                    deprel[k] = 'iobj'
                elif 'obj' in v and 'nsubj:pass' in v:
                    deprel[k] = 'obj'
                elif 'nsubj:pass' in v:
                    deprel[k] = 'nsubj:pass'
                elif 'obj' in v:
                    deprel[k] = 'obj'
                else:
                    deprel[k] = v[1]

            for k, v in deprel.items():
                if v == 'iobj'and dative == True:
                    deprel[k] = 'obl:to'

            new_heads = []
            # print(len(heads))

            # -------------------- This deals with multiple relations -------------------- #
            
            for k, v in heads.items():
                if len(v) < 2:
                    new_heads.append(v[0])
                else:
                    deprelations = [headdep[1] for headdep in v]
                    # print(deprelations)
                    # print(v)
                    if 'agent' in deprelations:
                        new_heads.append(v[deprelations.index('agent')])
                        # if _question == False:
                        #     deprel[k] = 'agent'
                    elif deprelations.count('theme') > 1:
                        main_verb_index = self.worddata[self.worddata['form'] == main_verb].index[0]
                        for item in v:
                            if item[0] == main_verb_index:
                                new_heads.append(item)
                            else:
                                new_heads.append(v[deprelations.index('theme')])
                                break
                
                    elif deprelations.count('theme') == 1:
                        new_heads.append(v[deprelations.index('theme')])

                    # elif deprelations.count('theme') == 2:
                    #     new_heads.append(v[max(idx for idx, val in enumerate(deprelations) if val == 'theme')])
                    # elif deprelations.count('theme') == 1:
                    #     new_heads.append(v[deprelations.index('theme')])
                    elif 'case' in deprelations:
                        new_heads.append(v[deprelations.index('case')])
                    else:
                        new_heads.append(v[1])

            # print(heads)
            # print(new_heads)


            new_heads = [v[0] for v in new_heads]

            if sentence['distribution'] == 'standalone_NP_RC' or sentence['distribution'] == 'standalone_NP_PP':
                new_heads[1] = 0
                deprel[1] = 'root'


            xpos = ['_' for i in range(len(words))]
            feats = ['_' for i in range(len(words))]
            deps = ['_' for i in range(len(words))]
            misc = ['_' for i in range(len(words))]
            self.worddata.index += 1 

            # print(new_heads)
            # print(deprel)

            self.worddata['pos'] = pos
            self.worddata['xpos'] = xpos
            self.worddata['feats'] = feats
            self.worddata['head'] = [head + 1 if head != 0 else 0 for head in new_heads]
            self.worddata['deprel'] = deprel.values()
            self.worddata['deps'] = deps
            self.worddata['misc'] = misc



            return self.worddata
        else:
            return None
        


# Example usage:
# module = DissertationModule()
# module.load_data('train.tsv')
# worddata = module.process_sentence(10798)
# print(worddata)

# ---------------------------------------------------------------------------- #
#                                  Main runner                                 #
# ---------------------------------------------------------------------------- #

module = DissertationModule()
module.load_data('gen_cogsLF.tsv')
sent_id = 1
for i in range(1, module.length):
    worddata = module.process_sentence(i)
    with open('gen_cogsLF.conllu', 'a') as f:
        f.write(f'# sent_id = {sent_id}\n')
        f.write(f"# text = {module.output[i]['sentence']}\n")
        f.write(f"# distribution = {module.output[i]['distribution']}\n")
        if worddata is not None:
            worddata.to_csv(f, sep='\t', index=True, header = False)
            f.write('\n')
        else:
            print('No data found for sentence', i)
            print('\n')
        sent_id += 1



