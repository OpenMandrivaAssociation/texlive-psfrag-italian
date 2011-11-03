# revision 15878
# category Package
# catalog-ctan /info/italian/psfrag
# catalog-date 2008-08-23 00:25:16 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-psfrag-italian
Version:	20080823
Release:	1
Summary:	PSfrag documentation in Italian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/italian/psfrag
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psfrag-italian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psfrag-italian.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a translation of the the documentation that comes with
the psfrag documentation.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/psfrag-italian/itpfgguide.pdf
%doc %{_texmfdistdir}/doc/latex/psfrag-italian/itpfgguide.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
