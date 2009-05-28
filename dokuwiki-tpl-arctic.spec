%define		snap	2009-03-25
%define		ver	%(echo %{snap} | tr -d -)
%define		tpl	arctic
Summary:	Arctic template for DokuWiki
Summary(pl.UTF-8):	Szablon Arctic dla Dokuwiki
Name:		dokuwiki-tpl-%{tpl}
Version:	%{ver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.chimeric.de/_media/projects/dokuwiki/template/arctic/download/template-arctic-%{snap}.tgz
# Source0-md5:	09debac544fd40d8f95a721ef724f20f
Source1:	dokuwiki-find-lang.sh
URL:		http://www.chimeric.de/projects/dokuwiki/template/arctic
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	dokuwiki >= 20080505
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		tpldir		%{dokudir}/lib/tpl/%{tpl}

%description
Yet Another Sidebar Template. ;-) Features: sidebar
(left/right/both/none), definable User-/Group-/Namespace-Sidebars,
fully configurable via configuration manager, TOC inside sidebar, user
defined sidebar actions.

%prep
%setup -q -n %{tpl}
cat > INSTALL <<'EOF'
To activate this template add the following to your conf/local.php file:
$conf['template'] = '%{tpl}';
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{tpldir}
cp -a . $RPM_BUILD_ROOT%{tpldir}
rm -f $RPM_BUILD_ROOT%{tpldir}/{COPYING,VERSION,INSTALL,README,style.ini.dist}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc INSTALL README VERSION
%dir %{tpldir}
%{tpldir}/*.php
%{tpldir}/*.css
%{tpldir}/*.html
%{tpldir}/script.js
%{tpldir}/style.ini
%{tpldir}/conf
%{tpldir}/images
