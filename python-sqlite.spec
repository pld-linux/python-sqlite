
%define		module	sqlite

Summary:	A DB API v2.0 compatible interface to SQLite
Summary(pl):	Interfejs do SQLite kompatybilny z DB API v2.0
Name:		python-%{module}
Version:	2.3.2
Release:	1
License:	zlib/libpng
Group:		Development/Languages/Python
Source0:	http://initd.org/pub/software/pysqlite/releases/2.3/%{version}/pysqlite-%{version}.tar.gz
# Source0-md5:	bb9a67d62ff91cd8c53720bd15c86a30
URL:		http://www.pysqlite.org/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an extension module for the SQLite embedded relational
database. It tries to conform to the Python DB-API Spec v2 as far as
possible. One problem is that SQLite returns everything as text. This
is a result of SQLite's internal representation of data, however it
still may be possible to return data in the type specified by the
table definitions.

%description -l pl
Ten pakiet zawiera modu� rozszerzenia dla osadzalnej relacyjnej bazy
danych SQLite. Pr�buje on by� w zgodzie ze specyfikacj� Python DB-API
v2 na tyle, na ile to mo�liwe. Jednym problemem jest to, �e SQLite
zwraca wszystko jako tekst. Jest to wynik wewn�trznej reprezentacji
danych przez SQLite; mimo to nadal jest mo�liwe zwracanie danych typu
podanego w definicji tabeli.

%prep
%setup -q -n pysqlite-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

PYTHONPATH=$RPM_BUILD_ROOT%{py_sitedir} \
	python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/pysqlite2/{,test/}*.py \
	$RPM_BUILD_ROOT%{_prefix}/pysqlite2-doc
cp -aR doc/code/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.txt
%dir %{py_sitedir}/pysqlite2
%{py_sitedir}/pysqlite2/*.py[co]
%attr(755,root,root) %{py_sitedir}/pysqlite2/_%{module}.so
%dir %{py_sitedir}/pysqlite2/test
%{py_sitedir}/pysqlite2/test/*.py[co]
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
