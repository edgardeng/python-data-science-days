import random
import pymongo
import pandas as pd


def get_open_door():
    db_client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = db_client["heisai_face_store"]
    pipe_line_1 = [
        {"$group": {"_id": "$face._id", "count": {"$sum": 1}}}
    ]
    face_id_count = db.hs_face_photo.aggregate(pipe_line_1)
    pipe_line_2 = [
        {"$group": {"_id": "$face._id"}}
    ]
    open_door_ids = db.hs_open_door_photo.aggregate(pipe_line_2)
    part_list(list(face_id_count), list(open_door_ids))


def part_list(list_face, list_open_door):

    pd_face = pd.DataFrame(list_face)
    pd_door = pd.DataFrame(list_open_door)
    # 并集
    # all_photo = pd.merge(pd_door, pd_face, on=['_id'], how='outer')
    # 1 无face的 测试集
    df1 = pd_door.append(pd_face)
    df1 = df1.append(pd_face)
    pd_door_test_out = df1.drop_duplicates(subset=['_id'], keep=False)
    print(pd_door_test_out)

    # 2 有face的测试
    # df.loc[(df['C']>2) & (df['D']<10) ]
    pd_train = pd_face.loc[pd_face['count'] > 10]
    print(pd_train)
    pd_face_test_in = pd_face.loc[pd_face['count'] <= 10]
    print(pd_face_test_in)
    pd_door_test_in = pd.merge(pd_door, pd_face_test_in, on=['_id'])
    pd_door_test = pd_door_test_in.append(pd_door_test_out)
    print('---- test ----')
    write_list_in(pd_door_test_in, 'test')
    print('---- origin ----')
    write_list_in(pd_door_test, 'origin')
    print('---- train ----')
    write_list_in(pd_train, 'train')


def write_list_in(data_list, file_name):
    # print(data_list)
    with open(file_name + '.txt', 'w') as file:
        for item in data_list['_id']:
            file.write('\r\n')
            file.write(str(item))
        # print(item['id'])


if __name__ == '__main__':
    get_open_door()
    print('ok')
