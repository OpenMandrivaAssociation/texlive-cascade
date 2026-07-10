%global tl_name cascade
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2a
Release:	%{tl_revision}.1
Summary:	Constructions with braces to present mathematical demonstrations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cascade
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cascade.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cascade.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cascade.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The LaTeX package cascade provides a command \Cascade to do
constructions to present mathematical demonstrations with successive
braces for the deductions.

