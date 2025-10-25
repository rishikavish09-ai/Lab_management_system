# Store & Manage Equipment Claim records.

from Python_SQL_Connectivity_module import mycon, cur

def e_claim_records():

    try:
        print(' '*138 ,' MENU ' ,' '*98)
        print(' '*138 ,'1.  Insert' ,' '*98)
        print(' '*138 ,'2.  Display' ,' '*98)
        print(' '*138 ,'3.  Search' ,' '*98)
        print(' '*138 ,'4.  Delete' ,' '*98)
        print(' '*138 ,'5.  Update' ,' '*98)
        print(' '*138 ,'6.  Exit' ,' '*98)
        ch = int(input('Enter choice:'))                                      # Choice

        if ch ==1 :
            print('FOR INSERTION :--')
            ci = input('Enter claim ID:')                                     # Equipment Cliam ID (unique Identifier)
            cd = input('Enter claim date:')                                   # Claim date 
            sn = input('Enter student name:')                                 # Student name
            ei = input('Enter equipment ID:')                                 # Equipment ID
            eq = int(input('Enter quantity:'))                                # Quantity 
            a = "select Cost_of_one_equipment,Certification_Status,size,Equipment_name from equipment where Equipment_ID = '{}'".format(ei)
            cur.execute(a)
            data = cur.fetchone()                                             # Fetched resultset from database 
            x = data[0]                                                       # Cost per unit
            s = data[1]                                                       # Certification or graduation status 
            si = data[2]                                                      # Size 
            e = data[3]                                                       # Equipment name
            t = x*eq                                                          # total cost (quantity*cost per unit)
            cur.execute("insert into e_claim(e_Chemical_ID,sname,c_date,Equipment_ID,Equipment_name,Certification_Status,size,e_quantity,Cost_of_one_equipment,total_cost) values('{}','{}','{}','{}','{}','{}','{}',{},{},{})".format(ci,sn,cd,ei,e,s,si,eq,x,t))
            mycon.commit()
            print('INSERTION DONE!')

        elif ch == 2:
            print()
            print('FOR DISPLAY :--')
            print()
            a="select e_Chemical_ID,sname,c_date,equipment.Equipment_ID,equipment.Equipment_name,equipment.size,equipment.Certification_Status,e_quantity,equipment.Cost_of_one_equipment,e_quantity*equipment.Cost_of_one_equipment as totalcost from e_claim join equipment on e_claim.Equipment_ID = equipment.Equipment_ID"
            cur.execute(a)
            data = cur.fetchall()
            if data is None:
                print("NO RECORDS AVAILABLE!!!!!")
            else:
                for row in data:
                    print(' _ '*50)
                    print()
                    print('EQUIPMENT CLAIM ID :  ',row[0])
                    print()
                    print('STUDENT NAME :  ',row[1])
                    print('CLAIM DATE :  ',row[2])
                    print('EQUIPMENT ID :  ',row[3])
                    print('EQUIPMENT NAME :  ',row[4])
                    print('SIZE :   ',row[5])
                    print('Certification_Status :  ',row[6])
                    print('EQUIPMENT QUANTITY :  ',row[7])
                    print('COST OF ONE EQUIPMENT :  ',row[8],'Rs.')
                    print('TOTAL COST :  ',row[9],'Rs')
                    print()
                    print(' _ '*50)

        elif ch == 3:
            print('FOR SEARCH :-- ')
            e = input('Enter claim id:')
            a="select e_Chemical_ID,sname,c_date,equipment.Equipment_ID,equipment.Equipment_name,equipment.size,equipment.Certification_Status,e_quantity,equipment.Cost_of_one_equipment,e_quantity*equipment.Cost_of_one_equipment as totalcost from e_claim join equipment on e_claim.Equipment_ID = equipment.Equipment_ID where e_Chemical_ID like '{}'".format(e)
            cur.execute(a)
            data = cur.fetchone()
            if data is None:
                print("NO RECORDS AVAILABLE!!!!!")
            else:
                a="select e_Chemical_ID,sname,c_date,equipment.Equipment_ID,equipment.Equipment_name,equipment.size,equipment.Certification_Status,e_quantity,equipment.Cost_of_one_equipment,e_quantity*equipment.Cost_of_one_equipment as totalcost from e_claim join equipment on e_claim.Equipment_ID = equipment.Equipment_ID where e_Chemical_ID like '{}'".format(e)
                cur.execute(a)
                data=cur.fetchall()
                print('HERE ARE THE RECORDS :--')
                for row in data:
                    print(' _ '*50)
                    print()
                    print('EQUIPMENT CLAIM ID :  ',row[0])
                    print()
                    print('STUDENT NAME :  ',row[1])
                    print('CLAIM DATE :  ',row[2])
                    print('EQUIPMENT ID :  ',row[3])
                    print('EQUIPMENT NAME :  ',row[4])
                    print('SIZE :   ',row[5])
                    print('CERTIFICATION STATUS :  ',row[6])
                    print('EQUIPMENT QUANTITY :  ',row[7])
                    print('COST OF ONE EQUIPMENT :  ',row[8],'Rs.')
                    print('TOTAL COST :  ',row[9],'Rs')
                    print()
                    print(' _ '*50)


        elif ch == 4:
            print('FORM DELETION :--')
            e = input('Enter claim id:')
            a = "select * from e_claim where e_Chemical_ID = '{}'".format(e)
            cur.execute(a)
            data = cur.fetchone()
            if data[0] == e :
                cur.execute("Delete from e_claim where e_Chemical_ID like '{}'".format(e))
                mycon.commit()
                print('RECORD DELETED SUCCESSFULLY!')
            else:
                print("SORRY! CAN'T FIND YOUR RECORDS.")

        elif ch == 5:
            print('FOR UPDATION :--')
            print(' '*178, 'Which record you wanna update')
            print(' '*178, '1. Claim date')
            print(' '*178, '2. Student name')
            print(' '*178, '3. Equipment id')
            print(' '*178, '4. Quantity')
            print(' '*178, '5. Exit')
            ch = int(input('Enter choice:'))

            if ch == 1:
                e = input('Enter claim ID in which you want to update:')
                cur.execute("select c_date from e_claim where e_Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new claim date for updation:')
                    cur.execute("update e_claim set c_date = '{}' where e_Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 2:
                e = input('Enter claim ID in which you want to update:')
                cur.execute("select sname from e_claim where e_Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new sname for updation:')
                    cur.execute("update e_claim set sname = '{}' where e_Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 3:
                e = input('Enter claim ID in which you want to update:')
                cur.execute("select Equipment_ID from e_claim where e_Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new equipment id for updation:')
                    cur.execute("update e_claim set Equipment_ID = '{}' where e_Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 4:
                e = input('Enter claim ID in which you want to update:')
                cur.execute("select e_quantity from e_claim where e_Chemical_ID like '{}'".format(e))
                f = cur.fetchone()
                if f is None:
                    print('WRONG ENTRY')
                else :
                    n = input('Enter new quantity for updation:')
                    cur.execute("update e_claim set e_quantity = {} where e_Chemical_ID like '{}'".format(n,e))
                    mycon.commit()
                    print('RECORD UPDATED SUCCESSFULLY!')

            elif ch == 5:
                menu()

        elif ch == 6:
            print('THANKYOU !')
            print("VISIT AGAIN :) ")
            exit()

        else :
            print('INVALID CHOICE!')
            menu()

    except Exception as e:
        print('EXCEPTION! :' ,e)