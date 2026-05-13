FROM osrf/ros:jazzy-desktop

# Install Gazebo Harmonic and all ROS-GZ dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gz-harmonic \
    ros-jazzy-ros-gz \
    ros-jazzy-ros-gz-bridge \
    ros-jazzy-ros-gz-sim \
    ros-jazzy-robot-state-publisher \
    ros-jazzy-joint-state-publisher \
    ros-jazzy-joint-state-publisher-gui \
    ros-jazzy-xacro \
    ros-jazzy-rviz2 \
    ros-jazzy-teleop-twist-keyboard \
    ros-jazzy-tf2-ros \
    python3-colcon-common-extensions \
    python3-rosdep \
    && rm -rf /var/lib/apt/lists/*

# Source ROS 2 and workspace overlay in every shell
RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc && \
    echo "[ -f /workspaces/openamrobot_ws/install/setup.bash ] && source /workspaces/openamrobot_ws/install/setup.bash" >> /root/.bashrc

WORKDIR /workspaces/openamrobot_ws

# Allow Gazebo to find package meshes and worlds
ENV GZ_SIM_RESOURCE_PATH=/workspaces/openamrobot_ws/install/openamrobot_description/share:/workspaces/openamrobot_ws/install/openamrobot_gazebo/share
