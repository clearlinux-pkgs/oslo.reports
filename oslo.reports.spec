#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : oslo.reports
Version  : 1.29.1
Release  : 33
URL      : http://tarballs.openstack.org/oslo.reports/oslo.reports-1.29.1.tar.gz
Source0  : http://tarballs.openstack.org/oslo.reports/oslo.reports-1.29.1.tar.gz
Source99 : http://tarballs.openstack.org/oslo.reports/oslo.reports-1.29.1.tar.gz.asc
Summary  : oslo.reports library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.reports-python3
Requires: oslo.reports-license
Requires: oslo.reports-python
Requires: Jinja2
Requires: oslo.i18n
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: psutil
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
Team and repository tags
        ========================

%package license
Summary: license components for the oslo.reports package.
Group: Default

%description license
license components for the oslo.reports package.


%package python
Summary: python components for the oslo.reports package.
Group: Default
Requires: oslo.reports-python3 = %{version}-%{release}

%description python
python components for the oslo.reports package.


%package python3
Summary: python3 components for the oslo.reports package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.reports package.


%prep
%setup -q -n oslo.reports-1.29.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537929001
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/oslo.reports
cp LICENSE %{buildroot}/usr/share/doc/oslo.reports/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/oslo.reports/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
