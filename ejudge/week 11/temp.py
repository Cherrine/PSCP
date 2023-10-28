def create_matrix(numbers, row_size):
    return [numbers[i:i+row_size] for i in range(0, len(numbers), row_size)]

# ตัวอย่างการใช้งาน
numbers = '123456789'
numbers = [int(num) for num in numbers]  # แปลงสตริงเป็น list ของตัวเลข
row_size = 3  # คุณสามารถเปลี่ยนขนาดของแถวได้ตามต้องการ
matrix = create_matrix(numbers, row_size)

for row in matrix:
    print(' '.join(str(num) for num in row))
