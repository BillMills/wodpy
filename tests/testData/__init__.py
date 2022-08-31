import os.path

def sample_data(filename: str):
    """Gives the path to the sampling data"""
    TEST_DATA_PATH = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(TEST_DATA_PATH, filename) 


