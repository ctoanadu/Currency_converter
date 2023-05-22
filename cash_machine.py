COIN_VALUES = {
    0.20: '0.20£',
    0.50: '0.50£',
    1: '1£',
    2: '2£'
}

BANKNOTE_VALUES = {
    5: '5£',
    10: '10£',
    20: '20£'
}


coins = {value: 0 for value in COIN_VALUES}
banknotes = {value: 0 for value in BANKNOTE_VALUES}



def eliminate_zero(dict_remove):
    dictt={}
    for i,j in dict_remove.items():
        if j!=0:
            dictt[i]=j
        else:
            pass
    return dictt


def load_coins(amount, coin_type):
    if coin_type not in coins:
        
        return 'INVALID COIN'
    else:
        coins[coin_type] += amount
        results=eliminate_zero(coins)
        results=', '.join([f"{count} {value}£" for value, count in results.items()])
        print(f'= {results}')
    


def calculate_coins(banknote_amount):
    

    update_coins=eliminate_zero(coins)
    target_value = banknote_amount
    coins_to_return = {}
    
    for coin_value in sorted(update_coins.keys()):
        coin_count = update_coins[coin_value]
        coin_needed = int(target_value // coin_value)
        coin_to_return = min(coin_count, coin_needed)
        
        if coin_to_return > 0:
            coins_to_return[coin_value] = coin_to_return
            target_value -= coin_value * coin_to_return

        if target_value == 0:
            return coins_to_return
    if coins_to_return=={}:
        return 'CANNOT EXCHANGE'
            

    return None



def exchange(banknote_amount):
    
    try:
        coin_return=calculate_coins(banknote_amount)
                
        for key, value in coins.items():
            if key in coin_return:
                coins[key]=value - coin_return[key] 
            else:
                pass
            
        update_coins=eliminate_zero(coins) 
         

        for i in banknotes.keys():
            if i==banknote_amount:
                banknotes[i]+=1
            else:
                pass 

        note_update=eliminate_zero(banknotes)

        update_coins_format=', '.join([f'{count} {value}£'for value, count in update_coins.items()])
        coin_return_format=', '.join([f'{count} {value}£'for value, count in coin_return.items()])
        note_update_format=', '.join([f'{count} {value}£'for value, count in note_update.items()])
        print(f"<{coin_return_format}")
        print(f'={update_coins_format}, {note_update_format}')
        
    except TypeError:
        print("<CANNOT EXCHANGE")
    


def process_commands(filename):
    with open(filename, 'r') as file:
        for line in file:
            command = line.strip().split(' ')
            print(f">{line.strip()}")

            if command[0] == 'LOAD':
                amount = int(command[1])
                coin_type = float(command[2])
                result=load_coins(amount, coin_type)
                
                
            elif command[0] == 'EXCHANGE':
                banknote_amount = int(command[1])
                result = exchange(banknote_amount)

        return result

if __name__=="__main__":
    
    process_commands("input.txt")
