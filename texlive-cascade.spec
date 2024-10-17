Name:		texlive-cascade
Version:	65757
Release:	1
Summary:	Constructions with braces to present mathematical demonstrations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cascade
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cascade.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cascade.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cascade.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The LaTeX package cascade provides a command \Cascade to do
constructions to present mathematical demonstrations with
successive braces for the deductions.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/cascade
%{_texmfdistdir}/tex/latex/cascade
%doc %{_texmfdistdir}/doc/latex/cascade

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
