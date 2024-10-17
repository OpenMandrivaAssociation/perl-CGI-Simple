%define upstream_name    CGI-Simple
%define upstream_version 1.25

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:   Simple totally OO CGI interface that is CGI.pm compliant
license:   Artistic
group:     Development/Perl
Url:       https://search.cpan.org/dist/%{upstream_name}
Source0:   http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl-IO-stringy
BuildRequires: perl-devel
BuildArch: noarch


%description
CGI::Simple provides a relatively lightweight drop in replacement for CGI.pm.
It shares an identical OO interface to CGI.pm for parameter parsing, file
upload, cookie handling and header generation. This module is entirely object
oriented, however a complete functional interface is available by using the
CGI::Simple::Standard module.

Essentially everything in CGI.pm that relates to the CGI (not HTML) side of
things is available. There are even a few new methods and additions to old
ones! If you are interested in what has gone on under the hood see the
Compatibility with CGI.pm section at the end.

In practical testing this module loads and runs about twice as fast as CGI.pm
depending on the precise task.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc README
%{perl_vendorlib}/CGI
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.113.0-2mdv2011.0
+ Revision: 680698
- mass rebuild

* Thu Dec 30 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.113.0-1mdv2011.0
+ Revision: 626242
- new version

* Tue Dec 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.112.0-2mdv2011.0
+ Revision: 621731
- P0: security fix for CVE-2010-2761
- P1: security fix for CVE-2010-4410
- enable the tests and fix deps

* Tue Jul 07 2009 Jérôme Quelin <jquelin@mandriva.org> 1.112.0-1mdv2011.0
+ Revision: 393092
- update to 1.112
- using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.1-4mdv2009.0
+ Revision: 255830
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.1-2mdv2008.1
+ Revision: 171023
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2008.0
+ Revision: 52483
- update to new version 1.1

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdv2008.0
+ Revision: 48175
- new version

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.080-1mdv2008.0
+ Revision: 19752
- 0.080
- clean up the spec file


* Wed Mar 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.077-2mdk
- fix man pages names

* Thu Mar 17 2005 Bruno Cornec <bcornec@mandrakesoft.org> 0.077-1mdk
- Initial build.

