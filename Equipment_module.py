# Store & Manage  equipment records.

from Python_SQL_Connectivity_module import mycon, cur

def equipment_records():

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
            ei = input('Enter equipment id :')                                     # Equipment ID (Unique Identifier)
            en = input('Enter equipment name :')                                   # Equipment name
            q = int(input('Enter quantity :'))                                     # Quantity
            s = input('Enter size(small/medium/large) : ')                         # Size
            g = input('Enter graduated/ungraduated : ')                            # Graduation Status 
            c = int(input('Enter cost of one(1) equipment {must mention} :'))      # Cost per unit
            t = q*c                                                                # Total cost (quantity*cost per unit)
            cur.execute("insert into equipment(Equipment_ID, Equipment_name, quantity,size,Certification_Status,Cost_of_one_equipment,total_cost) values('{}','{}',{},'{}','{}',{},{})".format(ei,en,q,s,g,c,t))
            mycon.commit()
            print('INSERTION DONE!')

        elif ch==2:
            print('FOR DISPLAY :--')
            import tabulate as t
            a="select Equipment_ID, Equipment_name, quantity,size,Certification_Status,Cost_of_one_equipment,total_cost from equipment"
            cur.execute(a)
            data = cur.fetchall()                                                  # Fetch resultset from database
            if data is None:
                print("NO RECORDS AVAILABLE!!!!!")
            else:
                a="select Equipment_ID, Equipment_name, quantity,size,Certification_Status,Cost_of_one_equipment,total_cost from equipment"
                cur.execute(a)
                data=cur.fetchall()
                print('HERE ARE THE RECORDS :--')
                g=['Equipment ID','Equipment name','Quantity','Size','Certification Certification_Status','Cost of one equipment','Total cost']
                print(t.tabulate(data,headers=g,tablefmt="psql"))

        elif ch == 3:
            import tabulate as t
            print("FOR SEARCH :--")
            e = input('Enter equipment id:')                                       # Input from user
            a="select Equipment_ID, Equipment_name, quantity,size,Certification_Status,Cost_of_one_equipment,total_cost from equipment where Equipment_ID like '{}'".format(e)
            cur.execute(a)
            data = cur.fetchone()
            if data is None:
                print("NO RECORDS AVAILABLE!!!!!")
            else:
                a="select Equipment_ID, Equipment_name, quantity,size,Certification_Status,Cost_of_one_equipment,total_cost from equipment where Equipment_ID like '{}'".format(e)
                cur.execute(a)
                data=cur.fetchall()
                print('HERE ARE THE RECORDS :--')
                g=['Equipment ID','Equipment name','Quantity','Size','Certification Certification_Status','Cost of one equipment','Total cost']
                print(t.tabulate(data,headers=g,tablefmt="psql"))


        elif ch == 4:
            print('FOR DELETION:--')
            e = input('Enter equipment id:')
            a = "select * from equipment where Equipment_ID = '{}'".format(e)
            cur.execute(a)
            data = cur.fetchone()
            if data[0] == e :
                cur.execute("Delete from equipment where Equipment_ID like '{}'".format(e))
                mycon.commit()
                print('RECORD DELETED SUCCESSFULLY!')
            else:
                print("SORRY! CAN'T FIND YOUR RECORDS.")

        elif ch == 5:
            print(' '*178, 'Which record you wanna update')
            print(' '*178, '1. Equipment name')
            print(' '*178, '2. Quantity')
            print(' '*178, '3. Size')
            print(' '*178, '4. Certification Certification_Status')
            print(' '*178, '5. Cost of one equipment')
            print(' '*178, '6. Exit')
            ch = int(input('Enter choice:'))

            if ch == 1 :
                e = input('Enter equipment ID in which you want to update:')
                cur.execute("select Equipment_name from equipment where Equipment_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new Equipment_name for updation:')
                    cur.execute("update equipment set Equipment_name = '{}' where Equipment_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 2:
                e = input('Enter equipment ID in which you want to update:')
                cur.execute("select * from equipment where Equipment_ID like '{}'".format(e))
                trydata = cur.fetchone()
                c = trydata[5]
                cur.execute("select quantity from equipment where Equipment_ID like '{}'".format(e))
                data = cur.fetchone()
                if data is None:
                    print('WRONG ENTRY')
                else:
                    f = int(input('Enter new quantity for updation:'))
                    t = c*f
                    cur.execute("update equipment set quantity = {}, total_cost = {} where Equipment_ID like '{}'".format(f,t,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 3:
                e = input('Enter equipment ID in which you want to update:')
                cur.execute("select size from equipment where Equipment_ID like '{}'".format(e))
                data = cur.fetchone()
                if data is None:
                    print('WRONG ENTRY')
                else:
                    f = input('Enter new size for updation:')
                    cur.execute("update equipment set size = '{}' where Equipment_ID like '{}'".format(f,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 4:
                e = input('Enter equipment ID in which you want to update:')
                cur.execute("select Certification_Status from equipment where Equipment_ID like '{}'".format(e))
                data = cur.fetchone()
                if data is None:
                    print('WRONG ENTRY')
                else:
                    f = input('Enter new certification Certification_Status for updation:')
                    cur.execute("update equipment set Certification_Status = '{}' where Equipment_ID like '{}'".format(f,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 5:
                e = input('Enter equipment ID in which you want to update:')
                cur.execute("select * from equipment where Equipment_ID like '{}'".format(e))
                trydata = cur.fetchone()
                c = trydata[2]
                cur.execute("select Cost_of_one_equipment from equipment where Equipment_ID like '{}'".format(e))
                data = cur.fetchone()
                if data is None:
                    print('WRONG ENTRY')
                else:
                    f = int(input('Enter new cost of 1 equipment for updation:'))
                    t = f*c
                    cur.execute("update equipment set Cost_of_one_equipment = {},total_cost = {} where Equipment_ID like '{}'".format(f,t,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 6:
                print("THANKYOU !")
                print("VISIT AGAIN :) ")
                exit()

        elif ch == 6:
            print("THANKYOU !")
            print("VISIT AGAIN :) ")
            exit()

        else :
            print('INVALID CHOICE!')
            menu()

    except Exception as e:
        print('EXCEPTION! :' ,e)