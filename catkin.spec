Name:		catkin
Version:	0.7.26
Release:	1
Summary:	This is ROS melodic Catkin Package
License:	GPL
URL:		https://github.com/ros-gbp/catkin-release/archive/release/melodic/catkin
Source0:	https://github.com/ros-gbp/catkin-release/archive/release/melodic/catkin/0.7.26-1.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	cmake
#BuildRequires:	libX11-devel
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

#%package devel
#Summary:	Development files for dlib
#License:	Boost and Public Domain
#Requires:	%{name}%{?_isa} = %{version}-%{release}

#%description devel
#Dlib is a general purpose cross-platform open source software library written
#in the C++ programming language. This package contains development files for
#the library.

#%package -n python3-%{name}
#Summary:	Python 3 interface to %{name}
#License:	Boost and Public Domain
#%{?python_provide:%python_provide python3-%{name}}

#%description -n python3-%{name}
#Dlib is a general purpose cross-platform open source software library written
#in the C++ programming language. This package contains Python 3 API for the
#library.

#%package_help

%prep
%setup -q
#find docs -type f -exec chmod 644 {} +
#find examples -type f -exec chmod 644 {} +
#mkdir -p build

%build
#pushd build
#%cmake ../dlib
#%make_build
#popd
#%define py_setup_args --no USE_SSE4_INSTRUCTIONS
#%py3_build

%install
#pushd build
#%make_install
#popd
#rm -f %{buildroot}/%{_libdir}/*.a
#rm -f %{buildroot}/%{_docdir}/dlib/LICENSE.txt
#%py3_install
#find %{buildroot}%{python3_sitearch}/dlib/ -type f -name '*.py' -exec sed -i '1s|^#!.*|#!%{__python3}|' {} \;
#find %{buildroot} -name '.*' -exec rm -rf {} +

#%post -p /sbin/ldconfig

#%postun -p /sbin/ldconfig

#%files
#%license dlib/LICENSE.txt
#%{_libdir}/libdlib.so.*

#%files devel
#%{_libdir}/libdlib.so
#%{_includedir}/dlib/
#%{_libdir}/cmake/dlib/
#%{_libdir}/pkgconfig/*.pc

#%files -n python3-%{name}
#%license dlib/LICENSE.txt
#%license python_examples/LICENSE_FOR_EXAMPLE_PROGRAMS.txt
#%{python3_sitearch}/dlib/
#%{python3_sitearch}/dlib-*.egg-info/

%files 
%defattr(-,root,root)
#%license examples/LICENSE_FOR_EXAMPLE_PROGRAMS.txt
#%license examples/video_frames/license.txt
#%doc documentation.html
#%doc docs
#%doc examples
#%exclude %{_docdir}/%{name}-doc/docs/python/.doctrees
#%exclude %{_docdir}/%{name}-doc/docs/python/.buildinfo

%changelog
* Thu May 28 2020 openEuler Buildteam <buildteam@openeuler.org> - 19.4-1
- Package init


