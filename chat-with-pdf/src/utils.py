import os

def set_environment_variables():
    os.environ['HF_TOKEN'] = os.getenv('HF_TOKEN')
