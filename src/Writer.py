#!usr/bin/env python
import rospy
import time  

class Writer():
    def __init__(self): 
        
        rospy.init_node('Writer', anonymous=True)
        target = rospy.get_param("target_publisher", "/camera_pose") # I should probaly make this a function that is try excpet case
        self.img_sub = rospy.Subscriber(target, Image, writer_callback)
        rospy.loginfo_once("The writer is created.")
        file = None; 
        is_file_open = False
        

    def writer_callback(self, data):
        if(self.is_file_open):
            self.file.write(data);
        else: 
            self.file.open(time.localtime()) 
            self.is_file_open = True






if __name__ == "__main__":
    try:
        writer = Writer()
        rospy.spin();
    except rospy.ROSInterruptException:
        pass