submit='N'
is_loop_exit='N'
account_number = []
start_number=1
trans_account=[]
trans_number=1

def switch_option(operation):
    global is_loop_exit
    if operation==1:
         create_account(submit)
    elif operation==2:
         number=int(input("enter your number"))
         display_account(account_number,number)
    elif operation ==3:
         transaction_account()   
    elif operation==4:
         payment_history()   
    elif operation==0:
         is_loop_exit='X'
         print("Exit....")   
    else:
        print("Invalid operation")
        
         



def create_account(submit):
    
    global account_number
    global start_number
    
    
    with open("Creating_account.txt","r") as file:
       account_info=file.readlines()
    if account_info:   
       last_account_line = account_info[-1].strip()  
       last_account_number = last_account_line.split(",")[0] 
       account_index=int(last_account_number)
                    
       print(f"Last account number:{last_account_number}")
                    
    else:
       account_index=0
      
    while submit=='N':
         print("For creating account Enter your details")
         name=input("Enter your name:")
         dob=input("Enter your date of birth[DD-MM-YY]:")
         phn=int(input("Enter your phone number:"))
         deposit=int(input("Enter your initial money"))
         submit=input("Enter Y to submit:")
       
         if submit == 'Y':
             
                 
                
             
                current_account_number= str(account_index+start_number)
               
                account_info=f"{current_account_number},{name},{dob},{phn},{deposit}"
                 
                with open("Creating_account.txt","a")as file:
                  file.write(account_info + "\n")
                print("Details saved in bank detail.txt")
                print("-----------Bank details--------")
                print(account_info)
                account_number.append(current_account_number)
                account_index +=1
               
         else:
             
             print("Account creation cancelled..try again")  
             
             
             
             
             
             
             
def display_account(account_number,number):
    
    
    
    
    
    with open("Creating_account.txt","r") as file:
             account_info=file.readlines()
             
             print(account_info)
             for info in account_info:
                 info_item=info.strip().split(',')
                 
                 
                 if str(number) == info_item[0]:
                    print("=============================")
                    print("account details ")
                    print("=============================")
                    print("Account number :",info_item[0])
                    print("Account name   :",info_item[1])    
                    print("Date of birth  :",info_item[2])  
                    print("Phone number   :",info_item[3])
                    print("Bank balance   :",info_item[4])
                    print("-----------------------------")
                
import time            
def transaction_account():
    global trans_number
    global trans_account
    
    with open("Creating_account.txt","r") as file:
             account_info=file.readlines()
             
    
    debit_number=int(input ("Enter your debit account number:")) 
    debit_found=False       
    for line in account_info:
        info_item=line.strip().split(',')
        
        if debit_number==int(info_item[0]):
           debit_found=True 
           debit_balance=int(info_item[4])
           
           print("Account name             :",info_item[1])  
           print("You current Bank balance :",debit_balance)
           
           benificiary_no=int(input("Enter your beneficiary account number:"))
           benificiary_found=False
           
           
           for ben_line in account_info:
               ben_info=ben_line.strip().split(',')
               
               if benificiary_no==int(ben_info[0]):
                   benificiary_found=True
                   
                   ben_amount=int(input("Enter amount:"))
                   narrative=input("Add narrative:")
                  
                   if ben_amount<=debit_balance:
                       
                         with open("Transaction_detail.txt","r")as file:
                             all_transaction=file.readlines()
                                     
                             if all_transaction:   
                                last_trans_line = all_transaction[-1].strip()  
                                last_trans_id = last_trans_line.split(',')[0]
                                last_trans_number=int(last_trans_id[6])
                                trans_index=last_trans_number+1
                                
                                
                             else:
                                trans_index=trans_number
                             
                         trans_id=f"TRF000{trans_index}"
                         current_date=time.strftime("%Y-%m-%d", time.localtime())
                         current_time=time.strftime("%H:%M:%S",time.localtime())
                         
                         
                         transaction_info=f"{trans_id},{debit_number},{benificiary_no},{ben_amount},{current_date},{current_time},{narrative}"
                         
                         print(transaction_info)
                         with open("Transaction_detail.txt","a")as file:
                            file.write(transaction_info + "\n")
                            
                         print("------Transaction details are successfully saved in text file----")   
                             

                         
                         
                         current_update_debit,current_update_credit=balance(account_info,debit_number,benificiary_no,ben_amount,debit_balance,ben_info)  
                        
                         
                         trans_debit=f"{trans_id},{debit_number},{benificiary_no}, Debit,-{ben_amount},{current_date},{current_time},{current_update_debit},{narrative}"
                         trans_credit=f"{trans_id},{benificiary_no},{debit_number}, Credit,+{ben_amount},{current_date},{current_time},{current_update_credit},{narrative}"
                         print("list",trans_debit)
                         print("list",trans_debit)
                         with open("payment_details.txt","a")as file:
                             file.write(trans_debit +"\n")
                             file.write(trans_credit +"\n")
                                 
                         
                                     
                         
                             
                                      
                         trans_list=transaction_info.split(',')   
                         print("|------Transaction details-----------------|")    
                         print(f"|Transaction I'd           :{trans_list[0]}")
                         print(f"|Debit account number      :{trans_list[1]}") 
                         print(f"|Benificiary account number:{trans_list[2]}")
                         print(f"|Credit amount             :{trans_list[3]}")
                         print(f"|Date                      :{trans_list[4]}")
                         print(f"|Time                      :{trans_list[5]}")
                         print(f"|Notes                     :{trans_list[6]}")      
                         print("--------------------------------------------")
                             
                   else:
                      print("insufficient bank balance") 
                   break 
                   
           if not benificiary_found:  
              print("This beneficiary account number is not existing...")  
               
    if not debit_found:   
        print("invalid account number")    
        
        
def balance(account_info,debit_number,benificiary_no,ben_amount,debit_balance,ben_info):
          
         
                         updated_lines=[]        
                         update_debit=debit_balance-ben_amount
                    
                         update_credit=int(ben_info[4])+ben_amount
                         
                         current_update_debit=str(update_debit)
                         current_update_credit=str(update_credit)
                         
                         
                         
                         
                         
                         for line in account_info:
                             info_item=line.strip().split(',')
                             
                             
                                 
                             
                             
                             if int(info_item[0])==debit_number:
                                  
                                  info_item[4]=current_update_debit
                                  
                             elif int(info_item[0])==benificiary_no:
                                  
                                  info_item[4]=current_update_credit
                                  
                             updated_line=','.join(info_item)
                             updated_lines.append(updated_line +'\n')  
                             
                            
                         with open("Creating_account.txt", "w") as file:
                                    file.writelines(updated_lines)
                                    

                         return current_update_debit, current_update_credit           
                                 
                             

                         
                         
      
             
def get_date_from_user(prompt):
    while True:
        user_input = input(prompt)
        
        
        if len(user_input) == 10 and user_input[4] == '-' and user_input[7] == '-':
            return user_input  
        else:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            

def payment_history():
    
    with open("payment_details.txt", "r") as file:
        transactions = file.readlines()
        for line in transactions:
            trans=line.strip().split(',')
            

    number = input("Enter your account number: ")
    from_date = get_date_from_user("Enter From date (YYYY-MM-DD): ")
    to_date = get_date_from_user("Enter To date (YYYY-MM-DD): ")

    found_trans = False
    account_found = False
    account_info = []
    current_balance=[]

    
    with open("Creating_account.txt", "r") as file:
        account_info = file.readlines()
        for line in account_info:
                                
            info_item = line.strip().split(',')
            account_info=info_item
            
            if int(number) == int(info_item[0]):
              account_found = True
                
              break  

    if not account_found:
        print("Account number not found.")
        return
    
    report_line=report_file(account_info,transactions,number,from_date,to_date)


    full_reports= "\n".join(report_line)
    with  open("Transaction_report","w")as file:
            file.write(full_reports)
           
    with  open("Transaction_report","r")as file:
            full_reports=file.readlines()
            for line in full_reports:
                statement=line.strip().split(',')
                print(statement)
        
    
def report_file(account_info,transactions,number,from_date,to_date):
    report_line=[]
    report_line.append("|============================================================================================\n")
    report_line.append(f"| Bank details               Your details                          | Statement period         |")
    report_line.append(f"|============================================================================================|")
    report_line.append(f"| {'Indian Bank':<12} |      {account_info[0]:<12}                          | {from_date:>5} - {to_date:>6}      |")
    report_line.append(f"| {'pasur':<12}       |      {account_info[1]:<12}  |                                              ")
    report_line.append(f"| {'Annur':<12}       |      {account_info[2]:<12}  |                                                   ")
    report_line.append(f"| {'coimbatore':<12}  |      {account_info[3]:<12}  |                                               ")
    report_line.append(f"|=============================================================================================|")
    report_line.append(f"{'Date':>10}     | {'Transaction Id':>15} | {'Narrative':>15} | {'Type':>10} | {'Amount':>10}  | {'Balance':<10} |")
    report_line.append("|=============================================================================================")




    found_trans=False    

    for line in transactions:  
             
             info = line.strip().split(',')
            
             trans_from = info[5]  
             account_num = info[1]
        

             if int(number) == int(account_num) and from_date <= trans_from <= to_date:
                found_trans = True
                
                transaction_id = info[0]  
            
                transaction_type = info[3] 
                amount=info[4]
                account_number=account_info[0]
                balance=info[7]
                narrative=info[8]
                
    
            
    
            
            
                report_line.append(f"{trans_from:>10} | {account_number}||{transaction_id:>15} |{narrative}|{transaction_type:>10} | {amount:>10} |{balance}|")
                
    if not found_trans:
        print("No transactions found for the given account number and date range.")


    return report_line


    

            
            


while is_loop_exit=='N':
    
     operation=int(input("     \n 1.Create account[enter y for submit],\n      2.display account details,\n      3.Transfer money,\n      4.payment details,\n      0.exit\n Enter your choice:"))
     switch_option(operation)