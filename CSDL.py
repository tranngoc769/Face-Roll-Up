import sqlite3
def checkExist(MSSV):
    ketNoiSql = sqlite3.connect("Database/DanhSach.db")
    querry = "SELECT * FROM HocVien WHERE MSSV='" + str(MSSV)+"'"
    OK = ketNoiSql.execute(querry)
    isExist = False
    for row in OK:
        isExist = True
    ketNoiSql.commit()
    ketNoiSql.close()
    return isExist
def Insert_UpdateStudent(MSSV, HoTen, Lop, GioiTinh):
    ketNoiSql = sqlite3.connect("Database/DanhSach.db")
    querry = "SELECT * FROM HocVien WHERE MSSV='" + str(MSSV)+"'"
    OK = ketNoiSql.execute(querry)
    isExist = False
    for row in OK:
        isExist = True
    if isExist!=True:
        temp = ketNoiSql.execute("SELECT COUNT(STT) FROM HocVien")
        for row in temp:
            STT = row[0] + 1
        querry = "INSERT INTO HocVien(MSSV,HoTen,Lop,GioiTinh,STT) Values('" + str(MSSV) + "','" + str(HoTen) + "','" + str(Lop) + "','" + str(GioiTinh)+"',"+str(STT) + ")"
    else:
    	querry = "UPDATE HocVien SET HoTen='" + str(HoTen) + "',Lop='" + str(Lop) + "',GioiTinh='" + str(GioiTinh) + "' WHERE MSSV= '" + str(MSSV)+"'"
    ketNoiSql.execute(querry)
    ketNoiSql.commit()
    ketNoiSql.close()
def soLuongHV(Class):
    ketNoiSql = sqlite3.connect("Database/DanhSach.db")
    querry = "SELECT COUNT(*) as SL FROM HocVien WHERE LOP='" + str(Class)+"'"
    OK = ketNoiSql.execute(querry)
    for row in OK:
        SL = row[0]
    ketNoiSql.commit()
    ketNoiSql.close()
    return SL
def ThongTinHV(MSSV):
    ketNoiSql = sqlite3.connect("Database/DanhSach.db")
    querry = "SELECT * FROM HocVien WHERE MSSV='" + str(MSSV)+"'"
    OK = ketNoiSql.execute(querry)
    for row in OK:
        SL = row
    ketNoiSql.commit()
    ketNoiSql.close()
    return SL[0],SL[1],SL[2],SL[3],SL[4]

def getData(id):
    ketNoiSql = sqlite3.connect("Database/DanhSach.db")
    querry="SELECT * FROM HocVien WHERE STT="+str(id)
    OK=ketNoiSql.execute(querry)
    profile=None
    for row in OK:
        profile=row
    ketNoiSql.close()
    return profile