%include	/usr/lib/rpm/macros.python

%define         module sqlite

Summary:	A DB API v2.0 compatible interface to SQLite
Summary(pl):	Interfejs do SQLite kompatybilny z DB API v2.0
Name:		python-%{module}
Version:	0.4.3
Release:	1
License:	Free
Source0:	http://dl.sourceforge.net/pysqlite/pysqlite-%{version}.tar.gz
# Source0-md5:	a55ae9b6f1968a5fe0df10731a5b5a7c
URL:		http://pysqlite.sourceforge.net/
Group:		Development/Languages/Python
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 2.2
BuildRequires:	sqlite-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an extension module for the SQLite embedded relational
database. It tries to conform to the Python DB-API Spec v2 as far as
possible. One problem is that SQLite returns everything as text. This
is a result of SQLite's internal representation of data, however it
still may be possible to return data in the type specified by the
table definitions.

%prep
%setup -q -n pysqlite-%{version}

%build
CFLAGS="%{rpmcflags}"
export CLFAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
        --root=$RPM_BUILD_ROOT --optimize=2
rm $RPM_BUILD_ROOT/%{py_sitedir}/%{module}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%{py_sitedir}/_%{module}.so
