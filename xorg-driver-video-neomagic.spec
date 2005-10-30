Summary:	X.org video driver for Neomagic graphics chipsets
Summary(pl):	Sterownik obrazu X.org dla uk³adów graficznych Neomagic
Name:		xorg-driver-video-neomagic
Version:	1.0.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-neomagic-%{version}.tar.bz2
# Source0-md5:	fdae85c9508806efb09078e53a0f709e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Neomagic graphics chipsets found in many laptop
computers. It supports the following chipsets: MagicGraph 128
(NM2070), MagicGraph 128V (NM2090), MagicGraph 128ZV (NM2093),
MagicGraph 128ZV+ (NM2097), MagicGraph 128XD (NM2160), MagicGraph
256AV (NM2200), MagicGraph 256AV+ (NM2230), MagicGraph 256ZX (NM2360),
MagicGraph 256XL+ (NM2380).

%description -l pl
Sterownik obrazu X.org dla uk³adów graficznych Neomagic, jakie mo¿na
znale¼æ w wielu laptopach. Obs³uguje nastêpuj±ce uk³ady: MagicGraph
128 (NM2070), MagicGraph 128V (NM2090), MagicGraph 128ZV (NM2093),
MagicGraph 128ZV+ (NM2097), MagicGraph 128XD (NM2160), MagicGraph
256AV (NM2200), MagicGraph 256AV+ (NM2230), MagicGraph 256ZX (NM2360),
MagicGraph 256XL+ (NM2380).

%prep
%setup -q -n xf86-video-neomagic-%{version}

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
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/neomagic_drv.so
%{_mandir}/man4/neomagic.4x*
