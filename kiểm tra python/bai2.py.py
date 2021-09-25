A = [1,1,2,3,5,8,13,21,34,55,88]
B = [1,3,5,4,7,88,66,59,40,54]
C = []
cho x trong A:
	cho s trong B:
		nếu x == s:
			in(x)
			C. thêmvào (x)

print("List C sau khi lưu trữ các số trùng bên list A,B: " ,C)
cho x trong C:
	cho s trong B:
		nếu x == s:
			B. loại bỏ(s)
cho x trong C:
	cho s trong A:
		nếu x == s:
			A. loại bỏ(s)
print("List A sau khi xoá: ",A)
print("List B sau khi xoá: ",B)