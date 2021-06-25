import rosbag

bag = rosbag.Bag('2021-05-28-13-33-04.bag')
# print(bag.get_type_and_topic_info())
time = list()
segs_size = list()
msgs = list()

for topic, msg, t in bag.read_messages(topics=['display_trajectory']):
    time.append(t.to_time())
    msgs.append(msg)
bag.close()

bag_out = rosbag.Bag('target_display.bag', 'w')
try:
    bag_out.write('display_trajectory', msgs[len(msgs)-1])
finally:
    bag_out.close()