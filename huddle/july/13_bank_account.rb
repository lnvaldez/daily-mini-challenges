# 13. Cuenta bancaria: Implementa una clase CuentaBancaria con métodos para depositar y consultar el saldo.

class BankAccount
    def initialize 
        @balance = 0
    end 

    def deposit(amount)
        if amount > 0
            @balance += amount 
            puts "Deposited #{amount}. Current balance is #{@balance}."
        else 
            puts "Invalid deposit amount."
        end
    end 

    def check_balance()
        puts "Your balance is $#{@balance}."
    end
end 

account = BankAccount.new
account.deposit(100)
account.check_balance
account.deposit(100)
account.check_balance
