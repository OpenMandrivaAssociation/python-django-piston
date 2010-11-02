%define oname   django-piston

Name:           python-django-piston
Version:        0.2.2
Release:        %mkrel 2
Summary:        A mini-framework for Django for creating RESTful APIs

Group:          Development/Python
License:        BSD
URL:            http://bitbucket.org/jespern/django-piston/
Source:         http://bitbucket.org/jespern/django-piston/downloads/%{oname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
Piston is a relatively small Django application that lets you
create application programming interfaces (API) for your sites.

%prep
%setup -q -n %{oname}

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

