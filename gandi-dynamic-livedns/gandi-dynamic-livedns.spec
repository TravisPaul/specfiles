Summary: A Gandi LiveDNS client that dynamically updates an A record.
Name: gandi-dynamic-livedns
Version: 0.0.1
Release: 1%{?dist}
License: BSD
URL: https://github.com/travispaul/gandi-dynamic-livedns
Source0: https://us-east.manta.joyent.com/tpaul/public/distfiles/%{name}-%{version}.tar.xz
Requires: libbsd
Requires: libcurl
BuildRequires: libbsd-devel
BuildRequires: libcurl-devel

%description
This program will retrieve your public IPv4 address from an
ifconfig.co compatible service and update or create an A record
using Gandi's LiveDNS API.

%prep
%autosetup -n %{name}

%build
make

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -c dldns %{buildroot}%{_bindir}/dldns
install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 -c dldns.1 %{buildroot}%{_mandir}/man1/dldns.1

%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sat Jun 1 2019 Travis Paul <tr@vispaul.me> - 0.0.1-1
- Initial spec
