Summary:	X.org video driver for Neomagic graphics chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych Neomagic
Name:		xorg-driver-video-neomagic
Version:	1.2.4
Release:	5
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-neomagic-%{version}.tar.bz2
# Source0-md5:	2d722ee9b9fe8da49109f280689c9c25
Patch0:		neomagic-usleep.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:  rpmbuild(macros) >= 1.389
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.0.99.901
Obsoletes:	X11-driver-neomagic < 1:7.0.0
Obsoletes:	XFree86-NeoMagic
Obsoletes:	XFree86-driver-neomagic < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Neomagic graphics chipsets found in many laptop
computers. It supports the following chipsets: MagicGraph 128
(NM2070), MagicGraph 128V (NM2090), MagicGraph 128ZV (NM2093),
MagicGraph 128ZV+ (NM2097), MagicGraph 128XD (NM2160), MagicGraph
256AV (NM2200), MagicGraph 256AV+ (NM2230), MagicGraph 256ZX (NM2360),
MagicGraph 256XL+ (NM2380).

%description -l pl.UTF-8
Sterownik obrazu X.org dla układów graficznych Neomagic, jakie można
znaleźć w wielu laptopach. Obsługuje następujące układy: MagicGraph
128 (NM2070), MagicGraph 128V (NM2090), MagicGraph 128ZV (NM2093),
MagicGraph 128ZV+ (NM2097), MagicGraph 128XD (NM2160), MagicGraph
256AV (NM2200), MagicGraph 256AV+ (NM2230), MagicGraph 256ZX (NM2360),
MagicGraph 256XL+ (NM2380).

%prep
%setup -q -n xf86-video-neomagic-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/neomagic_drv.so
%{_mandir}/man4/neomagic.4*
