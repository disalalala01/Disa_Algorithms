#---------------------------------------Лекция № 8(Рекурсия)-----------------------------------------
# ------------------Задачка из leetcode two sum ---------------------------
A = [1,2,3,7,5,56]
target = 9
count = 0
for i in range(len(A)):
    count +=1
    for k in range(len(A)):
        if i+k==target:
            print(i, k+i, count)

def find_target_index(A:list, target):
    """A[] Перибирем лист если две цифры в листе равны target
    то нужно написать его индекс
    """
    for i in A:
        left = A[i+1:]
        for k in range(len(left)):
            if A[i]+left[k]==target:
                print("func")
                return i, k+1+i
A = [1,2,3,4,5]
t = 9
m = find_target_index(A, t)
print(m)

for i in range(len(A)):
            left = A[i+1::]#start , stop , step
            for j in range(len(left)):
                if (A[i] + left[j]) == target:
                    print(i, j+i+1)

C= [1,2,3,7]
toolis=9
for i in C:
    for k in C:
        if i+k==toolis:
            print("Here")
            print(i,k)

#----------------------------------leetcode---------------------------------------
