Summary:	The "Maximum RPM" book
Name:		maximum-rpm
Version:	1.0
Release:	0.20010429
License:	OPL
Group:		Documentation
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	docbook-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Maximum RPM" is a book about the RPM Package Manager or, as it is
known to its friends, RPM.

The book is divided into two major sections. The first section is for
anyone who needs to use RPM on his/her system. The second section
covers all there is to know about build packages using RPM.

%description
"Maximum RPM" to ksi±¿ka o Zarz±dcy Pakietów RPM (RPM Package Manager)
lub, miêdzy przyjació³mi, RPMie.

Ksi±¿ka ta podzielona jest na dwa g³ówne rozdzia³y. Pierwszy jest 
przeznaczony dla ka¿dego, kto potrzbuje RPM'a w swoim systemie. Drugi
pokrywa wszystko co mo¿e byæ powiedziane o budowania pakietów z
u¿yciem RPM'a.

Ksi±¿ka jest napisana w jêzyku angielskim.

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
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc html/*
