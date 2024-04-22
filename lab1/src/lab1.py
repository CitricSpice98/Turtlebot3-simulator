#! /usr/bin/env python3

# importing libraries and dependencies
from hashlib import new
from turtle import distance, position
from unicodedata import name
import rospy
import math
import random
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

# Function Definition - Publisher Node
def publisher_node() :
    publisher = rospy.Publisher('/husky_velocity_controller/cmd_vel',Twist,queue_size=1)
    rospy.init_node('publisher_node',anonymous=True)
    rate = rospy.Rate(1)
    subscriber_node()
    # Loop to generate and publish randomised float values for linear and angular coordinates
    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = random.uniform(0,maxLin)
        msg.angular.z = random.uniform(-maxAng,maxAng)
        rospy.loginfo(msg)
        publisher.publish(msg)
        rate.sleep()

# Function Definition - Subscriber node is called
def subscriber_node() :
    rospy.Subscriber('/odometry/filtered',Odometry,callback)

# Function Definition - Callback function 
def callback(subscriber_data) :
    position_data = subscriber_data.pose.pose.position
    position_X_coordinate = position_data.x
    position_y_coordinate = position_data.y
    position_z_coordinate = position_data.z
    origin_x_coordinate = 0.0
    origin_y_coordinate = 0.0
    origin_z_coordinate = 0.0
    #Calculating Euclidian distance between current postion and origin, formatting distance and logging
    distance_covered = math.dist([position_X_coordinate,position_y_coordinate,position_z_coordinate],[origin_x_coordinate,origin_y_coordinate,origin_z_coordinate])
    formatted_distance = "{:.2f}".format(distance_covered)
    rospy.loginfo(formatted_distance)

#Print and recieve input values
if __name__ == '__main__':
    print("hello world")
    maxLin = float(input("Enter the value for maximum linear coordinates : "))
    maxAng = float(input("Enter the value for maximum angular coordinates : "))
    publisher_node()





