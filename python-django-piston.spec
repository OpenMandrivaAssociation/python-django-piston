%define oname   django-piston
%define mercurial_snapshot e539a104d516
%define rel 1

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
Source:         https://bitbucket.org/jespern/django-piston/get/%{mercurial_snapshot}.tar.bz2
%else
Source:         http://bitbucket.org/jespern/django-piston/downloads/%{oname}-%{version}.tar.gz
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/*

