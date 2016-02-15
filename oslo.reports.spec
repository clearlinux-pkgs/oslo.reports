#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.reports
Version  : 1.4.0
Release  : 9
URL      : http://tarballs.openstack.org/oslo.reports/oslo.reports-1.4.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.reports/oslo.reports-1.4.0.tar.gz
Summary  : oslo.reports library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.reports-python
BuildRequires : Jinja2
BuildRequires : MarkupSafe-python
BuildRequires : PyYAML-python
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : appdirs-python
BuildRequires : docutils-python
BuildRequires : eventlet-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : funcsigs-python
BuildRequires : greenlet-python
BuildRequires : hacking
BuildRequires : iso8601-python
BuildRequires : keystoneauth1-python
BuildRequires : mccabe-python
BuildRequires : mox3-python
BuildRequires : msgpack-python-python
BuildRequires : netifaces-python
BuildRequires : os-client-config-python
BuildRequires : oslo.config
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : psutil-python
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : wrapt-python

%description
===================================
oslo.reports
===================================

%package python
Summary: python components for the oslo.reports package.
Group: Default
Requires: Jinja2
Requires: oslo.serialization-python
Requires: oslo.utils-python
Requires: psutil-python

%description python
python components for the oslo.reports package.


%prep
%setup -q -n oslo.reports-1.4.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
