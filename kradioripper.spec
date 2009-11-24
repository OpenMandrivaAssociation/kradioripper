Summary:	Ripping internet radios
Name:		kradioripper
Version: 	0.6
Release: 	%mkrel 1
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
