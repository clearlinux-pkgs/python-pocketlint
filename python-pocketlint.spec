#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-pocketlint
Version  : 0.17
Release  : 26
URL      : https://github.com/rhinstaller/pocketlint/archive/0.17.tar.gz
Source0  : https://github.com/rhinstaller/pocketlint/archive/0.17.tar.gz
Summary  : Support for running pylint against projects
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: python-pocketlint-license = %{version}-%{release}
Requires: python-pocketlint-python = %{version}-%{release}
Requires: python-pocketlint-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Addon pylint modules and configuration settings for checking the validity of
Python-based source projects.

%package license
Summary: license components for the python-pocketlint package.
Group: Default

%description license
license components for the python-pocketlint package.


%package python
Summary: python components for the python-pocketlint package.
Group: Default
Requires: python-pocketlint-python3 = %{version}-%{release}

%description python
python components for the python-pocketlint package.


%package python3
Summary: python3 components for the python-pocketlint package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-pocketlint package.


%prep
%setup -q -n pocketlint-0.17
cd %{_builddir}/pocketlint-0.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583214514
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-pocketlint
cp %{_builddir}/pocketlint-0.17/COPYING %{buildroot}/usr/share/package-licenses/python-pocketlint/4cc77b90af91e615a64ae04893fdffa7939db84c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-pocketlint/4cc77b90af91e615a64ae04893fdffa7939db84c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
