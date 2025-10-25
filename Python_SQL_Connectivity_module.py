# Building connectivity between Python & MySQL.

# Works with MySQL on PC and SQLite on Android (Pydroid 3)

try:
    # Try to connect to MySQL (for Windows/Linux PC)
    import mysql.connector as sqltor
    mycon = sqltor.connect(
        host='localhost',
        user='root',
        password='1234',
        database='lab_management'
    )
    cur = mycon.cursor()
    print("Connected to MySQL database successfully!\n")
    cur.execute("create database if not exists LAB_MANAGEMENT")
    cur.execute("use LAB_MANAGEMENT ")

except Exception as e:
    # Fallback to SQLite (for Android / Pydroid)
    print(" MySQL connection failed — switching to SQLite mode.\nError:", e)
    import sqlite3 as sqltor
    mycon = sqltor.connect("lab_management.db")
    cur = mycon.cursor()
    print(" Connected to SQLite database successfully!\n")


# AUTO TABLE CREATION (for all modules)


try:
    # Login table
    cur.execute("create table if not exists account(uname varchar(20) primary key, paswrd varchar(20) not null )")
    # Equipment table
    cur.execute("create table if not exists equipment(Equipment_ID varchar(10) primary key,Equipment_name varchar(20) not null ,quantity int(10),size varchar(20), Certification_Status varchar(20),Cost_of_one_equipment int(5), total_cost int(10))")
    # Chemical table
    cur.execute("create table if not exists chemical(Chemical_ID varchar(20) primary key, common_name varchar(50), IUPAC_name varchar(40), formula varchar(30) not null, physical_state varchar(20) ,Boiling_or_Melting_point int(3) ,hazzards varchar(20) ,expiry_date date,quantity int(10),cost_of_unit_chemical int(10),total_cost int(15))")
    # Chemical Claim table
    cur.execute("create table if not exists c_claim(c_Chemical_ID varchar(10) primary key, sname varchar(20) not null, c_date date, Chemical_ID varchar(20), common_name varchar(50), formula varchar(30) not null, Chemical_Quantity int(5), cost_of_unit_chemical int(10),total_cost int(15), foreign key (Chemical_ID) references chemical(Chemical_ID) on delete cascade on update cascade)")
    # Equipment Claim table
    cur.execute("create table if not exists e_claim(e_Chemical_ID varchar(10) primary key, sname varchar(20) not null, c_date date, Equipment_ID varchar(10),Equipment_name varchar(20), Certification_Status varchar(20), size varchar(20), e_quantity int(5), Cost_of_one_equipment int(5), total_cost int(10), foreign key (Equipment_ID) references equipment(Equipment_ID) on delete cascade on update cascade)")
    # Equipment Bill table
    cur.execute("create table if not exists e_bill(e_bill_id varchar(10) primary key,e_Chemical_ID varchar(10) ,Equipment_ID varchar(10), amt_paid int(5) ,due int(5), foreign key (e_Chemical_ID) references e_claim(e_Chemical_ID) on delete cascade on update cascade, foreign key (Equipment_ID) references equipment(Equipment_ID) on delete cascade on update cascade)")
    # Chemical Bill table
    cur.execute("create table if not exists c_bill(c_bill_id varchar(10) primary key,c_Chemical_ID varchar(10) ,Chemical_ID varchar(20), amt_paid int(5) ,due int(5), foreign key (c_Chemical_ID) references c_claim(c_Chemical_ID) on delete cascade on update cascade, foreign key (Chemical_ID) references chemical(Chemical_ID) on delete cascade on update cascade)")
    mycon.commit()
    print("🗂️ All required tables verified/created successfully!\n")

except Exception as err:
    print("⚠️ Table creation skipped or failed:", err)



