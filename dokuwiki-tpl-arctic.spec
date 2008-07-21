%define		_snap	2008-05-04
%define		_ver	%(echo %{_snap} | tr -d -)
%define		tpl	arctic
Summary:	Arctic template for DokuWiki
Summary(pl.UTF-8):	Szablon Arctic dla Dokuwiki
Name:		dokuwiki-tpl-%{tpl}
Version:	%{_ver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.chimeric.de/_media/projects/dokuwiki/template/arctic/download/template-arctic-%{_snap}.tgz
# Source0-md5:	2b15ce8d15e39615fabaa1fccdb85da2
Source1:	dokuwiki-find-lang.sh
URL:		http://www.chimeric.de/projects/dokuwiki/template/arctic
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	dokuwiki >= 20070626
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		tpldir		%{dokudir}/lib/tpl/%{tpl}

%description
Yet Another Sidebar Template. ;-) Features: sidebar
(left/right/both/none), definable User-/Group-/Namespace-Sidebars,
fully configurable via configuration manager, TOC inside sidebar, user
defined sidebar actions.

%prep
%setup -q -n %{tpl}

rm -f LICENSE # GPL v2
rm -f *~

cat > INSTALL <<'EOF'
To activate this template add the following to your conf/local.php file:
$conf['template'] = '%{tpl}';
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{tpldir}
cp -a . $RPM_BUILD_ROOT%{tpldir}
rm -f $RPM_BUILD_ROOT%{tpldir}/{INSTALL,README}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING INSTALL README VERSION
%dir %{tpldir}
%{tpldir}/*.php
%{tpldir}/*.css
%{tpldir}/*.html
%{tpldir}/script.js
%{tpldir}/style.ini
%{tpldir}/conf
%{tpldir}/images
%{tpldir}/sidebars