%global	cvsDATE	20130104
%global	cvsTIME	1435

Summary:	Dictionaries for SKK (Simple Kana-Kanji conversion program)
Name:		skkdic
Version:	%{cvsDATE}
Release:	5.T%{cvsTIME}%{?dist}.1
License:	GPLv2+
Group:		System Environment/Libraries
# To create source tarball, use Source10
Source0:	skkdic-%{cvsDATE}T%{cvsTIME}.tar.bz2
Source1:	http://openlab.ring.gr.jp/skk/skk/tools/unannotation.awk
Source10:	create-skkdic-source.sh
Source200:	README-skkdic.rh.ja
URL:		http://openlab.ring.gr.jp/skk/skk/dic/
BuildArch:	noarch

%description
This package includes the SKK dictionaries, including the large dictionary
SKK-JISYO.L and pubdic+ dictionary.

%prep
%setup -q

cp -p %SOURCE200 .
cp -p %SOURCE1 .
mv zipcode/README.ja zipcode/README-zipcode.ja 

%build
for dic in \
	SKK-JISYO.L.unannotated \
	SKK-JISYO.wrong
do
	rm -f $dic
	make $dic TOOLS_DIR=.
done

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/skk

for f in SKK-JISYO* zipcode/SKK-JISYO*
do
	install -p -m 644 $f $RPM_BUILD_ROOT%{_datadir}/skk
done
gzip -9 ChangeLog

%files
%doc	ChangeLog.gz
%doc	README-skkdic.rh.ja
%doc	READMEs/committers.txt
%doc	edict_doc.txt
%doc	zipcode/README-zipcode.ja

%{_datadir}/skk/


%changelog
* Mon Jul 29 2013 Daiki Ueno <dueno@redhat.com> - 20130104-5.T1435.1
- drop buildroot cleanup
- remove %defattr(-,root,root,-) in %%files
- fix wrong changelog dates

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130104-5.T1435
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 20130104-4.T1435
- Update to the latest data

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111016-3.T0540
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111016-2.T0540
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 16 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 20111016-1.T0540
- Update for F16

* Wed Mar 09 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 20110309-1.T1520
- Update dictionaries

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090929-2.T0800
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 20090929-1.T0800
- Update for F12Beta

* Wed Aug  5 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 20090805-1.T0306
- Update for F12Alpha
- A bit clean up for spec file

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080904-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080904-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 20080904-1
- fix license tag
- update source files

* Sat Sep 23 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20050614-2
- mass rebuilding

* Tue Jun 14 2005 Jens Petersen <petersen@redhat.com> - 20050614-1
- initial import to Fedora Extras
- update to latest dictionaries

* Wed Sep 22 2004 Jens Petersen <petersen@redhat.com> - 20040922-1
- update to latest dictionaries
- update url
- gzip ChangeLog since it is growing fast

* Thu Apr 15 2004 Jens Petersen <petersen@redhat.com> - 20040415-1
- update to latest
- update README-skkdic.rh.ja and convert it to utf-8

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 11 2003 Jens Petersen <petersen@redhat.com> - 20030211-1
- update dictionaries
- move rh readme file into cvs
- don't build unannotated dictionaries

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 20020724-2
- rebuild

* Wed Jul 24 2002 Jens Petersen <petersen@redhat.com> 20020724-1
- update dictionaries

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Feb 21 2002 Jens Petersen <petersen@redhat.com> 20020220-2
- rebuild in new environment

* Wed Feb 20 2002 Jens Petersen <petersen@redhat.com> 20020220-1
- update to latest dictionaries
- put source in one bzip2ed tar file
- tidy spec file
- make unannotated
- include SKK-JISYO.pubdic+

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sat Jun 23 2001 SATO Satoru <ssato@redhat.com>
- update and add more dictionaries: (jinmei,) law, okinawa, geo
- add README files

* Mon Jan 22 2001 SATO Satoru <ssato@redhat.com>
- update dictionaris
- add cdb-dictionaries
- clean up SPEC

* Thu Dec 28 2000 SATO Satoru <ssato@redhat.com>
- add many extra dictionaries
- clean up SPEC

* Tue Sep  5 2000 SATO Satoru <ssato@redhat.com>
- Initial release
