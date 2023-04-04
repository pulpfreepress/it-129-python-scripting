"""Demonstrates JSON Encoding and Decoding.
"""
import json

def main():
    classes = {}
    classes['it-129'] = ['Jose', 'Sammy', 'Kristian']
    classes['it-566'] = ['Jeff', 'Sapna', 'Coralie']
    
    print(classes)
    print(json.dumps(classes))

if __name__ == '__main__':
    main()