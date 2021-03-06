echo 'set cms environment'
source /cvmfs/cms.cern.ch/cmsset_default.sh
#echo 'set crab3 environment'
#source /cvmfs/cms.cern.ch/crab3/crab_slc6.sh.standalone
cd ../..
echo 'set cmssw environment...'
cmsenv
echo 'set cmssw environment:' $CMSSW_RELEASE_BASE
echo 'set cms vo proxy'
voms-proxy-init --rfc --voms cms --valid 72:00
cd -
# export X509_USER_PROXY=$HOME/private/cms.proxy # conflict with xrdcp
mkdir -p $HOME/private
cp $X509_USER_PROXY $HOME/myproxy
