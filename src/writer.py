#!/usr/bin/env python
import rospy
import time  
import os
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
import random
import json


class Writer():
    def __init__(self): 
        
        rospy.init_node('Writer', anonymous=True)
        # Launch file params
        self.target = rospy.get_param("target_publisher") # I should probaly make this a function that is try excpet case
        self.file_type = rospy.get_param('file_type')
        rospy.loginfo_once("The writer is created.")
        self.file = None
        self.is_file_open = False
        self.sub = rospy.Subscriber(self.target, PoseStamped, self.writer_callback)

    '''
    def file_filter(self, raw_message):
        # Parse the raw message into the wanted parts
        parsed_msg = {}
        parsed_msg['seq'] = raw_message.header.seq
        parsed_msg['secs'] = raw_message.header.stamp.secs
        parsed_msg['nsecs'] = raw_message.header.stamp.nsecs
        parsed_msg['pose_x'] = raw_message.pose.position.x
        parsed_msg['pose_y'] = raw_message.pose.position.y
        parsed_msg['pose_z'] = raw_message.pose.position.z
        return parsed_msg
    '''

    def writer_callback(self, data):
        # The callback that creates the file and writes to the file
        if(self.is_file_open):
            if self.file_type == ".json":
                filter_data = self.file_filter(data)
                cleaned = json.dumps(filter_data)
                self.file.write(cleaned+",")
            else:
                filter_data = self.file_filter(data)
                self.file.write(str(filter_data)+","+"\n")
        else: 
            cwd = os.getcwd()
        
            fileName = cwd+"/"+str(random.randint(1,100000000)) +self.file_type 
            self.file = open(fileName,"w")
            if self.file_type == ".json":
                self.file.write("[") 
            self.is_file_open = True
            rospy.loginfo_once("Created File! The file is located at "+ fileName)

    def close(self):
        rospy.loginfo_once("Closing File!") 
        self.file.close()



if __name__ == "__main__":
    try:
        writer = Writer()
        rospy.spin()
    except rospy.ROSInterruptException:
        self.file.write("]")
        writer.close()