%define		module	sqlite
Summary:	A DB API v2.0 compatible interface to SQLite
Summary(pl.UTF-8):	Interfejs do SQLite kompatybilny z DB API v2.0
Name:		python-%{module}
Version:	2.6.3
Release:	4
License:	zlib/libpng
Group:		Development/Languages/Python
Source0:	http://pysqlite.googlecode.com/files/pysqlite-%{version}.tar.gz
# Source0-md5:	711afa1062a1d2c4a67acdf02a33d86e
URL:		http://pysqlite.googlecode.com/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	sqlite3-devel >= 3.6.11
Requires:	python-modules
Provides:	python(sqlite)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an extension module for the SQLite embedded relational
database. It tries to conform to the Python DB-API Spec v2 as far as
possible. One problem is that SQLite returns everything as text. This
is a result of SQLite's internal representation of data, however it
still may be possible to return data in the type specified by the
table definitions.

%description -l pl.UTF-8
Ten pakiet zawiera moduł rozszerzenia dla osadzalnej relacyjnej bazy
danych SQLite. Próbuje on być w zgodzie ze specyfikacją Python DB-API
v2 na tyle, na ile to możliwe. Jednym problemem jest to, że SQLite
zwraca wszystko jako tekst. Jest to wynik wewnętrznej reprezentacji
danych przez SQLite; mimo to nadal jest możliwe zwracanie danych typu
podanego w definicji tabeli.

%prep
%setup -q -n pysqlite-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

PYTHONPATH=$RPM_BUILD_ROOT%{py_sitedir} \
	%py_install

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/pysqlite2/test/py25
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/pysqlite2/{,test/}*.py \
	$RPM_BUILD_ROOT%{_prefix}/pysqlite2-doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.txt
%dir %{py_sitedir}/pysqlite2
%{py_sitedir}/*.egg-info
%{py_sitedir}/pysqlite2/*.py[co]
%attr(755,root,root) %{py_sitedir}/pysqlite2/_%{module}.so
%dir %{py_sitedir}/pysqlite2/test
%{py_sitedir}/pysqlite2/test/*.py[co]
