import os
import joblib

# controller/ folder
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# backend/ folder (one level up from controller/)
BACKEND_DIR = os.path.dirname(CURRENT_DIR)

# stroke_model.pkl inside backend/
MODEL_PATH = os.path.join(BACKEND_DIR, "stroke_model.pkl")


def load_model():
    """
    Load the trained stroke model from stroke_model.pkl.
    Raises FileNotFoundError if the file does not exist.
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file not found at {MODEL_PATH}. Please train the model first."
        )

    model = joblib.load(MODEL_PATH)
    return model





