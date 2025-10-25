# Store & Manage Chemical Claim records.

from Python_SQL_Connectivity_module import mycon, cur

def c_claim_records():

    try:
        print(' '*138 ,' MENU ' ,' '*98)
        print(' '*138 ,'1.  Insert' ,' '*98)
        print(' '*138 ,'2.  Display' ,' '*98)
        print(' '*138 ,'3.  Search' ,' '*98)
        print(' '*138 ,'4.  Delete' ,' '*98)
        print(' '*138 ,'5.  Update' ,' '*98)
        print(' '*138 ,'6.  Exit' ,' '*98)
        ch = int(input('Enter choice:'))

        if ch ==1 :
            print('FOR INSERTION :--')
            ci = input('Enter claim ID:')                                     # Chemical Claim records
            cd = input('Enter claim date:')                                   # Claim date 
            sn = input('Enter student name:')                                 # Student name 
            ei = input('Enter chemical ID:')                                  # Chemical ID
            eq = int(input('Enter quantity:'))                                # Quantity 
            a = "select cost_of_unit_chemical,common_name,formula from chemical where Chemical_ID = '{}'".format(ei)
            cur.execute(a)
            data = cur.fetchone()                                             # Fetched result set from database
            x = data[0]                                                       # Cost per unit 
            c = data[1]                                                       # Common name
            f = data[2]                                                       # Formula
            t = x*eq                                                          # Total cost (quantity*cost per unit)
            cur.execute("insert into c_claim(c_Chemical_ID,sname,c_date,Chemical_ID,common_name,formula,Chemical_Quantity,cost_of_unit_chemical,total_cost) values('{}','{}','{}','{}','{}','{}',{},{},{})".format(ci,sn,cd,ei,c,f,eq,x,t))
            mycon.commit()
            print('INSERTION DONE!')

        elif ch == 2:
            print()
            print('FOR DISPLAY :--')
            print()
            a="select c_Chemical_ID,sname,c_date,chemical.Chemical_ID,chemical.common_name,chemical.Boiling_or_Melting_point,chemical.formula,chemical.physical_state,Chemical_Quantity,chemical.cost_of_unit_chemical,Chemical_Quantity*chemical.cost_of_unit_chemical as totalcost from c_claim join chemical on c_claim.Chemical_ID = chemical.Chemical_ID"
            cur.execute(a)
            data = cur.fetchall()
            if data is None:
                print("NO RECORDS AVAILABLE!!!!!")
            else:
                for row in data:
                    print(' _ '*50)
                    print()
                    print('CHEMICAL CLAIM ID :  ',row[0])
                    print()
                    print('STUDENT NAME :  ',row[1])
                    print('CLAIM DATE :  ',row[2])
                    print('CHEMICAL ID :  ',row[3])
                    print('COMMON NAME :  ',row[4])
                    print('BOILING/MELTING POINT :   ',row[5])
                    print('FORMULA :  ',row[6])
                    print('PHYSICAL STATE :  ',row[7])
                    print('QUANTITY :  ',row[8])
                    print('COST OF UNIT CHEMICAL :  ',row[9],'Rs.')
                    print('TOTAL COST :  ',row[10],'Rs')
                    print()
                    print(' _ '*50)

        elif ch == 3:
            print('FOR SEARCH :-- ')
            e = input('Enter claim id:')
            a="select c_Chemical_ID,sname,c_date,chemical.Chemical_ID,chemical.common_name,chemical.Boiling_or_Melting_point,chemical.formula,chemical.physical_state,Chemical_Quantity,chemical.cost_of_unit_chemical,Chemical_Quantity*chemical.cost_of_unit_chemical as totalcost from c_claim join chemical on c_claim.Chemical_ID = chemical.Chemical_ID where c_Chemical_ID like '{}'".format(e)
            cur.execute(a)
            data = cur.fetchone()
            if data is None:
                print("NO RECORDS AVAILABLE!!!!!")
            else:
                a="select c_Chemical_ID,sname,c_date,chemical.Chemical_ID,chemical.common_name,chemical.Boiling_or_Melting_point,chemical.formula,chemical.physical_state,Chemical_Quantity,chemical.cost_of_unit_chemical,Chemical_Quantity*chemical.cost_of_unit_chemical as totalcost from c_claim join chemical on c_claim.Chemical_ID = chemical.Chemical_ID where c_Chemical_ID like '{}'".format(e)
                cur.execute(a)
                data=cur.fetchall()
                print('HERE ARE THE RECORDS :--')
                for row in data:
                    print(' _ '*50)
                    print()
                    print('CHEMICAL CLAIM ID :  ',row[0])
                    print()
                    print('STUDENT NAME :  ',row[1])
                    print('CLAIM DATE :  ',row[2])
                    print('CHEMICAL ID :  ',row[3])
                    print('COMMON NAME :  ',row[4])
                    print('BOILING/MELTING POINT :   ',row[5])
                    print('FORMULA :  ',row[6])
                    print('PHYSICAL STATE :  ',row[7])
                    print('QUANTITY :  ',row[8])
                    print('COST OF UNIT CHEMICAL :  ',row[9],'Rs.')
                    print('TOTAL COST :  ',row[10],'Rs')
                    print()
                    print(' _ '*50)

        elif ch == 4:
            print('FORM DELETION :--')
            e = input('Enter claim id:')
            a = "select * from c_claim where c_Chemical_ID = '{}'".format(e)
            cur.execute(a)
            data = cur.fetchone()
            if data[0] == e :
                cur.execute("Delete from c_claim where c_Chemical_ID like '{}'".format(e))
                mycon.commit()
                print('RECORD DELETED SUCCESSFULLY!')
            else:
                print("SORRY! CAN'T FIND YOUR RECORDS.")

        elif ch == 5:
            print('FOR UPDATION :--')
            print(' '*178, 'Which record you wanna update')
            print(' '*178, '1. claim date')
            print(' '*178, '2. student name')
            print(' '*178, '3. chemical id')
            print(' '*178, '4. quantity')
            print(' '*178, '5. Exit')
            ch = int(input('Enter choice:'))                                      # choice 

            if ch == 1:
                e = input('Enter claim ID in which you want to update:')
                cur.execute("select c_date from c_claim where c_Chemical_ID like '{}'".format(e))
                f = cur.fetchone()                                                # Fetched result set from database 
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new claim date for updation:')
                    cur.execute("update c_claim set c_date = '{}' where c_Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 2:
                e = input('Enter claim ID in which you want to update:')
                cur.execute("select sname from c_claim where c_Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new student name for updation:')
                    cur.execute("update c_claim set sname = '{}' where c_Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 3:
                e = input('Enter claim ID in which you want to update:')
                cur.execute("select Chemical_ID from c_claim where c_Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new chemical id for updation:')
                    cur.execute("update c_claim set Chemical_ID = '{}' where c_Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 4:
                e = input('Enter claim ID in which you want to update:')
                cur.execute("select Chemical_Quantity from c_claim where c_Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new quantity for updation:')
                    cur.execute("update c_claim set Chemical_Quantity = {} where c_Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 5:
                menu()

        elif ch == 6:
            menu()

        else :
            print('INVALID CHOICE!')
            menu()

    except Exception as e:
        print('EXCEPTION! :' ,e)

