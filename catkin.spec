Name:		catkin
Version:	0.7.26
Release:	1
Summary:	This is ROS melodic Catkin Package
License:	GPL
URL:		https://github.com/ros-gbp/catkin-release/archive/release/melodic/catkin
Source0:	https://github.com/ros-gbp/catkin-release/archive/release/melodic/catkin-0.7.26.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	cmake
#BuildRequires:	python-empy
#BuildRequires:	libpng-devel
#BuildRequires:	libjpeg-turbo-devel
#BuildRequires:	gcc-gfortran
#BuildRequires:	openblas-devel
#BuildRequires:	sqlite-devel
#BuildRequires:	fftw-devel
#BuildRequires:	boost-devel
#BuildRequires:	python3-devel
#BuildRequires:	boost-python3-devel

%description
This is ROS melodic Catkin Package include catkin_make, catkin_init_workspace, and so on.

%prep
%setup -q

#%build


%install




%files 
%defattr(-,root,root)

%changelog
* Thu May 28 2020 openEuler Buildteam <buildteam@openeuler.org> - 19.4-1
- Package init


