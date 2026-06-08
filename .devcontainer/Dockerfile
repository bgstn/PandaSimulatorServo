FROM chillerrobot/ros-noetic-moveit-panda:first

# Remove ROS apt source to prevent GPG key expiry errors during feature installation.
# All ROS packages are already installed in the base image.
RUN rm -f /etc/apt/sources.list.d/ros*.list /etc/apt/sources.list.d/ros1*.list

#RUN apt-get install -y --no-install-recommends *add your installs here*
RUN apt update && apt install -y vim

#RUN pip3 install *add your packages here*

RUN echo "source ./catkin_ws/devel/setup.bash" >> ~/.bashrc