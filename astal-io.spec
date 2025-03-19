%global astal_commit 69efb4c91e590adcb5a3d8938454f987982e3891
%global astal_shortcommit %(c=%{astal_commit}; echo ${c:0:7})
%global bumpver 1

%global _vpath_srcdir lib/astal/io

%define libname %mklibname astal-io
%define devname %mklibname astal-io -d

Name:		astal-io
Version:	0~%{bumpver}.git%{astal_shortcommit}
Release:	1
Source0:	https://github.com/aylur/astal/archive/%{astal_commit}/%{name}-%{astal_shortcommit}.tar.gz
Summary:	Building blocks for creating custom desktop shells
URL:		https://github.com/astal-io/astal-io
License:	LGPL-2.1-only
Group:		System/Libraries
BuildRequires:	meson
BuildSystem:	meson

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  vala
BuildRequires:  valadoc
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(python-gobject3)

%description

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Provides:    libastal-io = %{EVRD}

%description -n %{libname}

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:    astal-io-devel = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -n astal-%{astal_commit} -p1

%files
%license LICENSE
%{_bindir}/astal

%files -n %{libname}
%{_libdir}/libastal-io.so.*
%{_libdir}/girepository-1.0/AstalIO-0.1.typelib



%files -n %{devname}
%{_includedir}/astal-io.h
%{_datadir}/*
%{_libdir}/pkgconfig/astal-io-0.1.pc
%{_libdir}/libastal-io.so


