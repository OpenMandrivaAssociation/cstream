Summary:	A general-purpose stream-handling tool
Name:		cstream
Version:	2.7.6
Release:	%mkrel 3
License:	MIT
Group:		Archiving/Backup
Url:		https://www.cons.org/cracauer/cstream.html
Source0:	http://www.cons.org/cracauer/download/cstream-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	autoconf2.5

%description
cstream is a general-purpose stream-handling tool like UNIX' dd,
usually used in commandline-constructed pipes.

%prep
%setup -q

%build
aclocal && autoconf && automake
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall
mkdir -p %{buildroot}/bin
mv -f %{buildroot}%{_bindir}/cstream %{buildroot}/bin

%files
%defattr(-,root,root)
%doc CHANGES COPYRIGHT README TODO
%attr(755,root,root) /bin/cstream
%{_mandir}/man1/*

