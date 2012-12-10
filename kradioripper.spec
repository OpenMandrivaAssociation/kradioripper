Summary:	Ripping internet radios
Name:		kradioripper
Version: 	0.6
Release: 	%mkrel 2
Source0: 	http://downloads.sourceforge.net/kradioripper/%{name}-%{version}.tar.bz2
License: 	GPLv2
Group: 		Sound
Url: 		http://kradioripper.sourceforge.net/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdelibs4-devel
#BuildRequires:	libproxy-devel
Requires:	streamripper >= 1.63

%description 
KRadioRipper is a KDE 4 program for ripping internet radios. It is based on
StreamRipper.

%if %mdkversion < 200900
%post
%update_menus

%postun
%update_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc NEWS
%_kde_bindir/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/%name
%_kde_datadir/config.kcfg/*.kcfg

#--------------------------------------------------------------------

%prep
%setup -q -n %name

%build
%cmake_kde4 -DWITHOUT_LIBPROXY=YES
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang %name --with-html

%clean
rm -rf %{buildroot}


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-2mdv2011.0
+ Revision: 612667
- the mass rebuild of 2010.1 packages

* Tue Nov 24 2009 Funda Wang <fwang@mandriva.org> 0.6-1mdv2010.1
+ Revision: 469409
- drop proxy support as there are some linkging problems regarding current libproxy 0.2.3
- BR proxy
- new version 0.6

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 0.5-1mdv2010.0
+ Revision: 370543
- New version 0.5

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 0.4.1-1mdv2009.1
+ Revision: 292023
- import kradioripper


