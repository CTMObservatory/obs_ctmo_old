from lsst.obs.ctmo.ingest import CTMOCameraParseTask
config.parse.retarget(CTMOCameraParseTask)


config.parse.translation = {'dataType':'IMGTYPE',
                            'expTime':'EXPTIME',
                            'frameId':'RUN-ID',
                            'filter':'FILTER',
                            'field':'OBJECT'}

config.parse.translators = {'dateObs':'translateDate',
                            'taiObs':'translateDate',
                            'visit':'translateVisit',
                            'ccd':'translateCcd'}


config.register.columns = {'frameId':'text',
                        'visit':'int',
                        'ccd':'int',
                        'filter':'text',
                        'dataType':'text',
                        'expTime':'double',
                        'dateObs':'text',
                        'taiObs':'text',
                        'field':'text' }

config.register.visit = ['visit', 'ccd', 'filter', 'dateObs', 'taiObs']

config.register.unique = ['visit', 'ccd']

# Subaru's config
# config.parse.defaults = {'ccdTemp': '0',
#                          'config': 'configuration',
#                          'autoguider': '0'
#                          }
# 
# config.parse.translation = {'proposal': 'PROP-ID',
#                             'dataType': 'DATA-TYP',
#                             'expTime': 'EXPTIME',
#                             'ccd': 'DET-ID',
#                             'pa': 'INR-STR',
#                             'autoguider': 'T_AG',
#                             'ccdTemp': 'T_CCDTV',
#                             'config': 'T_CFGFIL',
#                             'frameId': 'FRAMEID',
#                             'expId': 'EXP-ID',
#                             'dateObs': 'DATE-OBS',
#                             'taiObs': 'DATE-OBS',
#                             }
