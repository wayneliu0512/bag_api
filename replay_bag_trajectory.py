import socket
from gipick_info.msg import trajectory_segs 
import sys
import time
import struct
import rospy
from rospy.core import rospyinfo
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

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_adress = ('192.168.2.179', 5002)
sock.bind(server_adress)
sock.listen(1)

pub = rospy.Publisher('test_display_trajectory_segs', trajectory_segs, queue_size=10)
rospy.init_node('replay_bag', anonymous=True)

# Wit for a connection
print('waiting for a connection')
connection, client_address = sock.accept()
# time.sleep(1)
print('connection from {0}'.format(client_address))

# while True: change to for msg
for i in range(0, len(msgs)):

    data = connection.recv(1024)
    result = data.decode(encoding="ascii")
    print(data)
    print(i)

    if data != 'recap\r\n':
        print('break')
        break
    
    # rospy.info(msgs[i])
    pub.publish(msgs[i])
    
    message = '0\r\n'
    message_bytes = message.encode(encoding="ascii")
    connection.send(message_bytes)
    # Clean up the connection
connection.close()
