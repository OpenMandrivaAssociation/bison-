%define name bison++
%define version 1.21.8
%define prefix %{_prefix}
%define release %mkrel 6

Name: %{name}
Summary: A GNU general-purpose parser generator for C++
Version: %{version}
Release: %{release}
License: GPL
Group: Development/Other
Source: ftp://ftp.tu-darmstadt.de/pub/programming/languages/C++/tools/flex++bison++/LATEST/%{name}-%{version}.tar.bz2
Patch0: bison++.cflags.patch.bz2

%description
Bison is a general purpose parser generator which converts a grammar
description for an LALR context-free grammar into a C program to parse that
grammar.

Bison++ is built on top of Bison; it takes advantage of the C++ language.

%prep

%setup -q
%patch0 -p0

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall mandir=$RPM_BUILD_ROOT%{_mandir}/man1
mv $RPM_BUILD_ROOT%{_datadir}/bison.* $RPM_BUILD_ROOT%{_libdir}

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/bison.cc
%{_libdir}/bison.h

%clean
rm -rf $RPM_BUILD_ROOT

