#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Tk-DoubleClick
Version  : 0.04
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Tk-DoubleClick-0.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Tk-DoubleClick-0.04.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtk-doubleclick-perl/libtk-doubleclick-perl_0.04-1.debian.tar.xz
Summary  : 'Correctly handle single-click vs double-click events,'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Tk-DoubleClick-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Tk)

%description
Tk-DoubleClick
how to install the module, any machine dependencies it may have (for
example C compilers and installed libraries) and any other information
that should be provided before the module is installed.

%package dev
Summary: dev components for the perl-Tk-DoubleClick package.
Group: Development
Provides: perl-Tk-DoubleClick-devel = %{version}-%{release}
Requires: perl-Tk-DoubleClick = %{version}-%{release}

%description dev
dev components for the perl-Tk-DoubleClick package.


%package perl
Summary: perl components for the perl-Tk-DoubleClick package.
Group: Default
Requires: perl-Tk-DoubleClick = %{version}-%{release}

%description perl
perl components for the perl-Tk-DoubleClick package.


%prep
%setup -q -n Tk-DoubleClick-0.04
cd %{_builddir}
tar xf %{_sourcedir}/libtk-doubleclick-perl_0.04-1.debian.tar.xz
cd %{_builddir}/Tk-DoubleClick-0.04
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Tk-DoubleClick-0.04/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Tk::DoubleClick.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
