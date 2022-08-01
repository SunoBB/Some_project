creat = []# Mã tên hãng giá
check = []


class Manager:
    def __init__(self, ma, ten, hang, gia):
        self.Ma = ma
        self.Ten = ten
        self.Hang = hang
        self.gia = gia
        check.append(ma)
    def _Add (self):
        print()
        for i in creat:
            if i[0] == self.Ma:
                print("Sản phẩm đã tồn tại")
                break
        else:
            creat.append((self.Ma, self.Ten, self.Hang, self.gia))
            print("Đã thêm")


    def _Xuat():
        print()
        print("Ma Sp"+"\t"+"Ten Sp"+"\t"+"Hang"+"\t"+"Gia")
        for i in creat:
            print(f"{i[0]} \t {i[1]} \t {i[2]} \t {i[3]}")


    def _Del():
        print()
        Del_product = input("Nhập mã sản phẩm cần xóa: ")
        if Del_product not in check:
            print("Không tìm thấy sản phẩm cần xóa")
        for i in creat:
            if i[0] == Del_product:
                creat.remove(i)
                print("Đã xóa")
                break


    def Update():
        print()
        Update_product = input("Nhập mã sản phẩm cần cập nhật: ")
        for i in creat:
            if i[0] == Update_product:
                # Ma = input("Nhập mã sản phẩm: ")
                i[1] = input("Nhập tên sản phẩm: ")
                i[2] = input("Nhập hãng sản phẩm: ")
                i[3] = input("Nhập giá sản phẩm: ")
                # creat.remove(i)
                # creat.append((Update_product, Ten, Hang, gia))
                print("Đã cập nhật")
                break
        else:
            print("Khoong tìm thấy sản phẩm cần cập nhật")


    def _Search():
        print()
        Search_product = input("Nhập mã sản phẩm cần tìm: ")
        for i in creat:
            if i[0] == Search_product:
                print("Ma Sp"+"\t"+"Ten Sp"+"\t"+"Hang"+"\t"+"Gia")
                print(f"{i[0]} \t {i[1]} \t {i[2]} \t {i[3]}")
                break
        else:
            print("Không tìm thấy sản phẩm cần tìm")
