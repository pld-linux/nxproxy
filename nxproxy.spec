%define		_version_major	2.0.0
%define		_version_minor	2

Summary:	Wrapper for the functionalities built into the nxcomp library
Summary(pl):	Wrapper dla funkcjonalno¶ci wbudowanych w biblioekê nxcomp
Name:		nxproxy
Version:	%{_version_major}.%{_version_minor}
Release:	1
License:	GPL
Group:		X11/Applications/Networking
#Source0Download: http://www.nomachine.com/sources.php
Source0:	http://64.34.161.181/download/%{_version_major}/sources/%{name}-%{_version_major}-%{_version_minor}.tar.gz
# Source0-md5:	b078c19372c82e85667cbbac880fa688
URL:		http://www.nomachine.com/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	nxcomp-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nxproxy, a stand alone program wrapping the functionalities built into
Xcomp library, needed to compress the X protocol produced by any
standard X client.

%description -l pl
nxproxy to samodzielny program obudowuj±cy funkcjonalno¶ci wbudowane w
bibliotekê Xcomp, potrzebne do kompresji protoko³u X wytwarzanego
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
