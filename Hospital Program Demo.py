print('''
Wellcome To Hospital Demo Patient List
Coded By: SaborRasoolipy
Github: https://www.github.com/saborrasoolipy
''')
Available_Service = ('''
                        Bathroom
                        24/7 Open
                        Pharmacy
                        ......
                        ....
                        ...
                        ..
                        .
                        
                        
''')
Available_doctors = ('''
                        Dr.Bashir Hussiani 
                        Dr.Rouhullah Majidi 
                        Dr........
                        .....
                        ....
                        ...
                        ..
                        .
                        (Etc)
''')
Ahmad_data = ('''
                                                Name : Ahmad 
                                                F/Name : Mahmoud
                                                Age  : 24 Years Old 
                                                Date of Birth : 2000/02/02
                                                Date of Comes in Hospital : 2024/01/01 
                                                Room Number : Room No. 54
                                                Type of Illness : Covid-19 
                                                Date of Out : Not Out
''')
print('''
                                                Services 
          1) Patient Check    2) Available Doctors (Available Soon)     3) Available Services (Available Soon)
 
''')
chosed_service = input('Chose a Service > ')
if chosed_service == '1':
    patient_name = input('Enter Name of Patient > ')
    if patient_name == 'Ahmad':
        print(Ahmad_data)
if chosed_service == '2':
    print(Available_doctors)
if chosed_service == '3':
    print(Available_Service)
else:
    print('''
 
Coded By Sabor Rasooli 
                                 S-----------------------------------R
                                 A-----------------------------------A
                                 B-----------------------------------S
                                 O-----------------------------------O
                                 R-----------------------------------O
                                 RasooliPY-----------------------------------LY    
''')