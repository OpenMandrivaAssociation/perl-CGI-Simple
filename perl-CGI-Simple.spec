%define pkgname CGI-Simple

name:      perl-%{pkgname}
summary:   CGI-Simple - A Simple totally OO CGI interface that is CGI.pm compliant
version:   0.080
release:   %mkrel 1

license:   Artistic
group:     Development/Perl
url:       http://www.cpan.org
buildroot: %{_tmppath}/%{name}-%{version}-%(id -u -n)
buildarch: noarch
source:    http://search.cpan.org/dist/J/JF/JFREEMAN/%{pkgname}-%{version}.tar.bz2

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
%setup -q -n %{pkgname}-%{version} 

%build
CFLAGS="$RPM_OPT_FLAGS"
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} 

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{makeinstall_std}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README SIGNATURE
%{perl_vendorlib}/*
%{_mandir}/*/*
