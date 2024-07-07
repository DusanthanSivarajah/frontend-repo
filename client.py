import yaml
class Client:

    def load_config(file_path='config.yaml'):
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config


    config = load_config()


    if config['run_localhost']:
        print("Error: Running on localhost is not allowed.")