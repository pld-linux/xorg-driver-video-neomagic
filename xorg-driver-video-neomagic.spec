Summary:	X.org video driver for Neomagic graphics chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych Neomagic
Name:		xorg-driver-video-neomagic
Version:	1.3.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-neomagic-%{version}.tar.xz
# Source0-md5:	737c60a2cd12eb2bf14fbdb08d5ca27f
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.0.99.901
Provides:	xorg-driver-video
Obsoletes:	X11-driver-neomagic < 1:7.0.0
Obsoletes:	XFree86-NeoMagic < 4
Obsoletes:	XFree86-driver-neomagic < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Neomagic graphics chipsets found in many laptop
computers. It supports the following chipsets:
- MagicGraph 128 (NM2070),
- MagicGraph 128V (NM2090),
- MagicGraph 128ZV (NM2093),
- MagicGraph 128ZV+ (NM2097),
- MagicGraph 128XD (NM2160),
- MagicGraph 256AV (NM2200),
- MagicGraph 256AV+ (NM2230),
- MagicGraph 256ZX (NM2360),
- MagicGraph 256XL+ (NM2380).

%description -l pl.UTF-8
Sterownik obrazu X.org dla układów graficznych Neomagic, jakie można
znaleźć w wielu laptopach. Obsługuje następujące układy:
- MagicGraph 128 (NM2070),
- MagicGraph 128V (NM2090),
- MagicGraph 128ZV (NM2093),
- MagicGraph 128ZV+ (NM2097),
- MagicGraph 128XD (NM2160),
- MagicGraph 256AV (NM2200),
- MagicGraph 256AV+ (NM2230),
- MagicGraph 256ZX (NM2360),
- MagicGraph 256XL+ (NM2380).

%prep
%setup -q -n xf86-video-neomagic-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/neomagic_drv.so
%{_mandir}/man4/neomagic.4*
