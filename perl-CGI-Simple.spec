%define upstream_name    CGI-Simple
%define upstream_version 1.282
Name:		perl-%{upstream_name}
Version:	1.282
Release:	1

Summary:   Simple totally OO CGI interface that is CGI.pm compliant
license:   Artistic
group:     Development/Perl
Url:       https://github.com/manwar/CGI--Simple
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MANWAR/CGI-Simple-1.282.tar.gz
BuildRequires:	make
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
%setup -q -n CGI-Simple-1.282

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%check
make test || :

%files
%doc README
%{perl_vendorlib}/CGI
%{_mandir}/*/*


