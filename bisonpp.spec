%define name bison++
%define version 1.21.8
%define prefix %{_prefix}
%define release 11

Name: %{name}
Summary: A GNU general-purpose parser generator for C++
Version: %{version}
Release: %{release}
License: GPL
Group: Development/Other
Source: ftp://ftp.tu-darmstadt.de/pub/programming/languages/C++/tools/flex++bison++/LATEST/%{name}-%{version}.tar.bz2
Patch0: bison++.cflags.patch.bz2
Buildroot: %{_tmppath}/%{name}-buildroot

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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.21.8-10mdv2011.0
+ Revision: 616775
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.21.8-9mdv2010.0
+ Revision: 424626
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.21.8-8mdv2009.0
+ Revision: 243320
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.21.8-6mdv2008.1
+ Revision: 135829
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import bison++


* Tue Aug 01 2006 Lenny Cartier <lenny@mandriva.com> 1.21.8-6mdv2007.0
- rebuild

* Tue Apr 26 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.21.8-5mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.21.8-4mdk
- rebuild

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.21.8-3mdk
- rebuild

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.Com> 1.21.8-2mdk
- rebuild

* Sat Aug 25 2001 Lenny Cartier <lenny@mandrakesoft.Com> 1.21.8-1mdk
- updated to 1.21.8

* Thu Jun 28 2001 Lenny Cartier <lenny@mandrakesoft.Com> 1.21.7-4mdk
- rebuild

* Fri Jan 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.21.7-3mdk
- rebuild

* Mon Jul 24 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.21.7-2mdk
- fixed path of bison.cc
- patched cflags

* Mon Jul 24 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.21.7-1mdk
- first Mandrake release

