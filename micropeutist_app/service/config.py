import configparser

def config(filename='db.ini', section='MySQL'):
    '''read db.ini file and return configuration parameters as dictionary'''
    parser = configparser.ConfigParser()
    parser.read(filename)

    db={}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} not found in the {filename} file.")
    
    return db
