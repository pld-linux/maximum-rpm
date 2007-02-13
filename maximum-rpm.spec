Summary:	The "Maximum RPM" book
Summary(pl.UTF-8):	Książka "Maximum RPM"
Name:		maximum-rpm
Version:	1.0
Release:	0.20010429.1
License:	OPL
Group:		Documentation
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	41c329eb4129f0cb5b3c47d42fa5c664
URL:		http://www.rpm.org/max-rpm/
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Maximum RPM" is a book about the RPM Package Manager or, as it is
known to its friends, RPM.

The book is divided into two major sections. The first section is for
anyone who needs to use RPM on his/her system. The second section
covers all there is to know about build packages using RPM.

%description -l pl.UTF-8
"Maximum RPM" to książka o Zarządcy Pakietów RPM (RPM Package Manager)
lub, między przyjaciółmi, RPM-ie.

Książka ta podzielona jest na dwa główne rozdziały. Pierwszy jest
przeznaczony dla każdego, kto potrzebuje RPM-a w swoim systemie. Drugi
pokrywa wszystko co może być powiedziane o budowania pakietów z
użyciem RPM-a.

Książka jest napisana w języku angielskim.

%prep
%setup -q

%build
# bundled configure and make are heavily broken... thus this dirty hack
mkdir html
cd html
dsl="`echo /usr/share/sgml/docbook/utils-*/docbook-utils.dsl`#html"
# it will fail with lack of generated-index.sgml
jade -d $dsl -t sgml -i html -V html-index ../max-rpm.sgml || true
perl /usr/bin/collateindex -o ../temp-index.sgml HTML.index
perl ../fix-index < ../temp-index.sgml > ../generated-index.sgml
# ok, we have generated-index now, so restart
cd ..
rm -rf html
mkdir html
cd html
jade -d $dsl -t sgml -i html ../max-rpm.sgml
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc html/*
