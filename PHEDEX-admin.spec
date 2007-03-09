### RPM cms PHEDEX-admin PHEDEX_2_5_1
%define downloadn %(echo %n | cut -f1 -d-)
Source: cvs://:pserver:anonymous@cmscvs.cern.ch:2401/cvs_server/repositories/CMSSW?passwd=AA_:yZZ3e&module=%{downloadn}&export=%{downloadn}&&tag=-r%{v}&output=/%{downloadn}.tar.gz
Requires: oracle oracle-env p5-time-hires p5-text-glob p5-compress-zlib p5-dbi p5-dbd-oracle p5-xml-parser srmcp python
Requires: py2-cx-oracle
Requires: dls dbs
Requires: PHEDEX

# Extra requires so we get everything necessary for env.{,c}sh.
Requires: zlib expat openssl bz2lib py2-pyxml py2-zsi py2-mysqldb mysql


%prep
%setup -n %{downloadn}
rm -rf Custom
rm -rf Deployment
rm -rf Documentation
rm -rf Toolkit/DropBox
rm -rf Toolkit/Infrastructure
rm -rf Toolkit/Request
rm -rf Toolkit/Transfer
rm -rf Toolkit/Management
rm -rf Toolkit/Monitoring
rm -rf Toolkit/Peers
rm -rf Toolkit/Test
rm -rf Toolkit/Workflow


%build

%install
mkdir -p %i/etc
tar -cf - * | (cd %i && tar -xf -)

mkdir -p %i/etc/profile.d
for x in %pkgreqs; do
 case $x in /* ) continue ;; esac
 p=%{instroot}/%{cmsplatf}/$(echo $x | sed 's/\([^+]*\)+\(.*\)+\([A-Z0-9].*\)/\1 \2 \3/' | tr ' ' '/')
 echo ". $p/etc/profile.d/init.sh" >> %i/etc/profile.d/env.sh
 echo "source $p/etc/profile.d/init.csh" >> %i/etc/profile.d/env.csh
done

%post
%{relocateConfig}etc/profile.d/env.sh
%{relocateConfig}etc/profile.d/env.csh
