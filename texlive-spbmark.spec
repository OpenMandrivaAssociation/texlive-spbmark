Name:		texlive-spbmark
Version:	64706
Release:	2
Summary:	Customize superscripts and subscripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spbmark
License:	cc-by-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spbmark.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spbmark.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides three commands \super, \sub and \supersub
to improve the layout of superscripts and subscripts which can
be adjusted with respect to relative position and format, and
can be used in text and math mode.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/spbmark
%doc %{_texmfdistdir}/doc/latex/spbmark

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
