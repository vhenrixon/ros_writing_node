#!/usr/bin/env python
import rospy
import time  
import os
from geometry_msgs.msg import PoseStamped 
import random

class Writer():
    def __init__(self): 
        
        rospy.init_node('Writer', anonymous=True)
        self.target = rospy.get_param("target_publisher", "/camera_pose") # I should probaly make this a function that is try excpet case
        rospy.loginfo_once("The writer is created.")
        self.file = None
        self.is_file_open = False
        self.sub = rospy.Subscriber(self.target, PoseStamped, self.writer_callback)


    def writer_callback(self, data):
        if(self.is_file_open):
            self.file.write(str(data)+",")
        else: 
            cwd = os.getcwd()
            fileName = cwd +"/"+self.target+str(random.randint(1,100000000)) +".csv" 
            self.file = open(fileName,"w") 
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
        writer.close()
        pass