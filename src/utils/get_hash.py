import hashlib


def get_hash[hashed_str](user_id: str | int) -> hashed_str:
    if isinstance(user_id, int):
        user_id = str(user_id)
    hash_object = hashlib.sha256(user_id.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig[:6]
