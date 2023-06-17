
import sys

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

#Created global coin dictionary with a default value of 0
coins = {coin: 0 for coin in COIN_VALUES.keys()}

#Created global banknote dictionary with a default value of 0
banknotes = {note: 0 for note in BANKNOTE_VALUES.keys()}



def eliminate_zero(dict_remove):
    """ This funcitons creates a dictionary by appending items from
     argument(dictionary) that has a value that is not equal to zero"""
    dictt={}
    for i,j in dict_remove.items():
        if j!=0:
            dictt[i]=j
        else:
            pass
    return dictt


def load_coins(amount, coin_type):
    """ Loads the amount and coin type which updates the global 
        coin dictionary and return a formated output
    """
    if coin_type not in coins:
        return 'INVALID COIN'
    else:
        coins[coin_type] += amount
        results=eliminate_zero(coins)
        results=', '.join([f"{count} {value}£" for value, count in results.items()])
        print(f'= {results}')
    


def calculate_coins(banknote_amount):
    """ Converts the banknote amount into coin by considering 
    the available coins in the global coin dictionary"""
    
    update_coins=eliminate_zero(coins)
    
    coins_to_return = {}
    
    for coin_value in update_coins.keys():
        coin_count = update_coins[coin_value]
        coin_needed = int(banknote_amount / coin_value)
        coin_to_return = min(coin_count, coin_needed)
        
        coins_to_return[coin_value] = coin_to_return
        banknote_amount -= coin_value * coin_to_return

        if banknote_amount == 0:
            return coins_to_return
    return None
    
            


def exchange(banknote_amount):
    
    try:
        coin_return=calculate_coins(banknote_amount)
                
        for key, value in coins.items():
            if key in coin_return:
                coins[key]=value - coin_return[key] 
             
        #Eliminate items that have values equal to zero 
        update_coins=eliminate_zero(coins) 

        #Update the banknote global dictionary with a valid banknote 
        for i in banknotes.keys():
            if i==banknote_amount:
                banknotes[i]+=1
            

        #Eliminate items that have values equal to zero
        note_update=eliminate_zero(banknotes)

        #formating the output of the function
        update_coins_format=', '.join([f'{count} {value}£'for value, count in update_coins.items()])
        coin_return_format=', '.join([f'{count} {value}£'for value, count in coin_return.items()])
        note_update_format=', '.join([f'{count} {value}£'for value, count in note_update.items()])
        print(f"<{coin_return_format}")
        print(f'={update_coins_format}, {note_update_format}')
        
    except TypeError:
         #formating the output of the function
        print("<CANNOT EXCHANGE")
        update_coins=eliminate_zero(coins) 
        note_update=eliminate_zero(banknotes)

        update_coins_format=', '.join([f'{count} {value}£'for value, count in update_coins.items()])
        note_update_format=', '.join([f'{count} {value}£'for value, count in note_update.items()])

        print(f'={update_coins_format}, {note_update_format}')

    


def process_commands(filename):
    """ reads the filepath and interates each line extracts parameters and  words 
    like 'Load' and 'exchnage' that determines the functions that would be executed """
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

            else:
                result='INVALID FUNCTION'

        return result

def main():
        
    filename=sys.argv[1]
    process_commands(filename)

if __name__=="__main__":
    main()

