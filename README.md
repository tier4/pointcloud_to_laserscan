# ROS 2 pointcloud <-> laserscan converters

This is a ROS 2 package that provides components to convert `sensor_msgs/msg/PointCloud2` messages to `sensor_msgs/msg/LaserScan` messages and back.
It is essentially a port of the original ROS 1 package.

## pointcloud\_to\_laserscan::PointCloudToLaserScanNode

This ROS 2 component projects `sensor_msgs/msg/PointCloud2` messages into `sensor_msgs/msg/LaserScan` messages.

### Published Topics

* `scan` (`sensor_msgs/msg/LaserScan`) - The output laser scan.

### Subscribed Topics

* `cloud_in` (`sensor_msgs/msg/PointCloud2`) - The input point cloud. No input will be processed if there isn't at least one subscriber to the `scan` topic.

### Parameters

#### pointcloud\_to\_laserscan\_node

{{ json_to_markdown("src/schema/pointcloud_to_laserscan.schema.json") }}

#### laserscan\_to\_pointcloud\_node

{{ json_to_markdown("src/schema/laserscan_to_pointcloud.schema.json") }}

## pointcloud\_to\_laserscan::LaserScanToPointCloudNode

This ROS 2 component re-publishes `sensor_msgs/msg/LaserScan` messages as `sensor_msgs/msg/PointCloud2` messages.

### Published Topics

* `cloud` (`sensor_msgs/msg/PointCloud2`) - The output point cloud.

### Subscribed Topics

* `scan_in` (`sensor_msgs/msg/LaserScan`) - The input laser scan. No input will be processed if there isn't at least one subscriber to the `cloud` topic.

### Parameters

* `queue_size` (double, default: detected number of cores) - Input laser scan queue size.
* `target_frame` (str, default: none) - If provided, transform the pointcloud into this frame before converting to a laser scan. Otherwise, laser scan will be generated in the same frame as the input point cloud.
* `transform_tolerance` (double, default: 0.01) - Time tolerance for transform lookups. Only used if a `target_frame` is provided.
* `use_inf` (boolean, default: true) - If disabled, report infinite range (no obstacle) as range_max + 1. Otherwise report infinite range as +inf.
