# Bag api example

這邊提供一個範例展示如何 parse bag 檔, 然後在將資料流到 Panda 做資料分析

## Panda

pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

[User guide](https://pandas.pydata.org/docs/user_guide/index.html)

## Cookbook

#### [`test_bag.py`](test_bag.py)

Parse data from bag file through bag api, and stream to panda show in tablure style.

#### [`filter_trajs_display.py`](filter_trajs_display.py)

It's a example show how to filter a last message from a bag file, and write to another bag file.

#### [`replay_bag_trajectory.py`](replay_bag_trajectory.py)

It's a example to replay a bag file used by bag api.