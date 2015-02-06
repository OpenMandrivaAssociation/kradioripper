Summary:	Ripping internet radios
Name:		kradioripper
Version:	0.6
Release:	4
License:	GPLv2+
Group:		Sound
Url:		http://kradioripper.sourceforge.net/
Source0:	http://downloads.sourceforge.net/kradioripper/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
Requires:	streamripper >= 1.63

%description
KRadioRipper is a KDE4 program for ripping internet radios. It is based on
StreamRipper.

%files -f %{name}.lang
%doc NEWS
%{_kde_bindir}/*
%{_kde_applicationsdir}/*.desktop
%{_kde_appsdir}/%{name}/
%{_kde_datadir}/config.kcfg/*.kcfg

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}

find . -perm 600 -exec chmod 644 "{}" \;

%build
%cmake_kde4 -DWITHOUT_LIBPROXY=YES
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

