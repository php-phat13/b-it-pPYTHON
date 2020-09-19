#b10: viết chương trình nhập vào tiền lương cơ bản , phụ cấp và số ngày đi làm trong tháng,in ra màn hình lương chính nhận được theo công thức:nhập tiền lương cơ bản , phụ cấp và số ngày đi làm lương chính = ((lương cơ bản + phụ cấp)/22)*số này đi làm
                  Luongcb = int(input('Nhap muc luong cua ban:'))
                   Phucap = int(input('Phu cap cua ban:'))
              Songaydilam = int(input('Nhap so ngay đi lam:'))
                         S=((Luongcb + Phucap)/22) * Songaydilam
                  print("Luong cua ban la",S)
