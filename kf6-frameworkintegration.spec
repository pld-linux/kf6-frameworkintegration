#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	6.15
%define		qtver		5.15.2
%define		kfname		frameworkintegration

Summary:	HTML rendering engine
Name:		kf6-%{kfname}
Version:	6.15.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	d907c070c53a2a350aa79afc9a012544
URL:		http://www.kde.org/
BuildRequires:	AppStream-qt6-devel >= 1.0
BuildRequires:	PackageKit-qt6-devel
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	fonts-TTF-KDE-Oxygen-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-attica-devel >= %{version}
BuildRequires:	kf6-extra-cmake-modules >= %{version}
BuildRequires:	kf6-kauth-devel >= %{version}
BuildRequires:	kf6-kbookmarks-devel >= %{version}
BuildRequires:	kf6-kcodecs-devel >= %{version}
BuildRequires:	kf6-kcompletion-devel >= %{version}
BuildRequires:	kf6-kconfig-devel >= %{version}
BuildRequires:	kf6-kconfigwidgets-devel >= %{version}
BuildRequires:	kf6-kcoreaddons-devel >= %{version}
BuildRequires:	kf6-kdbusaddons-devel >= %{version}
BuildRequires:	kf6-kglobalaccel-devel >= %{version}
BuildRequires:	kf6-kguiaddons-devel >= %{version}
BuildRequires:	kf6-ki18n-devel >= %{version}
BuildRequires:	kf6-kiconthemes-devel >= %{version}
BuildRequires:	kf6-kio-devel >= %{version}
BuildRequires:	kf6-kitemviews-devel >= %{version}
BuildRequires:	kf6-kjobwidgets-devel >= %{version}
BuildRequires:	kf6-knewstuff-devel >= %{version}
BuildRequires:	kf6-knotifications-devel >= %{version}
BuildRequires:	kf6-kservice-devel >= %{version}
BuildRequires:	kf6-ktextwidgets-devel >= %{version}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf6-kwindowsystem-devel >= %{version}
BuildRequires:	kf6-kxmlgui-devel >= %{version}
BuildRequires:	kf6-solid-devel >= %{version}
BuildRequires:	kf6-sonnet-devel >= %{version}
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	kf6-dirs
#Obsoletes:	kf5-%{kfname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
KHTML is a web rendering engine, based on the KParts technology and
using KJS for JavaScript support.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
#Obsoletes:	kf5-%{kfname}-devel < %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKF6Style.so.6
%attr(755,root,root) %{_libdir}/libKF6Style.so.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/FrameworkIntegrationPlugin.so
%{_datadir}/knotifications6/plasma_workspace.notifyrc
%dir %{_prefix}/libexec/kf6/kpackagehandlers
%attr(755,root,root) %{_prefix}/libexec/kf6/kpackagehandlers/knshandler
%attr(755,root,root) %{_prefix}/libexec/kf6/kpackagehandlers/appstreamhandler

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/KStyle
%{_includedir}/KF6/FrameworkIntegration
%{_libdir}/cmake/KF6FrameworkIntegration
%{_libdir}/libKF6Style.so
