%define oname   django-piston
%define mercurial_snapshot e539a104d516
%define rel 2

Name:           python-django-piston
Version:        0.2.3
%if %mercurial_snapshot
Release:        %mkrel 0.0.%rel.%mercurial_snapshot
%else
Release:        %mkrel %rel
%endif
Summary:        A mini-framework for Django for creating RESTful APIs

Group:          Development/Python
License:        BSD
URL:            http://bitbucket.org/jespern/django-piston/
%if %mercurial_snapshot
Source0:        https://bitbucket.org/jespern/django-piston/get/%{mercurial_snapshot}.tar.bz2
%else
Source0         http://bitbucket.org/jespern/django-piston/downloads/%{oname}-%{version}.tar.gz
%endif

BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
Piston is a relatively small Django application that lets you
create application programming interfaces (API) for your sites.

%prep
%if %mercurial_snapshot
%setup -q -n jespern-django-piston-%mercurial_snapshot
touch piston/__init__.py
%else
%setup -q -n %{oname}
%endif
%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
touch %buildroot/%{python_sitelib}/piston/__init__.py

%files
%{python_sitelib}/*
