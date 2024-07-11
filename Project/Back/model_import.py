import pickle
import os
class importer_model:

    @staticmethod
    def import_model():
        with open('./Project/Back/BD/random_forest_model.pkl', 'rb') as f:  # Replace 'model.pkl' with the actual filename
            model = pickle.load(f)
        return model



if __name__ == 'main':
    model = importer_model.import_model()
    print(type(model))