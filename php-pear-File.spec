%define	_class	File
%define	modname	%{_class}

Summary:	Common file and directory routines
Name:		php-pear-%{modname}
Version:	1.4.1
Release:	11
License:	PHP License
Group:		Development/PHP
Url:		https://pear.php.net/package/File/
Source0:	http://download.pear.php.net/package/File-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear
Suggests:	php-pear-File_Util
Suggests:	php-pear-File_CSV

%description
Provides easy access to read/write to files along with some common routines
to deal with paths.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{modname}.xml

