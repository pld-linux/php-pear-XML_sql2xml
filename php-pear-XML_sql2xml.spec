%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       sql2xml
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Returns XML from a SQL-Query
Summary(pl):	%{_pearname} - Konwertuje SQL-Query ma format XML
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class takes a PEAR::DB-Result Object, a sql-query-string, an
array and/or an xml-string/file and returns a xml-representation of
it.

%description -l pl
Ta klasa pobiera obiekt PEAR::DB-Result oraz tekst zapytania SQL.
Zwraca jego reprezentacje XML.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/doc/*
%doc %{_pearname}-%{version}/%{_subclass}_ext.php
%{php_pear_dir}/%{_class}/%{_subclass}.php
