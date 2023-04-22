from random import randint

angry_stickers = ['CAACAgIAAxkBAAIBEWQ8MAABVwkMtzDAy3fSRwOYXu_LJQACXwADTlzSKXaSHy8QpwgkLwQ'
                  , 'CAACAgIAAxkBAAIBB2Q8L4hlrkz5BEMa3OS5W-iYytexAAK6FgACi_oIStYglWIvKM6PLwQ'
                  , 'CAACAgIAAxkBAAIGumRCpq99YzCSN6W2U-az0FT6rUyNAAIMAQACVp29Cqpv9dJA3OI9LwQ'
                  , 'CAACAgIAAxkBAAIGvGRCpruHyK1GKVhlnHtTW3O_76NMAAKvAAPBnGAM0-8CGMFDHlMvBA'
                  , 'CAACAgIAAxkBAAIGwGRCptXxnyCOvZX5dfv942EPFOemAAI5DwACdrIpSvr8TNGlMJ1aLwQ'
                  , 'CAACAgIAAxkBAAIGwmRCpuz0fxCmo4hNgTHHbF3NTFHjAAKRAgACVp29ChPetSBAuAsiLwQ'
                  , 'CAACAgIAAxkBAAIGxGRCpve5aMUH5z7zysfqaHEaZkTmAAIvAAPBnGAMr4xEeO5l0YovBA']

def get_angry_sticker():
    return angry_stickers[randint(0, len(angry_stickers) - 1)]