cmake_minimum_required(VERSION 3.5)

PROJECT(test)

ADD_EXECUTABLE( test test.cpp )

FIND_PACKAGE( Boost 1.55 COMPONENTS thread date_time REQUIRED )
INCLUDE_DIRECTORIES( ${Boost_INCLUDE_DIR} )
TARGET_LINK_LIBRARIES( test ${Boost_LIBRARIES} )
