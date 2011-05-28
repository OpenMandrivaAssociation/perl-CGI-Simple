%define upstream_name    CGI-Simple
%define upstream_version 1.113

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:   Simple totally OO CGI interface that is CGI.pm compliant
license:   Artistic
group:     Development/Perl
Url:       http://search.cpan.org/dist/%{upstream_name}
Source0:   http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl-IO-stringy
buildarch: noarch
buildroot: %{_tmppath}/%{name}-%{version}-%{release}

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
%make

%check
make test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/CGI
%{_mandir}/*/*
