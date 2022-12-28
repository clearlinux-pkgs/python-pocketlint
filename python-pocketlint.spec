#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-pocketlint
Version  : 0.24
Release  : 38
URL      : https://github.com/rhinstaller/pocketlint/archive/0.24/pocketlint-0.24.tar.gz
Source0  : https://github.com/rhinstaller/pocketlint/archive/0.24/pocketlint-0.24.tar.gz
Summary  : Support for running pylint against projects
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: python-pocketlint-license = %{version}-%{release}
Requires: python-pocketlint-python = %{version}-%{release}
Requires: python-pocketlint-python3 = %{version}-%{release}
Requires: pypi(polib)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(packaging)
BuildRequires : pypi(polib)
BuildRequires : pypi(pylint)

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
Provides: pypi(pocketlint)
Requires: pypi(packaging)
Requires: pypi(polib)
Requires: pypi(pylint)

%description python3
python3 components for the python-pocketlint package.


%prep
%setup -q -n pocketlint-0.24
cd %{_builddir}/pocketlint-0.24
pushd ..
cp -a pocketlint-0.24 buildavx2
cp -a pocketlint-0.24 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672198006
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-pocketlint
cp %{_builddir}/pocketlint-%{version}/COPYING %{buildroot}/usr/share/package-licenses/python-pocketlint/4cc77b90af91e615a64ae04893fdffa7939db84c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
