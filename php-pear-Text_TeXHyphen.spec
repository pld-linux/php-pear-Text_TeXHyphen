%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	TeXHyphen
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - automated word hyphenation with the TeX algorithm
Summary(pl):	%{_pearname} - automatyczne przenoszenie wyrazów przy u¿yciu algorytmu TeXa
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	2.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2f3ab275d65cefd477cd0c9707842027
URL:		http://pear.php.net/package/Text_TeXHyphen/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package implements the TeX hyphenation algorithm based on
pattern.

The package can support various backends for pattern retrieval. At
this stage only flat files with TeX pattern were implemented. The
advantage of the TeX pattern is the available multi-language support.
Currently German, Oxford and American English are supported.

For speed purposes an interface for a cache of hyphenated words was
implemented.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet jest implementacj± przenoszenia wyrazów z TeXa w oparciu o
wzorce.

Pakiet mo¿e obs³ugiwaæ ró¿ne backendy do uzyskiwania wzorców. Na tym
etapie zaimplementowane s± tylko p³askie pliki z wzorcami TeXowymi.
Zalet± wzorców TeXowych jest mo¿liwo¶æ obs³ugi wielu jêzyków.
Aktualnie obs³ugiwany jest jêzyk niemiecki oraz oksfordzki i
amerykañski angielski.

W celu przyspieszenia dzia³ania zosta³ zaimplementowany interfejs do
buforowania z³amanych wyrazów.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

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
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%{php_pear_dir}/data/%{_pearname}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
