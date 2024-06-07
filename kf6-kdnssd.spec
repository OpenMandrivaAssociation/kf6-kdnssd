%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6DNSSD
%define devname %mklibname KF6DNSSD -d
#define git 20240217

Name: kf6-kdnssd
Version: 6.3.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kdnssd/-/archive/master/kdnssd-master.tar.bz2#/kdnssd-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/kdnssd-%{version}.tar.xz
%endif
Summary: Network service discovery using Zeroconf
URL: https://invent.kde.org/frameworks/kdnssd
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: pkgconfig(avahi-core)
BuildRequires: pkgconfig(avahi-client)
Requires: %{libname} = %{EVRD}

%description
Network service discovery using Zeroconf

%package -n %{libname}
Summary: Network service discovery using Zeroconf
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Network service discovery using Zeroconf

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Network service discovery using Zeroconf

%prep
%autosetup -p1 -n kdnssd-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang

%files -n %{devname}
%{_includedir}/KF6/KDNSSD
%{_libdir}/cmake/KF6DNSSD
%{_qtdir}/doc/KF6DNSSD.*

%files -n %{libname}
%{_libdir}/libKF6DNSSD.so*
