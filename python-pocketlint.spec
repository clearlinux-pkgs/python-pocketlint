#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-pocketlint
Version  : 0.15
Release  : 6
URL      : https://github.com/rhinstaller/pocketlint/archive/0.15.tar.gz
Source0  : https://github.com/rhinstaller/pocketlint/archive/0.15.tar.gz
Summary  : Support for running pylint against projects
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: python-pocketlint-python3
Requires: python-pocketlint-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Addon pylint modules and configuration settings for checking the validity of
Python-based source projects.

%package python
Summary: python components for the python-pocketlint package.
Group: Default
Requires: python-pocketlint-python3

%description python
python components for the python-pocketlint package.


%package python3
Summary: python3 components for the python-pocketlint package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-pocketlint package.


%prep
%setup -q -n pocketlint-0.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523042070
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
