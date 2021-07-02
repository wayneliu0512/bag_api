from sys import path
import rosbag
import pandas as pd

filename = '2021-07-01-11-18-27.bag'
bag = rosbag.Bag(filename)
# print(bag.get_type_and_topic_info())
time = list()
motion_plan_times = list()
paths_size = list()
motion_plan_result = list()

path_timestamps = list()
path_times = list()
path_result = list()

waypoint_timestamps = list()
ik_collision_time = list()
disturbtion_time = list()
cartesian_result = list()
filter_result = list()

cartesian_timestamps = list()
cartesian_time = list()

for topic, msg, t in bag.read_messages(topics=['g_move_group/benchmark']):
    time.append(t.to_time())
    motion_plan_times.append(msg.motion_plan_time)
    paths_size.append(len(msg.paths_benchmark))
    motion_plan_result.append(msg.result)

    for path in msg.paths_benchmark:
        path_timestamps.append(t.to_time())
        path_times.append(path.path_time)
        path_result.append(path.result)

        for waypoint in path.waypoints_benchmark:
            waypoint_timestamps.append(t.to_time())
            ik_collision_time.append(waypoint.ik_collision_time)
            disturbtion_time.append(waypoint.disturbtion_time)
            cartesian_result.append(waypoint.cartesian_result)
            filter_result.append(waypoint.filter_result)

            for cartesian in waypoint.cartesian_plan_poses_time:
                cartesian_timestamps.append(t.to_time())
                cartesian_time.append(cartesian)
bag.close()

dict_motion_plan = {
    "timestamp": time,
    "motion_plan_time": motion_plan_times,
    "paths_size": paths_size,
    "result": motion_plan_result
}
df_motion_plan = pd.DataFrame(dict_motion_plan)
print(df_motion_plan)

dict_path = {
    "timestamp": path_timestamps,
    "path_time": path_times,
    "path_result": path_result
}
df_path = pd.DataFrame(dict_path)
print(df_path)

dict_waypoint = {
    "timestamp": waypoint_timestamps,
    "ik_collision_time": ik_collision_time,
    "disturbtion_time": disturbtion_time,
    "cartesian_result": cartesian_result,
    "filter_result": filter_result
}
df_waypoint = pd.DataFrame(dict_waypoint)
print(df_waypoint)

dict_cartesian = {
    "timestamp": cartesian_timestamps,
    "cartesian_time": cartesian_time
}
df_cartesian = pd.DataFrame(dict_cartesian)
print(df_cartesian)

df_motion_plan.to_csv(filename + '_motion_plan.csv', index=True)
df_path.to_csv(filename + '_path.csv', index=True)
df_waypoint.to_csv(filename + '_waypoint.csv', index=True)
df_cartesian.to_csv(filename + '_cartesian.csv', index=True)