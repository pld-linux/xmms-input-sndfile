
%define		_orig_name	xmms_sndfile

Summary:	XMMS input plugin that uses libsndfile to read files
Summary(pl.UTF-8):	Wtyczka wejściowa dla XMMS-a używająca libsndfile do czytania plików
Name:		xmms-input-sndfile
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.zipworld.com.au/~erikd/XMMS/%{_orig_name}-%{version}.tar.gz
# Source0-md5:	6028307cf7b1310f0c302a4a0c212ae9
URL:		http://www.xmms.org/plugins_input.html#122
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmms_sndfile is an input plugin for XMMS. Using xmms_sndfile extends
the capabilities of XMMS to open and play any file which can be opened
and read by libsndfile, including WAV, AIFF, AU, and SVX files and
many compressed version of these file formats.

%description -l pl.UTF-8
xmms_sndfile to wtyczka wejściowa dla XMMS-a. Jej użycie rozszerza
możliwości XMMS-a o otwieranie i odtwarzanie dowolnych plików, które
można otworzyć i odczytać przy pomocy biblioteki libsndfile, w tym
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

# useless
rm -f $RPM_BUILD_ROOT%{xmms_input_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO NEWS README ChangeLog
%attr(755,root,root) %{xmms_input_plugindir}/*.so
