## CoreEmbeddedSpeechRecognition

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition`

```diff

-3500.110.4.0.0
-  __TEXT.__text: 0x182d64
-  __TEXT.__auth_stubs: 0x2d80
-  __TEXT.__objc_methlist: 0x41a8
+3500.115.2.0.0
+  __TEXT.__text: 0x1843a0
+  __TEXT.__auth_stubs: 0x2da0
+  __TEXT.__objc_methlist: 0x4348
   __TEXT.__const: 0x1618
-  __TEXT.__cstring: 0xb334
+  __TEXT.__cstring: 0xb5e8
   __TEXT.__swift5_typeref: 0x1c76
   __TEXT.__swift5_capture: 0x46c0
   __TEXT.__constg_swiftt: 0xa74
-  __TEXT.__swift5_reflstr: 0x893
-  __TEXT.__swift5_fieldmd: 0x7f8
+  __TEXT.__swift5_reflstr: 0x8a3
+  __TEXT.__swift5_fieldmd: 0x804
   __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_assocty: 0x150
   __TEXT.__swift5_proto: 0xa0
   __TEXT.__swift5_types: 0xa0
-  __TEXT.__oslogstring: 0x8304
+  __TEXT.__oslogstring: 0x8543
   __TEXT.__swift_as_entry: 0x160
-  __TEXT.__swift_as_ret: 0x1c0
+  __TEXT.__swift_as_ret: 0x1c4
   __TEXT.__gcc_except_tab: 0xc40
-  __TEXT.__unwind_info: 0x2360
-  __TEXT.__eh_frame: 0x2360
-  __TEXT.__objc_classname: 0xa6c
-  __TEXT.__objc_methname: 0xda30
-  __TEXT.__objc_methtype: 0x2cf4
-  __TEXT.__objc_stubs: 0x77a0
-  __DATA_CONST.__got: 0xf78
-  __DATA_CONST.__const: 0x14e0
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __TEXT.__unwind_info: 0x23a0
+  __TEXT.__eh_frame: 0x2388
+  __TEXT.__objc_classname: 0xa97
+  __TEXT.__objc_methname: 0xe2b6
+  __TEXT.__objc_methtype: 0x2d54
+  __TEXT.__objc_stubs: 0x7d20
+  __DATA_CONST.__got: 0xfd0
+  __DATA_CONST.__const: 0x1540
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xc8
+  __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d78
+  __DATA_CONST.__objc_selrefs: 0x2eb8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x200
-  __DATA_CONST.__objc_arraydata: 0x190
-  __AUTH_CONST.__auth_got: 0x16d8
-  __AUTH_CONST.__const: 0xbdc0
-  __AUTH_CONST.__cfstring: 0x4960
-  __AUTH_CONST.__objc_const: 0x8388
-  __AUTH_CONST.__objc_intobj: 0x630
+  __DATA_CONST.__objc_superrefs: 0x210
+  __DATA_CONST.__objc_arraydata: 0x380
+  __AUTH_CONST.__auth_got: 0x16e8
+  __AUTH_CONST.__const: 0xbe40
+  __AUTH_CONST.__cfstring: 0x4980
+  __AUTH_CONST.__objc_const: 0x8600
+  __AUTH_CONST.__objc_intobj: 0x9a8
   __AUTH_CONST.__objc_arrayobj: 0x1e0
-  __AUTH.__objc_data: 0xbf0
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH.__objc_data: 0xc90
   __AUTH.__data: 0x808
-  __DATA.__objc_ivar: 0x530
-  __DATA.__data: 0x14b0
-  __DATA.__bss: 0xd88
+  __DATA.__objc_ivar: 0x554
+  __DATA.__data: 0x1500
+  __DATA.__bss: 0xdc8
   __DATA.__common: 0x90
-  __DATA_DIRTY.__objc_data: 0xde0
+  __DATA_DIRTY.__objc_data: 0xd90
   __DATA_DIRTY.__data: 0x10c8
-  __DATA_DIRTY.__bss: 0x768
+  __DATA_DIRTY.__bss: 0x758
   __DATA_DIRTY.__common: 0x12
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0DDF1FF9-1749-359A-8E1F-BC9BD6DBEAB3
-  Functions: 4628
-  Symbols:   5998
-  CStrings:  4667
+  UUID: 12EAA623-22C3-3C57-909B-7EE7C52212E8
+  Functions: 4665
+  Symbols:   6161
+  CStrings:  4756
 
Symbols:
+ +[CESRSpeechProfileDispatcher _maintenanceReasonForDarwinNotificationEventWithName:]
+ +[CESRSpeechProfileSelfHelper _cleanupMetricsWithIsIngestionEnabled:numEntitiesContainingEmoji:numEntitiesContainingSpecialCharacters:numEntitiesCleaned:]
+ +[CESRSpeechProfileSelfHelper _extractionMetricsWithIsIngestionEnabled:isExtractionSetupSuccessful:numEntitiesExtractionAttempted:numEntitiesContainingExtractions:numEntitiesExtracted:]
+ +[CESRSpeechProfileSettings _isDeviceChargingAboveThreshold]
+ +[CESRSpeechProfileSettings _isDevicePowerConstrained]
+ +[CESRSpeechProfileSettings _shouldUpdateOnM11WatchForSets:]
+ +[CESRSpeechProfileSettings deviceHasFavorablePowerConditions]
+ +[CESRSpeechProfileSettings updateCadenceForSets:]
+ +[CESRUtilities isUODCapableWatchOSDevice]
+ -[CESRSpeechProfileDispatcher newPersonas:]
+ -[CESRSpeechProfileDispatcher removedPersonas:]
+ -[CESRSpeechProfileMetrics description]
+ -[CESRSpeechProfileMetrics init]
+ -[CESRSpeechProfileMetrics isCleanupIngestionEnabled]
+ -[CESRSpeechProfileMetrics isExtractionIngestionEnabled]
+ -[CESRSpeechProfileMetrics isExtractionSetupSuccessful]
+ -[CESRSpeechProfileMetrics numEntitiesCleaned]
+ -[CESRSpeechProfileMetrics numEntitiesContainingEmoji]
+ -[CESRSpeechProfileMetrics numEntitiesContainingExtractions]
+ -[CESRSpeechProfileMetrics numEntitiesContainingSpecialCharacters]
+ -[CESRSpeechProfileMetrics numEntitiesExtracted]
+ -[CESRSpeechProfileMetrics numEntitiesExtractionAttempted]
+ -[CESRSpeechProfileMetrics reset]
+ -[CESRSpeechProfileMetrics setIsCleanupIngestionEnabled:]
+ -[CESRSpeechProfileMetrics setIsExtractionIngestionEnabled:]
+ -[CESRSpeechProfileMetrics setIsExtractionSetupSuccessful:]
+ -[CESRSpeechProfileMetrics setNumEntitiesCleaned:]
+ -[CESRSpeechProfileMetrics setNumEntitiesContainingEmoji:]
+ -[CESRSpeechProfileMetrics setNumEntitiesContainingExtractions:]
+ -[CESRSpeechProfileMetrics setNumEntitiesContainingSpecialCharacters:]
+ -[CESRSpeechProfileMetrics setNumEntitiesExtracted:]
+ -[CESRSpeechProfileMetrics setNumEntitiesExtractionAttempted:]
+ -[CESRSpeechProfileMetrics setTotalNumEntitiesReceived:]
+ -[CESRSpeechProfileMetrics totalNumEntitiesReceived]
+ -[CESRSpeechProfileSelfHelper .cxx_destruct]
+ -[CESRSpeechProfileSelfHelper init]
+ -[CESRSpeechProfileSelfHelper logASRSpeechProfileUpdateEndedWithTotalNumEntitiesReceived:entityCleanupMetrics:entityExtractionMetrics:]
+ -[CESRSpeechProfileSelfHelper logASRSpeechProfileUpdateEndedWithUserDataMetrics:]
+ -[CESRSpeechProfileSelfHelper logASRSpeechProfileUpdateFailedWithReason:]
+ -[CESRSpeechProfileSelfHelper logASRSpeechProfileUpdateStarted]
+ -[CESRSpeechProfileSelfHelper wrapAndEmitTopLevelEvent:]
+ -[CESRSpeechProfileSiteManager _maintainAllSites:shouldDefer:]
+ -[CESRSpeechProfileSiteManager _maintainSiteAtURL:rebuildOnly:shouldDefer:]
+ -[CESRSpeechProfileSiteManager handleNewPersonas:]
+ -[CESRSpeechProfileSiteManager handleRemovedPersonas:]
+ -[CESRSpeechProfileSiteManager performMaintenance:shouldDefer:]
+ -[CESRSpeechProfileSiteWriter _verifyAllProfileInstances:shouldDefer:]
+ -[CESRSpeechProfileSiteWriter verifyAllProfileInstances:shouldDefer:]
+ GCC_except_table1014
+ GCC_except_table1068
+ GCC_except_table1069
+ GCC_except_table1070
+ GCC_except_table1071
+ GCC_except_table1072
+ GCC_except_table1073
+ GCC_except_table1077
+ GCC_except_table1078
+ GCC_except_table1081
+ GCC_except_table1218
+ GCC_except_table1308
+ GCC_except_table1314
+ GCC_except_table1319
+ GCC_except_table1323
+ GCC_except_table133
+ GCC_except_table1367
+ GCC_except_table1375
+ GCC_except_table1380
+ GCC_except_table1384
+ GCC_except_table154
+ GCC_except_table199
+ GCC_except_table276
+ GCC_except_table295
+ GCC_except_table298
+ GCC_except_table345
+ GCC_except_table366
+ GCC_except_table46
+ GCC_except_table516
+ GCC_except_table524
+ GCC_except_table528
+ GCC_except_table531
+ GCC_except_table534
+ GCC_except_table537
+ GCC_except_table540
+ GCC_except_table543
+ GCC_except_table546
+ GCC_except_table63
+ GCC_except_table643
+ GCC_except_table678
+ GCC_except_table68
+ GCC_except_table711
+ GCC_except_table75
+ GCC_except_table84
+ GCC_except_table89
+ GCC_except_table906
+ GCC_except_table911
+ _AFIsUODCapableWatchOSDevice
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileClientEvent
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted
+ _OBJC_CLASS_$_CESRSpeechProfileMetrics
+ _OBJC_CLASS_$_CESRSpeechProfileSelfHelper
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_SFSpeechProfileResourceMonitor
+ _OBJC_IVAR_$_CESRSpeechProfileMetrics._isCleanupIngestionEnabled
+ _OBJC_IVAR_$_CESRSpeechProfileMetrics._isExtractionIngestionEnabled
+ _OBJC_IVAR_$_CESRSpeechProfileMetrics._isExtractionSetupSuccessful
+ _OBJC_IVAR_$_CESRSpeechProfileMetrics._numEntitiesCleaned
+ _OBJC_IVAR_$_CESRSpeechProfileMetrics._numEntitiesContainingEmoji
+ _OBJC_IVAR_$_CESRSpeechProfileMetrics._numEntitiesContainingExtractions
+ _OBJC_IVAR_$_CESRSpeechProfileMetrics._numEntitiesContainingSpecialCharacters
+ _OBJC_IVAR_$_CESRSpeechProfileMetrics._numEntitiesExtracted
+ _OBJC_IVAR_$_CESRSpeechProfileMetrics._numEntitiesExtractionAttempted
+ _OBJC_IVAR_$_CESRSpeechProfileMetrics._totalNumEntitiesReceived
+ _OBJC_IVAR_$_CESRSpeechProfileSelfHelper._componentId
+ _OBJC_METACLASS_$_CESRSpeechProfileMetrics
+ _OBJC_METACLASS_$_CESRSpeechProfileSelfHelper
+ __OBJC_$_CLASS_METHODS_CESRSpeechProfileSelfHelper
+ __OBJC_$_INSTANCE_METHODS_CESRSpeechProfileMetrics
+ __OBJC_$_INSTANCE_METHODS_CESRSpeechProfileSelfHelper
+ __OBJC_$_INSTANCE_VARIABLES_CESRSpeechProfileMetrics
+ __OBJC_$_INSTANCE_VARIABLES_CESRSpeechProfileSelfHelper
+ __OBJC_$_PROP_LIST_CESRSpeechProfileMetrics
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SFPersonaManagerObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SFSpeechProfileResourceMonitorObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFSpeechProfileResourceMonitorObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFPersonaManagerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFSpeechProfileResourceMonitorObserver
+ __OBJC_$_PROTOCOL_REFS_SFPersonaManagerObserver
+ __OBJC_$_PROTOCOL_REFS_SFSpeechProfileResourceMonitorObserver
+ __OBJC_CLASS_RO_$_CESRSpeechProfileMetrics
+ __OBJC_CLASS_RO_$_CESRSpeechProfileSelfHelper
+ __OBJC_LABEL_PROTOCOL_$_SFPersonaManagerObserver
+ __OBJC_LABEL_PROTOCOL_$_SFSpeechProfileResourceMonitorObserver
+ __OBJC_METACLASS_RO_$_CESRSpeechProfileMetrics
+ __OBJC_METACLASS_RO_$_CESRSpeechProfileSelfHelper
+ __OBJC_PROTOCOL_$_SFPersonaManagerObserver
+ __OBJC_PROTOCOL_$_SFSpeechProfileResourceMonitorObserver
+ ___103-[CoreEmbeddedSpeechRecognizer preheatSpeechRecognitionWithAssetConfig:preheatSource:modelOverrideURL:]_block_invoke.345
+ ___120-[CESRSpeechProfileBuilder _setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:]_block_invoke.380
+ ___43-[CESRSpeechProfileDispatcher newPersonas:]_block_invoke
+ ___43-[CoreEmbeddedSpeechRecognizer _connection]_block_invoke.341
+ ___47-[CESRSpeechProfileDispatcher removedPersonas:]_block_invoke
+ ___48-[CESRSpeechProfileBuilder addCodepathId:error:]_block_invoke.384
+ ___49+[CESRSpeechProfileBuilder _fieldTypeFromString:]_block_invoke
+ ___49-[CESRSpeechProfileBuilder _flushItemsWithError:]_block_invoke.395
+ ___50-[CESRSpeechProfileSiteManager handleNewPersonas:]_block_invoke
+ ___50-[CESRSpeechProfileSiteManager handleNewPersonas:]_block_invoke.314
+ ___51+[CoreEmbeddedSpeechRecognizer forceCooldownIfIdle]_block_invoke.358
+ ___51-[CESRSpeechProfileBuilder removeCodepathId:error:]_block_invoke.385
+ ___52-[CESRSpeechProfileBuilder getCodepathIdsWithError:]_block_invoke.387
+ ___54-[CESRSpeechProfileBuilder cancelCategoriesWithError:]_block_invoke.396
+ ___54-[CESRSpeechProfileSiteManager handleRemovedPersonas:]_block_invoke
+ ___55-[CESRSpeechProfileBuilder finishAndSaveProfile:error:]_block_invoke.397
+ ___56-[CESRSpeechProfileBuilder getVersionForCategory:error:]_block_invoke.382
+ ___58+[CoreEmbeddedSpeechRecognizer cleanupUnusedSubscriptions]_block_invoke.349
+ ___58-[CESRSpeechProfileSiteWriter logRequiredProfileInstances]_block_invoke.287
+ ___60+[CESRSpeechProfileSettings _shouldUpdateOnM11WatchForSets:]_block_invoke
+ ___62+[CESRSpeechProfileSettings itemTypesRequiringImmediateUpdate]_block_invoke
+ ___62+[CoreEmbeddedSpeechRecognizer handlePostInstallSubscriptions]_block_invoke.347
+ ___62-[CESRSpeechProfileSiteManager _maintainAllSites:shouldDefer:]_block_invoke
+ ___62-[CESRSpeechProfileSiteManager handleSiteAvailableForPersona:]_block_invoke.313
+ ___63-[CESRSpeechProfileSiteManager performMaintenance:shouldDefer:]_block_invoke
+ ___65-[CoreEmbeddedSpeechRecognizer removePersonalizedLMForFidesOnly:]_block_invoke.423
+ ___68+[CoreEmbeddedSpeechRecognizer compileAllAssetsWithType:completion:]_block_invoke.353
+ ___69-[CESRSpeechProfileDispatcher handleDarwinNotificationEventWithName:]_block_invoke.353
+ ___69-[CESRSpeechProfileSiteManager _registerTrialExperimentUpdateHandler]_block_invoke.302
+ ___70-[CESRSpeechProfileSiteWriter _verifyAllProfileInstances:shouldDefer:]_block_invoke
+ ___70-[CESRSpeechProfileSiteWriter addBookmarksForLocale:toChangeRegistry:]_block_invoke.293
+ ___73+[CESRUtilities AFSpeechInfoPackageForEARSpeechRecognitionResultPackage:]_block_invoke.349
+ ___74-[CESRSpeechProfileBuilder beginWithCategoriesAndVersions:bundleId:error:]_block_invoke.389
+ ___75+[CoreEmbeddedSpeechRecognizer compilePrimaryAssistantAssetWithCompletion:]_block_invoke.357
+ ___78-[CoreEmbeddedSpeechRecognizer deleteAllDESRecordsForDictationPersonalization]_block_invoke.397
+ ___83-[CESRSpeechProfileSiteWriter _updateRequiredProfileInstancesWithSets:shouldDefer:]_block_invoke.308
+ ___84+[CESRSpeechProfileDispatcher _maintenanceReasonForDarwinNotificationEventWithName:]_block_invoke
+ ___86-[CoreEmbeddedSpeechRecognizer preheatSpeechRecognitionWithLanguage:modelOverrideURL:]_block_invoke.343
+ ___93-[CoreEmbeddedSpeechRecognizer startSpeechRecognitionWithParameters:didStartHandlerWithInfo:]_block_invoke.371
+ ___93-[CoreEmbeddedSpeechRecognizer startSpeechRecognitionWithParameters:didStartHandlerWithInfo:]_block_invoke.372
+ ___Block_byref_object_copy_.1055
+ ___Block_byref_object_copy_.1429
+ ___Block_byref_object_copy_.1922
+ ___Block_byref_object_copy_.2167
+ ___Block_byref_object_copy_.2870
+ ___Block_byref_object_copy_.3358
+ ___Block_byref_object_copy_.383
+ ___Block_byref_object_copy_.449
+ ___Block_byref_object_copy_.4493
+ ___Block_byref_object_copy_.941
+ ___Block_byref_object_dispose_.1056
+ ___Block_byref_object_dispose_.1430
+ ___Block_byref_object_dispose_.1923
+ ___Block_byref_object_dispose_.2168
+ ___Block_byref_object_dispose_.2871
+ ___Block_byref_object_dispose_.3359
+ ___Block_byref_object_dispose_.384
+ ___Block_byref_object_dispose_.4494
+ ___Block_byref_object_dispose_.450
+ ___Block_byref_object_dispose_.942
+ ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e15_B16?0"NSURL"8ls32l8s40l8
+ ___block_descriptor_57_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_65_e8_32s40s48bs56r_e21_v20?0"NSLocale"8C16ls32l8r56l8s40l8s48l8
+ ___block_literal_global.1465
+ ___block_literal_global.196
+ ___block_literal_global.1992
+ ___block_literal_global.2151
+ ___block_literal_global.220
+ ___block_literal_global.2262
+ ___block_literal_global.228
+ ___block_literal_global.2937
+ ___block_literal_global.302
+ ___block_literal_global.312
+ ___block_literal_global.324
+ ___block_literal_global.333
+ ___block_literal_global.335
+ ___block_literal_global.3395
+ ___block_literal_global.340
+ ___block_literal_global.344
+ ___block_literal_global.345
+ ___block_literal_global.347
+ ___block_literal_global.349
+ ___block_literal_global.353
+ ___block_literal_global.358
+ ___block_literal_global.360
+ ___block_literal_global.362
+ ___block_literal_global.364
+ ___block_literal_global.364.746
+ ___block_literal_global.370
+ ___block_literal_global.3755
+ ___block_literal_global.376
+ ___block_literal_global.379
+ ___block_literal_global.381
+ ___block_literal_global.396
+ ___block_literal_global.420
+ ___block_literal_global.422
+ ___block_literal_global.4259
+ ___block_literal_global.427
+ ___block_literal_global.4535
+ ___block_literal_global.725
+ ___block_literal_global.741
+ __fieldTypeFromString:.fieldTypeForString
+ __fieldTypeFromString:.onceToken
+ __maintenanceReasonForDarwinNotificationEventWithName:.maintenanceReasonForEventName
+ __maintenanceReasonForDarwinNotificationEventWithName:.onceToken
+ __shouldUpdateOnM11WatchForSets:.onceToken
+ __shouldUpdateOnM11WatchForSets:.watchUpdatableItemTypes
+ _itemTypesRequiringImmediateUpdate.highPriorityItemTypes
+ _itemTypesRequiringImmediateUpdate.onceToken
+ _kSFUserSpecificDataSiteName
+ _objc_msgSend$_cleanupMetricsWithIsIngestionEnabled:numEntitiesContainingEmoji:numEntitiesContainingSpecialCharacters:numEntitiesCleaned:
+ _objc_msgSend$_extractionMetricsWithIsIngestionEnabled:isExtractionSetupSuccessful:numEntitiesExtractionAttempted:numEntitiesContainingExtractions:numEntitiesExtracted:
+ _objc_msgSend$_isDeviceChargingAboveThreshold
+ _objc_msgSend$_isDevicePowerConstrained
+ _objc_msgSend$_maintainAllSites:shouldDefer:
+ _objc_msgSend$_maintainSiteAtURL:rebuildOnly:shouldDefer:
+ _objc_msgSend$_maintenanceReasonForDarwinNotificationEventWithName:
+ _objc_msgSend$_verifyAllProfileInstances:shouldDefer:
+ _objc_msgSend$defaultMessageStream
+ _objc_msgSend$deviceHasFavorablePowerConditions
+ _objc_msgSend$emitMessage:isolatedStreamUUID:
+ _objc_msgSend$handleNewPersonas:
+ _objc_msgSend$handleRemovedPersonas:
+ _objc_msgSend$initWithNSUUID:
+ _objc_msgSend$isCleanupIngestionEnabled
+ _objc_msgSend$isExtractionIngestionEnabled
+ _objc_msgSend$isExtractionSetupSuccessful
+ _objc_msgSend$isLowPowerModeEnabled
+ _objc_msgSend$logASRSpeechProfileUpdateEndedWithTotalNumEntitiesReceived:entityCleanupMetrics:entityExtractionMetrics:
+ _objc_msgSend$numEntitiesCleaned
+ _objc_msgSend$numEntitiesContainingEmoji
+ _objc_msgSend$numEntitiesContainingExtractions
+ _objc_msgSend$numEntitiesContainingSpecialCharacters
+ _objc_msgSend$numEntitiesExtracted
+ _objc_msgSend$numEntitiesExtractionAttempted
+ _objc_msgSend$performMaintenance:shouldDefer:
+ _objc_msgSend$processInfo
+ _objc_msgSend$registerLaunchOnDemand
+ _objc_msgSend$reset
+ _objc_msgSend$setEnded:
+ _objc_msgSend$setEntityCleanupMetrics:
+ _objc_msgSend$setEntityExtractionMetrics:
+ _objc_msgSend$setEventMetadata:
+ _objc_msgSend$setExists:
+ _objc_msgSend$setFailed:
+ _objc_msgSend$setIsCleanupIngestionEnabled:
+ _objc_msgSend$setIsExtractionIngestionEnabled:
+ _objc_msgSend$setIsExtractionSetupSuccessful:
+ _objc_msgSend$setNumEntitiesCleaned:
+ _objc_msgSend$setNumEntitiesContainingEmoji:
+ _objc_msgSend$setNumEntitiesContainingExtractions:
+ _objc_msgSend$setNumEntitiesContainingSpecialCharacters:
+ _objc_msgSend$setNumEntitiesExtracted:
+ _objc_msgSend$setNumEntitiesExtractionAttempted:
+ _objc_msgSend$setSpeechProfileId:
+ _objc_msgSend$setSpeechProfileUpdateContext:
+ _objc_msgSend$setSpeechProfileUpdateFailureReason:
+ _objc_msgSend$setStartedOrChanged:
+ _objc_msgSend$setTotalNumEntitiesReceived:
+ _objc_msgSend$sharedAnalytics
+ _objc_msgSend$thermalState
+ _objc_msgSend$totalNumEntitiesReceived
+ _objc_msgSend$updateCadenceForSets:
+ _objc_msgSend$verifyAllProfileInstances:shouldDefer:
+ _objc_msgSend$wrapAndEmitTopLevelEvent:
+ _sharedManager.onceToken.2936
+ _sharedManager.onceToken.724
+ _sharedManager.sharedMyManager.2938
+ _sharedManager.sharedMyManager.726
- +[CESRSpeechProfileResourceMonitor sharedMonitor]
- -[CESRSpeechProfileResourceMonitor .cxx_destruct]
- -[CESRSpeechProfileResourceMonitor _initWithQueue:]
- -[CESRSpeechProfileResourceMonitor _registerLaunchOnDemand]
- -[CESRSpeechProfileResourceMonitor _startSession]
- -[CESRSpeechProfileResourceMonitor _stopSession]
- -[CESRSpeechProfileResourceMonitor addObserver:]
- -[CESRSpeechProfileResourceMonitor init]
- -[CESRSpeechProfileResourceMonitor observers]
- -[CESRSpeechProfileResourceMonitor removeObserver:]
- -[CESRSpeechProfileResourceMonitor setObservers:]
- -[CESRSpeechProfileSiteManager _maintainAllSites:]
- -[CESRSpeechProfileSiteManager _maintainSiteAtURL:shouldDefer:]
- -[CESRSpeechProfileSiteManager performMaintenance:]
- -[CESRSpeechProfileSiteWriter _refreshRankedItemCaches:]
- -[CESRSpeechProfileSiteWriter _verifyAllProfileInstances:]
- -[CESRSpeechProfileSiteWriter verifyAllProfileInstances:]
- GCC_except_table1031
- GCC_except_table1032
- GCC_except_table1033
- GCC_except_table1034
- GCC_except_table1035
- GCC_except_table1036
- GCC_except_table104
- GCC_except_table1040
- GCC_except_table1041
- GCC_except_table1044
- GCC_except_table1181
- GCC_except_table1271
- GCC_except_table1277
- GCC_except_table1282
- GCC_except_table1286
- GCC_except_table1330
- GCC_except_table1338
- GCC_except_table1343
- GCC_except_table1347
- GCC_except_table141
- GCC_except_table162
- GCC_except_table175
- GCC_except_table252
- GCC_except_table271
- GCC_except_table274
- GCC_except_table320
- GCC_except_table341
- GCC_except_table491
- GCC_except_table496
- GCC_except_table499
- GCC_except_table503
- GCC_except_table506
- GCC_except_table509
- GCC_except_table512
- GCC_except_table515
- GCC_except_table518
- GCC_except_table60
- GCC_except_table612
- GCC_except_table647
- GCC_except_table680
- GCC_except_table78
- GCC_except_table83
- GCC_except_table875
- GCC_except_table880
- GCC_except_table90
- GCC_except_table979
- GCC_except_table99
- _OBJC_CLASS_$_CESRSpeechProfileResourceMonitor
- _OBJC_IVAR_$_CESRSpeechProfileResourceMonitor._observers
- _OBJC_IVAR_$_CESRSpeechProfileResourceMonitor._queue
- _OBJC_METACLASS_$_CESRSpeechProfileResourceMonitor
- __OBJC_$_CLASS_METHODS_CESRSpeechProfileResourceMonitor
- __OBJC_$_INSTANCE_METHODS_CESRSpeechProfileResourceMonitor
- __OBJC_$_INSTANCE_VARIABLES_CESRSpeechProfileResourceMonitor
- __OBJC_$_PROP_LIST_CESRSpeechProfileResourceMonitor
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CESRSpeechProfileResourceMonitorDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CESRSpeechProfileResourceMonitorDelegate
- __OBJC_$_PROTOCOL_REFS_CESRSpeechProfileResourceMonitorDelegate
- __OBJC_CLASS_RO_$_CESRSpeechProfileResourceMonitor
- __OBJC_LABEL_PROTOCOL_$_CESRSpeechProfileResourceMonitorDelegate
- __OBJC_METACLASS_RO_$_CESRSpeechProfileResourceMonitor
- __OBJC_PROTOCOL_$_CESRSpeechProfileResourceMonitorDelegate
- ___103-[CoreEmbeddedSpeechRecognizer preheatSpeechRecognitionWithAssetConfig:preheatSource:modelOverrideURL:]_block_invoke.348
- ___120-[CESRSpeechProfileBuilder _setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:]_block_invoke.383
- ___43-[CoreEmbeddedSpeechRecognizer _connection]_block_invoke.344
- ___48-[CESRSpeechProfileBuilder addCodepathId:error:]_block_invoke.387
- ___48-[CESRSpeechProfileResourceMonitor addObserver:]_block_invoke
- ___49+[CESRSpeechProfileResourceMonitor sharedMonitor]_block_invoke
- ___49-[CESRSpeechProfileBuilder _flushItemsWithError:]_block_invoke.398
- ___50-[CESRSpeechProfileSiteManager _maintainAllSites:]_block_invoke
- ___51+[CoreEmbeddedSpeechRecognizer forceCooldownIfIdle]_block_invoke.361
- ___51-[CESRSpeechProfileBuilder removeCodepathId:error:]_block_invoke.388
- ___51-[CESRSpeechProfileResourceMonitor removeObserver:]_block_invoke
- ___51-[CESRSpeechProfileSiteManager performMaintenance:]_block_invoke
- ___52-[CESRSpeechProfileBuilder getCodepathIdsWithError:]_block_invoke.390
- ___54-[CESRSpeechProfileBuilder cancelCategoriesWithError:]_block_invoke.399
- ___55-[CESRSpeechProfileBuilder finishAndSaveProfile:error:]_block_invoke.400
- ___56-[CESRSpeechProfileBuilder getVersionForCategory:error:]_block_invoke.385
- ___58+[CoreEmbeddedSpeechRecognizer cleanupUnusedSubscriptions]_block_invoke.352
- ___58-[CESRSpeechProfileSiteWriter _verifyAllProfileInstances:]_block_invoke
- ___58-[CESRSpeechProfileSiteWriter logRequiredProfileInstances]_block_invoke.290
- ___62+[CoreEmbeddedSpeechRecognizer handlePostInstallSubscriptions]_block_invoke.350
- ___62-[CESRSpeechProfileSiteManager handleSiteAvailableForPersona:]_block_invoke.316
- ___65-[CoreEmbeddedSpeechRecognizer removePersonalizedLMForFidesOnly:]_block_invoke.426
- ___68+[CoreEmbeddedSpeechRecognizer compileAllAssetsWithType:completion:]_block_invoke.356
- ___69-[CESRSpeechProfileDispatcher handleDarwinNotificationEventWithName:]_block_invoke.55
- ___69-[CESRSpeechProfileSiteManager _registerTrialExperimentUpdateHandler]_block_invoke.305
- ___70-[CESRSpeechProfileSiteWriter addBookmarksForLocale:toChangeRegistry:]_block_invoke.296
- ___73+[CESRUtilities AFSpeechInfoPackageForEARSpeechRecognitionResultPackage:]_block_invoke.352
- ___74-[CESRSpeechProfileBuilder beginWithCategoriesAndVersions:bundleId:error:]_block_invoke.392
- ___75+[CoreEmbeddedSpeechRecognizer compilePrimaryAssistantAssetWithCompletion:]_block_invoke.360
- ___78-[CoreEmbeddedSpeechRecognizer deleteAllDESRecordsForDictationPersonalization]_block_invoke.400
- ___83-[CESRSpeechProfileSiteWriter _updateRequiredProfileInstancesWithSets:shouldDefer:]_block_invoke.311
- ___86-[CoreEmbeddedSpeechRecognizer preheatSpeechRecognitionWithLanguage:modelOverrideURL:]_block_invoke.346
- ___93-[CoreEmbeddedSpeechRecognizer startSpeechRecognitionWithParameters:didStartHandlerWithInfo:]_block_invoke.374
- ___93-[CoreEmbeddedSpeechRecognizer startSpeechRecognitionWithParameters:didStartHandlerWithInfo:]_block_invoke.375
- ___Block_byref_object_copy_.1363
- ___Block_byref_object_copy_.1839
- ___Block_byref_object_copy_.2090
- ___Block_byref_object_copy_.2796
- ___Block_byref_object_copy_.3264
- ___Block_byref_object_copy_.409
- ___Block_byref_object_copy_.4382
- ___Block_byref_object_copy_.475
- ___Block_byref_object_copy_.878
- ___Block_byref_object_copy_.992
- ___Block_byref_object_dispose_.1364
- ___Block_byref_object_dispose_.1840
- ___Block_byref_object_dispose_.2091
- ___Block_byref_object_dispose_.2797
- ___Block_byref_object_dispose_.3265
- ___Block_byref_object_dispose_.410
- ___Block_byref_object_dispose_.4383
- ___Block_byref_object_dispose_.476
- ___Block_byref_object_dispose_.879
- ___Block_byref_object_dispose_.993
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56r_e21_v20?0"NSLocale"8C16ls32l8r56l8s40l8s48l8
- ___block_literal_global.1909
- ___block_literal_global.2074
- ___block_literal_global.2186
- ___block_literal_global.224
- ___block_literal_global.248
- ___block_literal_global.256
- ___block_literal_global.2861
- ___block_literal_global.327
- ___block_literal_global.3297
- ___block_literal_global.336
- ___block_literal_global.341
- ___block_literal_global.346
- ___block_literal_global.348
- ___block_literal_global.350
- ___block_literal_global.352
- ___block_literal_global.359
- ___block_literal_global.361
- ___block_literal_global.363
- ___block_literal_global.365
- ___block_literal_global.3660
- ___block_literal_global.367
- ___block_literal_global.373
- ___block_literal_global.382
- ___block_literal_global.384
- ___block_literal_global.402
- ___block_literal_global.402.4378
- ___block_literal_global.4149
- ___block_literal_global.423
- ___block_literal_global.428
- ___block_literal_global.430
- ___block_literal_global.4427
- ___block_literal_global.53
- ___block_literal_global.672
- ___block_literal_global.685
- _objc_msgSend$_maintainAllSites:
- _objc_msgSend$_maintainSiteAtURL:shouldDefer:
- _objc_msgSend$_registerLaunchOnDemand
- _objc_msgSend$_startSession
- _objc_msgSend$_stopSession
- _objc_msgSend$_verifyAllProfileInstances:
- _objc_msgSend$isEqualToSet:
- _objc_msgSend$observers
- _objc_msgSend$performMaintenance:
- _objc_msgSend$refreshRankedItemCaches
- _objc_msgSend$verifyAllProfileInstances:
- _sharedManager.onceToken.2860
- _sharedManager.onceToken.671
- _sharedManager.sharedMyManager.2862
- _sharedManager.sharedMyManager.673
- _sharedMonitor.onceToken
- _sharedMonitor.sharedMonitor
CStrings:
+ "%s %@ did not match any known field type."
+ "%s (%@) Deferring update due to platform constraints."
+ "%s (%@) Deferring update due to power conditions."
+ "%s A supported notification was not handled: %@"
+ "%s Failed to resolve site URL for new persona: %@"
+ "%s Failed to resolve site URL for removed persona: %@"
+ "%s Handling new personas: %@"
+ "%s Handling removed personas: %@"
+ "%s Handling sysdiagnose started."
+ "%s Handling updated sets: %@"
+ "%s No known maintenance reason for notification: %@"
+ "%s No required Assistant locale."
+ "%s No required Dictation locales."
+ "%s Performing maintenance for reason: %lu, rebuildOnly: %@"
+ "%s Performing post-install speech profile migration."
+ "%s Required Assistant locale: %@"
+ "%s Required Dictation locales: %@"
+ "%s SELF: Wrapping and logging an event of type %@"
+ "%s Using a deferral window of %lld minutes."
+ "%s eventName cannot be nil."
+ "%s fieldTypeAsString cannot be nil."
+ "%s thermalState=%ld, isLowPowerModeEnabled=%@"
+ "+[CESRSpeechProfileBuilder _fieldTypeFromString:]"
+ "+[CESRSpeechProfileDispatcher _maintenanceReasonForDarwinNotificationEventWithName:]"
+ "+[CESRSpeechProfileSettings _isDevicePowerConstrained]"
+ "-[CESRSpeechProfileDispatcher _notifyChangeToSets:]_block_invoke"
+ "-[CESRSpeechProfileDispatcher handleDarwinNotificationEventWithName:]_block_invoke_5"
+ "-[CESRSpeechProfileSelfHelper wrapAndEmitTopLevelEvent:]"
+ "-[CESRSpeechProfileSiteManager _maintainAllSites:shouldDefer:]"
+ "-[CESRSpeechProfileSiteManager _maintainSiteAtURL:rebuildOnly:shouldDefer:]"
+ "-[CESRSpeechProfileSiteManager handleNewPersonas:]_block_invoke"
+ "-[CESRSpeechProfileSiteManager handleRemovedPersonas:]_block_invoke"
+ "-[CESRSpeechProfileSiteWriter _verifyAllProfileInstances:shouldDefer:]"
+ "<%@: %p; totalNumEntitiesReceived: %u; isCleanupIngestionEnabled: %d; numEntitiesContainingEmoji: %u; numEntitiesContainingSpecialCharacters: %u; numEntitiesCleaned: %u; isExtractionIngestionEnabled: %d; isExtractionSetupSuccessful: %d; numEntitiesExtractionAttempted: %u; numEntitiesContainingExtractions: %u; numEntitiesExtracted: %u>"
+ "@32@0:8B16I20I24I28"
+ "@36@0:8B16B20I24I28I32"
+ "AppIntentsExtractedEntityContent_businessMembershipCard_issuedBy"
+ "B28@0:8B16@?20"
+ "B36@0:8@16B24@?28"
+ "CESRSpeechProfileMetrics"
+ "CESRSpeechProfileSelfHelper"
+ "SFPersonaManagerObserver"
+ "SFSpeechProfileResourceMonitorObserver"
+ "TB,N,V_isCleanupIngestionEnabled"
+ "TB,N,V_isExtractionIngestionEnabled"
+ "TB,N,V_isExtractionSetupSuccessful"
+ "TI,N,V_numEntitiesCleaned"
+ "TI,N,V_numEntitiesContainingEmoji"
+ "TI,N,V_numEntitiesContainingExtractions"
+ "TI,N,V_numEntitiesContainingSpecialCharacters"
+ "TI,N,V_numEntitiesExtracted"
+ "TI,N,V_numEntitiesExtractionAttempted"
+ "TI,N,V_totalNumEntitiesReceived"
+ "The specified locale is not valid."
+ "_cleanupMetricsWithIsIngestionEnabled:numEntitiesContainingEmoji:numEntitiesContainingSpecialCharacters:numEntitiesCleaned:"
+ "_componentId"
+ "_extractionMetricsWithIsIngestionEnabled:isExtractionSetupSuccessful:numEntitiesExtractionAttempted:numEntitiesContainingExtractions:numEntitiesExtracted:"
+ "_isCleanupIngestionEnabled"
+ "_isDeviceChargingAboveThreshold"
+ "_isDevicePowerConstrained"
+ "_isExtractionIngestionEnabled"
+ "_isExtractionSetupSuccessful"
+ "_maintainAllSites:shouldDefer:"
+ "_maintainSiteAtURL:rebuildOnly:shouldDefer:"
+ "_maintenanceReasonForDarwinNotificationEventWithName:"
+ "_numEntitiesCleaned"
+ "_numEntitiesContainingEmoji"
+ "_numEntitiesContainingExtractions"
+ "_numEntitiesContainingSpecialCharacters"
+ "_numEntitiesExtracted"
+ "_numEntitiesExtractionAttempted"
+ "_shouldUpdateOnM11WatchForSets:"
+ "_totalNumEntitiesReceived"
+ "_verifyAllProfileInstances:shouldDefer:"
+ "com.apple.corespeechd.speechprofileupdate"
+ "deviceHasFavorablePowerConditions"
+ "handleNewPersonas:"
+ "handleRemovedPersonas:"
+ "isCleanupIngestionEnabled"
+ "isExtractionIngestionEnabled"
+ "isExtractionSetupSuccessful"
+ "isLowPowerModeEnabled"
+ "isUODCapableWatchOSDevice"
+ "logASRSpeechProfileUpdateEndedWithTotalNumEntitiesReceived:entityCleanupMetrics:entityExtractionMetrics:"
+ "logASRSpeechProfileUpdateEndedWithUserDataMetrics:"
+ "logASRSpeechProfileUpdateFailedWithReason:"
+ "logASRSpeechProfileUpdateStarted"
+ "newPersonas:"
+ "numEntitiesCleaned"
+ "numEntitiesContainingEmoji"
+ "numEntitiesContainingExtractions"
+ "numEntitiesContainingSpecialCharacters"
+ "numEntitiesExtracted"
+ "numEntitiesExtractionAttempted"
+ "performMaintenance:shouldDefer:"
+ "registerLaunchOnDemand"
+ "removedPersonas:"
+ "reset"
+ "setEntityCleanupMetrics:"
+ "setEntityExtractionMetrics:"
+ "setExists:"
+ "setIsCleanupIngestionEnabled:"
+ "setIsExtractionIngestionEnabled:"
+ "setIsExtractionSetupSuccessful:"
+ "setNumEntitiesCleaned:"
+ "setNumEntitiesContainingEmoji:"
+ "setNumEntitiesContainingExtractions:"
+ "setNumEntitiesContainingSpecialCharacters:"
+ "setNumEntitiesExtracted:"
+ "setNumEntitiesExtractionAttempted:"
+ "setSpeechProfileId:"
+ "setSpeechProfileUpdateContext:"
+ "setSpeechProfileUpdateFailureReason:"
+ "setTotalNumEntitiesReceived:"
+ "thermalState"
+ "totalNumEntitiesReceived"
+ "updateCadenceForSets:"
+ "v24@0:8@\"NSSet\"16"
+ "v36@0:8I16@20@28"
+ "verifyAllProfileInstances:shouldDefer:"
+ "wrapAndEmitTopLevelEvent:"
- "%s (%@) Aborting update due to deferral signal."
- "%s A supported notification was NOT handled: %@"
- "%s Performing maintenance due to notification: %@"
- "%s Performing post-upgrade speech profile migration."
- "%s Required locales for Dictation have changed, previous: %@, current: %@"
- "%s The required locale for Assistant has changed, previous: %@, current: %@"
- "-[CESRSpeechProfileSiteManager _maintainAllSites:]"
- "-[CESRSpeechProfileSiteManager _maintainSiteAtURL:shouldDefer:]"
- "-[CESRSpeechProfileSiteWriter _refreshRankedItemCaches:]"
- "-[CESRSpeechProfileSiteWriter _verifyAllProfileInstances:]"
- "@\"NSHashTable\""
- "AppIntentsExtractedEntityContent_businessMembershipCard_issueBy"
- "CESRSpeechProfileResourceMonitor"
- "CESRSpeechProfileResourceMonitorDelegate"
- "T@\"NSHashTable\",&,N,V_observers"
- "_maintainAllSites:"
- "_maintainSiteAtURL:shouldDefer:"
- "_observers"
- "_refreshRankedItemCaches:"
- "_registerLaunchOnDemand"
- "_startSession"
- "_stopSession"
- "_verifyAllProfileInstances:"
- "com.apple.corespeechd.speechprofileassetstartup"
- "com.apple.corespeechd.speechprofileassetupdate"
- "com.apple.corespeechd.speechprofilefirstunlock"
- "com.apple.corespeechd.speechprofilesettingschange"
- "com.apple.corespeechd.speechprofilesysdiagnosestarted"
- "isEqualToSet:"
- "observers"
- "performMaintenance:"
- "removeObserver:"
- "setObservers:"
- "verifyAllProfileInstances:"

```
