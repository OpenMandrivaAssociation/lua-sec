%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define oname luasec

Name:           lua-sec
Version:        0.4
Release:        4
Summary:        OpenSSL binding for Lua
Group:          Development/Other
License:        MIT
URL:            https://www.inf.puc-rio.br/~brunoos/luasec/
Source0:        http://luaforge.net/frs/download.php/4255/%{oname}-%{version}.tar.gz
Patch0:		luasec-0.4-fix-link.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  lua >= %{luaver}, lua-devel >= %{luaver}
BuildRequires:  openssl-devel 
Requires:       lua >= %{luaver}
Requires:       lua-socket

%description
LuaSec is a binding for OpenSSL library to provide TLS/SSL communication. 
This version delegates to LuaSocket the TCP connection establishment 
between the client and server. Then LuaSec uses this connection to start 
a secure TLS/SSL session.


%prep
%setup -q -n %{oname}-%{version}
%patch0 -p0

%build
#perl -pi -e 's/(CFLAGS =)/$1 -fPIC/' config
#echo 'LUA_VERSION_NUM=501' >> config 
%make  linux

%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{lualibdir} $RPM_BUILD_ROOT%{luapkgdir}
make install LUACPATH=$RPM_BUILD_ROOT%{lualibdir} LUAPATH=$RPM_BUILD_ROOT%{luapkgdir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGELOG samples/*
%{lualibdir}/*
%{luapkgdir}/*


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-3mdv2011.0
+ Revision: 612781
- the mass rebuild of 2010.1 packages

* Mon Apr 19 2010 Funda Wang <fwang@mandriva.org> 0.4-2mdv2010.1
+ Revision: 536627
- link against lua 5.1

* Tue Feb 02 2010 Rémy Clouard <shikamaru@mandriva.org> 0.4-1mdv2010.1
+ Revision: 499821
- update to 0.4

* Fri May 01 2009 Michael Scherer <misc@mandriva.org> 0.3.1-1mdv2010.0
+ Revision: 369964
- add BuildRequires
- import lua-sec


