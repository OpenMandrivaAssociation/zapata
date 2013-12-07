%define	major 1.0
%define tone  1
%define libname %mklibname zap %{major}
%define develname %mklibname zap -d

Summary:	Zapata Telecom Library
Name:		zapata
Version:	1.4.12.1
Release:	12
License:	GPL
Group:		System/Libraries
URL:            http://www.asterisk.org/
Source0:	zaptel-%{version}.tar.gz
Source1:	autoconf.h
Patch0:		zaptel-1.4.12.1-printf.diff
Patch1:		zaptel-1.4.12.1-makefile.diff
Patch2:		zaptel-1.4.12.1-firmware.diff
BuildRequires:	libtool
BuildRequires:	kernel-devel
BuildRequires:	wget

%description
The Zapata library implements function calls allowing the user
easy access to the telephony functionality.

%package	firmware
Summary:	Shared Zapata Telecom Library
Group:          System/Libraries

%description 	firmware
The Zapata library implements function calls allowing the user
easy access to the telephony functionality.  These are firmware files.

%package -n	%{name}-tools
Summary:	Shared Zapata Telecom Library
Group:          Communications
Requires:	%{libname} = %{version}

%description -n	%{name}-tools
The Zapata library implements function calls allowing the user
easy access to the telephony functionality.  These are tools files.

%package -n	%{libname}
Summary:	Shared Zapata Telecom Library
Group:          System/Libraries
Requires:	zapata

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

%package -n	perl-%{name}
Summary:	Zapata Telecom Library perl files
Group:		Development/Perl
Provides:	%{name}-perl = %{version}

%description -n	perl-%{name}
The Zapata library implements function calls allowing the user
easy access to the telephony functionality.

This package contains the perl library and its header
files for the Zapata Telecom Library.

%prep
%setup -q -n zaptel-%{version}
%patch0 -p1 -b .fprintf
%patch1 -p1 -b .kernel
%patch2 -p0 -b .firmware
cp %{SOURCE1} .

%build
%configure2_5x

%make \
    CFLAGS="%{optflags} -fPIC -DPIC -D_REENTRANT -Iinclude -DSTANDALONE_ZAPATA -DZAPTEL_CONFIG=\"zaptel.conf\" -DCONFIG_FILENAME\"zaptel.conf\"" \
    libdir=%{_libdir}

%install
install -d %{buildroot}/%{_initrddir}
install -d %{buildroot}/%{_sysconfdir}
install -d %{buildroot}/etc/sysconfig
install -m0644 zaptel.conf.sample %{buildroot}/%{_sysconfdir}/zaptel.conf
install -m0755 zaptel.init %{buildroot}/%{_initrddir}/zaptel
install -m0644 zaptel.sysconfig %{buildroot}/etc/sysconfig/zaptel

%makeinstall_std \
    libdir=%{_libdir} \
    includedir=%{_includedir} 

# (cg) Fix udev rules location
mkdir -p %{buildroot}/lib
mv %{buildroot}%{_sysconfdir}/udev %{buildroot}/lib/
# do not pack it 
# it conflicts with tonezone-devel
rm -f %{buildroot}/%{_libdir}/libtonezone.so

%post
%_post_service zaptel

%preun
%_preun_service zaptel

%files
%{_sysconfdir}/zaptel.conf
%{_initrddir}/zaptel
%{_sysconfdir}/sysconfig/zaptel
/sbin/ztcfg
/sbin/ztmonitor
/sbin/ztscan
/sbin/ztspeed
/sbin/zttest
%{_sbindir}/genzaptelconf
%{_sbindir}/lszaptel
%{_sbindir}/zaptel_hardware
%{_sbindir}/zapconf
%{_sbindir}/zt_registration
%{_mandir}/man8/genzaptelconf.8.xz
%{_mandir}/man8/lszaptel.8.xz
%{_mandir}/man8/zapconf.8.xz
%{_mandir}/man8/zaptel_hardware.8.xz
%{_mandir}/man8/zt_registration.8.xz
%{_mandir}/man8/ztcfg.8.xz
%{_mandir}/man8/ztmonitor.8.xz
%{_mandir}/man8/ztscan.8.xz
%{_mandir}/man8/ztspeed.8.xz
%{_mandir}/man8/zttest.8.xz
%{_datadir}/zaptel/FPGA_1141.hex
%{_datadir}/zaptel/FPGA_1151.hex
%{_datadir}/zaptel/FPGA_FXS.hex
%{_datadir}/zaptel/USB_FW.hex
%{_datadir}/zaptel/init_card_1_30
%{_datadir}/zaptel/init_card_2_30
%{_datadir}/zaptel/init_card_3_30
%{_datadir}/zaptel/init_card_4_30
%{_datadir}/zaptel/init_fxo_modes

%files -n %{name}-tools
/sbin/fxotune
%{_sbindir}/xpp_blink
%{_sbindir}/xpp_sync
%{_datadir}/zaptel/xpp_fxloader
%{_mandir}/man8/xpp_blink.8.xz
%{_mandir}/man8/xpp_sync.8.xz
%{_mandir}/man8/fxotune.8.xz
%{_udevrulesdir}/xpp.rules
%{_sysconfdir}/hotplug/usb/xpp_fxloader
%{_sysconfdir}/hotplug/usb/xpp_fxloader.usermap

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.a

%files -n perl-%{name}
%{perl_sitelib}/Zaptel.pm
%{perl_sitelib}/Zaptel

%files firmware
/lib/firmware/.zaptel*
/lib/firmware/zaptel*
/usr/lib/hotplug/firmware/.zaptel*
/usr/lib/hotplug/firmware/zaptel*
