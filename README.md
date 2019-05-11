# specfiles
Specfiles for RPMs not found where I need them (often missing from EPEL) or personal/custom stuff.

Example yum repo file for the [RPMs that are available](https://us-east.manta.joyent.com/tpaul/public/centos/7/x86_64/repoview/index.html)

```
[miscrepo]
name=Misc RPMs for Enterprise Linux 7 - $basearch
baseurl=https://us-east.manta.joyent.com/tpaul/public/centos/7/x86_64
enabled=1
gpgcheck=1
gpgkey=https://travispaul.me/pgp.asc.txt
```

The spec files themselves (foo.spec) are MIT licensed as per the [Fedora Guidelines](https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#License_of_Fedora_SPEC_Files):

> All original Fedora contributions are governed by the Fedora Project Contributor Agreement (FPCA). This means that unless a    spec file contains an explicit license attribution within it, it is available under the terms of the MIT license.


