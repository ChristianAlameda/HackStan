import string
import time
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Download NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Preprocess data
def preprocess(data):
    # Tokenize data
    tokens = nltk.word_tokenize(data)

    # Lowercase all words
    tokens = [word.lower() for word in tokens]

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]

    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens

def loadDataset(filename):
    # Load data
    with open(filename, 'r') as f:
        raw_data = f.read()

    # Preprocess data
    processed_data = [preprocess(qa) for qa in raw_data.split('\n')]
    return processed_data

processed_data = loadDataset('bot/dictionary.csv')

print("Devices Available: ", len(tf.config.list_physical_devices()), '\n', tf.config.list_physical_devices())

modelName = 'bot/chatbotModel.keras' # location and name

vocab_size = 5000
embedding_dim = 64
max_length = 100
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"
training_size = len(processed_data)
tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)

def saveModel(model):
        """Saves the model to a file using the name provided in self.__modelFilename
        """
        try:
            # model.summary()
            model.save(modelName)
            print(str(time.ctime())+' - Saved model as '+modelName)
        except:
            print(str(time.ctime())+' - Could not save '+modelName)

def buildModel():
    """Reads a model from file using the name provided in self.__modelFilename
    """
    try:
        # Load and Train
        model = tf.keras.models.load_model(modelName)
        #model.summary()
        
        # Train model
        num_epochs = 50
        history = model.fit(training_data, training_labels, epochs=num_epochs, verbose=2)
        saveModel(model)
        return model
    except:
        # Build and training

        # Set parameters
        vocab_size = 5000
        embedding_dim = 64
        max_length = 100
        trunc_type='post'
        padding_type='post'
        oov_tok = "<OOV>"
        training_size = len(processed_data)

        # Create tokenizer
        tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
        tokenizer.fit_on_texts(processed_data)
        word_index = tokenizer.word_index

        # Create sequences
        sequences = tokenizer.texts_to_sequences(processed_data)
        padded_sequences = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

        # Create training data
        training_data = padded_sequences[:training_size]
        training_labels = padded_sequences[:training_size, 0]

        # Build model
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Conv1D(64, 5, activation='relu'),
            tf.keras.layers.MaxPooling1D(pool_size=4),
            tf.keras.layers.LSTM(64),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(vocab_size, activation='softmax')
        ])

        # Compile model
        model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        # Train model
        num_epochs = 50
        history = model.fit(training_data, training_labels, epochs=num_epochs, verbose=2)
        saveModel(model)
        return model

model = buildModel()

# Define function to predict answer
def predict_answer(model, tokenizer, question):
    # Preprocess question
    question = preprocess(question)
    # Convert question to sequence
    sequence = tokenizer.texts_to_sequences([question])
    # Pad sequence
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    # Predict answer
    pred = model.predict(padded_sequence)[0]
    # Get index of highest probability
    idx = np.argmax(pred)
    # Get answer
    answer = tokenizer.index_word[idx]
    return answer

# Start chatbot
while True:
    question = input('You: ')
    answer = predict_answer(model, tokenizer, question)
    print('Chatbot:', answer)

