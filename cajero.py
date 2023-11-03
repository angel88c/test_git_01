import uuid
import random
from abc import ABC, abstractmethod

class Account():
    def __init__(self, name, father_last_name, mother_last_name, day, month, year,
                 gender, balance):
        self.id = f'{uuid.uuid4()}'
        self.name = name
        self.father_last_name = father_last_name
        self.mother_last_name = mother_last_name
        self.day = day
        self.month = month
        self.year = year
        self.gender = gender
        self.rfc = ''
        self.curp = ''
        self.balance = balance
        
        self.__get_rfc()
        self.__get_curp()

    def __get_random_alphanumeric(self, num_characters: int, option=None):
        XYZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890"
        if option is not None:
            if option == "alpha":
                XYZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if option == "numeric":
                XYZ = "01234567890"
                
        key = ""
        for i in range(num_characters):
            key += random.choice(XYZ)
        return key
        
    def __get_rfc(self):
        if not self.rfc:
            self.rfc += self.father_last_name[:2].upper()
            self.rfc += self.mother_last_name[:1].upper()
            self.rfc += self.name[:1].upper()
            self.rfc += f'{self.year:02d}'[-2:]
            self.rfc += f'{self.month:02d}'[:2]
            self.rfc += f'{self.day:02d}'[:2]
            self.rfc += self.__get_random_alphanumeric(3)

        return self.rfc
        
    def __get_curp(self):
        self.curp += self.father_last_name[:2].upper()
        self.curp += self.mother_last_name[:1].upper()
        self.curp += self.name[:1].upper()
        self.curp += f'{self.year:02d}'[-2:]
        self.curp += f'{self.month:02d}'[:2]
        self.curp += f'{self.day:02d}'[:2]
        self.curp += self.__get_random_alphanumeric(6, option="alpha")
        self.curp += self.__get_random_alphanumeric(2, option="numeric")
        
#Clase abstracta Cajero (Privada)
class ATM(ABC):
    
    def __init__(self) -> None:
        self._accounts = list()
        super().__init__()
    
    @abstractmethod
    def create_account(self, name: str, father_last_name: str, mother_last_name: str,
                       day: int, month: int, year: int, gender: str, balance: float):

        full_name = f'{name} {father_last_name} {mother_last_name}'
        account_found = False
        for account in self._accounts:
            account_full_name = f'{account.name} {account.father_last_name} {account.mother_last_name}'
            if full_name.lower() == account_full_name.lower():
                print(f"Account with name '{full_name}' already exists with id={account.id}")
                account_found = True

        if not account_found:
            new_account = Account(name, father_last_name, mother_last_name, 
                                       day, month, year, gender, balance)
            self._accounts.append(new_account)
    
    @abstractmethod
    def view_account(self, name: str, father_last_name: str, mother_last_name: str):
        full_name = f'{name} {father_last_name} {mother_last_name}'
        account_found = False
        for account in self._accounts:
            account_full_name = f'{account.name} {account.father_last_name} {account.mother_last_name}'
            if full_name.lower() == account_full_name.lower():
                print(f"Account for '{full_name}':")
                print(f'{"Id": >{20}}: {account.id}')
                print(f'{"Name": >{20}}: {account.name}')
                print(f'{"Father Last Name": >{20}}: {account.father_last_name}')
                print(f'{"Mother Last Name": >{20}}: {account.mother_last_name}')
                print(f'{"Day of Birdth": >{20}}: {account.day}')
                print(f'{"Month of Birdth": >{20}}: {account.month}')
                print(f'{"Year of Birdth": >{20}}: {account.year}')
                print(f'{"RFC": >{20}}: {account.rfc}')
                print(f'{"CURP": >{20}}: {account.curp}')
                print(f'{"Balance": >{20}}: {account.balance}')
                print(f'')
                account_found = True

        if not account_found:
            print(f"Account with name '{full_name}' Not Found in database.")
                
    @abstractmethod
    def delete_account(self, name: str, father_last_name: str, mother_last_name: str):
        full_name = f'{name} {father_last_name} {mother_last_name}'
        account_found = False
        for index, account in enumerate(self._accounts):
            account_full_name = f'{account.name} {account.father_last_name} {account.mother_last_name}'
            if full_name.lower() == account_full_name.lower():
                self._accounts.pop(index)
                print(f"Account with name '{full_name}' Was deleted.")
                account_found = True
                break
            
        if not account_found:
            print(f"Account with name '{full_name}' Not Found in database.")
            
    @abstractmethod
    def deposit(self, name: str, father_last_name: str, mother_last_name: str, amount: float):
        full_name = f'{name} {father_last_name} {mother_last_name}'
        account_found = False
        for account in self._accounts:
            account_full_name = f'{account.name} {account.father_last_name} {account.mother_last_name}'
            if full_name.lower() == account_full_name.lower():
                if (amount + account.balance) > 8000:
                    amount_exceeded = (amount + account.balance) - 8000
                    print(f"Maximum to balance is $8000 for Account with name '{full_name}', amount exceeded by ${amount_exceeded}")
                else:
                    account.balance += amount
                    
                account_found = True
                break
            
        if not account_found:
            print(f"Account with name '{full_name}' Not Found in database.")
    
    @abstractmethod
    def withdraw(self, name: str, father_last_name: str, mother_last_name: str, amount: float):
        full_name = f'{name} {father_last_name} {mother_last_name}'
        account_found = False
        for account in self._accounts:
            account_full_name = f'{account.name} {account.father_last_name} {account.mother_last_name}'
            if full_name.lower() == account_full_name.lower():
                if (amount > account.balance):
                    print(f"Account with name '{full_name}' Doesn't have enough balance to withdraw.")
                else:
                    account.balance -= amount
                account_found = True
                break
            
        if not account_found:
            print(f"Account with name '{full_name}' Not Found in database.")

#Clase Practicaja
class Practicaja(ATM):
    
    #def __init__(self):
    #    self._accounts = {}
    
    def create_account(self, name: str, father_name: str, mother_name: str, day: int, month: int, year: int, gender: str, balance: float):
        return super().create_account(name, father_name, mother_name, day, month, year, gender, balance)    
    
    def view_account(self, name: str, father_last_name: str, mother_last_name: str):
        return super().view_account(name, father_last_name, mother_last_name)
    
    def delete_account(self, name: str, father_last_name: str, mother_last_name: str):
        return super().delete_account(name, father_last_name, mother_last_name)
    
    def deposit(self, name: str, father_last_name: str, mother_last_name: str, amount: float):
        return super().deposit(name, father_last_name, mother_last_name, amount)
    
    def withdraw(self, name: str, father_last_name: str, mother_last_name: str, amount: float):
        return super().withdraw(name, father_last_name, mother_last_name, amount)
    
    def save_all_accounts(self):
        if self._accounts:
            with open("final_accounts.txt", mode='a') as file:
                for account in self._accounts:
                    account_full_name = f'{account.name} {account.father_last_name} {account.mother_last_name}'
                    file.write(f"Account for '{account_full_name}':\n")
                    file.write(f'{"Id": >{20}}: {account.id}\n')
                    file.write(f'{"Name": >{20}}: {account.name}\n')
                    file.write(f'{"Father Last Name": >{20}}: {account.father_last_name}\n')
                    file.write(f'{"Mother Last Name": >{20}}: {account.mother_last_name}\n')
                    file.write(f'{"Day of Birdth": >{20}}: {account.day}\n')
                    file.write(f'{"Month of Birdth": >{20}}: {account.month}\n')
                    file.write(f'{"Year of Birdth": >{20}}: {account.year}\n')
                    file.write(f'{"RFC": >{20}}: {account.rfc}\n')
                    file.write(f'{"CURP": >{20}}: {account.curp}\n')
                    file.write(f'{"Balance": >{20}}: {account.balance}\n')
                    file.write(f'\n')
        else:
            print("No Acconts to Save")

practicaja = Practicaja()
practicaja.create_account("Juanito", "Perez", "Lopez", 10, 12, 1967, "H", 1500)
practicaja.create_account("Maria", "Estrada", "Ochoa", 6, 6, 1992, "M", 2500)
practicaja.create_account("Astrid", "Peña", "Gallardo", 13, 1, 1984, "M", 3000)
practicaja.create_account("Daniela", "Lopez", "Cruz", 5, 3, 1970, "M", 7000)
practicaja.create_account("Joaquin", "Diaz", "Perez", 21, 3, 2001, "H", 4500)

practicaja.view_account("Joaquin", "Diaz", "Perez")
practicaja.view_account("Maria", "Estrada", "Ochoa")

practicaja.delete_account("Joaquin", "Diaz", "Perez")

#These accounts don't exist
practicaja.view_account("Joaquin", "Diaz", "Perez")
practicaja.view_account("Everardo", "Rodriguez", "Ambriz")

practicaja.deposit("Maria", "Estrada", "Ochoa", 6500)
practicaja.view_account("Maria", "Estrada", "Ochoa")

practicaja.withdraw("Maria", "Estrada", "Ochoa", 2600)
practicaja.view_account("Maria", "Estrada", "Ochoa")

#Save all accounts in txt file
practicaja.save_all_accounts()
