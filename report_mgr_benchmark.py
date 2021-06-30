import rosbag
import pandas as pd

bag = rosbag.Bag('2021-06-29-18-33-19.bag')
# print(bag.get_type_and_topic_info())
time = list()
find_obj_cmd_times = list()
find_path_cmd_times = list()
match_times = list()
layover_times = list()
plan_times = list()

for topic, msg, t in bag.read_messages(topics=['gipick_mgr/benchmark']):
    time.append(t.to_time())
    find_obj_cmd_times.append(msg.find_object_time)
    find_path_cmd_times.append(msg.find_path_time)
    match_times.append(msg.match_time)
    layover_times.append(msg.layover_time)
    plan_times.append(msg.plan_time)
bag.close()

dict_msgs = {"timestamp": time,  
            "find_object_time": find_obj_cmd_times,
            "find_path_time": find_path_cmd_times,
            "match_time": match_times,
            "layover_time": layover_times,
            "plan_time": plan_times
}

msgs_df = pd.DataFrame(dict_msgs)
print(msgs_df)

compression_opts = dict(method='zip',
                        archive_name='out.csv')  
msgs_df.to_csv('out.csv', index=True)