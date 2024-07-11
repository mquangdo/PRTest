#Dạng 1

#Bài 1
#a
a <- 1:10
b <- 1:10
plot(a, b, type = 'l', main = 'My plot')
so_tien <- c(525, 500, 500, 300, 200, 475)
ti_le <- round(prop.table(so_tien), 2) * 100
khoan_chi <- c("National Defender", "Social Security", "Medical", "Pay", "Social Programs", "Another payments")
pie(ti_le, labels = khoan_chi, col = rainbow(6), main = "Paymens", sub = "2006")

#b
barplot(so_tien, col = rainbow(6), main = "Biểu đồ các khoản chi tiêu", sub = "Số liệu năm 2006", names.arg = khoan_chi)
barplot(ti_le, col = rainbow(6), main = "Biểu đồ các khoản chi tiêu", sub = "Số liệu năm 2006", names.arg = khoan_chi)
mtext("%", at = 0, col = "black")


#c
pie(so_tien, labels = paste(khoan_chi, ":", ti_le, "%"), col = rainbow(6), main = "Biểu đồ các khoản chi tiêu", sub = "Số liệu năm 2006")


#Bài 2
#a
passenger_car <- c(9.436, 8.687, 8.273, 8.142, 8.697, 8.852, 8.422, 8.082)
SUV_light = c(4.733, 6.517, 7.226, 7.821, 8.717, 8.965, 9.050, 9.036)
matrix = rbind(passenger_car, SUV_light)
matrix
barplot(matrix, beside = TRUE, xlab = "Year", ylab = "Số lượng xe", col = c("cyan", "pink"), main = "Sự thay đổi về việc lựa chọn xe", sub = "Số liệu năm 2002", names.arg = c(1990, 1995, 1997, 1998, 1999, 2000, 2001, 2002), ylim = c(0, 12))
legend(x = "topright", legend = c("Passenger cars", "SUV/Light"), fill = c("cyan", "pink"), title = "Chú thích")
mtext("Nghìn xe", at = 1, col = 'black')

#Bài 3

#prepare
practice_family = c(47.8, 57.6, 59.9, 64.6, 66.2, 67.5, 70)
total = c(271.3, 359.9, 427.3, 468.8, 473.2, 490.4, 514)

#a
barplot(practice_family, main = "Sự tăng lên của số lượng bác sĩ gia đình qua các năm", names.arg = c(1980, 1990, 1995, 1998, 1999, 2000, 2001), xlab = "Năm", ylab = "Số lương", col = "cyan")
mtext("Người", at = 0.1)

#b
ti_le1 = round(practice_family / total, 2)
barplot(ti_le1, ylim = c(0, 1), main = "Tỉ lệ", names.arg = c(1980, 1990, 1995, 1998, 1999, 2000, 2001), xlab = "Năm", ylab = "Tỉ lệ", col = "cyan")
mtext("Người", at = 0.1)

#c
#Xu hướng của biểu đồ 1 về số lượng của các bác sĩ gia đình là tăng dần qua các năm
#Biểu đồ tỉ lệ thì giảm dần nhưng ổn định từ năm 1995


#Bài 4
nong_do = c(0.75, 0.86, 0.84, 0.85, 0.97, 0.94, 0.89, 0.84, 0.83, 0.89, 0.88, 0.78, 0.77, 0.76, 0.82, 0.72, 0.92, 1.05, 0.94, 0.83, 0.81, 0.85, 0.97, 0.93, 0.79)
hist(nong_do, main = "Nồng độ florua", xlab = 'Nồng độ', ylab = "Số ngày", col = "cyan", border = "purple", labels = T, ylim = c(0, 11), breaks = 10)
mtext("Triệu (ppm)", at = 0, col = "red")


#Bài 5


standard = c(4, 15, 24, 10, 1, 27, 31, 14, 2, 16, 32, 7, 13, 36, 29, 6, 12, 18, 14, 15, 18, 6, 13, 21, 20, 8, 3, 24)
new = c(5, 20, 29, 15, 7, 32, 36, 17, 15, 19, 35, 10, 16, 9, 27, 14, 10, 16, 12, 13, 16, 9, 18, 33, 30, 29, 31, 27)

hist(standard, xlab = "Thời gian sống", ylab = "Số người", col = "orange", main = "Phương pháp cũ", breaks = 5) #breaks = 30 để các số liệu thêm chi tiết
hist(new, xlab = "Thời gian sống", ylab = "Số người", col = "pink", main = "Phương pháp mới")
updateR()


#Bài 6

#prepare
install.packages('Stat2Data')
library(Stat2Data)
data(AHCAvote2017)
data <- AHCAvote2017
View(data)
attach(data)

#a
table(STATE)

#c
party_count = table(Party)
party_count
barplot(party_count, names.arg = c("Democracy", "Republic"), col = c("purple", "green"), main = "Number", border = "black", ylab = "Number of members", xlab = "Party")
mtext("Person", at = 0)


#Bài 7
#prepare
data(BirdNest)
data = BirdNest
attach(data)
View(data)


#a
table(Nesttype)

#b
m = min(Length)
m
M = max(Length)
M
print(paste(data[Length == m, "Species"], "có chiều dài nhỏ nhất"))
print(paste(data[Length == M, "Species"], "có chiều dài lớn nhất"))

#c
#cách 1
barplot(table(Location), col = rainbow(9), main = "Vị trí làm tổ của các loài chim", sub = "Bộ dữ liệu BirdNest", xlab = "Các vị trí làm tổ", ylab = "Số lượng", density = c(30, 30, 30, 30, 30), angle = c(0, 45, 90, 11, 36))
abline(v = c(4.9, 9.7), col = "grey")


#cách 2
table = data.frame(table(Location))
table

my_bar = barplot(table$Freq, names.arg = table$Location, col = rainbow(9), main = "Vị trí làm tổ của các loài chim", sub = "Bộ dữ liệu BirdNest", xlab = "Các vị trí làm tổ", ylab = "Số lượng", density = c(30, 30, 30, 30, 30), angle = c(0, 45, 90, 11, 36), ylim = c(0, 25))
abline(v = c(4.9, 9.7), col = "grey")
text(my_bar, table$Freq + 0.5, paste("n : ", table$Freq, sep = ""), cex = 1)


#Test
data <- data.frame(
  name = c("DD", "with himself", "with DC", "with Silur", "DC", "with himself", "with DD", "with Silur", "Silur", "with himself", "with DD", "with DC"),
  average = sample(seq(1, 10), 12, replace = T),
  number = sample(seq(4, 39), 12, replace = T)
)

# Increase bottom margin
par(mar = c(6, 4, 4, 4))

c = c(1:12)

my_bar <- barplot(c, border = F, names.arg = data$name,
                  las = 2,
                  col = c(rgb(0.3, 0.1, 0.4, 0.6), rgb(0.3, 0.5, 0.4, 0.6), rgb(0.3, 0.9, 0.4, 0.6), rgb(0.3, 0.9, 0.4, 0.6)),
                  ylim = c(0, 13),
                  main = "")

# Add abline
abline(v = c(4.9, 9.7), col = "grey")

# Add the text 
text(my_bar, c + 0.4, paste("n: ", data$number, sep = ""), cex = 1)

#Legende
legend("topleft", legend = c("Alone", "with Himself", "With other genotype"),
       col = c(rgb(0.3, 0.1, 0.4, 0.6), rgb(0.3, 0.5, 0.4, 0.6), rgb(0.3, 0.9, 0.4, 0.6), rgb(0.3, 0.9, 0.4, 0.6)),
       bty = "n", pch = 20, pt.cex = 2, cex = 0.8, horiz = FALSE, inset = c(0.05, 0.05))


#Bài 8
data("BlueJays")
data = BlueJays
attach(data)
#a
table(KnownSex)

#c
hist(Mass, breaks = 10, labels = T, col = c("#4D1A6699", "#4D1A66FF", "#4D1A66CC", "#4D1A6699", "#4D1A9966", "#4D1ACC66", "#4D1AFF66", "#4D66991A", "#4D6699CC", "#4D6699FF", "#4D99CC1A", "#4D99CC66"), main = "Tần số trọng lượng của loài chim", sub = "Bộ dữ liệu BlueJays", density = c(90, 90, 90, 90, 90), angle = c(0, 45, 90, 11, 36))

#d
plot(BillWidth, BillLength, ylim = c(20, 28), xlim = c(8, 10), col = "purple", main = "Chiều dài và rộng của các loài", type = "p")
grid(nx = NULL, ny = NULL, lty = 1, col = "gray")


#Bài 9
data("BritishUnions")
data = BritishUnions
attach(data)
View(data)

#a
my_plot = plot(Unemployment, type = "l", col = "green", lwd = 2, lty = "solid", xlab = "Thời gian", ylab = "Tỉ lệ thất nghiệp", main = "Tỉ lệ thất nghiệp theo thời gian")
mtext("%", at = 0)
grid(nx = NULL, ny = NULL, lty = 1, col = "gray")


#Bài 10
data("CAFE")
data = CAFE
attach(data)
View(data)

#a
table(State)

#Bài 11
data("Clothing")
data = Clothing
attach(data)
View(data)

#a
table(Card)

#b
install.packages('ggplot2')
use('ggplot2')
data()
?BOD

ggplot(data = BOD, mapping = aes(x = Time, y = demand)) + geom_point(size = 5)