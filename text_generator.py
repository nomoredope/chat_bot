import time
import random
from pathlib import Path
import pandas as pd


def rand_photo():
    photo = ['https://i.pinimg.com/736x/c5/3b/8e/c53b8efc3ebc0fa6df3455bddeb3a5d2.jpg',
             'https://i.pinimg.com/564x/2b/47/8f/2b478f068c6ee2295cb11aef8685d625.jpg',
             'https://i.pinimg.com/564x/48/ab/e0/48abe0c33d6c95f886816738219a5f32.jpg',
             'https://i.pinimg.com/564x/d5/d8/1d/d5d81d89f61ce7d4238ded3dd733281a.jpg',
             'https://i.pinimg.com/564x/94/f7/ad/94f7ad1598831a379164c0c519d2f87f.jpg',
             'https://i.pinimg.com/564x/38/bc/97/38bc9726373f611bd21b66dde7dbe290.jpg',
             'https://i.pinimg.com/564x/3a/4c/09/3a4c096c72d7466b557becc5ecb81f07.jpg',
             'https://i.pinimg.com/564x/bf/d1/8b/bfd18b5cfe3b7ab7e0e7ee005e60860c.jpg',
             'https://i.pinimg.com/564x/ad/aa/2e/adaa2eb9dbd76b9f7279829be15ad5a2.jpg',
             'https://i.pinimg.com/564x/66/e2/0f/66e20f25ea43bbf70410e288b6373b66.jpg',
             'https://i.pinimg.com/564x/44/d8/f8/44d8f812f86a42c84cff2b868bef5516.jpg',
             'https://i.pinimg.com/564x/91/fa/08/91fa0872ec685fe40bf7470988531cec.jpg',
             'https://i.pinimg.com/564x/9b/5a/da/9b5adabbe1b3a711bfaa44420bf9c435.jpg',
             'https://i.pinimg.com/474x/bb/9a/a0/bb9aa0fa35112dca07a7ec8bbf40e141.jpg',
             'https://i.pinimg.com/564x/90/66/7d/90667db202c1c8821758f2e0df248da0.jpg',
             'https://i.pinimg.com/564x/f3/a9/aa/f3a9aab85e6f7c2a48032db84998cb79.jpg']

    lengh = len(photo)
    rnd = random.randint(0, lengh)
    result_photo = photo[rnd]
    return result_photo


def text_gen(chat_id):
    temp_frame = pd.read_json(f'data/dict_data/dict_{chat_id}_db.json')
    rnd = random.randint(0, len(temp_frame)-1)
    text = temp_frame[rnd]
    text = text.to_dict()
    print(text)
    return text
