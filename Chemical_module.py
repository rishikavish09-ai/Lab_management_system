# Store & Manage Chemical records.

from Python_SQL_Connectivity_module import mycon, cur

def chemical_records():

    try:
        print(' '*138 ,' MENU ' ,' '*98)
        print(' '*138 ,'1.  Insert' ,' '*98)
        print(' '*138 ,'2.  Display' ,' '*98)
        print(' '*138 ,'3.  Search' ,' '*98)
        print(' '*138 ,'4.  Delete' ,' '*98)
        print(' '*138 ,'5.  Update' ,' '*98)
        print(' '*138 ,'6.  Exit' ,' '*98)
        ch = int(input('Enter choice:'))                                          # Choice 

        if ch ==1 :
            print('FOR INSERTION :--')
            ci = input('Enter chemical id :')                                     # Chemical ID (Unique Identifier)
            cn = input('Enter common name:')                                      # Common name 
            i = input('Enter IUPAC name:')                                        # IUPAC name 
            f = input('Enter formula:')                                           # Formula 
            p = input('Enter physical state:')                                    # Physical state 
            t = input('Enter melting/boiling point:')                             # Boiling or melting point
            h = input('Enter hazzards :')                                         # Hazzards or safety info
            e = input('Enter expiry date:')                                       # Expiry date 
            q = int(input('Enter quantity (in ml/l):'))                           # Quantity 
            c = int(input('Enter cost of unit chemical NOTE :- IN SAME UNIT AS YOU WRITE IN QUANTITY {must mention} :'))                                     # Cost per unit
            tc = q*c                                                              # Total cost (quantity*cost per unit)
            cur.execute("insert into chemical(Chemical_ID,common_name,IUPAC_name,formula,physical_state,Boiling_or_Melting_point,hazzards,expiry_date,quantity,cost_of_unit_chemical,total_cost) values('{}','{}','{}','{}','{}','{}','{}','{}',{},{},{})".format(ci,cn,i,f,p,t,h,e,q,c,tc))
            mycon.commit()
            print('INSERTION DONE!')

        elif ch == 2 :
            print('FOR DISPLAY :--')
            import tabulate as t
            a="select * from chemical"
            cur.execute(a)
            data = cur.fetchall()                                                  # Fetched result set from database 
            if data is None:
                print("NO RECORDS AVAILABLE!!!!!")
            else:
                a="select * from chemical"
                cur.execute(a)
                data=cur.fetchall()
                print('HERE ARE THE RECORDS :--')
                g=['chemical ID', 'common name','IUPAC name','formula','physical state','boiling/melting point','hazzards','expiry date','Quantity','Cost of unit chemical','Total cost']
                print(t.tabulate(data,headers=g,tablefmt="psql"))

        elif ch == 3:
            import tabulate as t
            print("FOR SEARCH :--")
            e = input('Enter chemical id:')
            a="select * from chemical"
            cur.execute(a)
            data = cur.fetchone()
            if data is None:
                print("NO RECORDS AVAILABLE!!!!!")
            else:
                a="select * from chemical"
                cur.execute(a)
                data=cur.fetchall()
                print('HERE ARE THE RECORDS :--')
                g=['chemical ID', 'common name','IUPAC name','formula','physical state','boiling/melting point','hazzards','expiry date','Quantity','Cost of unit chemical','Total cost']
                print(t.tabulate(data,headers=g,tablefmt="psql"))

        elif ch == 4:
            print('FOR DELETION')
            e = input('Enter chemical id:')
            a = "select * from chemical where Chemical_ID = '{}'".format(e)
            cur.execute(a)
            data = cur.fetchone()
            if data[0] == e :
                cur.execute("Delete from chemical where Chemical_ID like '{}'".format(e))
                mycon.commit()
                print('RECORD DELETED SUCCESSFULLY!')
            else:
                print("SORRY! CAN'T FIND YOUR RECORDS.")

        elif ch == 5:
            print(' '*178, 'WHICH RECORD YOU WANNA UPDATE :--')
            print(' '*178, '1. Common name')
            print(' '*178, '2. IUPAC name')
            print(' '*178, '3. Formula')
            print(' '*178, '4. Physical state')
            print(' '*178, '5. Boiling/Melting point')
            print(' '*178, '6. Hazzards')
            print(' '*178, '7. Expiry date')
            print(' '*178, '8. Quantity')
            print(' '*178, '9. Cost of unit chemical')
            print(' '*178, '10. Exit')
            ch = int(input('Enter choice:'))

            if ch == 1 :
                e = input('Enter chemical ID in which you want to update:')
                cur.execute("select common_name from chemical where Chemical_ID like '{}'".format(e))
                f = cur.fetchone()                                               # Fetched result set from database
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new common_name for updation:')
                    cur.execute("update chemical set common_name = '{}' where Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 2 :
                e = input('Enter chemical ID in which you want to update:')
                cur.execute("select IUPAC_name from chemical where Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new IUPAC_name for updation:')
                    cur.execute("update chemical set IUPAC_name = '{}' where Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 3 :
                e = input('Enter chemical ID in which you want to update:')
                cur.execute("select formula from chemical where Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new formula for updation:')
                    cur.execute("update chemical set formula = '{}' where Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 4 :
                e = input('Enter chemical ID in which you want to update:')
                cur.execute("select physical_state from chemical where Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new physical_state for updation:')
                    cur.execute("update chemical set physical_state = '{}' where Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 5 :
                e = input('Enter chemical ID in which you want to update:')
                cur.execute("select Boiling_or_Melting_point from chemical where Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new Boiling_or_Melting_point for updation:')
                    cur.execute("update chemical set Boiling_or_Melting_point = '{}' where Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 6 :
                e = input('Enter chemical ID in which you want to update:')
                cur.execute("select hazzards from chemical where Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new hazzards for updation:')
                    cur.execute("update chemical set hazzards = '{}' where Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 7 :
                e = input('Enter chemical ID in which you want to update:')
                cur.execute("select expiry_date from chemical where Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new expiry_date for updation:')
                    cur.execute("update chemical set expiry_date = '{}' where Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 8:
                e = input('Enter chemical ID in which you want to update:')
                cur.execute("select cost_of_unit_chemical from chemical where Chemical_ID like '{}'".format(e))
                trydata = cur.fetchone()
                c = trydata[0]
                cur.execute("select quantity from chemical where Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = int(input('Enter new quantity for updation:'))
                    t = n*c
                    cur.execute("update chemical set quantity = {}, total_cost = {} where Chemical_ID like '{}'".format(n,t,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 9:
                e = input('Enter chemical ID in which you want to update:')
                cur.execute("select quantity from chemical where Chemical_ID like '{}'".format(e))
                trydata = cur.fetchone()
                c = trydata[0]
                cur.execute("select cost_of_unit_chemical from chemical where Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = int(input('Enter new cost of unit chemical for updation:'))
                    t = n*c
                    cur.execute("update chemical set cost_of_unit_chemical = {}, total_cost = {}  where Chemical_ID like '{}'".format(n,t,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 10:
                print("THANKYOU !")
                print("VISIT AGAIN :) ")
                exit()

            else:
                print('INVALID CHOICE!')
                menu()

        elif ch == 6:
            print("THANKYOU !")
            print("VISIT AGAIN :) ")
            exit()

        else :
            print('INVALID CHOICE!')
            menu()

    except Exception as e:
        print('EXCEPTION! :' ,e)