from handle import *



# while True:
#     print("\n" + ("=" * 20))
#     print("""
# 1. Hiển thị Danh sách sản phẩm
# 2. Thêm sản phân
# 3. Xóa sản phẩm
# 4. Cập nhật sản phẩm
# 5. Tìm sản phẩm
# 0. Exit
#     """)
#     choice = int(input("Nhập lựa chọn: "))
#     if choice == 0:
#         break
#     elif choice == 1:
#         Manager._Xuat()
#     elif choice == 2:
#         x = input().split()
#         x = Manager(x[0], x[1], x[2], x[3])
#         Manager._Add(x)
#     elif choice == 3:
#         Manager._Del()
#     elif choice == 4:
#         Manager.Update()
#     elif choice == 5:
#         Manager._Search()
#     else:
#         print("Nhập sai lựa chọn. Vui lòng chọn lại!")
#         continue


while True:
    print("\n" + ("=" * 20))
    print("""
1. Hiển thị Danh sách sản phẩm
2. Thêm sản phân
3. Xóa sản phẩm
4. Cập nhật sản phẩm
5. Tìm sản phẩm
0. Exit
    """)
    choice = int(input("Nhập lựa chọn: "))
    match choice:
        case 1:
            Manager._Xuat()
        case 2:
            x = input().split()
            x = Manager(x[0], x[1], x[2], x[3])
            Manager._Add(x)
        case 3:
            Manager._Del()
        case 4:
            Manager.Update()
        case 5:
            Manager._Search()  
        case 0:
            exit()
        case default:
            print("Nhập sai lựa chọn. Vui lòng chọn lại!")


