# Install script for directory: /home/shantam/catkin_ws/src/youbot_gui/src/youbot_ros_samples/youbot_ros_simple_trajectory

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/shantam/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/shantam/catkin_ws/build/youbot_gui/src/youbot_ros_samples/youbot_ros_simple_trajectory/catkin_generated/installspace/youbot_ros_simple_trajectory.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/youbot_ros_simple_trajectory/cmake" TYPE FILE FILES
    "/home/shantam/catkin_ws/build/youbot_gui/src/youbot_ros_samples/youbot_ros_simple_trajectory/catkin_generated/installspace/youbot_ros_simple_trajectoryConfig.cmake"
    "/home/shantam/catkin_ws/build/youbot_gui/src/youbot_ros_samples/youbot_ros_simple_trajectory/catkin_generated/installspace/youbot_ros_simple_trajectoryConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/youbot_ros_simple_trajectory" TYPE FILE FILES "/home/shantam/catkin_ws/src/youbot_gui/src/youbot_ros_samples/youbot_ros_simple_trajectory/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory" TYPE EXECUTABLE FILES "/home/shantam/catkin_ws/devel/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory"
         OLD_RPATH "/opt/ros/kinetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory")
    endif()
  endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory" TYPE EXECUTABLE FILES "/home/shantam/catkin_ws/devel/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory"
         OLD_RPATH "/opt/ros/kinetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/youbot_ros_simple_trajectory/youbot_ros_simple_trajectory")
    endif()
  endif()
endif()

