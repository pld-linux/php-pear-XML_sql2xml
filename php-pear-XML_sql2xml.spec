%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	sql2xml
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - returns XML from a SQL-query
Summary(pl.UTF-8):   %{_pearname} - konwersja zapytań SQL ma format XML
Name:		php-pear-%{_pearname}
Version:	0.3.2
Release:	5
License:	PHP 2.02
Group:		Development/Languages/PHP
#Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
Source0:	%{_pearname}-%{version}.tgz
# Source0-md5:	7b5e24e7b5cec429ef9ffaaa91043990
URL:		http://pear.php.net/package/XML_sql2xml/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(domxml)
Requires:	php-common < 3:5
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class takes a PEAR::DB-Result Object, a sql-query-string, an
array and/or an xml-string/file and returns a xml-representation of
it.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa pobiera obiekt PEAR::DB-Result oraz tekst zapytania SQL.
Zwraca jego reprezentacje XML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/doc/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
