import rosbag
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

bag = rosbag.Bag('/home/g4user-18/Desktop/test_/2021-05-28-13-33-04.bag')
# print(bag.get_type_and_topic_info())
time = list()
segs_size = list()
msgs = list()

for topic, msg, t in bag.read_messages(topics=['display_trajectory_segs']):
    time.append(t.to_time())
    segs_size.append(len(msg.segments))
    msgs.append(msg)

dict_msgs = {"time": time,  
             "segment_size": segs_size
            }
msgs_df = pd.DataFrame(dict_msgs)

print('By msgs:')
print(msgs_df)

print('==============================================================')

trajectory_points_size = list()
frame_id = list()

for seg in msgs[0].segments:
    trajectory_points_size.append(len(seg.points))
    frame_id.append(seg.header.frame_id)

dict_segs = {
    "trajectory_points_size": trajectory_points_size,
    "frame_id": frame_id 
}
segs_df = pd.DataFrame(dict_segs)

print('By msg[0] -> segments:')
print(segs_df)

print('==============================================================')

joint1 = list()
joint2 = list()
joint3 = list()
joint4 = list()
joint5 = list()
joint6 = list()

for point in msgs[0].segments[0].points:
    joint1.append(point.positions[0])
    joint2.append(point.positions[1])
    joint3.append(point.positions[2])
    joint4.append(point.positions[3])
    joint5.append(point.positions[4])
    joint6.append(point.positions[5])

dict_points = {
    "joint1": joint1,
    "joint2": joint2,
    "joint3": joint3,
    "joint4": joint4,
    "joint5": joint5,
    "joint6": joint6
}
points_df = pd.DataFrame(dict_points)

print('By msg[0] -> segments[0] -> trajectorys:')
print(points_df)

print('==============================================================')