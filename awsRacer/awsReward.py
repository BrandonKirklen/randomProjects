def reward_function (on_track, x, y, distance_from_center, car_orientation, progress, steps, throttle, steering, track_width, waypoints, closest_waypoint):
    import math

    carCords = (x, y)
    waypointCords = ( waypoints[closest_waypoint][0], waypoints[closest_waypoint][1]) 

    def centerReward (distance_from_center, track_width):
        normalizedDistance = distance_from_center/track_width*2
        return (-0.6 + (1.6)/(1 + math.pow((normalizedDistance/0.8025183), 2.321928)))

    def progressReward (progress):
        return (1.221821 + (-0.004925491 - 1.221821)/(1 + math.pow((progress/0.579462), 2.703006)))
    
    def steeringReward (car_orientation, carCords, waypointCords, steering):
        waypoint_orientation = math.atan2((waypointCords[1]-carCords[1]), (waypointCords[0]-carCords[0]))/math.pi
        # Car - Waypoint means negative is left positive is right
        angleOfDifference = car_orientation - waypoint_orientation
        return (1 - math.fabs(steering + angleOfDifference))

    def throttleReward(car_orientation, carCords, waypointCords, steering, throttle):
        waypoint_orientation = math.atan2((waypointCords[1]-carCords[1]), (waypointCords[0]-carCords[0]))/math.pi
        # Car - Waypoint means negative is left positive is right
        angleOfDifference = car_orientation - waypoint_orientation
        if (1 - math.fabs(steering + angleOfDifference)) >= 1:
            return (0.01142857 + 0.1619048*throttle + 2.171429*math.pow(throttle, 2)
                    - math.pow(2.133333*throttle, 3))
        else:
            return (0.01428571 + 3.085714*throttle - 6.285714*math.pow(throttle, 2)
                    + 3.2 * math.pow(x, 3))

    finalReward = (centerReward(distance_from_center, track_width))
                #    + progressReward(progress)
                #    + steeringReward(car_orientation, carCords, waypointCords, steering)
                #    + throttleReward(car_orientation, carCords, waypointCords, steering, throttle))

    return float(finalReward)


