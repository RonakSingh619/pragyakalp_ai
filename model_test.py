import json
import pickle
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
import numpy as np

with open("intents.json") as file:
    data = json.load(file)

model = load_model("chat_model.h5")

with open("tokenizer.pki", "rb") as f:
    tokenizer = pickle.load(f)

with open("labelEncoder.pki", "rb") as encoderFile:
    labelEncoder = pickle.load(encoderFile)


while True:
    inputText = input("Enter something: ")
    padded = pad_sequences(tokenizer.texts_to_sequences([inputText]), maxlen=20, truncating='post')
    result = model.predict(padded)
    tag = labelEncoder.inverse_transform([np.argmax(result)])

    for i in data["intents"]:
        if i['tag'] == tag:
            print(np.random.choice(i['responses']))