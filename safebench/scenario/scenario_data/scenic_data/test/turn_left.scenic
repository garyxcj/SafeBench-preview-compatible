'''The ego starts an unprotected left turn at an intersection while yielding to an oncoming car when the oncoming car's throttle malfunctions, leading to an unexpected acceleration and forcing the ego to quickly modify its turning path to avoid a collision.
'''

param map = localPath('../maps/Town05.xodr') 
param carla_map = 'Town05'
model scenic.simulators.carla.model
EGO_MODEL = "vehicle.tesla.model3"

## MONITORS
monitor TrafficLights:
    freezeTrafficLights()
    while True:
        if withinDistanceToTrafficLight(ego, 100):
            setClosestTrafficLightStatus(ego, "green")
        if withinDistanceToTrafficLight(adversary, 100):
            setClosestTrafficLightStatus(adversary, "green")
        wait

behavior AdversaryBehavior(SPEED, TRAJECTORY, DISTANCE):
    try:
        do FollowTrajectoryBehavior(SPEED, trajectory=TRAJECTORY)
    interrupt when (distance from self to ego) < DISTANCE:
        take SetThrottleAction(1)
    
intersection = Uniform(*filter(lambda i: i.is4Way and i.isSignalized, network.intersections))
egoInitLane = Uniform(*intersection.incomingLanes)
egoManeuver = Uniform(*filter(lambda m: m.type is ManeuverType.LEFT_TURN, egoInitLane.maneuvers))
egoTrajectory = [egoInitLane, egoManeuver.connectingLane, egoManeuver.endLane]

advManeuvers = filter(lambda i: i.type == ManeuverType.STRAIGHT, egoManeuver.conflictingManeuvers)
advManeuver = Uniform(*advManeuvers)
advTrajectory = [advManeuver.startLane, advManeuver.connectingLane, advManeuver.endLane]

egoSpawnPt = OrientedPoint in egoManeuver.startLane.centerline
advSpawnPt = advManeuver.connectingLane.centerline[0]

route_0 = egoSpawnPt.position.coordinates
route_1 = egoTrajectory[0].centerline.end.position.coordinates
route_2 = egoTrajectory[1].centerline.end.position.coordinates
route_3 = egoTrajectory[2].centerline.end.position.coordinates
param Trajectory = [route_0, route_1, route_2, route_3]

ego = Car at egoSpawnPt,
    with blueprint EGO_MODEL

adversary = Car following roadDirection from advSpawnPt for Range(-5, 0),
    with behavior AdversaryBehavior(Range(6, 10), advTrajectory, Range(35, 45))
    
require 25 <= (distance to intersection) <= 45
require 160 deg <= abs(RelativeHeading(adversary)) <= 180 deg
require adversary in advManeuver.startLane or adversary in advManeuver.connectingLane

