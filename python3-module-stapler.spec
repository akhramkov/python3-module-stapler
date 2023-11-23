%define pypi_name stapler

%def_without check

Name:    python3-module-%pypi_name
Version: 1.0.0
Release: alt1

Summary: A small utility making use of the pypdf library to provide a (somewhat) lighter alternative to pdftk 

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/hellerbarde/stapler
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel python3-module-poetry

Source: %pypi_name-%version.tar

Requires: %name-staplelib = %EVR

%description
Tool for manipulating PDF documents from the command line.

%package staplelib
Summary: Module staplelib of pdf-stapler
Group:   Development/Python3
Requires: python3-module-PyPDF2

%description staplelib
Tool for manipulating PDF documents from the command line.

This package contains lib for stapler.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%_bindir/%pypi_name
%_bindir/pdf-stapler
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files staplelib
%doc README.rst LICENSE
%python3_sitelibdir/staplelib

%changelog
* Wed Nov 22 2023 Andrey Khramkov <aki@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
