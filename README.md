# ros_writing_node

A simple python based ros writing node. 


## Installation

 - git clone this repository 
 - catkin_make

## Use

roslaunch ros_writing_node writing.launch

params:
target_publisher: The ros topics that will be subscribed to.

file_type: The file type that will be used. Currently, a .json format is supported, and otherwise, it will default to a .csv

NOTE: The .json format will not write the end character meaning that the JSON array object will not be closed. A ']' needs to be added to the end of any JSON file created

Additionally, If the node is not writing any data, the writing node could be set on the wrong message type, which can be changed at line 20. 