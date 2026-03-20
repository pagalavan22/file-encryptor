import os
import random

def shred_file(filepath):
    """
    Securely delete a file by overwriting it
    with random data 3 times before deleting.
    """
    try:
        size = os.path.getsize(filepath)

        with open(filepath, "wb") as f:
            for _ in range(3):
                f.write(os.urandom(size))
                f.flush()
                os.fsync(f.fileno())

        os.remove(filepath)
        return True
    except Exception as e:
        print(f"  Shred error: {e}")
        return False