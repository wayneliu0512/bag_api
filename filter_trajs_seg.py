import rosbag

bag = rosbag.Bag('2021-05-28-13-33-04.bag')
# print(bag.get_type_and_topic_info())
time = list()
segs_size = list()
msgs = list()

for topic, msg, t in bag.read_messages(topics=['display_trajectory_segs']):
    time.append(t.to_time())
    segs_size.append(len(msg.segments))
    msgs.append(msg)
bag.close()

bag_out = rosbag.Bag('target.bag', 'w')
try:
    bag_out.write('test_display_trajectory_segs', msgs[len(msgs)-1])
finally:
    bag_out.close()