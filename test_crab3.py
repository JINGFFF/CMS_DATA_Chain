from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName   = 'test'
#config.General.saveLogs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'PrivateMC'
config.JobType.generator = 'lhe'
config.JobType.inputFiles = ['1.lhe']
# Name of the CMSSW configuration file
config.JobType.psetName    = 'pLHE-cfg.py'


config.section_("Data")
# This string determines the primary dataset of the newly-produced outputs.
# For instance, this dataset will be named /CrabTestSingleMu/something/USER
#config.Data.inputDataset = '/WH1000-LH'
config.Data.outputPrimaryDataset = 'Bulk'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 200
config.Data.totalUnits = 50000
config.Data.publication = True

# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'test'

config.section_("Site")
# Where the output files will be transmitted to
config.Site.storageSite = 'T2_CN_Beijing'
#config.Site.whitelist = ['T2_CH_CERN']
