%global tl_name psfrag-italian
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	PSfrag documentation in Italian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/italian/psfrag
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/psfrag-italian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/psfrag-italian.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a translation of the documentation that comes with the psfrag
documentation.

