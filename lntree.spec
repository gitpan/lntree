Summary: lntree is a tool to compare directory trees, and link identical files
Name: lntree
Version: 1.10
Release: 1
Source: http://www.perl.com/CPAN/authors/id/JV/%{name}-%{version}.tar.gz
Copyright: GPL or Artistic
Group: File/Tools
Packager: Johan Vromans <jvromans@squirrel.nl>
BuildRoot: /usr/tmp/%{name}-buildroot
Requires: perl >= 5.6.0
BuildRequires: perl >= 5.6.0
BuildArchitectures: noarch

%description
'lntree old-dir new-dir' recursively examines all files in the two
source trees and link the files that are equal. To be precise: if two
files are equal (same size, same contents), the one in directory
new-dir is replaced by a link to the file in old-dir.

This results in cleaner source trees, and a substantial saving of disk
space, for example when multiple versions of the same source tree need
to be kept on-line.

%prep
%setup

%build
perl Makefile.PL
make all
make test

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
make install PREFIX=$RPM_BUILD_ROOT/usr

# Remove some unwanted files
find $RPM_BUILD_ROOT -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -name perllocal.pod -exec rm -f {} \;

# Compress manual pages
test -x /usr/lib/rpm/brp-compress && /usr/lib/rpm/brp-compress

# Build distribution list
( cd $RPM_BUILD_ROOT ; find * -type f -printf "/%p\n" ) > files

%files -f files
%doc README
