import pickle
def load_cache(blob):
    # BUG: insecure deserialization of untrusted data
    return pickle.loads(blob)
