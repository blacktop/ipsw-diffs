## SpeakerRecognition

> `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`

```diff

-3304.82.8.1.2
-  __TEXT.__text: 0x670b8
-  __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_methlist: 0x4498
-  __TEXT.__const: 0x170
-  __TEXT.__gcc_except_tab: 0x1c58
-  __TEXT.__cstring: 0xb940
-  __TEXT.__oslogstring: 0xae1e
+3305.27.1.0.0
+  __TEXT.__text: 0x722c0
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__objc_methlist: 0x5158
+  __TEXT.__const: 0x178
+  __TEXT.__gcc_except_tab: 0x1e7c
+  __TEXT.__cstring: 0xca51
+  __TEXT.__oslogstring: 0xb4e1
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1258
+  __TEXT.__unwind_info: 0x14ac
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0xb15
-  __TEXT.__objc_methname: 0xe7f3
-  __TEXT.__objc_methtype: 0x1fa4
-  __TEXT.__objc_stubs: 0x8860
+  __TEXT.__objc_classname: 0xca0
+  __TEXT.__objc_methname: 0x10479
+  __TEXT.__objc_methtype: 0x21e6
+  __TEXT.__objc_stubs: 0x9360
   __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x1998
-  __DATA_CONST.__objc_classlist: 0x220
+  __DATA_CONST.__const: 0x1b78
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x110
+  __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xce08
-  __DATA_CONST.__objc_selrefs: 0x2ff0
+  __DATA_CONST.__objc_const: 0xec30
+  __DATA_CONST.__objc_selrefs: 0x3480
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x4d8
-  __DATA_CONST.__objc_superrefs: 0x180
-  __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__cfstring: 0x4760
-  __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__objc_const: 0x1970
-  __AUTH_CONST.__objc_dictobj: 0x1b8
+  __DATA_CONST.__objc_classrefs: 0x530
+  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_arraydata: 0x170
+  __AUTH_CONST.__cfstring: 0x4e60
+  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__objc_const: 0x1cd0
+  __AUTH_CONST.__objc_dictobj: 0x398
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x5e0
-  __AUTH.__objc_data: 0x13b0
-  __DATA.__objc_ivar: 0x664
-  __DATA.__data: 0xce8
-  __DATA.__bss: 0xb8
+  __AUTH_CONST.__auth_got: 0x5f0
+  __AUTH.__objc_data: 0x1720
+  __DATA.__objc_ivar: 0x7cc
+  __DATA.__data: 0xd48
+  __DATA.__common: 0x8
+  __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__common: 0x18
   __DATA_DIRTY.__bss: 0x60

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4A8C056A-7FFF-3A8C-A8CE-B9757A3D2518
-  Functions: 1721
-  Symbols:   6564
-  CStrings:  5075
+  UUID: 9DDD57C2-EBB5-35B8-8ACE-F051FF9FC6EA
+  Functions: 2005
+  Symbols:   7457
+  CStrings:  5556
 
Symbols:
+ +[CoreSpeechExclaveAssetController sharedInstance]
+ +[SSRSpeakerProfileEmbeddingExtractor _extractProfileData:completion:]
+ +[SSRSpeakerRecognitionScorer createVoiceScorersWithVoiceProfiles:withConfigFile:withResourceFile:withOffsetsType:forRetraining:]
+ -[CSVTUIAudioSessionRecorder audioSessionRecorderDelegate]
+ -[CSVTUIAudioSessionRecorder initWithDelegate:]
+ -[CSVTUIAudioSessionRecorder setAudioSessionRecorderDelegate:]
+ -[CoreSpeechExclaveAssetController .cxx_destruct]
+ -[CoreSpeechExclaveAssetController _assetCategoryForAssetType:]
+ -[CoreSpeechExclaveAssetController _assetCategoryPathKeyForAssetType:]
+ -[CoreSpeechExclaveAssetController _configFileNameForAssetType:]
+ -[CoreSpeechExclaveAssetController _initializeCurrentDevicePlatform]
+ -[CoreSpeechExclaveAssetController _initializePreInstalledSecureAssetBundle]
+ -[CoreSpeechExclaveAssetController currentHardwarePlatform]
+ -[CoreSpeechExclaveAssetController fetchSecureAssetForLocale:assetType:]
+ -[CoreSpeechExclaveAssetController init]
+ -[CoreSpeechExclaveAssetController preInstalledBundle]
+ -[CoreSpeechExclaveAssetController setCurrentHardwarePlatform:]
+ -[CoreSpeechExclaveAssetController setPreInstalledBundle:]
+ -[SSRMobileAssetProvider _installedMobileAssetOfType:forLanguage:ofType:]
+ -[SSRSpeakerRecognitionModelContext initWithConfigFilePath:withModelFilePaths:withModelFilePathsExclave:]
+ -[SSRSpeakerRecognitionModelContext voiceProfilesModelFilePathsExclave]
+ -[SSRSpeakerRecognitionScorer initWithProfileID:withModelFile:withConfigFile:withResourceFile:configData:memoryIndex:withOffsetsType:forRetraining:]
+ -[SSRSpeakerRecognitionScorer initWithProfileID:withModelFile:withConfigFile:withResourceFile:withOffsetsType:forRetraining:]
+ -[SSRVTUITrainingMessageHandler audioSessionDelegate]
+ -[SSRVTUITrainingMessageHandler audioSession]
+ -[SSRVTUITrainingMessageHandler requestAudioProviderForTrainingWithSyncBlock:]
+ -[SSRVTUITrainingMessageHandler setAudioSession:]
+ -[SSRVTUITrainingMessageHandler setAudioSessionDelegate:]
+ -[SSRVoiceProfile exclaveVoiceProfileModelFilePathForRecognizerType:spIdType:]
+ -[SSRVoiceProfile profileBasePathExclave]
+ -[SSRVoiceProfile setProfileBasePathExclave:]
+ -[SSRVoiceProfile updateVoiceProfilePathExclave:]
+ -[SSRVoiceProfile voiceProfilePathExclave]
+ -[SSRVoiceProfileModelContext initWithConfigFilePath:withModelPath:withModelPathExclave:withCompareModelFilePaths:]
+ -[SSRVoiceProfileModelContext secureProfileModelFilePath]
+ -[SSRVoiceProfileRetrainerPSRExclave .cxx_destruct]
+ -[SSRVoiceProfileRetrainerPSRExclave _composeSpeakerConfusionWithScores:forProfiles:]
+ -[SSRVoiceProfileRetrainerPSRExclave _logSpeakerConfusion:forProfileArray:withPrependString:]
+ -[SSRVoiceProfileRetrainerPSRExclave _logSpeakerConfusionWithExplicitScores:withImplicitScores:withPurgeUtterances:forProfile:forConfigVersion:]
+ -[SSRVoiceProfileRetrainerPSRExclave _processAudioFile:]
+ -[SSRVoiceProfileRetrainerPSRExclave _processSpeakerVector:withSize:withScorers:processedAudioDurationMs:]
+ -[SSRVoiceProfileRetrainerPSRExclave addUtterances:withPolicy:withCompletion:]
+ -[SSRVoiceProfileRetrainerPSRExclave asset]
+ -[SSRVoiceProfileRetrainerPSRExclave bestTriggerScore]
+ -[SSRVoiceProfileRetrainerPSRExclave comparativeModels]
+ -[SSRVoiceProfileRetrainerPSRExclave configBridge]
+ -[SSRVoiceProfileRetrainerPSRExclave configFilePath]
+ -[SSRVoiceProfileRetrainerPSRExclave configVersion]
+ -[SSRVoiceProfileRetrainerPSRExclave ctx]
+ -[SSRVoiceProfileRetrainerPSRExclave currUttLengthInMs]
+ -[SSRVoiceProfileRetrainerPSRExclave dealloc]
+ -[SSRVoiceProfileRetrainerPSRExclave description]
+ -[SSRVoiceProfileRetrainerPSRExclave implicitTrainingRequired]
+ -[SSRVoiceProfileRetrainerPSRExclave initWithVoiceRetrainingContext:]
+ -[SSRVoiceProfileRetrainerPSRExclave initWithVoiceRetrainingContext:secureAsset:]
+ -[SSRVoiceProfileRetrainerPSRExclave maximumSpeakerVectors]
+ -[SSRVoiceProfileRetrainerPSRExclave modelFilePath]
+ -[SSRVoiceProfileRetrainerPSRExclave needsRetrainingWithAudioFiles:]
+ -[SSRVoiceProfileRetrainerPSRExclave processedAudioDurationMs]
+ -[SSRVoiceProfileRetrainerPSRExclave psrModelFilePath]
+ -[SSRVoiceProfileRetrainerPSRExclave psrScorer]
+ -[SSRVoiceProfileRetrainerPSRExclave purgeConfusionInformationWithPolicy:]
+ -[SSRVoiceProfileRetrainerPSRExclave purgeLastSpeakerEmbedding]
+ -[SSRVoiceProfileRetrainerPSRExclave queue]
+ -[SSRVoiceProfileRetrainerPSRExclave resetModelForRetraining]
+ -[SSRVoiceProfileRetrainerPSRExclave resourceFilePath]
+ -[SSRVoiceProfileRetrainerPSRExclave retrainerType]
+ -[SSRVoiceProfileRetrainerPSRExclave setAsset:]
+ -[SSRVoiceProfileRetrainerPSRExclave setBestTriggerScore:]
+ -[SSRVoiceProfileRetrainerPSRExclave setComparativeModels:]
+ -[SSRVoiceProfileRetrainerPSRExclave setConfigBridge:]
+ -[SSRVoiceProfileRetrainerPSRExclave setConfigFilePath:]
+ -[SSRVoiceProfileRetrainerPSRExclave setConfigVersion:]
+ -[SSRVoiceProfileRetrainerPSRExclave setCtx:]
+ -[SSRVoiceProfileRetrainerPSRExclave setCurrUttLengthInMs:]
+ -[SSRVoiceProfileRetrainerPSRExclave setMaximumSpeakerVectors:]
+ -[SSRVoiceProfileRetrainerPSRExclave setProcessedAudioDurationMs:]
+ -[SSRVoiceProfileRetrainerPSRExclave setPsrModelFilePath:]
+ -[SSRVoiceProfileRetrainerPSRExclave setPsrScorer:]
+ -[SSRVoiceProfileRetrainerPSRExclave setQueue:]
+ -[SSRVoiceProfileRetrainerPSRExclave setResourceFilePath:]
+ -[SSRVoiceProfileRetrainerPSRExclave setSpIdType:]
+ -[SSRVoiceProfileRetrainerPSRExclave setSpeakerVector:]
+ -[SSRVoiceProfileRetrainerPSRExclave setSpeakerVectorSize:]
+ -[SSRVoiceProfileRetrainerPSRExclave setVoiceProfile:]
+ -[SSRVoiceProfileRetrainerPSRExclave spIdType]
+ -[SSRVoiceProfileRetrainerPSRExclave speakerVectorSize]
+ -[SSRVoiceProfileRetrainerPSRExclave speakerVector]
+ -[SSRVoiceProfileRetrainerPSRExclave voiceProfile]
+ -[SSRVoiceProfileRetrainerSATExclave .cxx_destruct]
+ -[SSRVoiceProfileRetrainerSATExclave _processAudioFile:]
+ -[SSRVoiceProfileRetrainerSATExclave _processSpeakerVector:withSize:withScorers:processedAudioDurationMs:]
+ -[SSRVoiceProfileRetrainerSATExclave addUtterances:withPolicy:withCompletion:]
+ -[SSRVoiceProfileRetrainerSATExclave asset]
+ -[SSRVoiceProfileRetrainerSATExclave bestTriggerScore]
+ -[SSRVoiceProfileRetrainerSATExclave comparativeModels]
+ -[SSRVoiceProfileRetrainerSATExclave configBridge]
+ -[SSRVoiceProfileRetrainerSATExclave configFilePath]
+ -[SSRVoiceProfileRetrainerSATExclave configVersion]
+ -[SSRVoiceProfileRetrainerSATExclave ctx]
+ -[SSRVoiceProfileRetrainerSATExclave currUttLengthInMs]
+ -[SSRVoiceProfileRetrainerSATExclave dealloc]
+ -[SSRVoiceProfileRetrainerSATExclave description]
+ -[SSRVoiceProfileRetrainerSATExclave implicitTrainingRequired]
+ -[SSRVoiceProfileRetrainerSATExclave initWithVoiceRetrainingContext:]
+ -[SSRVoiceProfileRetrainerSATExclave initWithVoiceRetrainingContext:secureAsset:]
+ -[SSRVoiceProfileRetrainerSATExclave maximumSpeakerVectors]
+ -[SSRVoiceProfileRetrainerSATExclave modelFilePath]
+ -[SSRVoiceProfileRetrainerSATExclave needsRetrainingWithAudioFiles:]
+ -[SSRVoiceProfileRetrainerSATExclave processedAudioDurationMs]
+ -[SSRVoiceProfileRetrainerSATExclave purgeConfusionInformationWithPolicy:]
+ -[SSRVoiceProfileRetrainerSATExclave purgeLastSpeakerEmbedding]
+ -[SSRVoiceProfileRetrainerSATExclave queue]
+ -[SSRVoiceProfileRetrainerSATExclave resetModelForRetraining]
+ -[SSRVoiceProfileRetrainerSATExclave resourceFilePath]
+ -[SSRVoiceProfileRetrainerSATExclave retrainerType]
+ -[SSRVoiceProfileRetrainerSATExclave satModelFilePath]
+ -[SSRVoiceProfileRetrainerSATExclave satScorer]
+ -[SSRVoiceProfileRetrainerSATExclave setAsset:]
+ -[SSRVoiceProfileRetrainerSATExclave setBestTriggerScore:]
+ -[SSRVoiceProfileRetrainerSATExclave setComparativeModels:]
+ -[SSRVoiceProfileRetrainerSATExclave setConfigBridge:]
+ -[SSRVoiceProfileRetrainerSATExclave setConfigFilePath:]
+ -[SSRVoiceProfileRetrainerSATExclave setConfigVersion:]
+ -[SSRVoiceProfileRetrainerSATExclave setCtx:]
+ -[SSRVoiceProfileRetrainerSATExclave setCurrUttLengthInMs:]
+ -[SSRVoiceProfileRetrainerSATExclave setMaximumSpeakerVectors:]
+ -[SSRVoiceProfileRetrainerSATExclave setProcessedAudioDurationMs:]
+ -[SSRVoiceProfileRetrainerSATExclave setQueue:]
+ -[SSRVoiceProfileRetrainerSATExclave setResourceFilePath:]
+ -[SSRVoiceProfileRetrainerSATExclave setSatModelFilePath:]
+ -[SSRVoiceProfileRetrainerSATExclave setSatScorer:]
+ -[SSRVoiceProfileRetrainerSATExclave setSpIdType:]
+ -[SSRVoiceProfileRetrainerSATExclave setSpeakerVector:]
+ -[SSRVoiceProfileRetrainerSATExclave setSpeakerVectorSize:]
+ -[SSRVoiceProfileRetrainerSATExclave setVoiceProfile:]
+ -[SSRVoiceProfileRetrainerSATExclave spIdType]
+ -[SSRVoiceProfileRetrainerSATExclave speakerVectorSize]
+ -[SSRVoiceProfileRetrainerSATExclave speakerVector]
+ -[SSRVoiceProfileRetrainerSATExclave voiceProfile]
+ -[SSRVoiceProfileStore updateVoiceProfile:withUserName:withBasePathExclave:]
+ -[SecureAssetBridge .cxx_destruct]
+ -[SecureAssetBridge _configData:]
+ -[SecureAssetBridge _initializeMemoryIndexForCategory:resourcePath:]
+ -[SecureAssetBridge assetConfigurationPath]
+ -[SecureAssetBridge assettype]
+ -[SecureAssetBridge cachedConfigInfo]
+ -[SecureAssetBridge cachedConfigSatInfo]
+ -[SecureAssetBridge cachedInfo]
+ -[SecureAssetBridge categoryConfigFileName]
+ -[SecureAssetBridge categoryResourcePathURL]
+ -[SecureAssetBridge category]
+ -[SecureAssetBridge configDataSat]
+ -[SecureAssetBridge configData]
+ -[SecureAssetBridge configVersion]
+ -[SecureAssetBridge containsCategory:]
+ -[SecureAssetBridge containsKey:category:]
+ -[SecureAssetBridge decodedInfo]
+ -[SecureAssetBridge getBool:category:defaultValue:]
+ -[SecureAssetBridge getDictionary:category:]
+ -[SecureAssetBridge getDictionaryArray:category:]
+ -[SecureAssetBridge getFloat:category:defaultValue:]
+ -[SecureAssetBridge getString:category:]
+ -[SecureAssetBridge getString:category:defaultValue:]
+ -[SecureAssetBridge getStringArray:category:]
+ -[SecureAssetBridge getUnsignedLongLongValue:category:defaultValue:]
+ -[SecureAssetBridge hashFromResourcePath]
+ -[SecureAssetBridge initWithAssetType:configurationPath:configVersion:category:categoryResourceURLPath:categoryConfigFileName:]
+ -[SecureAssetBridge init]
+ -[SecureAssetBridge memoryIndex]
+ -[SecureAssetBridge resourcePath]
+ -[SecureAssetBridge satMemoryIndex]
+ -[SecureAssetBridge setCachedConfigInfo:]
+ -[SecureAssetBridge setCachedConfigSatInfo:]
+ -[SecureAssetMetaData .cxx_destruct]
+ -[SecureAssetMetaData assetPathURL]
+ -[SecureAssetMetaData configVersion]
+ -[SecureAssetMetaData description]
+ -[SecureAssetMetaData initWithConfigVersion:resourcePath:assetPathURL:]
+ -[SecureAssetMetaData resourcePath]
+ -[SecureAssetPreInstalledBundleBridge .cxx_destruct]
+ -[SecureAssetPreInstalledBundleBridge _fetchJsonDictionaryFromFileURL:]
+ -[SecureAssetPreInstalledBundleBridge _getSecureAssetRootDirectory:]
+ -[SecureAssetPreInstalledBundleBridge _initializePreinstalledAssetBundle]
+ -[SecureAssetPreInstalledBundleBridge fetchAssetConfigFileURL:]
+ -[SecureAssetPreInstalledBundleBridge fetchAssetMetaDataForLocale:categoryResourcePathKey:]
+ -[SecureAssetPreInstalledBundleBridge fetchCategoryResourceDirURL:]
+ -[SecureAssetPreInstalledBundleBridge hardwarePlatform]
+ -[SecureAssetPreInstalledBundleBridge initWithHardwarePlatform:]
+ -[SecureAssetPreInstalledBundleBridge preinstalledAssetBundle]
+ -[SecureAssetPreInstalledBundleBridge rootDirectory]
+ -[SecureMemoryIndex .cxx_destruct]
+ -[SecureMemoryIndex _santizedIndexName:]
+ -[SecureMemoryIndex description]
+ -[SecureMemoryIndex indexCount]
+ -[SecureMemoryIndex initWithResourcePath:memoryIndexes:]
+ -[SecureMemoryIndex injectMemoryIndex:resource:size:]
+ -[SecureMemoryIndex iterateMemoryIndexes:]
+ -[SecureMemoryIndex mIndexData]
+ -[SecureMemoryIndex mIndexes]
+ -[SecureMemoryIndex memoryIndexCount]
+ -[SecureMemoryIndex resourcePath]
+ -[SecureMemoryIndex setMIndexData:]
+ -[SecureMemoryIndex setMIndexes:]
+ -[SecureMemoryIndex setMemoryIndexCount:]
+ -[SecureMemoryIndex setResourcePath:]
+ -[SecureMemoryIndexDataBridge .cxx_destruct]
+ -[SecureMemoryIndexDataBridge dataInBytes]
+ -[SecureMemoryIndexDataBridge dataLength]
+ -[SecureMemoryIndexDataBridge data]
+ -[SecureMemoryIndexDataBridge indexDataLength]
+ -[SecureMemoryIndexDataBridge initWithIndexName:data:dataLength:]
+ -[SecureMemoryIndexDataBridge nameString]
+ -[SecureMemoryIndexDataBridge name]
+ -[SecureMemoryIndexDataBridge setData:]
+ -[SecureMemoryIndexDataBridge setName:]
+ -[SecureSpeakerRecognitionConfigBridge .cxx_destruct]
+ -[SecureSpeakerRecognitionConfigBridge combinationWeight]
+ -[SecureSpeakerRecognitionConfigBridge description]
+ -[SecureSpeakerRecognitionConfigBridge implicitProfileDeltaThreshold]
+ -[SecureSpeakerRecognitionConfigBridge implicitProfileThreshold]
+ -[SecureSpeakerRecognitionConfigBridge implicitTrainingEnabled]
+ -[SecureSpeakerRecognitionConfigBridge implicitVTThreshold]
+ -[SecureSpeakerRecognitionConfigBridge initWithPhraseConfigs:numPruningRetentionUtt:pruningExplicitSATThreshold:pruningExplicitPSRThreshold:pruningSATThreshold:pruningPSRThreshold:combinationWeight:implicitProfileThreshold:implicitProfileDeltaThreshold:implicitVTThreshold:maxEnrollmentUtterances:implicit_training_enabled:multiUserHighScoreThreshold:multiUserLowScoreThreshold:multiUserConfidentScoreThreshold:multiUserDeltaScoreThreshold:useTDTIEnrollment:]
+ -[SecureSpeakerRecognitionConfigBridge iteratePhraseConfigs:]
+ -[SecureSpeakerRecognitionConfigBridge maxEnrollmentUtterances]
+ -[SecureSpeakerRecognitionConfigBridge multiUserConfidentScoreThreshold]
+ -[SecureSpeakerRecognitionConfigBridge multiUserDeltaScoreThreshold]
+ -[SecureSpeakerRecognitionConfigBridge multiUserHighScoreThreshold]
+ -[SecureSpeakerRecognitionConfigBridge multiUserLowScoreThreshold]
+ -[SecureSpeakerRecognitionConfigBridge numPruningRetentionUtt]
+ -[SecureSpeakerRecognitionConfigBridge phraseConfigs]
+ -[SecureSpeakerRecognitionConfigBridge pruningExplicitPSRThreshold]
+ -[SecureSpeakerRecognitionConfigBridge pruningExplicitSATThreshold]
+ -[SecureSpeakerRecognitionConfigBridge pruningPSRThreshold]
+ -[SecureSpeakerRecognitionConfigBridge pruningSATThreshold]
+ -[SecureSpeakerRecognitionConfigBridge setCombinationWeight:]
+ -[SecureSpeakerRecognitionConfigBridge setImplicitProfileDeltaThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setImplicitProfileThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setImplicitTrainingEnabled:]
+ -[SecureSpeakerRecognitionConfigBridge setImplicitVTThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setMaxEnrollmentUtterances:]
+ -[SecureSpeakerRecognitionConfigBridge setMultiUserConfidentScoreThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setMultiUserDeltaScoreThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setMultiUserHighScoreThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setMultiUserLowScoreThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setNumPruningRetentionUtt:]
+ -[SecureSpeakerRecognitionConfigBridge setPhraseConfigs:]
+ -[SecureSpeakerRecognitionConfigBridge setPruningExplicitPSRThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setPruningExplicitSATThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setPruningPSRThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setPruningSATThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setUseTDTIEnrollment:]
+ -[SecureSpeakerRecognitionConfigBridge useTDTIEnrollment]
+ -[SecureSpeakerRecognitionPhraseConfigBridge .cxx_destruct]
+ -[SecureSpeakerRecognitionPhraseConfigBridge initWithName:satThreshold:]
+ -[SecureSpeakerRecognitionPhraseConfigBridge name]
+ -[SecureSpeakerRecognitionPhraseConfigBridge satThreshold]
+ -[SecureSpeakerRecognitionPhraseConfigBridge setName:]
+ -[SecureSpeakerRecognitionPhraseConfigBridge setSatThreshold:]
+ -[SecureVoiceTriggerSpeakerRecognitionDecoder _decodePhraseConfig:]
+ -[SecureVoiceTriggerSpeakerRecognitionDecoder _getBooleanValue:forKey:withDefaultValue:]
+ -[SecureVoiceTriggerSpeakerRecognitionDecoder _getFloatValue:forKey:withDefaultValue:]
+ -[SecureVoiceTriggerSpeakerRecognitionDecoder _getIntValue:forKey:withDefaultValue:]
+ -[SecureVoiceTriggerSpeakerRecognitionDecoder decodeSecureVoiceTriggerSpeakerRecognitionConfigForAsset:]
+ -[SecureVoiceTriggerSpeakerRecognitionDecoder init]
+ GCC_except_table1007
+ GCC_except_table1037
+ GCC_except_table1091
+ GCC_except_table1095
+ GCC_except_table1113
+ GCC_except_table1189
+ GCC_except_table1190
+ GCC_except_table1192
+ GCC_except_table1202
+ GCC_except_table1206
+ GCC_except_table1215
+ GCC_except_table1220
+ GCC_except_table1224
+ GCC_except_table1276
+ GCC_except_table1280
+ GCC_except_table1284
+ GCC_except_table1287
+ GCC_except_table1309
+ GCC_except_table1358
+ GCC_except_table1373
+ GCC_except_table1545
+ GCC_except_table1561
+ GCC_except_table1571
+ GCC_except_table1578
+ GCC_except_table1583
+ GCC_except_table1599
+ GCC_except_table1603
+ GCC_except_table1607
+ GCC_except_table1613
+ GCC_except_table162
+ GCC_except_table1621
+ GCC_except_table167
+ GCC_except_table168
+ GCC_except_table1682
+ GCC_except_table1686
+ GCC_except_table1708
+ GCC_except_table1713
+ GCC_except_table173
+ GCC_except_table1763
+ GCC_except_table1772
+ GCC_except_table1786
+ GCC_except_table1795
+ GCC_except_table1811
+ GCC_except_table1828
+ GCC_except_table316
+ GCC_except_table334
+ GCC_except_table363
+ GCC_except_table369
+ GCC_except_table372
+ GCC_except_table430
+ GCC_except_table482
+ GCC_except_table486
+ GCC_except_table501
+ GCC_except_table505
+ GCC_except_table580
+ GCC_except_table588
+ GCC_except_table590
+ GCC_except_table594
+ GCC_except_table739
+ GCC_except_table778
+ GCC_except_table783
+ GCC_except_table809
+ GCC_except_table812
+ GCC_except_table901
+ GCC_except_table902
+ GCC_except_table905
+ GCC_except_table906
+ GCC_except_table907
+ GCC_except_table908
+ GCC_except_table909
+ GCC_except_table910
+ GCC_except_table911
+ GCC_except_table912
+ GCC_except_table913
+ GCC_except_table915
+ GCC_except_table916
+ GCC_except_table918
+ _CSLogContextFacilityCoreSpeechExclave
+ _CSSecureLogInitIfNeeded
+ _CSSecureLogInitIfNeeded.once
+ _OBJC_CLASS_$_CoreSpeechExclaveAssetController
+ _OBJC_CLASS_$_SSRVoiceProfileRetrainerPSRExclave
+ _OBJC_CLASS_$_SSRVoiceProfileRetrainerSATExclave
+ _OBJC_CLASS_$_SecureAssetBridge
+ _OBJC_CLASS_$_SecureAssetMetaData
+ _OBJC_CLASS_$_SecureAssetPreInstalledBundleBridge
+ _OBJC_CLASS_$_SecureMemoryIndex
+ _OBJC_CLASS_$_SecureMemoryIndexDataBridge
+ _OBJC_CLASS_$_SecureSpeakerRecognitionConfigBridge
+ _OBJC_CLASS_$_SecureSpeakerRecognitionPhraseConfigBridge
+ _OBJC_CLASS_$_SecureVoiceTriggerSpeakerRecognitionDecoder
+ _OBJC_IVAR_$_CSVTUIAudioSessionRecorder._audioSessionRecorderDelegate
+ _OBJC_IVAR_$_CoreSpeechExclaveAssetController._currentHardwarePlatform
+ _OBJC_IVAR_$_CoreSpeechExclaveAssetController._preInstalledBundle
+ _OBJC_IVAR_$_SSRSpeakerRecognitionModelContext._voiceProfilesModelFilePathsExclave
+ _OBJC_IVAR_$_SSRVTUITrainingMessageHandler._audioSession
+ _OBJC_IVAR_$_SSRVTUITrainingMessageHandler._audioSessionDelegate
+ _OBJC_IVAR_$_SSRVoiceProfile._profileBasePathExclave
+ _OBJC_IVAR_$_SSRVoiceProfileModelContext._secureProfileModelFilePath
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._asset
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._bestTriggerScore
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._comparativeModels
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._configBridge
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._configFilePath
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._configVersion
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._ctx
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._currUttLengthInMs
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._maximumSpeakerVectors
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._novDetector
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._processedAudioDurationMs
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._psrModelFilePath
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._psrScorer
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._queue
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._resourceFilePath
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._spIdType
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._speakerVector
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._speakerVectorSize
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerPSRExclave._voiceProfile
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._asset
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._bestTriggerScore
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._comparativeModels
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._configBridge
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._configFilePath
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._configVersion
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._ctx
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._currUttLengthInMs
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._maximumSpeakerVectors
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._novDetector
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._processedAudioDurationMs
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._queue
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._resourceFilePath
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._satModelFilePath
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._satScorer
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._spIdType
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._speakerVector
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._speakerVectorSize
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainerSATExclave._voiceProfile
+ _OBJC_IVAR_$_SecureAssetBridge._assetConfigurationPath
+ _OBJC_IVAR_$_SecureAssetBridge._assettype
+ _OBJC_IVAR_$_SecureAssetBridge._cachedConfigInfo
+ _OBJC_IVAR_$_SecureAssetBridge._cachedConfigSatInfo
+ _OBJC_IVAR_$_SecureAssetBridge._cachedInfo
+ _OBJC_IVAR_$_SecureAssetBridge._category
+ _OBJC_IVAR_$_SecureAssetBridge._categoryConfigFileName
+ _OBJC_IVAR_$_SecureAssetBridge._categoryResourcePathURL
+ _OBJC_IVAR_$_SecureAssetBridge._configVersion
+ _OBJC_IVAR_$_SecureAssetBridge._memoryIndex
+ _OBJC_IVAR_$_SecureAssetBridge._resourcePath
+ _OBJC_IVAR_$_SecureAssetBridge._satMemoryIndex
+ _OBJC_IVAR_$_SecureAssetMetaData._assetPathURL
+ _OBJC_IVAR_$_SecureAssetMetaData._configVersion
+ _OBJC_IVAR_$_SecureAssetMetaData._resourcePath
+ _OBJC_IVAR_$_SecureAssetPreInstalledBundleBridge._hardwarePlatform
+ _OBJC_IVAR_$_SecureAssetPreInstalledBundleBridge._preinstalledAssetBundle
+ _OBJC_IVAR_$_SecureAssetPreInstalledBundleBridge._rootDirectory
+ _OBJC_IVAR_$_SecureMemoryIndex._mIndexData
+ _OBJC_IVAR_$_SecureMemoryIndex._mIndexes
+ _OBJC_IVAR_$_SecureMemoryIndex._memoryIndexCount
+ _OBJC_IVAR_$_SecureMemoryIndex._resourcePath
+ _OBJC_IVAR_$_SecureMemoryIndexDataBridge._data
+ _OBJC_IVAR_$_SecureMemoryIndexDataBridge._indexDataLength
+ _OBJC_IVAR_$_SecureMemoryIndexDataBridge._name
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._combinationWeight
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._implicitProfileDeltaThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._implicitProfileThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._implicitTrainingEnabled
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._implicitVTThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._maxEnrollmentUtterances
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._multiUserConfidentScoreThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._multiUserDeltaScoreThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._multiUserHighScoreThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._multiUserLowScoreThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._numPruningRetentionUtt
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._phraseConfigs
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._pruningExplicitPSRThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._pruningExplicitSATThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._pruningPSRThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._pruningSATThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._useTDTIEnrollment
+ _OBJC_IVAR_$_SecureSpeakerRecognitionPhraseConfigBridge._name
+ _OBJC_IVAR_$_SecureSpeakerRecognitionPhraseConfigBridge._satThreshold
+ _OBJC_METACLASS_$_CoreSpeechExclaveAssetController
+ _OBJC_METACLASS_$_SSRVoiceProfileRetrainerPSRExclave
+ _OBJC_METACLASS_$_SSRVoiceProfileRetrainerSATExclave
+ _OBJC_METACLASS_$_SecureAssetBridge
+ _OBJC_METACLASS_$_SecureAssetMetaData
+ _OBJC_METACLASS_$_SecureAssetPreInstalledBundleBridge
+ _OBJC_METACLASS_$_SecureMemoryIndex
+ _OBJC_METACLASS_$_SecureMemoryIndexDataBridge
+ _OBJC_METACLASS_$_SecureSpeakerRecognitionConfigBridge
+ _OBJC_METACLASS_$_SecureSpeakerRecognitionPhraseConfigBridge
+ _OBJC_METACLASS_$_SecureVoiceTriggerSpeakerRecognitionDecoder
+ __OBJC_$_CLASS_METHODS_CoreSpeechExclaveAssetController
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.4065
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.7706
+ __OBJC_$_INSTANCE_METHODS_CoreSpeechExclaveAssetController
+ __OBJC_$_INSTANCE_METHODS_SSRVoiceProfileRetrainerPSRExclave
+ __OBJC_$_INSTANCE_METHODS_SSRVoiceProfileRetrainerSATExclave
+ __OBJC_$_INSTANCE_METHODS_SecureAssetBridge
+ __OBJC_$_INSTANCE_METHODS_SecureAssetMetaData
+ __OBJC_$_INSTANCE_METHODS_SecureAssetPreInstalledBundleBridge
+ __OBJC_$_INSTANCE_METHODS_SecureMemoryIndex
+ __OBJC_$_INSTANCE_METHODS_SecureMemoryIndexDataBridge
+ __OBJC_$_INSTANCE_METHODS_SecureSpeakerRecognitionConfigBridge
+ __OBJC_$_INSTANCE_METHODS_SecureSpeakerRecognitionPhraseConfigBridge
+ __OBJC_$_INSTANCE_METHODS_SecureVoiceTriggerSpeakerRecognitionDecoder
+ __OBJC_$_INSTANCE_VARIABLES_CoreSpeechExclaveAssetController
+ __OBJC_$_INSTANCE_VARIABLES_SSRVoiceProfileRetrainerPSRExclave
+ __OBJC_$_INSTANCE_VARIABLES_SSRVoiceProfileRetrainerSATExclave
+ __OBJC_$_INSTANCE_VARIABLES_SecureAssetBridge
+ __OBJC_$_INSTANCE_VARIABLES_SecureAssetMetaData
+ __OBJC_$_INSTANCE_VARIABLES_SecureAssetPreInstalledBundleBridge
+ __OBJC_$_INSTANCE_VARIABLES_SecureMemoryIndex
+ __OBJC_$_INSTANCE_VARIABLES_SecureMemoryIndexDataBridge
+ __OBJC_$_INSTANCE_VARIABLES_SecureSpeakerRecognitionConfigBridge
+ __OBJC_$_INSTANCE_VARIABLES_SecureSpeakerRecognitionPhraseConfigBridge
+ __OBJC_$_PROP_LIST_CoreSpeechExclaveAssetController
+ __OBJC_$_PROP_LIST_NSObject.1059
+ __OBJC_$_PROP_LIST_NSObject.1195
+ __OBJC_$_PROP_LIST_NSObject.1390
+ __OBJC_$_PROP_LIST_NSObject.140
+ __OBJC_$_PROP_LIST_NSObject.1809
+ __OBJC_$_PROP_LIST_NSObject.2041
+ __OBJC_$_PROP_LIST_NSObject.2478
+ __OBJC_$_PROP_LIST_NSObject.2794
+ __OBJC_$_PROP_LIST_NSObject.282
+ __OBJC_$_PROP_LIST_NSObject.3131
+ __OBJC_$_PROP_LIST_NSObject.3703
+ __OBJC_$_PROP_LIST_NSObject.3803
+ __OBJC_$_PROP_LIST_NSObject.414
+ __OBJC_$_PROP_LIST_NSObject.4404
+ __OBJC_$_PROP_LIST_NSObject.4594
+ __OBJC_$_PROP_LIST_NSObject.5220
+ __OBJC_$_PROP_LIST_NSObject.5599
+ __OBJC_$_PROP_LIST_NSObject.5791
+ __OBJC_$_PROP_LIST_NSObject.6137
+ __OBJC_$_PROP_LIST_NSObject.6367
+ __OBJC_$_PROP_LIST_NSObject.6406
+ __OBJC_$_PROP_LIST_NSObject.6761
+ __OBJC_$_PROP_LIST_NSObject.681
+ __OBJC_$_PROP_LIST_NSObject.7365
+ __OBJC_$_PROP_LIST_NSObject.7468
+ __OBJC_$_PROP_LIST_NSObject.892
+ __OBJC_$_PROP_LIST_SSRSpeakerRecognizer.3132
+ __OBJC_$_PROP_LIST_SSRVoiceProfileRetrainer.1196
+ __OBJC_$_PROP_LIST_SSRVoiceProfileRetrainer.2795
+ __OBJC_$_PROP_LIST_SSRVoiceProfileRetrainer.5043
+ __OBJC_$_PROP_LIST_SSRVoiceProfileRetrainerPSRExclave
+ __OBJC_$_PROP_LIST_SSRVoiceProfileRetrainerSATExclave
+ __OBJC_$_PROP_LIST_SecureAssetBridge
+ __OBJC_$_PROP_LIST_SecureAssetMetaData
+ __OBJC_$_PROP_LIST_SecureAssetPreInstalledBundleBridge
+ __OBJC_$_PROP_LIST_SecureMemoryIndex
+ __OBJC_$_PROP_LIST_SecureMemoryIndexDataBridge
+ __OBJC_$_PROP_LIST_SecureSpeakerRecognitionConfigBridge
+ __OBJC_$_PROP_LIST_SecureSpeakerRecognitionPhraseConfigBridge
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.4066
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.7707
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVTUIAudioSessionDelegate.5600
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVTUIAudioSessionDelegate.5792
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVTUIAudioSessionRecorderDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVTUIEndPointDelegate.5793
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.4067
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.7708
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1060
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1197
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1391
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.141
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1810
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2042
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2479
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2796
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.283
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3133
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3704
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3804
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.415
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4405
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4595
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5044
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5221
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5601
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5794
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6138
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6368
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6407
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6762
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.682
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7366
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7469
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.893
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EARSyncPSRAudioProcessorDelegate.2797
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1061
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1198
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1392
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.142
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1811
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2043
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2480
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2798
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.284
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3134
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3705
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3805
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.416
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4406
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4596
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5045
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5222
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5602
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5795
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6139
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6369
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6408
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6763
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.683
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7367
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7470
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.894
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SFSpeechRecognitionTaskDelegate.5796
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRAssetProviding.6409
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingService.1393
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingService.1812
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingService.4407
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingServiceDelegate.1813
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingServiceDelegate.4408
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRAssetProviding.6410
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRSpeakerRecognizer.3135
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVTUITrainingService.1394
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVTUITrainingService.1814
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVTUITrainingService.4409
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVoiceProfileRetrainer.1199
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVoiceProfileRetrainer.2799
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVoiceProfileRetrainer.5046
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVTUIAudioSessionDelegate.5603
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVTUIAudioSessionDelegate.5797
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVTUIAudioSessionRecorderDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVTUIEndPointDelegate.5798
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EARSyncPSRAudioProcessorDelegate.2800
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.4068
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.7709
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1062
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1200
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1395
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.143
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1815
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2044
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2481
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2801
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.285
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3136
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3706
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3806
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.417
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4410
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4597
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5047
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5223
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5604
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5799
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6140
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6370
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6411
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6764
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.684
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7368
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7471
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.895
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.4069
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.7710
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFSpeechRecognitionTaskDelegate.5800
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRAssetProviding.6412
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRSpeakerRecognizer.3137
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingService.1396
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingService.1816
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingService.4411
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingServiceDelegate.1817
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingServiceDelegate.4412
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVoiceProfileRetrainer.1201
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVoiceProfileRetrainer.2802
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVoiceProfileRetrainer.5048
+ __OBJC_$_PROTOCOL_REFS_CSVTUIAudioSessionDelegate.5605
+ __OBJC_$_PROTOCOL_REFS_CSVTUIAudioSessionDelegate.5801
+ __OBJC_$_PROTOCOL_REFS_CSVTUIAudioSessionRecorderDelegate
+ __OBJC_$_PROTOCOL_REFS_CSVTUIEndPointDelegate.5802
+ __OBJC_$_PROTOCOL_REFS_EARSyncPSRAudioProcessorDelegate.2803
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.4070
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.7711
+ __OBJC_$_PROTOCOL_REFS_SFSpeechRecognitionTaskDelegate.5803
+ __OBJC_$_PROTOCOL_REFS_SSRAssetProviding.6413
+ __OBJC_$_PROTOCOL_REFS_SSRSpeakerRecognizer.3138
+ __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingService.1397
+ __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingService.1818
+ __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingService.4413
+ __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingServiceDelegate.1819
+ __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingServiceDelegate.4414
+ __OBJC_$_PROTOCOL_REFS_SSRVoiceProfileRetrainer.1202
+ __OBJC_$_PROTOCOL_REFS_SSRVoiceProfileRetrainer.2804
+ __OBJC_$_PROTOCOL_REFS_SSRVoiceProfileRetrainer.5049
+ __OBJC_CLASS_PROTOCOLS_$_SSRVoiceProfileRetrainerPSRExclave
+ __OBJC_CLASS_PROTOCOLS_$_SSRVoiceProfileRetrainerSATExclave
+ __OBJC_CLASS_RO_$_CoreSpeechExclaveAssetController
+ __OBJC_CLASS_RO_$_SSRVoiceProfileRetrainerPSRExclave
+ __OBJC_CLASS_RO_$_SSRVoiceProfileRetrainerSATExclave
+ __OBJC_CLASS_RO_$_SecureAssetBridge
+ __OBJC_CLASS_RO_$_SecureAssetMetaData
+ __OBJC_CLASS_RO_$_SecureAssetPreInstalledBundleBridge
+ __OBJC_CLASS_RO_$_SecureMemoryIndex
+ __OBJC_CLASS_RO_$_SecureMemoryIndexDataBridge
+ __OBJC_CLASS_RO_$_SecureSpeakerRecognitionConfigBridge
+ __OBJC_CLASS_RO_$_SecureSpeakerRecognitionPhraseConfigBridge
+ __OBJC_CLASS_RO_$_SecureVoiceTriggerSpeakerRecognitionDecoder
+ __OBJC_LABEL_PROTOCOL_$_CSVTUIAudioSessionRecorderDelegate
+ __OBJC_METACLASS_RO_$_CoreSpeechExclaveAssetController
+ __OBJC_METACLASS_RO_$_SSRVoiceProfileRetrainerPSRExclave
+ __OBJC_METACLASS_RO_$_SSRVoiceProfileRetrainerSATExclave
+ __OBJC_METACLASS_RO_$_SecureAssetBridge
+ __OBJC_METACLASS_RO_$_SecureAssetMetaData
+ __OBJC_METACLASS_RO_$_SecureAssetPreInstalledBundleBridge
+ __OBJC_METACLASS_RO_$_SecureMemoryIndex
+ __OBJC_METACLASS_RO_$_SecureMemoryIndexDataBridge
+ __OBJC_METACLASS_RO_$_SecureSpeakerRecognitionConfigBridge
+ __OBJC_METACLASS_RO_$_SecureSpeakerRecognitionPhraseConfigBridge
+ __OBJC_METACLASS_RO_$_SecureVoiceTriggerSpeakerRecognitionDecoder
+ __OBJC_PROTOCOL_$_CSVTUIAudioSessionRecorderDelegate
+ ___102-[CSVTUITrainingSession closeSessionWithStatus:successfully:voiceTriggerEventInfo:completeWithResult:]_block_invoke.424
+ ___108-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:withCompletion:]_block_invoke.705
+ ___108-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:withCompletion:]_block_invoke.719
+ ___142-[SSRRemoteControlClient addImplicitTrainingUtteranceToRemoteFilePath:forVoiceProfileId:withVoiceTriggerCtxt:locale:withOtherCtxt:completion:]_block_invoke.469
+ ___142-[SSRRemoteControlClient addImplicitTrainingUtteranceToRemoteFilePath:forVoiceProfileId:withVoiceTriggerCtxt:locale:withOtherCtxt:completion:]_block_invoke.481
+ ___148-[SSRSpeakerRecognitionScorer initWithProfileID:withModelFile:withConfigFile:withResourceFile:configData:memoryIndex:withOffsetsType:forRetraining:]_block_invoke
+ ___182-[SSRVoiceProfileManager notifyImplicitTrainingUtteranceAvailable:forVoiceProfileId:withRecordDeviceInfo:withRecordCtxt:withVoiceTriggerCtxt:withOtherCtxt:assetToUse:withCompletion:]_block_invoke.496
+ ___182-[SSRVoiceProfileManager notifyImplicitTrainingUtteranceAvailable:forVoiceProfileId:withRecordDeviceInfo:withRecordCtxt:withVoiceTriggerCtxt:withOtherCtxt:assetToUse:withCompletion:]_block_invoke.517
+ ___182-[SSRVoiceProfileManager notifyImplicitTrainingUtteranceAvailable:forVoiceProfileId:withRecordDeviceInfo:withRecordCtxt:withVoiceTriggerCtxt:withOtherCtxt:assetToUse:withCompletion:]_block_invoke.520
+ ___42-[CSVTUITrainingSession handleAudioInput:]_block_invoke.430
+ ___42-[SecureMemoryIndex iterateMemoryIndexes:]_block_invoke
+ ___42-[SecureMemoryIndex iterateMemoryIndexes:]_block_invoke_2
+ ___43-[SSRRemoteControlClient didDeviceConnect:]_block_invoke.432
+ ___56-[SSRVoiceProfileRetrainerPSRExclave _processAudioFile:]_block_invoke
+ ___56-[SSRVoiceProfileRetrainerSATExclave _processAudioFile:]_block_invoke
+ ___56-[SecureMemoryIndex initWithResourcePath:memoryIndexes:]_block_invoke
+ ___57+[SSRUtils getExplicitEnrollmentUtterancesFromDirectory:]_block_invoke.800
+ ___57+[SSRUtils getExplicitEnrollmentUtterancesFromDirectory:]_block_invoke.802
+ ___57+[SSRUtils getExplicitEnrollmentUtterancesFromDirectory:]_block_invoke_2.806
+ ___57+[SSRUtils getImplicitEnrollmentUtterancesFromDirectory:]_block_invoke.811
+ ___59-[SSRVoiceProfileManager notifyUserVoiceProfileUpdateReady]_block_invoke.538
+ ___61-[SecureSpeakerRecognitionConfigBridge iteratePhraseConfigs:]_block_invoke
+ ___66-[SSRSpeakerRecognitionOrchestrator getLatestVoiceRecognitionInfo]_block_invoke.482
+ ___67-[SecureVoiceTriggerSpeakerRecognitionDecoder _decodePhraseConfig:]_block_invoke
+ ___69-[CSVTUIAudioSessionRecorder _forceFetchAudioProvider:recordContext:]_block_invoke.14
+ ___70-[CSVTUITrainingSession closeSessionWithStatus:successfully:complete:]_block_invoke.422
+ ___75+[SSRSpeakerProfileEmbeddingExtractor _extractWithModelContext:completion:]_block_invoke
+ ___79-[CSVTUITrainingSessionWithPayload speechRecognitionTask:didFinishRecognition:]_block_invoke.429
+ ___79-[CSVTUITrainingSessionWithPayload speechRecognitionTask:didFinishRecognition:]_block_invoke.430
+ ___81-[SSRVoiceProfileRetrainerPSRExclave initWithVoiceRetrainingContext:secureAsset:]_block_invoke
+ ___81-[SSRVoiceProfileRetrainerSATExclave initWithVoiceRetrainingContext:secureAsset:]_block_invoke
+ ___86-[CSVTUITrainingSessionWithPayload speechRecognitionTask:didHypothesizeTranscription:]_block_invoke.428
+ ___93-[SSRVoiceProfileRetrainerPSRExclave _logSpeakerConfusion:forProfileArray:withPrependString:]_block_invoke
+ ___94-[SSRVoiceProfileManager uploadUserVoiceProfileForSiriProfileId:withUploadTrigger:completion:]_block_invoke.600
+ ___Block_byref_object_copy_.1097
+ ___Block_byref_object_copy_.1227
+ ___Block_byref_object_copy_.1750
+ ___Block_byref_object_copy_.1986
+ ___Block_byref_object_copy_.2148
+ ___Block_byref_object_copy_.2673
+ ___Block_byref_object_copy_.3374
+ ___Block_byref_object_copy_.3541
+ ___Block_byref_object_copy_.4241
+ ___Block_byref_object_copy_.4496
+ ___Block_byref_object_copy_.4735
+ ___Block_byref_object_copy_.4926
+ ___Block_byref_object_copy_.5844
+ ___Block_byref_object_copy_.6089
+ ___Block_byref_object_copy_.6215
+ ___Block_byref_object_copy_.6494
+ ___Block_byref_object_copy_.6885
+ ___Block_byref_object_copy_.723
+ ___Block_byref_object_copy_.845
+ ___Block_byref_object_copy_.977
+ ___Block_byref_object_dispose_.1098
+ ___Block_byref_object_dispose_.1228
+ ___Block_byref_object_dispose_.1751
+ ___Block_byref_object_dispose_.1987
+ ___Block_byref_object_dispose_.2149
+ ___Block_byref_object_dispose_.2674
+ ___Block_byref_object_dispose_.3375
+ ___Block_byref_object_dispose_.3542
+ ___Block_byref_object_dispose_.4242
+ ___Block_byref_object_dispose_.4497
+ ___Block_byref_object_dispose_.4736
+ ___Block_byref_object_dispose_.4927
+ ___Block_byref_object_dispose_.5845
+ ___Block_byref_object_dispose_.6090
+ ___Block_byref_object_dispose_.6216
+ ___Block_byref_object_dispose_.6495
+ ___Block_byref_object_dispose_.6886
+ ___Block_byref_object_dispose_.724
+ ___Block_byref_object_dispose_.846
+ ___Block_byref_object_dispose_.978
+ ___CSSecureLogInitIfNeeded_block_invoke
+ ___block_descriptor_32_e37_v16?0"SecureMemoryIndexDataBridge"8l
+ ___block_descriptor_40_e8_32bs_e44_v32?0"SecureMemoryIndexDataBridge"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32bs_e59_v32?0"SecureSpeakerRecognitionPhraseConfigBridge"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32r_e25_v16?0"CSAudioProvider"8lr32l8
+ ___block_descriptor_40_e8_32s_e29_v32?0"NSDictionary"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32bs40w_e25_v32?0"NSString"8Q16^B24lw40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e37_v16?0"SecureMemoryIndexDataBridge"8lr40l8s32l8
+ ___block_descriptor_64_e8_32r40r48r56r_e34_v32?0"NSData"8I16I20"NSError"24lr32l8r40l8r48l8r56l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e62_v44?0{AudioBufferList=I[1{AudioBuffer=II^v}]}8B32"NSError"36ls32l8r48l8s40l8r56l8r64l8
+ ___block_literal_global.12.18
+ ___block_literal_global.1237
+ ___block_literal_global.1405
+ ___block_literal_global.1757
+ ___block_literal_global.2564
+ ___block_literal_global.3220
+ ___block_literal_global.3395
+ ___block_literal_global.3456
+ ___block_literal_global.4283
+ ___block_literal_global.5180
+ ___block_literal_global.5859
+ ___block_literal_global.6252
+ ___block_literal_global.6394
+ ___block_literal_global.649
+ ___block_literal_global.652
+ ___block_literal_global.6646
+ ___block_literal_global.6722
+ ___block_literal_global.6993
+ ___block_literal_global.7326
+ ___block_literal_global.805
+ ___block_literal_global.808
+ ___block_literal_global.810
+ ___block_literal_global.813
+ __unnamed_array_storage.104
+ __unnamed_array_storage.13
+ __unnamed_array_storage.14
+ __unnamed_array_storage.20
+ __unnamed_array_storage.21
+ __unnamed_array_storage.2239
+ __unnamed_array_storage.27
+ __unnamed_array_storage.28
+ __unnamed_array_storage.34
+ __unnamed_array_storage.35
+ __unnamed_array_storage.41
+ __unnamed_array_storage.42
+ __unnamed_array_storage.442
+ __unnamed_array_storage.448
+ __unnamed_array_storage.449
+ __unnamed_array_storage.455
+ __unnamed_array_storage.456
+ __unnamed_array_storage.477
+ __unnamed_array_storage.478
+ __unnamed_array_storage.48
+ __unnamed_array_storage.487
+ __unnamed_array_storage.49
+ __unnamed_array_storage.491
+ __unnamed_array_storage.497
+ __unnamed_array_storage.498
+ __unnamed_array_storage.501
+ __unnamed_array_storage.504
+ __unnamed_array_storage.505
+ __unnamed_array_storage.508
+ __unnamed_array_storage.509
+ __unnamed_array_storage.55
+ __unnamed_array_storage.56
+ __unnamed_array_storage.5947
+ __unnamed_array_storage.62
+ __unnamed_array_storage.63
+ __unnamed_array_storage.6520
+ __unnamed_array_storage.69
+ __unnamed_array_storage.70
+ __unnamed_array_storage.702
+ __unnamed_array_storage.703
+ __unnamed_array_storage.77
+ __unnamed_array_storage.78
+ __unnamed_array_storage.8
+ _kSSRVoiceProfilePathExclave
+ _nd_addresource
+ _nd_endwavedata
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$URLForResource:withExtension:subdirectory:
+ _objc_msgSend$_assetCategoryForAssetType:
+ _objc_msgSend$_assetCategoryPathKeyForAssetType:
+ _objc_msgSend$_configData:
+ _objc_msgSend$_configFileNameForAssetType:
+ _objc_msgSend$_decodePhraseConfig:
+ _objc_msgSend$_extractProfileData:completion:
+ _objc_msgSend$_fetchJsonDictionaryFromFileURL:
+ _objc_msgSend$_getBooleanValue:forKey:withDefaultValue:
+ _objc_msgSend$_getFloatValue:forKey:withDefaultValue:
+ _objc_msgSend$_getIntValue:forKey:withDefaultValue:
+ _objc_msgSend$_getSecureAssetRootDirectory:
+ _objc_msgSend$_initializeCurrentDevicePlatform
+ _objc_msgSend$_initializeMemoryIndexForCategory:resourcePath:
+ _objc_msgSend$_initializePreInstalledSecureAssetBundle
+ _objc_msgSend$_initializePreinstalledAssetBundle
+ _objc_msgSend$_installedMobileAssetOfType:forLanguage:ofType:
+ _objc_msgSend$_processAudioFile:
+ _objc_msgSend$_santizedIndexName:
+ _objc_msgSend$assetPathURL
+ _objc_msgSend$bundleURL
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$cString
+ _objc_msgSend$category
+ _objc_msgSend$configData
+ _objc_msgSend$configDataSat
+ _objc_msgSend$createVoiceScorersWithVoiceProfiles:withConfigFile:withResourceFile:withOffsetsType:forRetraining:
+ _objc_msgSend$dataInBytes
+ _objc_msgSend$dataLength
+ _objc_msgSend$decodeSecureVoiceTriggerSpeakerRecognitionConfigForAsset:
+ _objc_msgSend$decodedInfo
+ _objc_msgSend$exclaveVoiceProfileModelFilePathForRecognizerType:spIdType:
+ _objc_msgSend$fetchAssetConfigFileURL:
+ _objc_msgSend$fetchAssetMetaDataForLocale:categoryResourcePathKey:
+ _objc_msgSend$fetchCategoryResourceDirURL:
+ _objc_msgSend$fetchSecureAssetForLocale:assetType:
+ _objc_msgSend$getBool:category:defaultValue:
+ _objc_msgSend$getDictionaryArray:category:
+ _objc_msgSend$getFloat:category:defaultValue:
+ _objc_msgSend$getString:category:
+ _objc_msgSend$getString:category:defaultValue:
+ _objc_msgSend$getStringArray:category:
+ _objc_msgSend$getUnsignedLongLongValue:category:defaultValue:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithAssetType:configurationPath:configVersion:category:categoryResourceURLPath:categoryConfigFileName:
+ _objc_msgSend$initWithConfigFilePath:withModelFilePaths:withModelFilePathsExclave:
+ _objc_msgSend$initWithConfigFilePath:withModelPath:withModelPathExclave:withCompareModelFilePaths:
+ _objc_msgSend$initWithConfigVersion:resourcePath:assetPathURL:
+ _objc_msgSend$initWithData:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithHardwarePlatform:
+ _objc_msgSend$initWithIndexName:data:dataLength:
+ _objc_msgSend$initWithName:satThreshold:
+ _objc_msgSend$initWithProfileID:withModelFile:withConfigFile:withResourceFile:configData:memoryIndex:withOffsetsType:forRetraining:
+ _objc_msgSend$initWithProfileID:withModelFile:withConfigFile:withResourceFile:withOffsetsType:forRetraining:
+ _objc_msgSend$initWithResourcePath:memoryIndexes:
+ _objc_msgSend$initWithVoiceRetrainingContext:secureAsset:
+ _objc_msgSend$iterateMemoryIndexes:
+ _objc_msgSend$mIndexData
+ _objc_msgSend$mIndexes
+ _objc_msgSend$maxEnrollmentUtterances
+ _objc_msgSend$memoryIndex
+ _objc_msgSend$nameString
+ _objc_msgSend$relativePath
+ _objc_msgSend$requestAudioProviderForTrainingWithSyncBlock:
+ _objc_msgSend$satMemoryIndex
+ _objc_msgSend$secureProfileModelFilePath
+ _objc_msgSend$setCombinationWeight:
+ _objc_msgSend$setImplicitProfileDeltaThreshold:
+ _objc_msgSend$setImplicitProfileThreshold:
+ _objc_msgSend$setImplicitTrainingEnabled:
+ _objc_msgSend$setImplicitVTThreshold:
+ _objc_msgSend$setMaxEnrollmentUtterances:
+ _objc_msgSend$setMultiUserConfidentScoreThreshold:
+ _objc_msgSend$setMultiUserDeltaScoreThreshold:
+ _objc_msgSend$setMultiUserHighScoreThreshold:
+ _objc_msgSend$setMultiUserLowScoreThreshold:
+ _objc_msgSend$setNumPruningRetentionUtt:
+ _objc_msgSend$setPhraseConfigs:
+ _objc_msgSend$setPruningExplicitPSRThreshold:
+ _objc_msgSend$setPruningExplicitSATThreshold:
+ _objc_msgSend$setPruningPSRThreshold:
+ _objc_msgSend$setPruningSATThreshold:
+ _objc_msgSend$setRequestListeningMicIndicatorLock:
+ _objc_msgSend$setRequestRecordModeLock:
+ _objc_msgSend$setUseTDTIEnrollment:
+ _objc_msgSend$updateVoiceProfile:withUserName:withBasePathExclave:
+ _objc_msgSend$updateVoiceProfilePathExclave:
+ _objc_msgSend$voiceProfilePathExclave
+ _objc_msgSend$voiceProfilesModelFilePathsExclave
+ _sharedInstance.controller
+ _sharedInstance.onceToken.3455
+ _sharedInstance.onceToken.6645
+ _sharedInstance.onceToken.6721
- +[SSRSpeakerRecognitionScorer createVoiceScorersWithVoiceProfiles:withConfigFile:withResourceFile:withOffsetsType:]
- -[CSVTUIAudioSessionRecorder init]
- -[SSRSpeakerRecognitionScorer initWithProfileID:withModelFile:withConfigFile:withResourceFile:withOffsetsType:]
- GCC_except_table1005
- GCC_except_table1009
- GCC_except_table1018
- GCC_except_table1023
- GCC_except_table1027
- GCC_except_table1079
- GCC_except_table1083
- GCC_except_table1087
- GCC_except_table1090
- GCC_except_table1112
- GCC_except_table1265
- GCC_except_table1281
- GCC_except_table1291
- GCC_except_table1298
- GCC_except_table1303
- GCC_except_table1319
- GCC_except_table1323
- GCC_except_table1327
- GCC_except_table1333
- GCC_except_table1341
- GCC_except_table1402
- GCC_except_table1406
- GCC_except_table1428
- GCC_except_table1433
- GCC_except_table1482
- GCC_except_table1490
- GCC_except_table1504
- GCC_except_table1513
- GCC_except_table1529
- GCC_except_table1546
- GCC_except_table160
- GCC_except_table161
- GCC_except_table164
- GCC_except_table169
- GCC_except_table281
- GCC_except_table324
- GCC_except_table330
- GCC_except_table333
- GCC_except_table391
- GCC_except_table407
- GCC_except_table477
- GCC_except_table485
- GCC_except_table487
- GCC_except_table632
- GCC_except_table670
- GCC_except_table675
- GCC_except_table701
- GCC_except_table704
- GCC_except_table748
- GCC_except_table749
- GCC_except_table752
- GCC_except_table753
- GCC_except_table754
- GCC_except_table755
- GCC_except_table756
- GCC_except_table757
- GCC_except_table758
- GCC_except_table759
- GCC_except_table760
- GCC_except_table762
- GCC_except_table763
- GCC_except_table765
- GCC_except_table768
- GCC_except_table845
- GCC_except_table899
- GCC_except_table903
- GCC_except_table992
- GCC_except_table993
- GCC_except_table995
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.3255
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.6347
- __OBJC_$_PROP_LIST_NSObject.1113
- __OBJC_$_PROP_LIST_NSObject.139
- __OBJC_$_PROP_LIST_NSObject.1473
- __OBJC_$_PROP_LIST_NSObject.1681
- __OBJC_$_PROP_LIST_NSObject.1957
- __OBJC_$_PROP_LIST_NSObject.2205
- __OBJC_$_PROP_LIST_NSObject.2530
- __OBJC_$_PROP_LIST_NSObject.276
- __OBJC_$_PROP_LIST_NSObject.2922
- __OBJC_$_PROP_LIST_NSObject.3022
- __OBJC_$_PROP_LIST_NSObject.3581
- __OBJC_$_PROP_LIST_NSObject.3770
- __OBJC_$_PROP_LIST_NSObject.4023
- __OBJC_$_PROP_LIST_NSObject.407
- __OBJC_$_PROP_LIST_NSObject.4272
- __OBJC_$_PROP_LIST_NSObject.4465
- __OBJC_$_PROP_LIST_NSObject.4817
- __OBJC_$_PROP_LIST_NSObject.5081
- __OBJC_$_PROP_LIST_NSObject.5415
- __OBJC_$_PROP_LIST_NSObject.585
- __OBJC_$_PROP_LIST_NSObject.6013
- __OBJC_$_PROP_LIST_NSObject.6115
- __OBJC_$_PROP_LIST_NSObject.780
- __OBJC_$_PROP_LIST_NSObject.941
- __OBJC_$_PROP_LIST_SSRSpeakerRecognizer.2531
- __OBJC_$_PROP_LIST_SSRVoiceProfileRetrainer.2206
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.3256
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.6348
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVTUIAudioSessionDelegate.4273
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVTUIAudioSessionDelegate.4466
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVTUIEndPointDelegate.4467
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.3257
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.6349
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1114
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.140
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1474
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1682
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1958
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2207
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2532
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.277
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2923
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3023
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3582
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3771
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4024
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.408
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4274
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4468
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4818
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5043
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5082
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5416
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.586
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6014
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6116
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.781
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.942
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EARSyncPSRAudioProcessorDelegate.2208
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1115
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.141
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1475
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1683
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1959
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2209
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2533
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.278
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2924
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3024
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3583
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3772
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4025
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.409
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4275
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4469
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4819
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5044
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5083
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5417
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.587
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6015
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6117
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.782
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.943
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SFSpeechRecognitionTaskDelegate.4470
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRAssetProviding.5084
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingService.1116
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingService.1476
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingService.3584
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingServiceDelegate.1477
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingServiceDelegate.3585
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRAssetProviding.5085
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRSpeakerRecognizer.2534
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVTUITrainingService.1117
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVTUITrainingService.1478
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVTUITrainingService.3586
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVoiceProfileRetrainer.2210
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVTUIAudioSessionDelegate.4276
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVTUIAudioSessionDelegate.4471
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVTUIEndPointDelegate.4472
- __OBJC_$_PROTOCOL_METHOD_TYPES_EARSyncPSRAudioProcessorDelegate.2211
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.3258
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.6350
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1118
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.142
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1479
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1684
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1960
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2212
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2535
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.279
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2925
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3025
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3587
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3773
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4026
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.410
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4277
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4473
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4820
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5045
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5086
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5418
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.588
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6016
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6118
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.783
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.944
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.3259
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.6351
- __OBJC_$_PROTOCOL_METHOD_TYPES_SFSpeechRecognitionTaskDelegate.4474
- __OBJC_$_PROTOCOL_METHOD_TYPES_SSRAssetProviding.5087
- __OBJC_$_PROTOCOL_METHOD_TYPES_SSRSpeakerRecognizer.2536
- __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingService.1119
- __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingService.1480
- __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingService.3588
- __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingServiceDelegate.1481
- __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingServiceDelegate.3589
- __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVoiceProfileRetrainer.2213
- __OBJC_$_PROTOCOL_REFS_CSVTUIAudioSessionDelegate.4278
- __OBJC_$_PROTOCOL_REFS_CSVTUIAudioSessionDelegate.4475
- __OBJC_$_PROTOCOL_REFS_CSVTUIEndPointDelegate.4476
- __OBJC_$_PROTOCOL_REFS_EARSyncPSRAudioProcessorDelegate.2214
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.3260
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.6352
- __OBJC_$_PROTOCOL_REFS_SFSpeechRecognitionTaskDelegate.4477
- __OBJC_$_PROTOCOL_REFS_SSRAssetProviding.5088
- __OBJC_$_PROTOCOL_REFS_SSRSpeakerRecognizer.2537
- __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingService.1120
- __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingService.1482
- __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingService.3590
- __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingServiceDelegate.1483
- __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingServiceDelegate.3591
- __OBJC_$_PROTOCOL_REFS_SSRVoiceProfileRetrainer.2215
- ___102-[CSVTUITrainingSession closeSessionWithStatus:successfully:voiceTriggerEventInfo:completeWithResult:]_block_invoke.409
- ___108-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:withCompletion:]_block_invoke.690
- ___108-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:withCompletion:]_block_invoke.704
- ___142-[SSRRemoteControlClient addImplicitTrainingUtteranceToRemoteFilePath:forVoiceProfileId:withVoiceTriggerCtxt:locale:withOtherCtxt:completion:]_block_invoke.454
- ___142-[SSRRemoteControlClient addImplicitTrainingUtteranceToRemoteFilePath:forVoiceProfileId:withVoiceTriggerCtxt:locale:withOtherCtxt:completion:]_block_invoke.466
- ___182-[SSRVoiceProfileManager notifyImplicitTrainingUtteranceAvailable:forVoiceProfileId:withRecordDeviceInfo:withRecordCtxt:withVoiceTriggerCtxt:withOtherCtxt:assetToUse:withCompletion:]_block_invoke.481
- ___182-[SSRVoiceProfileManager notifyImplicitTrainingUtteranceAvailable:forVoiceProfileId:withRecordDeviceInfo:withRecordCtxt:withVoiceTriggerCtxt:withOtherCtxt:assetToUse:withCompletion:]_block_invoke.502
- ___182-[SSRVoiceProfileManager notifyImplicitTrainingUtteranceAvailable:forVoiceProfileId:withRecordDeviceInfo:withRecordCtxt:withVoiceTriggerCtxt:withOtherCtxt:assetToUse:withCompletion:]_block_invoke.505
- ___42-[CSVTUITrainingSession handleAudioInput:]_block_invoke.415
- ___43-[SSRRemoteControlClient didDeviceConnect:]_block_invoke.417
- ___57+[SSRUtils getExplicitEnrollmentUtterancesFromDirectory:]_block_invoke.785
- ___57+[SSRUtils getExplicitEnrollmentUtterancesFromDirectory:]_block_invoke.787
- ___57+[SSRUtils getExplicitEnrollmentUtterancesFromDirectory:]_block_invoke_2.791
- ___57+[SSRUtils getImplicitEnrollmentUtterancesFromDirectory:]_block_invoke.796
- ___59-[SSRVoiceProfileManager notifyUserVoiceProfileUpdateReady]_block_invoke.523
- ___66-[SSRSpeakerRecognitionOrchestrator getLatestVoiceRecognitionInfo]_block_invoke.467
- ___70-[CSVTUITrainingSession closeSessionWithStatus:successfully:complete:]_block_invoke.407
- ___79-[CSVTUITrainingSessionWithPayload speechRecognitionTask:didFinishRecognition:]_block_invoke.414
- ___79-[CSVTUITrainingSessionWithPayload speechRecognitionTask:didFinishRecognition:]_block_invoke.415
- ___86-[CSVTUITrainingSessionWithPayload speechRecognitionTask:didHypothesizeTranscription:]_block_invoke.413
- ___94-[SSRVoiceProfileManager uploadUserVoiceProfileForSiriProfileId:withUploadTrigger:completion:]_block_invoke.585
- ___Block_byref_object_copy_.1416
- ___Block_byref_object_copy_.1634
- ___Block_byref_object_copy_.1789
- ___Block_byref_object_copy_.2107
- ___Block_byref_object_copy_.2612
- ___Block_byref_object_copy_.2769
- ___Block_byref_object_copy_.3428
- ___Block_byref_object_copy_.3673
- ___Block_byref_object_copy_.3903
- ___Block_byref_object_copy_.4520
- ___Block_byref_object_copy_.4769
- ___Block_byref_object_copy_.4896
- ___Block_byref_object_copy_.5169
- ___Block_byref_object_copy_.5532
- ___Block_byref_object_copy_.733
- ___Block_byref_object_copy_.858
- ___Block_byref_object_copy_.967
- ___Block_byref_object_dispose_.1417
- ___Block_byref_object_dispose_.1635
- ___Block_byref_object_dispose_.1790
- ___Block_byref_object_dispose_.2108
- ___Block_byref_object_dispose_.2613
- ___Block_byref_object_dispose_.2770
- ___Block_byref_object_dispose_.3429
- ___Block_byref_object_dispose_.3674
- ___Block_byref_object_dispose_.3904
- ___Block_byref_object_dispose_.4521
- ___Block_byref_object_dispose_.4770
- ___Block_byref_object_dispose_.4897
- ___Block_byref_object_dispose_.5170
- ___Block_byref_object_dispose_.5533
- ___Block_byref_object_dispose_.734
- ___Block_byref_object_dispose_.859
- ___Block_byref_object_dispose_.968
- ___block_literal_global.1128
- ___block_literal_global.1423
- ___block_literal_global.2044
- ___block_literal_global.2633
- ___block_literal_global.2694
- ___block_literal_global.3461
- ___block_literal_global.3984
- ___block_literal_global.4535
- ___block_literal_global.4933
- ___block_literal_global.5070
- ___block_literal_global.5301
- ___block_literal_global.5376
- ___block_literal_global.5640
- ___block_literal_global.5974
- ___block_literal_global.634
- ___block_literal_global.637
- ___block_literal_global.780
- ___block_literal_global.790
- ___block_literal_global.793
- ___block_literal_global.798
- ___block_literal_global.976
- __unnamed_array_storage.427
- __unnamed_array_storage.433
- __unnamed_array_storage.434
- __unnamed_array_storage.440
- __unnamed_array_storage.441
- __unnamed_array_storage.462
- __unnamed_array_storage.4626
- __unnamed_array_storage.463
- __unnamed_array_storage.471
- __unnamed_array_storage.472
- __unnamed_array_storage.475
- __unnamed_array_storage.476
- __unnamed_array_storage.482
- __unnamed_array_storage.483
- __unnamed_array_storage.489
- __unnamed_array_storage.493
- __unnamed_array_storage.494
- __unnamed_array_storage.687
- __unnamed_array_storage.688
- _objc_msgSend$createVoiceScorersWithVoiceProfiles:withConfigFile:withResourceFile:withOffsetsType:
- _objc_msgSend$initWithConfigFilePath:withModelFilePaths:
- _objc_msgSend$initWithProfileID:withModelFile:withConfigFile:withResourceFile:withOffsetsType:
- _sharedInstance.onceToken.2693
- _sharedInstance.onceToken.5300
- _sharedInstance.onceToken.5375
CStrings:
+ "\t"
+ "\x1b"
+ "$\x15\x11!\x11"
+ "%s ::: CoreSpeech Secure logging initialized"
+ "%s Asset Bridge: %@"
+ "%s Asset Path %s"
+ "%s Asset config path: %s"
+ "%s ERR: Cannot create SAT nd detector"
+ "%s ERROR!!!! %s"
+ "%s ERROR!!!! Missing index name %s"
+ "%s Empty profile"
+ "%s Failed to add resource %{private}s"
+ "%s Failed to fetch root directory of the pre-installed asset bundle"
+ "%s Failed to initialize nov detector with error %s"
+ "%s Failed to initialize preinstalled bundles"
+ "%s Fetched audioProvider!!"
+ "%s Fetching audioProvider from SpeechManager, this should only apply to Exclave hardware"
+ "%s Fetching json dictionary from URL %s"
+ "%s Fetching meta data from %s"
+ "%s Hardware platform is nil. Cannot parse preinstalled assets"
+ "%s Missing asset config path"
+ "%s New asset %p"
+ "%s Preinstalled bundles initialized"
+ "%s SecureSpeakerRecognitionConfig string %s"
+ "%s SpeakerVector: %{private}@ [dimension=%ld]"
+ "%s SpkrId:: Bailing out since we don't have modelPath for inference"
+ "%s SpkrId:: ERR: Cannot create SAT Scorer"
+ "%s SpkrId:: ERR: Failed to initialize _novDetect: config path or config data or memory index is nil"
+ "%s SpkrId:: ERR: Failed to initialize secure _novDetect: err=[%{public}d]:%{public}s"
+ "%s SpkrId:: ERR: numVectors:%d for inference, abort"
+ "%s SpkrId:: PSRModel Retraining asset is nil! - Skipping"
+ "%s SpkrId:: SATModel Retraining asset is nil! - Skipping"
+ "%s SpkrId:: SATModel Retraining context is nil! - Skipping"
+ "%s SpkrId:: Secure Speaker detector config is nil"
+ "%s SpkrId:: Secure Speaker detector failed to create nov detector."
+ "%s Successfully created nov detector"
+ "%s URL is nil. Exiting json fetch operation"
+ "%s Updating profile %{public}@ with basePath %{public}@"
+ "%s locale:%s asset meta data: %s"
+ "%s locale:%s category: %s, resourcePath: %s"
+ "%s nil vector"
+ "%s reading memory index from %s"
+ "+[SSRSpeakerProfileEmbeddingExtractor _extractProfileData:completion:]"
+ "+[SSRSpeakerRecognitionScorer createVoiceScorersWithVoiceProfiles:withConfigFile:withResourceFile:withOffsetsType:forRetraining:]"
+ "-[CSVTUIAudioSessionRecorder _forceFetchAudioProvider:recordContext:]_block_invoke"
+ "-[CSVTUIAudioSessionRecorder initWithDelegate:]"
+ "-[CoreSpeechExclaveAssetController fetchSecureAssetForLocale:assetType:]"
+ "-[SSRMobileAssetProvider _installedMobileAssetOfType:forLanguage:ofType:]"
+ "-[SSRSpeakerRecognitionScorer initWithProfileID:withModelFile:withConfigFile:withResourceFile:configData:memoryIndex:withOffsetsType:forRetraining:]"
+ "-[SSRSpeakerRecognitionScorer initWithProfileID:withModelFile:withConfigFile:withResourceFile:configData:memoryIndex:withOffsetsType:forRetraining:]_block_invoke"
+ "-[SSRVoiceProfileRetrainerPSRExclave _logSpeakerConfusionWithExplicitScores:withImplicitScores:withPurgeUtterances:forProfile:forConfigVersion:]"
+ "-[SSRVoiceProfileRetrainerPSRExclave _processAudioFile:]"
+ "-[SSRVoiceProfileRetrainerPSRExclave _processAudioFile:]_block_invoke"
+ "-[SSRVoiceProfileRetrainerPSRExclave addUtterances:withPolicy:withCompletion:]"
+ "-[SSRVoiceProfileRetrainerPSRExclave dealloc]"
+ "-[SSRVoiceProfileRetrainerPSRExclave implicitTrainingRequired]"
+ "-[SSRVoiceProfileRetrainerPSRExclave initWithVoiceRetrainingContext:secureAsset:]"
+ "-[SSRVoiceProfileRetrainerPSRExclave initWithVoiceRetrainingContext:secureAsset:]_block_invoke"
+ "-[SSRVoiceProfileRetrainerPSRExclave needsRetrainingWithAudioFiles:]"
+ "-[SSRVoiceProfileRetrainerPSRExclave purgeConfusionInformationWithPolicy:]"
+ "-[SSRVoiceProfileRetrainerPSRExclave purgeLastSpeakerEmbedding]"
+ "-[SSRVoiceProfileRetrainerPSRExclave resetModelForRetraining]"
+ "-[SSRVoiceProfileRetrainerSATExclave _processAudioFile:]"
+ "-[SSRVoiceProfileRetrainerSATExclave _processAudioFile:]_block_invoke"
+ "-[SSRVoiceProfileRetrainerSATExclave addUtterances:withPolicy:withCompletion:]"
+ "-[SSRVoiceProfileRetrainerSATExclave dealloc]"
+ "-[SSRVoiceProfileRetrainerSATExclave implicitTrainingRequired]"
+ "-[SSRVoiceProfileRetrainerSATExclave initWithVoiceRetrainingContext:secureAsset:]"
+ "-[SSRVoiceProfileRetrainerSATExclave initWithVoiceRetrainingContext:secureAsset:]_block_invoke"
+ "-[SSRVoiceProfileRetrainerSATExclave needsRetrainingWithAudioFiles:]"
+ "-[SSRVoiceProfileRetrainerSATExclave purgeLastSpeakerEmbedding]"
+ "-[SSRVoiceProfileRetrainerSATExclave resetModelForRetraining]"
+ "-[SSRVoiceProfileStore updateVoiceProfile:withUserName:withBasePathExclave:]"
+ "-[SecureAssetBridge decodedInfo]"
+ "-[SecureAssetPreInstalledBundleBridge _fetchJsonDictionaryFromFileURL:]"
+ "-[SecureAssetPreInstalledBundleBridge fetchAssetMetaDataForLocale:categoryResourcePathKey:]"
+ "-[SecureAssetPreInstalledBundleBridge initWithHardwarePlatform:]"
+ "-[SecureMemoryIndex iterateMemoryIndexes:]_block_invoke"
+ "-[SecureMemoryIndex iterateMemoryIndexes:]_block_invoke_2"
+ "-[SecureVoiceTriggerSpeakerRecognitionDecoder decodeSecureVoiceTriggerSpeakerRecognitionConfigForAsset:]"
+ "/private/preboot/Cryptexes/ExclaveOS/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework"
+ ":"
+ "@\"<CSVTUIAudioSessionRecorderDelegate>\""
+ "@\"<SSRVTUITrainingAudioSessionDelegate>\""
+ "@\"NSBundle\""
+ "@\"NSMutableData\""
+ "@\"NSMutableString\""
+ "@\"SSRVoiceProfileRetrainingContext\""
+ "@\"SecureAssetBridge\""
+ "@\"SecureAssetPreInstalledBundleBridge\""
+ "@\"SecureMemoryIndex\""
+ "@\"SecureSpeakerRecognitionConfigBridge\""
+ "@28@0:8@16f24"
+ "@40@0:8Q16@24q32"
+ "@52@0:8@16@24@32Q40B48"
+ "@60@0:8@16@24@32@40Q48B56"
+ "@64@0:8Q16@24@32@40@48@56"
+ "@76@0:8@16@24@32@40r^v48@56Q64B72"
+ "@88@0:8@16I24f28f32f36f40f44f48f52f56I60B64I68I72I76I80B84"
+ "A!"
+ "CONFIGSTR: "
+ "CSSecureLogInitIfNeeded_block_invoke"
+ "CSVTUIAudioSessionRecorderDelegate"
+ "CoreSpeechExclaveAssetController"
+ "HS"
+ "I40@0:8@16@24Q32"
+ "Invalid exclave base path"
+ "Q40@0:8@16@24Q32"
+ "SSRVoiceProfileRetrainerPSRExclave"
+ "SSRVoiceProfileRetrainerSATExclave"
+ "SecureAssetBridge"
+ "SecureAssetMetaData"
+ "SecureAssetPreInstalledBundleBridge"
+ "SecureMemoryIndex"
+ "SecureMemoryIndexDataBridge"
+ "SecureSpeakerRecognitionConfigBridge"
+ "SecureSpeakerRecognitionPhraseConfigBridge"
+ "SecureVoiceTriggerSpeakerRecognitionDecoder"
+ "T@\"<CSVTUIAudioSession>\",&,N,V_audioSession"
+ "T@\"<CSVTUIAudioSessionRecorderDelegate>\",W,N,V_audioSessionRecorderDelegate"
+ "T@\"<SSRVTUITrainingAudioSessionDelegate>\",W,N,V_audioSessionDelegate"
+ "T@\"NSArray\",C,N,V_phraseConfigs"
+ "T@\"NSBundle\",R,N,V_preinstalledAssetBundle"
+ "T@\"NSDictionary\",R,C,N,V_cachedInfo"
+ "T@\"NSDictionary\",R,N,V_voiceProfilesModelFilePathsExclave"
+ "T@\"NSMutableArray\",&,N,V_mIndexData"
+ "T@\"NSMutableArray\",&,N,V_mIndexes"
+ "T@\"NSMutableData\",&,N,V_data"
+ "T@\"NSMutableString\",&,N,V_name"
+ "T@\"NSString\",&,N,V_cachedConfigInfo"
+ "T@\"NSString\",&,N,V_cachedConfigSatInfo"
+ "T@\"NSString\",&,N,V_currentHardwarePlatform"
+ "T@\"NSString\",&,N,V_profileBasePathExclave"
+ "T@\"NSString\",C,N,V_name"
+ "T@\"NSString\",R,C,N,V_category"
+ "T@\"NSString\",R,C,N,V_categoryConfigFileName"
+ "T@\"NSString\",R,C,N,V_configVersion"
+ "T@\"NSString\",R,N,V_hardwarePlatform"
+ "T@\"NSString\",R,N,V_rootDirectory"
+ "T@\"NSURL\",&,N,V_resourcePath"
+ "T@\"NSURL\",R,C,N,V_assetConfigurationPath"
+ "T@\"NSURL\",R,C,N,V_assetPathURL"
+ "T@\"NSURL\",R,C,N,V_categoryResourcePathURL"
+ "T@\"NSURL\",R,C,N,V_resourcePath"
+ "T@\"NSURL\",R,N,V_secureProfileModelFilePath"
+ "T@\"SSRVoiceProfileRetrainingContext\",&,V_ctx"
+ "T@\"SecureAssetBridge\",&,V_asset"
+ "T@\"SecureAssetPreInstalledBundleBridge\",&,N,V_preInstalledBundle"
+ "T@\"SecureMemoryIndex\",R,C,N,V_memoryIndex"
+ "T@\"SecureMemoryIndex\",R,C,N,V_satMemoryIndex"
+ "T@\"SecureSpeakerRecognitionConfigBridge\",&,N,V_configBridge"
+ "TB,N,V_implicitTrainingEnabled"
+ "TB,N,V_useTDTIEnrollment"
+ "TI,N,V_maxEnrollmentUtterances"
+ "TI,N,V_multiUserConfidentScoreThreshold"
+ "TI,N,V_multiUserDeltaScoreThreshold"
+ "TI,N,V_multiUserHighScoreThreshold"
+ "TI,N,V_multiUserLowScoreThreshold"
+ "TI,N,V_numPruningRetentionUtt"
+ "TQ,N,V_maximumSpeakerVectors"
+ "TQ,N,V_memoryIndexCount"
+ "TQ,R,N,V_assettype"
+ "TQ,R,N,V_indexDataLength"
+ "Tf,N,V_bestTriggerScore"
+ "Tf,N,V_combinationWeight"
+ "Tf,N,V_implicitProfileDeltaThreshold"
+ "Tf,N,V_implicitProfileThreshold"
+ "Tf,N,V_implicitVTThreshold"
+ "Tf,N,V_pruningExplicitPSRThreshold"
+ "Tf,N,V_pruningExplicitSATThreshold"
+ "Tf,N,V_pruningPSRThreshold"
+ "Tf,N,V_pruningSATThreshold"
+ "Tf,N,V_satThreshold"
+ "URLForResource:withExtension:"
+ "URLForResource:withExtension:subdirectory:"
+ "UserVoiceProfilePathExclave"
+ "_assetCategoryForAssetType:"
+ "_assetCategoryPathKeyForAssetType:"
+ "_assetConfigurationPath"
+ "_assetPathURL"
+ "_assettype"
+ "_audioSessionDelegate"
+ "_audioSessionRecorderDelegate"
+ "_cachedConfigInfo"
+ "_cachedConfigSatInfo"
+ "_cachedInfo"
+ "_category"
+ "_categoryConfigFileName"
+ "_categoryResourcePathURL"
+ "_combinationWeight: %f\n"
+ "_configBridge"
+ "_configData:"
+ "_configFileNameForAssetType:"
+ "_ctx"
+ "_currentHardwarePlatform"
+ "_decodePhraseConfig:"
+ "_extractProfileData:completion:"
+ "_fetchJsonDictionaryFromFileURL:"
+ "_getBooleanValue:forKey:withDefaultValue:"
+ "_getFloatValue:forKey:withDefaultValue:"
+ "_getIntValue:forKey:withDefaultValue:"
+ "_getSecureAssetRootDirectory:"
+ "_hardwarePlatform"
+ "_implicitProfileDeltaThreshold"
+ "_implicitProfileThreshold"
+ "_implicitProfileThreshold: %f\n"
+ "_implicitTrainingEnabled"
+ "_implicitVTThreshold"
+ "_implicitVTThreshold: %f\n"
+ "_implicit_training_enabled: %d\n"
+ "_indexDataLength"
+ "_initializeCurrentDevicePlatform"
+ "_initializeMemoryIndexForCategory:resourcePath:"
+ "_initializePreInstalledSecureAssetBundle"
+ "_initializePreinstalledAssetBundle"
+ "_installedMobileAssetOfType:forLanguage:ofType:"
+ "_mIndexData"
+ "_mIndexes"
+ "_maxEnrollmentUtterances"
+ "_maxEnrollmentUtterances: %u\n"
+ "_memoryIndex"
+ "_memoryIndexCount"
+ "_multiUserConfidentScoreThreshold"
+ "_multiUserConfidentScoreThreshold: %u\n"
+ "_multiUserDeltaScoreThreshold"
+ "_multiUserDeltaScoreThreshold: %u\n"
+ "_multiUserHighScoreThreshold"
+ "_multiUserHighScoreThreshold: %u\n"
+ "_multiUserLowScoreThreshold"
+ "_multiUserLowScoreThreshold: %u\n"
+ "_name"
+ "_novDetector"
+ "_numPruningRetentionUtt"
+ "_numPruningRetentionUtt: %u\n"
+ "_phraseConfigs"
+ "_preInstalledBundle"
+ "_preinstalledAssetBundle"
+ "_processAudioFile:"
+ "_profileBasePathExclave"
+ "_pruningExplicitPSRThreshold"
+ "_pruningExplicitPSRThreshold: %f\n"
+ "_pruningExplicitSATThreshold"
+ "_pruningExplicitSATThreshold: %f\n"
+ "_pruningPSRThreshold"
+ "_pruningPSRThreshold: %f\n"
+ "_pruningSATThreshold"
+ "_pruningSATThreshold: %f\n"
+ "_resourcePath"
+ "_rootDirectory"
+ "_santizedIndexName:"
+ "_satMemoryIndex"
+ "_satThreshold"
+ "_secureProfileModelFilePath"
+ "_useTDTIEnrollment"
+ "_useTDTIEnrollment: %d\n"
+ "_voiceProfilesModelFilePathsExclave"
+ "assetConfigurationPath"
+ "assetPathURL"
+ "assettype"
+ "audioSession"
+ "audioSessionDelegate"
+ "audioSessionRecorderDelegate"
+ "bestTriggerScore"
+ "bundleURL"
+ "bundleWithPath:"
+ "cString"
+ "cachedConfigInfo"
+ "cachedConfigSatInfo"
+ "cachedInfo"
+ "cannot extract profile embedding; cookie match failed"
+ "cannot extract profile embedding; failed to read profile"
+ "cannot read profile compatible version"
+ "category"
+ "categoryConfigFileName"
+ "categoryResourcePathURL"
+ "com.apple.corespeech.speakerretrain.secure.psrq"
+ "com.apple.corespeech.speakerretrain.secure.satq"
+ "configBridge"
+ "configData"
+ "configDataSat"
+ "configVers=%s, resourcePathURL=%s, assetPathURL=%s0"
+ "config_checker.txt"
+ "config_rt.txt"
+ "config_sat.txt"
+ "config_sr.txt"
+ "containsKey:category:"
+ "corespeech"
+ "createVoiceScorersWithVoiceProfiles:withConfigFile:withResourceFile:withOffsetsType:forRetraining:"
+ "ctx"
+ "currentHardwarePlatform"
+ "dataInBytes"
+ "dataLength"
+ "decodeSecureVoiceTriggerSpeakerRecognitionConfigForAsset:"
+ "decodedInfo"
+ "empty profile"
+ "exclave"
+ "exclaveVoiceProfileModelFilePathForRecognizerType:spIdType:"
+ "f36@0:8@16@24f32"
+ "fetchAssetConfigFileURL:"
+ "fetchAssetMetaDataForLocale:categoryResourcePathKey:"
+ "fetchCategoryResourceDirURL:"
+ "fetchSecureAssetForLocale:assetType:"
+ "file stride is less than number of vectors"
+ "getBool:category:defaultValue:"
+ "getDictionary:category:"
+ "getDictionaryArray:category:"
+ "getFloat:category:defaultValue:"
+ "getString:category:"
+ "getString:category:defaultValue:"
+ "getStringArray:category:"
+ "getUnsignedLongLongValue:category:defaultValue:"
+ "hardwarePlatform"
+ "header specified implausible filesize"
+ "implicitTrainingEnabled"
+ "indexCount"
+ "indexDataLength"
+ "initWithArray:"
+ "initWithAssetType:configurationPath:configVersion:category:categoryResourceURLPath:categoryConfigFileName:"
+ "initWithConfigFilePath:withModelFilePaths:withModelFilePathsExclave:"
+ "initWithConfigFilePath:withModelPath:withModelPathExclave:withCompareModelFilePaths:"
+ "initWithConfigVersion:resourcePath:assetPathURL:"
+ "initWithData:"
+ "initWithData:encoding:"
+ "initWithHardwarePlatform:"
+ "initWithIndexName:data:dataLength:"
+ "initWithName:satThreshold:"
+ "initWithPhraseConfigs:numPruningRetentionUtt:pruningExplicitSATThreshold:pruningExplicitPSRThreshold:pruningSATThreshold:pruningPSRThreshold:combinationWeight:implicitProfileThreshold:implicitProfileDeltaThreshold:implicitVTThreshold:maxEnrollmentUtterances:implicit_training_enabled:multiUserHighScoreThreshold:multiUserLowScoreThreshold:multiUserConfidentScoreThreshold:multiUserDeltaScoreThreshold:useTDTIEnrollment:"
+ "initWithProfileID:withModelFile:withConfigFile:withResourceFile:configData:memoryIndex:withOffsetsType:forRetraining:"
+ "initWithProfileID:withModelFile:withConfigFile:withResourceFile:withOffsetsType:forRetraining:"
+ "initWithResourcePath:memoryIndexes:"
+ "initWithVoiceRetrainingContext:secureAsset:"
+ "injectMemoryIndex:resource:size:"
+ "invalid data format"
+ "iterateMemoryIndexes:"
+ "iteratePhraseConfigs:"
+ "mIndexData"
+ "mIndexes"
+ "maximumSpeakerVectors"
+ "memoryIndex"
+ "memoryIndexCount"
+ "mindex"
+ "mindex:"
+ "mindex_sat"
+ "nameString"
+ "nil vector"
+ "nohash"
+ "phraseConfigs-count: %ld\n"
+ "platforms"
+ "preInstalledBundle"
+ "preinstalledAssetBundle"
+ "preinstalledMeta"
+ "profileBasePathExclave"
+ "r*16@0:8"
+ "r^v16@0:8"
+ "relativeAOPKeywordResourcePath"
+ "relativeKeywordResourcePath"
+ "relativePath"
+ "relativeResourcePath"
+ "relativeSpeakerRecognizerResourcePath"
+ "requestAudioProviderForTrainingWithSyncBlock:"
+ "rootDirectory"
+ "rtblobaop"
+ "satMemoryIndex"
+ "secureProfileModelFilePath"
+ "setAudioSession:"
+ "setAudioSessionDelegate:"
+ "setAudioSessionRecorderDelegate:"
+ "setBestTriggerScore:"
+ "setCachedConfigInfo:"
+ "setCachedConfigSatInfo:"
+ "setCombinationWeight:"
+ "setConfigBridge:"
+ "setCtx:"
+ "setCurrentHardwarePlatform:"
+ "setData:"
+ "setImplicitProfileDeltaThreshold:"
+ "setImplicitProfileThreshold:"
+ "setImplicitTrainingEnabled:"
+ "setImplicitVTThreshold:"
+ "setMIndexData:"
+ "setMIndexes:"
+ "setMaxEnrollmentUtterances:"
+ "setMaximumSpeakerVectors:"
+ "setMemoryIndexCount:"
+ "setMultiUserConfidentScoreThreshold:"
+ "setMultiUserDeltaScoreThreshold:"
+ "setMultiUserHighScoreThreshold:"
+ "setMultiUserLowScoreThreshold:"
+ "setName:"
+ "setNumPruningRetentionUtt:"
+ "setPhraseConfigs:"
+ "setPreInstalledBundle:"
+ "setProfileBasePathExclave:"
+ "setPruningExplicitPSRThreshold:"
+ "setPruningExplicitSATThreshold:"
+ "setPruningPSRThreshold:"
+ "setPruningSATThreshold:"
+ "setRequestListeningMicIndicatorLock:"
+ "setRequestRecordModeLock:"
+ "setResourcePath:"
+ "setSatThreshold:"
+ "setUseTDTIEnrollment:"
+ "stride is less than width"
+ "t8132"
+ "unexpected file size"
+ "unexpectedly reached eof"
+ "unused"
+ "updateVoiceProfile:withUserName:withBasePathExclave:"
+ "updateVoiceProfilePathExclave:"
+ "v16@?0@\"CSAudioProvider\"8"
+ "v16@?0@\"SecureMemoryIndexDataBridge\"8"
+ "v20@0:8I16"
+ "v24@0:8@?<v@?@\"CSAudioProvider\">16"
+ "v32@?0@\"NSDictionary\"8Q16^B24"
+ "v32@?0@\"SecureMemoryIndexDataBridge\"8Q16^B24"
+ "v32@?0@\"SecureSpeakerRecognitionPhraseConfigBridge\"8Q16^B24"
+ "v36@0:8r*16r^f24I32"
+ "voiceProfilePathExclave"
+ "voiceProfilesModelFilePathsExclave"
+ "voiceTriggerFirstPass"
+ "{%@:%@:%@:%@}"
+ "\x81"
- "\b"
- "+[SSRSpeakerRecognitionScorer createVoiceScorersWithVoiceProfiles:withConfigFile:withResourceFile:withOffsetsType:]"
- "-[CSVTUIAudioSessionRecorder init]"
- "-[SSRMobileAssetProvider _installedMobileAssetOfType:forLanguage:]"
- "-[SSRSpeakerRecognitionScorer initWithProfileID:withModelFile:withConfigFile:withResourceFile:withOffsetsType:]"
- "@48@0:8@16@24@32Q40"
- "@56@0:8@16@24@32@40Q48"
- "createVoiceScorersWithVoiceProfiles:withConfigFile:withResourceFile:withOffsetsType:"
- "initWithProfileID:withModelFile:withConfigFile:withResourceFile:withOffsetsType:"

```
