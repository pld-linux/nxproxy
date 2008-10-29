%define		_version_major	3.2.0
%define		_version_minor	1

Summary:	Wrapper for the functionalities built into the nxcomp library
Summary(pl.UTF-8):	Wrapper dla funkcjonalności wbudowanych w biblioekę nxcomp
Name:		nxproxy
Version:	%{_version_major}.%{_version_minor}
Release:	2
License:	GPL
Group:		X11/Applications/Networking
#Source0Download: http://www.nomachine.com/sources.php
Source0:	http://64.34.161.181/download/%{_version_major}/sources/%{name}-%{_version_major}-%{_version_minor}.tar.gz
# Source0-md5:	ac31e8f2f112e3720f3c00cec67c0734
URL:		http://www.nomachine.com/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	nxcomp-devel
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nxproxy, a stand alone program wrapping the functionalities built into
Xcomp library, needed to compress the X protocol produced by any
standard X client.

%description -l pl.UTF-8
nxproxy to samodzielny program obudowujący funkcjonalności wbudowane w
bibliotekę Xcomp, potrzebne do kompresji protokołu X wytwarzanego
przez dowolnego standardowego klienta X.

%prep
%setup -q -n %{name}
sed -i 's/CXXFLAGS="-O3"/CXXFLAGS="%{rpmcflags}"/' configure.in
sed -i 's/CPPFLAGS="-O3"/CPPFLAGS="%{rpmcflags}"/' configure.in

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%attr(755,root,root) %{_bindir}/*
