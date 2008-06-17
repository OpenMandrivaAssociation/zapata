%define	major 1
%define libname %mklibname zap %{major}
%define develname %mklibname zap -d

Summary:	Zapata Telecom Library
Name:		zapata
Version:	1.0.1
Release:	%mkrel 7
License:	GPL
Group:		System/Libraries
URL:            http://www.asterisk.org/
Source0:	%{name}-%{version}.tar.bz2
Source1:	zapata_Makefile
Patch0:		zapata-1.0.0-mdk.diff
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{develname}
Summary:	Zapata Telecom Library development files
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}
Provides:	libzap-devel = %{version}
Obsoletes:	%{name}-devel
Obsoletes:	%{mklibname zap 1 -d}

%description -n	%{develname}
The Zapata library implements function calls allowing the user
easy access to the telephony functionality.

This package contains the development library and its header
files for the Zapata Telecom Library.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1

cp %{SOURCE1} Makefile

%build

%make \
    CFLAGS="%{optflags} -fPIC -DPIC -D_REENTRANT -Iinclude" \
    libdir=%{_libdir}

%install
rm -rf %{buildroot}

%makeinstall_std \
    libdir=%{_libdir} \
    includedir=%{_includedir}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
