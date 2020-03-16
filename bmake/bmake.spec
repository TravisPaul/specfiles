Summary:       The NetBSD make(1) tool
Name:          bmake
Version:       20180222
Release:       2%{?dist}
License:       BSD with advertising
Group:         Development/Tools
URL:           https://ftp.NetBSD.org/pub/NetBSD/misc/sjg/
Source0:       https://ftp.NetBSD.org/pub/NetBSD/misc/sjg/bmake-%{version}.tar.gz
Requires:      mk-files
BuildRequires: mk-files
BuildRequires: util-linux

%description
bmake, the NetBSD make tool, is a program designed to simplify the
maintenance of other programs.  The input of bmake is a list of specifications
indicating the files upon which the targets (programs and other files) depend.
bmake then detects which targets are out of date based on their dependencies
and triggers the necessary commands to bring them up to date when that happens.

bmake is similar to GNU make, even though the syntax for the advanced features
supported in Makefiles is very different.

%prep
%autosetup -n %{name}

%build
%configure --with-default-sys-path=%{_datadir}/mk
sh ./make-bootstrap.sh

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -c bmake %{buildroot}%{_bindir}/bmake
install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 -c make.1 %{buildroot}%{_mandir}/man1/bmake.1

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Mar 27 2018 Travis Paul <tr@vispaul.me> - 20180222-1
- New upstream version
- parse.c: avoid calling sysconf for every call to loadfile
- var.c: Var_Set handle NULL value anytime.
- parse.c: do not treat .info as warning with -W

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171207-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Luis Bazan <lbazan@fedoraproject.org> - 20171207-1
- New Upstream version

* Wed Nov 22 2017 Luis Bazan <lbazan@fedoraproject.org> - 20171118-1
- new upstream version

* Sun Nov 05 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 20171028-1
- New upstream version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150910-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150910-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150910-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150910-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 03 2015 Luis Bazan <lbazan@fedoraproject.org> - 20150910-1
- new upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20141111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 15 2014 Luis Bazan <lbazan@fedoraproject.org> - 20141111-1
- New upstream version

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140620-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 2 2014 Luis Bazan <lbazan@fedoraproject.org> - 20140620-1
- new upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140214-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 18 2014 Luis Bazan <lbazan@fedoraproject.org> - 20140214-1
- new upstream version

* Wed Jan 15 2014 Luis Bazan <lbazan@fedoraproject.org> - 20140101-1
- New Upstream version

* Tue Oct 29 2013 Luis Bazan <lbazan@fedoraproject.org> - 20131001-1
- New Upstream version

* Wed Aug 14 2013 Luis Bazan <lbazan@fedoraproject.org> - 20130730-1
- New Upstream Version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130330-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Luis Bazan <lbazan@fedoraproject.org> - 20130330-1
- New Upstream Version

* Wed Mar 06 2013 Luis Bazan <lbazan@fedoraproject.org> - 20130123-1
- New Upstream Version

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120831-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 05 2012 Luis Bazan <lbazan@fedoraproject.org> - 20120831-1
- New Upstream Version

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120604-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Luis Bazan <bazanluis20@gmail.com> 20120604-2
- Changing destination of the sources

* Tue Jun 05 2012 Luis Bazan <bazanluis20@gmail.com> 20120604-1
- New Upstream Version 20120604-1.

* Mon Feb 06 2012 Julio Merino <jmmv@NetBSD.org> 20111111-1
- New upstream version.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090222-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090222-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Stepan Kasal <skasal@redhat.com> - 20090222-1
- new upstream version

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080515-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 02 2008 Julio M. Merino Vidal <jmmv@NetBSD.org> - 20080515-1
- Initial release for Fedora.
