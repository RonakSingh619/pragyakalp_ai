from datetime import datetime
import json
import pickle
import time
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D # type: ignore
from tensorflow.keras.preprocessing.text import Tokenizer # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
from sklearn.preprocessing import LabelEncoder
import Data.Credentials as Crd

Cred = Crd.Credentail()

def cal_day():
    day = datetime.today().weekday()+1
    dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if day in dict.keys():
        dayOfWeek = dict[day]
    return dayOfWeek
def GetDateAndTime():
    hr = int(datetime.now().hour)
    t = time.strftime("%I:%M:%p")
    day = cal_day()
    return f"it's {day} and the time is {t}"
def UpdateDate(data):
    for obj in data['intents']:
        if obj['tag'] == "datetime":
            obj['responses'][0] = GetDateAndTime()
            # print(obj)
    return data

with open("intents.json") as file:
    data = json.load(file)
    data = UpdateDate(data)
with open("intents.json", 'w') as F:
    json.dump(data, F, indent=4)


training_sentences = []
training_labels = []
labels = []
responses = []

for intent in data['intents']:
    for pattern in  intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])

    if intent['tag'] not in labels:
        labels.append(intent['tag'])

noOfClasses = len(labels)

print(noOfClasses)

labelEncoder = LabelEncoder()
labelEncoder.fit(training_labels)
training_labels = labelEncoder.transform(training_labels)

vocabSize = 1000
oov_token = "<OOV>"
max_len = 20
embeddingDim = 16
tokenizer = Tokenizer(num_words=vocabSize, oov_token=oov_token)
tokenizer.fit_on_texts(training_sentences)

wordIndex = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(training_sentences)
paddedSequences = pad_sequences(sequences, truncating='post', maxlen=max_len)

model = Sequential()
model.add(Embedding(vocabSize, embeddingDim, input_length=max_len))
model.add(GlobalAveragePooling1D())
model.add(Dense(16, activation="relu"))
model.add(Dense(16, activation="relu"))
model.add(Dense(noOfClasses, activation="softmax"))

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.summary()

history = model.fit(paddedSequences, np.array(training_labels), epochs=1000)

model.save("chat_model.h5")

with open("tokenizer.pki", "wb") as f:
    pickle.dump(tokenizer, f, protocol=pickle.HIGHEST_PROTOCOL)

with open("labelEncoder.pki", "wb") as EncoderFile:
    pickle.dump(labelEncoder, EncoderFile, protocol=pickle.HIGHEST_PROTOCOL)