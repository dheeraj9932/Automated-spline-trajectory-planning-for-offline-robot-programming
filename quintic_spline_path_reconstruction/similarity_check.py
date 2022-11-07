from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import similaritymeasures

x = np.array([[1,1,1],[5,5,5],[8,8,8]])
# y = np.array([[1,1,1],[5,5,5],[8,8,8]])

# x = np.array([[1,1,1],[5,5,5],[8,8,8],[4,4,4],[2,2,2]])
y = np.array([[1.1,1.1,1.1],[5,5,5],[8.0,8.0,8.0],[5.1,4.4,4],[21,22,23]])

# x,y = np.array([[0, 0, 0],[1,1,1]]), np.array([[0, 0, 0],[-1,-1,-1]])

dtw, d = similaritymeasures.dtw(x, y)
print(dtw)
print(d)

from io import StringIO
import csv

trial = []
with open('experiment_id_and_indexes.csv', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        trial.append(row)
        # print(row)
print((trial[0:5]))
print((trial[0][0]))
print(type(trial[0][0]))
letter_list = trial[0][0].split(",")
print(letter_list)
print(type(letter_list))
print(int(letter_list[2]), type(int(letter_list[2])))
names = []
row_indexes = []
experiment_id = []
for i in range(len(trial)):
    temp = trial[i][0].split(",")
    # print((temp[0]),(int(temp[1])),(int(temp[2])))
    names.append(temp[0])
    row_indexes.append(int(temp[1]))
    experiment_id.append(int(temp[2]))

print(names)
# print((row_indexes))
print(experiment_id)
records = np.rec.fromarrays((np.asarray(names),np.asarray(row_indexes),np.asarray(experiment_id)),
                            names=('pos','index','exp_id'))

print(records['index'])
# itemindex = np.where(records['exp_id'] == 1)
# segment = records['index'][itemindex[0]]
# print(segment)
def exp_seg(ex,seg_start, seg_end):
    item_index = np.where(records['exp_id'] == ex)
    # print("item_index")
    # print(item_index)
    segment = records['index'][item_index[0]]
    # print("segment")
    # print(segment)
    seg_start_index = np.where(records['pos'][item_index[0]]==seg_start)
    seg_end_index = np.where(records['pos'][item_index[0]]==seg_end)
    # print(seg_start_index[0])
    # print(seg_end_index[0])
    # print('\n')
    # print(segment[seg_start_index[0]])
    # print(segment[seg_end_index[0]])
    k = segment[seg_start_index[0]]
    l = segment[seg_end_index[0]]
    print("***************************")
    print(records['pos'][item_index[0]])
    print(segment)
    print(k)
    print(l)
    print("***************************")
    if len(k) == 1 and len(l)==1:
        if k[0]<l[0]:
            return k[0],l[0]
        else:
            print("please enter a valid order of points")
            return 0,0
    elif len(k) == 1 and len(l)>1:
        if k[0] < l[0]:
            return k[0],l[0]
        else:
            return k[0], l[-1]
    elif len(k) > 1 and len(l)==1:
        if k[-1]<l[0]:
            return k[-1], l[0]
        else:
            return k[0], l[0]
    elif len(k) > 1 and len(l) > 1:
        return k[0], l[-1]
        # if len(l) > 1:

    # if len(k)
    # return segment[seg_start_index[0]], segment[seg_end_index[0]]
print("#############################################")
k, l = exp_seg(10,'p1','p2'); print("1")
print(k, l);print('\n')
k,l = exp_seg(10,'p1','p3');print("2")
print(k, l);print('\n')
k,l = exp_seg(10,'p2','p3');print("3")
print(k, l);print('\n')
k,l = exp_seg(10,'p3','p1');print("4")
print(k, l);print('\n')
k,l = exp_seg(10,'p1','p5');print("5")
print(k, l);print('\n')
k,l = exp_seg(10,'p1','p1');print("6")
print(k, l);print('\n')














# x = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)],
#              dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
# print(x)
# x = np.append(x,np.array([('box',10,1.1)]), axis=1)
# print(x)
# simpler version with split() on newlines:

# reader = csv.reader(scsv.split('\n'), delimiter=',')
# for row in reader:
#     print('\t'.join(row))

# print(cosine_similarity(x,y))