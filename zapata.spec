%define	major	1
%define libname	%mklibname zap %{major}

Summary:	Zapata Telecom Library
Name:		zapata
Version:	1.0.1
Release:	%mkrel 6
License:	GPL
Group:		System/Libraries
URL:            http://www.asterisk.org/
Source0:	%{name}-%{version}.tar.bz2
Source1:	zapata_Makefile.bz2
Patch0:		zapata-1.0.0-mdk.diff
BuildRequires:	libtool

%description
The Zapata library implements function calls allowing the user
easy access to the telephony functionality.

%package -n	%{libname}
Summary:	Shared Zapata Telecom Library
Group:          System/Libraries
#Obsoletes:	%{name}
#Provides:	%{name}

%description -n	%{libname}
The Zapata library implements function calls allowing the user
easy access to the telephony functionality.

%package -n	%{libname}-devel
Summary:	Zapata Telecom Library development files
Group:		Development/C
Obsoletes:	%{name}-devel libzap-devel
Provides:	%{name}-devel = %{version}
Provides:	libzap-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
The Zapata library implements function calls allowing the user
easy access to the telephony functionality.

This package contains the development library and its header
files for the Zapata Telecom Library.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1

bzcat %{SOURCE1} > Makefile

%build

%make \
    CFLAGS="%{optflags} -fPIC -DPIC -D_REENTRANT -Iinclude" \
    libdir=%{_libdir}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std \
    libdir=%{_libdir} \
    includedir=%{_includedir}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la

