%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define oname luasec

Name:           lua-sec
Version:        0.4
Release:        %mkrel 1
Summary:        OpenSSL binding for Lua
Group:          Development/Other
License:        MIT
URL:            http://www.inf.puc-rio.br/~brunoos/luasec/
Source0:        http://luaforge.net/frs/download.php/4255/%{oname}-%{version}.tar.gz
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
