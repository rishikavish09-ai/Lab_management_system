# Generate, Store & Manage bill records.

from Python_SQL_Connectivity_module import mycon, cur

def bill_records():
    try:
        print()
        print('1. CHEMICAL CLAIM BILL')
        print('2. EQUIPMENT CLAIM BILL')
        print()
        ch = int(input('Enter choice: '))
        if ch == 1:
            print('_'*70 ,'CHEMICAL CLAIM BILL' ,'_'*70)
            print()
            b = input('Enter Bill ID : ')                                     # Bill ID (unique identifier)
            c = input('Enter Chemical Claim ID : ')                           # Chemical claim id
            x = int(input('Enter Amount paid :'))                             # Amount paid
            z = "select Chemical_ID,total_cost from c_claim where c_Chemical_ID = '{}'".format(c)
            cur.execute(z)
            dataa = cur.fetchone()
            z1 = dataa[0]                                                     # Chemical id
            t1 = dataa[1]                                                     # Total claimed cost(quantity*cost per unit)
            d = t1 - x                                                        # Due (total claimed cost - amount paid)
            cur.execute("insert into c_bill(c_bill_id,c_Chemical_ID,Chemical_ID,amt_paid,due) values('{}','{}','{}',{},{})".format(b,c,z1,x,d))
            mycon.commit()
            a = "select c_bill_id,c_bill.c_Chemical_ID,c_claim.sname,c_claim.c_date,c_claim.Chemical_ID,c_claim.common_name,c_claim.formula,c_claim.Chemical_Quantity,c_claim.cost_of_unit_chemical,c_claim.total_cost,amt_paid,due from c_bill join c_claim on c_bill.c_Chemical_ID = c_claim.c_Chemical_ID where c_bill.c_bill_id like '{}'".format(b)
            cur.execute(a)
            data = cur.fetchone()
            if data is None:
                print("NO SUCH RECORD AVAILABLE!!!!!")
            else:
                a = "select c_bill_id,c_bill.c_Chemical_ID,c_claim.sname,c_claim.c_date,c_claim.Chemical_ID,c_claim.common_name,c_claim.formula,c_claim.Chemical_Quantity,c_claim.cost_of_unit_chemical,c_claim.total_cost,amt_paid,due from c_bill join c_claim on c_bill.c_Chemical_ID = c_claim.c_Chemical_ID where c_bill.c_bill_id like '{}'".format(b)
                cur.execute(a)
                data=cur.fetchall()
                for row in data:
                    print(' _ '*50)
                    print()
                    print('CHEMICAL BILL ID :  ',row[0])
                    print()
                    print('CHEMICAL CLAIM ID :  ',row[1])
                    print('STUDENT NAME :  ',row[2])
                    print('CLAIM DATE :  ',row[3])
                    print('CHEMICAL ID :  ',row[4])
                    print('CHEMICAL NAME :   ',row[5])
                    print('FORMULA :  ',row[6])
                    print('QUANTITY :  ',row[7])
                    print('COST OF UNIT CHEMICAL :  ',row[8],'rs')
                    print('TOTAL COST :  ',row[9],'rs')
                    print('AMOUNT PAID :  ',row[10],'rs')
                    print('DUE :  ',row[11],'rs')
                    print()
                    print(' _ '*50)
                    if  d == 0:
                        cur.execute("Delete from c_claim where Chemical_ID like '{}'".format(c))
                        mycon.commit()
                        print()
                        print('THIS CLAIM RECORD DELETED SUCCESSFULLY FROM CLAIM RECORDS.')
                    else:
                        print()
                        print(row[11],'RS. IS PENDING.')
                        print()
                        print('NOTE :-- IF THE STUDENT IS PAYING AMOUNT IN PARTS, RECORD WILL NOT DELETE AUTOMATICALLY!')

        elif ch == 2:
            print('_'*70 ,'EQUIPMENT CLAIM BILL' ,'_'*70)
            print()
            b = input('Enter Bill ID : ')
            c = input('Enter equipment Claim ID : ')                                     # Equipment claim id
            x = int(input('Enter Amount paid :'))
            z = "select Equipment_ID,total_cost from e_claim where e_Chemical_ID = '{}'".format(c)
            cur.execute(z)
            dataa = cur.fetchone()
            z1 = dataa[0]
            t1 = dataa[1]
            d = t1 - x
            cur.execute("insert into e_bill(e_bill_id,e_Chemical_ID,Equipment_ID,amt_paid,due) values('{}','{}','{}',{},{})".format(b,c,z1,x,d))
            mycon.commit()
            print('INSERTION DONE')
            a = "select e_bill_id,e_bill.e_Chemical_ID,e_claim.sname,e_claim.c_date,e_claim.Equipment_ID,e_claim.Equipment_name,e_claim.Certification_Status,e_claim.size,e_claim.e_quantity,e_claim.Cost_of_one_equipment,e_claim.total_cost,amt_paid,due from e_bill join e_claim on e_bill.e_Chemical_ID = e_claim.e_Chemical_ID where e_bill.e_bill_id like '{}'".format(b)
            cur.execute(a)
            data = cur.fetchone()
            if data is None:
                print("NO SUCH RECORD AVAILABLE!!!!!")
            else:
                a = "select e_bill_id,e_bill.e_Chemical_ID,e_claim.sname,e_claim.c_date,e_claim.Equipment_ID,e_claim.Equipment_name,e_claim.Certification_Status,e_claim.size,e_claim.e_quantity,e_claim.Cost_of_one_equipment,e_claim.total_cost,amt_paid,due from e_bill join e_claim on e_bill.e_Chemical_ID = e_claim.e_Chemical_ID where e_bill.e_bill_id like '{}'".format(b)
                cur.execute(a)
                data=cur.fetchall()
                for row in data:
                    print(' _ '*50)
                    print()
                    print('EQUIPMENT BILL ID :  ',row[0])
                    print()
                    print('EQUIPMENT CLAIM ID :  ',row[1])
                    print('STUDENT NAME :  ',row[2])
                    print('CLAIM DATE :  ',row[3])
                    print('EQUIPMENT ID :  ',row[4])
                    print('EQUIPMENT NAME :   ',row[5])
                    print('Certification_Status :  ',row[6])
                    print('SIZE :  ',row[7])
                    print('QUANTITY :  ',row[8])
                    print('COST OF ONE EQUIPMENT :  ',row[9],'rs')
                    print('TOTAL COST :  ',row[10],'rs')
                    print('AMOUNT PAID :  ',row[11],'rs')
                    print('DUE :  ',row[12],'rs')
                    print()
                    print(' _ '*50)
                    if  d == 0:
                        cur.execute("Delete from e_claim where Equipment_ID like '{}'".format(c))
                        mycon.commit()
                        print()
                        print('THIS CLAIM RECORD DELETED SUCCESSFULLY FROM CLAIM RECORDS.')
                    else:
                        print()
                        print(row[11],'RS. IS PENDING.')
                        print()
                        print('NOTE :-- IF THE STUDENT IS PAYING AMOUNT IN PARTS, RECORD WILL NOT DELETE AUTOMATICALLY!')

    except Exception as e:
         print('EXCEPTION : ', e)