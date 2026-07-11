%global tl_name spbmark
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.46y
Release:	%{tl_revision}.1
Summary:	Customize superscripts and subscripts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/spbmark
License:	cc-by-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spbmark.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spbmark.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides three commands \super, \sub and \supersub to
improve the layout of superscripts and subscripts which can be adjusted
with respect to relative position and format, and can be used in text
and math mode.

