%define	major 1
%define libname %mklibname zap %{major}
%define develname %mklibname zap -d

Summary:	Zapata Telecom Library
Name:		zapata
Version:	1.0.1
Release:	9
License:	GPL
Group:		System/Libraries
URL:            http://www.asterisk.org/
Source0:	%{name}-%{version}.tar.bz2
Source1:	zapata_Makefile
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

%package -n	%{develname}
Summary:	Zapata Telecom Library development files
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}
Provides:	libzap-devel = %{EVRD}
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
%makeinstall_std \
    libdir=%{_libdir} \
    includedir=%{_includedir}


%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-8mdv2010.0
+ Revision: 435377
- rebuild

* Tue Jun 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-7mdv2009.0
+ Revision: 223775
- fix linkage
- fix devel package naming

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.0.1-6mdv2008.1
+ Revision: 141006
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Aug 03 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-6mdv2007.0
- fix typo

* Wed Aug 02 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdv2007.0
- rebuild

* Sun May 07 2006 Stefan van der Eijk <stefan@eijk.nu> 1.0.1-4mdk
- BuildRequires: libtool

* Fri Sep 16 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdk
- maintain our own libtool aware makefile

* Fri Sep 02 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdk
- rebuild

* Thu Jul 21 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.1-1mdk
- New release 1.0.1

* Sun Mar 13 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0.0-3mdk
- use the %%mkrel macro

* Sun Dec 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0.0-2mdk
- use newer zaptel header in P0
- use also -DPIC -D_REENTRANT in CFLAGS

* Fri Sep 24 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0.0-1mdk
- 1.0.0
- fix url

* Sat Sep 11 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-0.RC2.1mdk
- initial mandrake package

