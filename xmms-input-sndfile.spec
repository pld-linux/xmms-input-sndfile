
%define		_orig_name	xmms_sndfile

Summary:	XMMS input plugin
Summary(pl):	Wtyczka wej¶ciowa XMMS
Name:		xmms-input-sndfile
Version:	1.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.zipworld.com.au/~erikd/XMMS/%{_orig_name}-%{version}.tar.gz
# Source0-md5:	6028307cf7b1310f0c302a4a0c212ae9
URL:		http://www.xmms.org/plugins_input.html#122
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmms_sndfile is an input plugin for XMMS. Using xmms_sndfile extends
the capabilities of XMMS to open and play any file which can be opened
and read by libsndfile, including WAV, AIFF, AU, and SVX files and
many compressed version of these file formats.

%description -l pl
xmms_sndfile to wtyczka wej¶ciowa dla XMMS-a. Jej u¿ycie rozszerza
mo¿liwo¶ci XMMS-a o otwieranie i odtwarzanie dowolnych plików, które
mo¿na otworzyæ i odczytaæ przy pomocy biblioteki libsndfile, w tym
WAV, AIFF, AU i SVX oraz wiele skompresowanych wersji tych formatów.

%prep
%setup -q -n %{_orig_name}-%{version}

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO NEWS README ChangeLog
%attr(755,root,root) %{_libdir}/xmms/Input/*.so
