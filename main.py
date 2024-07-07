

def main():
    config = load_config()

    if config['run_localhost']:
        print("Error: Running on localhost is not allowed.")
    else:
        
        print("Running on production environment.")

if __name__ == "__main__":
    main()