Summary:	wrapper for the functionalities built into the nxcomp library
Summary(pl):	wrapper dla funkcjonalności wbudowanych w biblioekę nxcomp
Name:		nxproxy
Version:	1.4.0_2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
#Source0Download: http://www.nomachine.com/sources.php
Source0:	http://www.nomachine.com/download/nxsources/%(echo %{version} | cut -f1 -d_)/%{name}-%(echo %{version} | tr _ -).tar.gz
# Source0-md5:	15d89810730c7ed0e669b5525e5f3620
URL:		http://www.nomachine.com/
BuildRequires:	XFree86-devel
BuildRequires:	nxcomp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nxproxy, a stand alone program wrapping the functionalities built into
Xcomp library, needed to compress the X protocol produced by any
standard X client.

%description -l pl
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
