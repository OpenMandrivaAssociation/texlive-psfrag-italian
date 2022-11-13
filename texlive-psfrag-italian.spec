Name:		texlive-psfrag-italian
Version:	15878
Release:	1
Summary:	PSfrag documentation in Italian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/italian/psfrag
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psfrag-italian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psfrag-italian.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a translation of the the documentation that comes with
the psfrag documentation.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/psfrag-italian/itpfgguide.pdf
%doc %{_texmfdistdir}/doc/latex/psfrag-italian/itpfgguide.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
