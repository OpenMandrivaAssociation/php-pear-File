%define		_class		File
%define		upstream_name	%{_class}

Summary:	Common file and directory routines
Name:		php-pear-%{upstream_name}
Version:	1.4.1
Release:	1
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/File/
Source0:	http://download.pear.php.net/package/File-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
Suggests:	php-pear-File_Util
Suggests:	php-pear-File_CSV

%description
Provides easy access to read/write to files along with some common routines
to deal with paths.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-3mdv2011.0
+ Revision: 667495
- mass rebuild

* Tue Apr 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-2
+ Revision: 650639
- fix deps

* Tue Apr 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-1
+ Revision: 650586
- 1.4.0

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-8mdv2011.0
+ Revision: 607098
- rebuild

* Mon Dec 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-7mdv2010.1
+ Revision: 478661
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.3.0-6mdv2010.0
+ Revision: 426618
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-5mdv2009.1
+ Revision: 321810
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.3.0-4mdv2009.0
+ Revision: 224732
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-3mdv2008.1
+ Revision: 178507
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jun 03 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2008.0
+ Revision: 34971
- the xml in the package.xml is ok now, remove the recoding

* Sun Jun 03 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1mdv2008.0
+ Revision: 34812
- 1.3.0

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-4mdv2008.0
+ Revision: 15425
- rule out the PHPUnit.php dep


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-3mdv2007.0
+ Revision: 81088
- Import php-pear-File

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-3mdk
- new group (Development/PHP)

* Sun Jan 15 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-2mdk
- fix the package.xml file so it will register

* Thu Sep 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-1mdk
- 1.2.2

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-5mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-4mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-3mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdk
- rebuild

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-1mdk
- 1.2.0
- fix spec file to conform with the others

* Sat Apr 16 2005 Pascal Terjan <pterjan@mandrake.org> 1.1.0-0.RC3.2mdk
- Fix requires

* Thu Jan 20 2005 Pascal Terjan <pterjan@mandrake.org> 1.1.0-0.RC3.1mdk
- First mdk package


