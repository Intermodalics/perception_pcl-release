Name:           ros-lunar-pcl-ros
Version:        1.5.2
Release:        0%{?dist}
Summary:        ROS pcl_ros package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/perception_pcl
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       pcl-devel
Requires:       proj-devel
Requires:       ros-lunar-dynamic-reconfigure
Requires:       ros-lunar-message-filters
Requires:       ros-lunar-nodelet
Requires:       ros-lunar-nodelet-topic-tools
Requires:       ros-lunar-pcl-conversions
Requires:       ros-lunar-pcl-msgs
Requires:       ros-lunar-pluginlib
Requires:       ros-lunar-rosbag
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-tf
Requires:       ros-lunar-tf2-eigen
Requires:       vtk-java
BuildRequires:  eigen3-devel
BuildRequires:  pcl-devel
BuildRequires:  proj-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cmake-modules
BuildRequires:  ros-lunar-dynamic-reconfigure
BuildRequires:  ros-lunar-genmsg
BuildRequires:  ros-lunar-message-filters
BuildRequires:  ros-lunar-nodelet
BuildRequires:  ros-lunar-nodelet-topic-tools
BuildRequires:  ros-lunar-pcl-conversions
BuildRequires:  ros-lunar-pcl-msgs
BuildRequires:  ros-lunar-pluginlib
BuildRequires:  ros-lunar-rosbag
BuildRequires:  ros-lunar-rosconsole
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-roslib
BuildRequires:  ros-lunar-rostest
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-tf
BuildRequires:  ros-lunar-tf2-eigen
BuildRequires:  vtk-java

%description
PCL (Point Cloud Library) ROS interface stack. PCL-ROS is the preferred bridge
for 3D applications involving n-D Point Clouds and 3D geometry processing in
ROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Sat Apr 29 2017 Paul Bovbel <paul@bovbel.com> - 1.5.2-0
- Autogenerated by Bloom

* Sat Apr 29 2017 Paul Bovbel <paul@bovbel.com> - 1.5.1-3
- Autogenerated by Bloom

* Thu Apr 27 2017 Paul Bovbel <paul@bovbel.com> - 1.5.1-2
- Autogenerated by Bloom

* Wed Apr 26 2017 Paul Bovbel <paul@bovbel.com> - 1.5.1-1
- Autogenerated by Bloom

* Wed Apr 26 2017 Paul Bovbel <paul@bovbel.com> - 1.5.1-0
- Autogenerated by Bloom

