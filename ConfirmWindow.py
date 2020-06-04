import sqlite3
def checkExist(MSSV):

def InsertOnePeople(MSSV, HoTen, Tuoi, GioiTinh):
    ketNoiSql = sqlite3.connect("DanhSach.db")
    querry = "SELECT * FROM HocVien WHERE MSSV=" + str(MSSV)
    OK = ketNoiSql.execute(querry)
    daTonTai = 0
    for row in OK:
        daTonTai = 1
    if daTonTai != 0:
        querry = "UPDATE HocVien SET HoTen='" + str(HoTen) + "',Tuoi=" + str(Lop) + ",GioiTinh='" + str(GioiTinh) + "'WHERE MSSV=" + str(MSSV)
    else:
    	querry = "INSERT INTO HocVien(MSSV,HoTen,Lop,GioiTinh) Values(" + str(MSSV) + ",'" + str(HoTen) + "','" + str(Lop) + "','" + str(GioiTinh) + "')"
    ketNoiSql.execute(querry)
    ketNoiSql.commit()
    ketNoiSql.close()
    print('Insert succesful')
