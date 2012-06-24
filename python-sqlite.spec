
%define         module	sqlite

Summary:	A DB API v2.0 compatible interface to SQLite
Summary(pl):	Interfejs do SQLite kompatybilny z DB API v2.0
Name:		python-%{module}
Version:	1.0
Release:	1
License:	Free
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pysqlite/pysqlite-%{version}.tar.gz
# Source0-md5:	f21b19ff048f6bafbbfc3edb86b4c4e4
URL:		http://pysqlite.sourceforge.net/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	sqlite-devel
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
%setup -q -n pysqlite

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
        --root=$RPM_BUILD_ROOT --optimize=2

rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*.py
cp -aR examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE doc/rest/manual.txt
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
%attr(755,root,root) %{py_sitedir}/_%{module}.so
