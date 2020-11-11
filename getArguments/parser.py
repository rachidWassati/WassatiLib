import argparse

def parser(**kwargs):
    parser = argparse.ArgumentParser()
    for key, value in kwargs.items():
        parser.add_argument('-' + str(key), '--' + str(value), required= True)

    return vars(parser.parse_args())
