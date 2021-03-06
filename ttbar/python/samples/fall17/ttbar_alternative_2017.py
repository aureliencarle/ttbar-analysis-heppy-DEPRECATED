import os 
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

creator = ComponentCreator()

json = os.path.expandvars('$CMSSW_BASE/src/CMGTools/ttbar/data/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt')
lumi = 41529.

############################################################################
# MC
############################################################################


alt_MC_hdampUp = creator.makeMCComponent("alt_MC_hdampUp","/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);

alt_MC_hdampUp_pmx = creator.makeMCComponent("alt_MC_hdampUp_pmx","/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);



alt_MC_hdampDown_pmx = creator.makeMCComponent("alt_MC_hdampDown_pmx","/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);

alt_MC_hdampDown = creator.makeMCComponent("alt_MC_hdampDown","/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_CP5Up_pmx = creator.makeMCComponent("alt_MC_CP5Up_pmx","/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_CP5Up = creator.makeMCComponent("alt_MC_CP5Up","/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_CP5Down_pmx = creator.makeMCComponent("alt_MC_CP5Down_pmx","/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_CP5Down = creator.makeMCComponent("alt_MC_CP5Down","/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);


##############


alt_MC_erdOn = creator.makeMCComponent("alt_MC_erdOn","/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_QCDbased = creator.makeMCComponent("alt_MC_QCDbased","/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_QCDbased_ext = creator.makeMCComponent("alt_MC_QCDbased_ext","/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_GluonMove = creator.makeMCComponent("alt_MC_GluonMove","/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_GluonMove_ext = creator.makeMCComponent("alt_MC_GluonMove","/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_mtop169p5_pmx = creator.makeMCComponent("alt_MC_mtop169p5_pmx","/TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_mtop169p5 = creator.makeMCComponent("alt_MC_mtop169p5","/TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_mtop175p5_pmx = creator.makeMCComponent("alt_MC_mtop175p5_pmx","/TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_mtop175p5 = creator.makeMCComponent("alt_MC_mtop175p5","/TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);




alt_ttbar = [
    alt_MC_hdampUp,
    alt_MC_hdampUp_pmx,
    alt_MC_hdampDown_pmx,
    alt_MC_hdampDown,
    alt_MC_CP5Up_pmx,
    alt_MC_CP5Up,
    alt_MC_CP5Down_pmx,
    alt_MC_CP5Down,
    alt_MC_erdOn,
    alt_MC_QCDbased,
    alt_MC_QCDbased_ext,
    alt_MC_GluonMove,
    alt_MC_GluonMove_ext,
    alt_MC_mtop169p5_pmx,
    alt_MC_mtop169p5,
    alt_MC_mtop175p5_pmx,
    alt_MC_mtop175p5
]




