import transformers
import torch
import h5py
import json
import tqdm

def get_word_embeddings(model, batch_encoding) -> list[torch.Tensor]:
    """
    Returns a list with one tensor per sentence in the batch.
    Each tensor has the shape (layers, num words, hidden dim)
    If a word is tokenized into multiple subwords, we only keep the embedding of the first subword.
    """
    with torch.no_grad():
        hidden_states = model(**{k:v.to(model.device) for k,v in batch_encoding.items()}, output_hidden_states=True).hidden_states 
    hidden_states = torch.stack(hidden_states).cpu()
    (layers, batch, num_tokens, hid_dim) = hidden_states.shape
    output_tensors = []
    for i in range(batch):
        seen_word_ids = set()
        word_reprs = []
        for idx, word_id in enumerate(batch_encoding.word_ids(i)):
            if word_id is not None and word_id not in seen_word_ids:
                word_reprs.append(hidden_states[:, i, idx, :])
                seen_word_ids.add(word_id)
        output_tensors.append(torch.stack(word_reprs, dim=1).numpy())
    return output_tensors

proper_nouns = {
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

def read_sents(fname):
    with open(fname) as f:
        for line in f:
            line = line.rstrip("\n")
            id, sent = line.split("\t")
            # Jacob lower-cased everything except for the proper nouns.
            words = [w.lower() if w not in proper_nouns else w for w in sent.split(" ")]
            yield words


def iterate(sents, tokenizer, bs = 32):
    i = 0
    while i < len(sents):
        yield tokenizer(sents[i:i+bs], is_split_into_words=True, padding=True, return_tensors="pt"), sents[i:i+bs]
        i += bs

model_name = "google-bert/bert-base-multilingual-cased"
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
model = transformers.AutoModel.from_pretrained(model_name)

if torch.cuda.device_count() > 0:
    print("using GPU")
    model = model.to(0)
else:
    print("using CPU, which is a little slow")

sents = list(read_sents("../data/allfiles.tsv"))

with h5py.File("bert_embeddings.hdf5", "w") as h5out:
    sent2id = dict()
    i = 0
    for batch, sent_batch in tqdm.tqdm(iterate(sents, tokenizer)):
        for embeddings, sent in zip(get_word_embeddings(model, batch), sent_batch):
            # embeddings has shape (num layers, num words, num hidden dim)
            sent2id[" ".join(sent)] = str(i)
            # Kulmizev report using layers 4-8. I assume this means layers 4,5,6,7,8
            # where layer 1 corresponds to the first contextualized layer (not the static word embeddings)
            h5out[str(i)] = embeddings[4:8+1, :, : ] 
            i+=1
    h5out["sentence_to_index"] = [json.dumps(sent2id)]
    


        
