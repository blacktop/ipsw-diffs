## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1329.80.6.0.0
-  __TEXT.__text: 0x264644
+1329.80.15.0.1
+  __TEXT.__text: 0x26807c
   __TEXT.__auth_stubs: 0x2390
-  __TEXT.__objc_stubs: 0x1fd80
-  __TEXT.__objc_methlist: 0xf0a0
-  __TEXT.__const: 0x494e
-  __TEXT.__objc_methname: 0x3797b
-  __TEXT.__cstring: 0x4d4fc
-  __TEXT.__objc_classname: 0xd7b
-  __TEXT.__objc_methtype: 0x35c5
-  __TEXT.__oslogstring: 0x31588
-  __TEXT.__gcc_except_tab: 0x2540
+  __TEXT.__objc_stubs: 0x20120
+  __TEXT.__objc_methlist: 0xf258
+  __TEXT.__const: 0x495e
+  __TEXT.__objc_methname: 0x37ee2
+  __TEXT.__cstring: 0x4d9ec
+  __TEXT.__objc_classname: 0xd93
+  __TEXT.__objc_methtype: 0x35fa
+  __TEXT.__oslogstring: 0x31d5d
+  __TEXT.__gcc_except_tab: 0x2564
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x10c4
   __TEXT.__constg_swiftt: 0x1530

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x4870
+  __TEXT.__unwind_info: 0x48e8
   __TEXT.__eh_frame: 0x30c4
   __DATA_CONST.__auth_got: 0x11d8
   __DATA_CONST.__got: 0x6c8
   __DATA_CONST.__auth_ptr: 0x9c8
-  __DATA_CONST.__const: 0x6700
-  __DATA_CONST.__cfstring: 0x31ce0
-  __DATA_CONST.__objc_classlist: 0x3e0
+  __DATA_CONST.__const: 0x6740
+  __DATA_CONST.__cfstring: 0x32280
+  __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8c18
+  __DATA_CONST.__objc_selrefs: 0x8d38
   __DATA_CONST.__objc_intobj: 0x3f0
-  __DATA_CONST.__objc_arraydata: 0x9b8
-  __DATA_CONST.__objc_arrayobj: 0x1e0
+  __DATA_CONST.__objc_arraydata: 0xab0
+  __DATA_CONST.__objc_arrayobj: 0x228
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x145e8
-  __DATA.__objc_classrefs: 0x7b0
-  __DATA.__objc_superrefs: 0x2e8
-  __DATA.__objc_ivar: 0x1290
-  __DATA.__objc_data: 0xd10
+  __DATA.__objc_const: 0x14868
+  __DATA.__objc_classrefs: 0x7b8
+  __DATA.__objc_superrefs: 0x2f0
+  __DATA.__objc_ivar: 0x12b8
+  __DATA.__objc_data: 0xd60
   __DATA.__data: 0x2608
-  __DATA.__bss: 0x53b0
+  __DATA.__bss: 0x53d0
   __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x1978
-  __DATA_DIRTY.__bss: 0x340
+  __DATA_DIRTY.__bss: 0x348
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8323
-  Symbols:   14937
-  CStrings:  15880
+  Functions: 8376
+  Symbols:   15046
+  CStrings:  16004
 
Symbols:
+ +[MADAutoAssetControlManager getHealthReportForSets:]
+ +[MobileAssetHealthReport sharedInstance]
+ -[MADAnalyticsManager recordDownloadAttemptForAssetType:clientName:baseUrl:relativePath:purpose:result:analyticsFileType:isAutoDownload:isPallas:pallasAssetAudience:isUserPriority:bytesWritten:bytesTransferredEst:brainVersion:withTaskMetrics:withOptions:additionalData:]
+ -[MADAutoAssetControlManager _getHealthReportForSets:]
+ -[MADAutoAssetControlManager _initializePeriodicHealthReport]
+ -[MADAutoAssetControlManager setStartupTransaction:]
+ -[MADAutoAssetControlManager startupTransaction]
+ -[MADAutoAssetStager _blendCandidateSetConfigurations:blendingIntoRequiredConfigurations:blendingFromOptionalConfigurations:]
+ -[MADAutoAssetStager _updateLookupResultsJustStagedAllMode:]
+ -[MADAutoAssetStager _updateLookupResultsJustStagedByGroupMode:]
+ -[MADAutoAssetStager _updateLookupResultsJustStagedByGroupMode:].cold.1
+ -[MADAutoAssetStager cachingEnabled]
+ -[MADAutoAssetStager getTargetLookupResultsForKey:]
+ -[MADAutoAssetStager indexForAssetType:representedInSetConfigurations:]
+ -[MADAutoAssetStager newSetLookupResult:forAssetType:forSetCatalog:]
+ -[MADAutoAssetStager setCachingEnabled:]
+ -[MADAutoAssetStager targetLookupResultsLoadedFromPersisted:targetLookupResultsKey:persistedEntryID:]
+ -[MobileAssetHealthReport .cxx_destruct]
+ -[MobileAssetHealthReport _collectAndSubmitReport]
+ -[MobileAssetHealthReport _collectAndSubmitReport].cold.1
+ -[MobileAssetHealthReport dateOfFirstRunInCurrentOS]
+ -[MobileAssetHealthReport getHealthReport]
+ -[MobileAssetHealthReport getLastReportDate]
+ -[MobileAssetHealthReport getSystemInformation]
+ -[MobileAssetHealthReport importantSetIdentifiers]
+ -[MobileAssetHealthReport initWithInterval:leeway:]
+ -[MobileAssetHealthReport initWithInterval:leeway:].cold.1
+ -[MobileAssetHealthReport logger]
+ -[MobileAssetHealthReport persistedStateDispatchQueue]
+ -[MobileAssetHealthReport reportCadance]
+ -[MobileAssetHealthReport reportLeeway]
+ -[MobileAssetHealthReport reportQueue]
+ -[MobileAssetHealthReport reportTimer]
+ -[MobileAssetHealthReport scheduleReport:]
+ -[MobileAssetHealthReport setDateOfFirstRunInCurrentOS:]
+ -[MobileAssetHealthReport setLastRerpotDate:]
+ -[MobileAssetHealthReport setPersistedStateDispatchQueue:]
+ -[MobileAssetHealthReport setReportCadance:]
+ -[MobileAssetHealthReport setReportLeeway:]
+ -[MobileAssetHealthReport setReportQueue:]
+ -[MobileAssetHealthReport setReportTimer:]
+ -[MobileAssetHealthReport setState:]
+ -[MobileAssetHealthReport state]
+ GCC_except_table0
+ GCC_except_table131
+ GCC_except_table138
+ GCC_except_table169
+ GCC_except_table250
+ GCC_except_table378
+ GCC_except_table543
+ GCC_except_table545
+ GCC_except_table548
+ GCC_except_table550
+ GCC_except_table564
+ GCC_except_table68
+ GCC_except_table696
+ GCC_except_table91
+ OBJC_IVAR_$_MADAutoAssetControlManager._startupTransaction
+ OBJC_IVAR_$_MADAutoAssetStager._cachingEnabled
+ OBJC_IVAR_$_MobileAssetHealthReport._dateOfFirstRunInCurrentOS
+ OBJC_IVAR_$_MobileAssetHealthReport._logger
+ OBJC_IVAR_$_MobileAssetHealthReport._persistedStateDispatchQueue
+ OBJC_IVAR_$_MobileAssetHealthReport._reportCadance
+ OBJC_IVAR_$_MobileAssetHealthReport._reportLeeway
+ OBJC_IVAR_$_MobileAssetHealthReport._reportQueue
+ OBJC_IVAR_$_MobileAssetHealthReport._reportTimer
+ OBJC_IVAR_$_MobileAssetHealthReport._state
+ _OBJC_CLASS_$_MobileAssetHealthReport
+ _OBJC_METACLASS_$_MobileAssetHealthReport
+ __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1114
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1043
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1047
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1063
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1125
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1126
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1130
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1149
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1149.cold.1
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1159
+ __27-[MABrainUpdater schedule:]_block_invoke_2.417
+ __27-[MABrainUpdater schedule:]_block_invoke_3.418
+ __42-[MobileAssetHealthReport scheduleReport:]_block_invoke.988
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1073
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1120
+ __46-[MABAACertManager issueAndCopyCertsInternal:]_block_invoke.359
+ __51-[MobileAssetHealthReport initWithInterval:leeway:]_block_invoke.cold.1
+ __51-[MobileAssetHealthReport initWithInterval:leeway:]_block_invoke.cold.2
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1169
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1169.cold.1
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1176
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1137
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1138
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1139
+ __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1003
+ __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.983
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.295
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1107
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1125
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1091
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1098
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1099
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2118
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2311
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2312
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2312.cold.1
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1076
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1077
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1078
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1112
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1113
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1113.cold.1
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1115
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1115.cold.1
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.2886
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.2887
+ __OBJC_$_CLASS_METHODS_MobileAssetHealthReport
+ __OBJC_$_INSTANCE_METHODS_MobileAssetHealthReport
+ __OBJC_$_INSTANCE_VARIABLES_MobileAssetHealthReport
+ __OBJC_$_PROP_LIST_MobileAssetHealthReport
+ __OBJC_CLASS_RO_$_MobileAssetHealthReport
+ __OBJC_METACLASS_RO_$_MobileAssetHealthReport
+ ___41+[MobileAssetHealthReport sharedInstance]_block_invoke
+ ___42-[MobileAssetHealthReport scheduleReport:]_block_invoke
+ ___44-[MobileAssetHealthReport getLastReportDate]_block_invoke
+ ___45-[MobileAssetHealthReport setLastRerpotDate:]_block_invoke
+ ___47-[MobileAssetHealthReport getSystemInformation]_block_invoke
+ ___51-[MobileAssetHealthReport initWithInterval:leeway:]_block_invoke
+ ___53+[MADAutoAssetControlManager getHealthReportForSets:]_block_invoke
+ ___54-[MADAutoAssetControlManager _getHealthReportForSets:]_block_invoke
+ ___54-[MADAutoAssetControlManager _getHealthReportForSets:]_block_invoke_2
+ ___block_descriptor_195_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8s144l8s152l8s160l8s168l8s176l8
+ __block_literal_global.1003
+ __block_literal_global.1005
+ __block_literal_global.1008
+ __block_literal_global.1012
+ __block_literal_global.1013
+ __block_literal_global.1037
+ __block_literal_global.1070
+ __block_literal_global.1072
+ __block_literal_global.1106
+ __block_literal_global.1127
+ __block_literal_global.1174
+ __block_literal_global.1201
+ __block_literal_global.1208
+ __block_literal_global.1224
+ __block_literal_global.1228
+ __block_literal_global.1233
+ __block_literal_global.1235
+ __block_literal_global.1302
+ __block_literal_global.1332
+ __block_literal_global.1366
+ __block_literal_global.1461
+ __block_literal_global.1496
+ __block_literal_global.1584
+ __block_literal_global.1589
+ __block_literal_global.1592
+ __block_literal_global.1623
+ __block_literal_global.1814
+ __block_literal_global.2043
+ __block_literal_global.2054
+ __block_literal_global.2062
+ __block_literal_global.2070
+ __block_literal_global.2078
+ __block_literal_global.2086
+ __block_literal_global.2094
+ __block_literal_global.2102
+ __block_literal_global.2110
+ __block_literal_global.2282
+ __block_literal_global.2331
+ __block_literal_global.278
+ __block_literal_global.281
+ __block_literal_global.284
+ __block_literal_global.2864
+ __block_literal_global.2882
+ __block_literal_global.3201
+ __block_literal_global.3271
+ __block_literal_global.3273
+ __block_literal_global.335
+ __block_literal_global.3413
+ __block_literal_global.3468
+ __block_literal_global.350
+ __block_literal_global.372
+ __block_literal_global.4199
+ __block_literal_global.420
+ __block_literal_global.559
+ __block_literal_global.580
+ __block_literal_global.966
+ __block_literal_global.976
+ __block_literal_global.979
+ __block_literal_global.988
+ __block_literal_global.990
+ __block_literal_global.992
+ __block_literal_global.994
+ __block_literal_global.995
+ __block_literal_global.998
+ _isCarrierReleaseType
+ _objc_msgSend$_blendCandidateSetConfigurations:blendingIntoRequiredConfigurations:blendingFromOptionalConfigurations:
+ _objc_msgSend$_collectAndSubmitReport
+ _objc_msgSend$_getHealthReportForSets:
+ _objc_msgSend$_incompleteTaskMetrics
+ _objc_msgSend$_initializePeriodicHealthReport
+ _objc_msgSend$_updateLookupResultsJustStagedAllMode:
+ _objc_msgSend$_updateLookupResultsJustStagedByGroupMode:
+ _objc_msgSend$allowsConstrainedAccess
+ _objc_msgSend$dateOfFirstRunInCurrentOS
+ _objc_msgSend$getHealthReport
+ _objc_msgSend$getHealthReportForSets:
+ _objc_msgSend$getLastReportDate
+ _objc_msgSend$getSystemInformation
+ _objc_msgSend$getTargetLookupResultsForKey:
+ _objc_msgSend$importantSetIdentifiers
+ _objc_msgSend$indexForAssetType:representedInSetConfigurations:
+ _objc_msgSend$initWithInterval:leeway:
+ _objc_msgSend$isCellular
+ _objc_msgSend$isConstrained
+ _objc_msgSend$isExpensive
+ _objc_msgSend$isMultipath
+ _objc_msgSend$newSetLookupResult:forAssetType:forSetCatalog:
+ _objc_msgSend$persistedStateDispatchQueue
+ _objc_msgSend$recordDownloadAttemptForAssetType:clientName:baseUrl:relativePath:purpose:result:analyticsFileType:isAutoDownload:isPallas:pallasAssetAudience:isUserPriority:bytesWritten:bytesTransferredEst:brainVersion:withTaskMetrics:withOptions:additionalData:
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$reportCadance
+ _objc_msgSend$reportLeeway
+ _objc_msgSend$reportQueue
+ _objc_msgSend$reportTimer
+ _objc_msgSend$scheduleReport:
+ _objc_msgSend$setLastRerpotDate:
+ _objc_msgSend$setReportTimer:
+ _objc_msgSend$setStartupTransaction:
+ _objc_msgSend$startupTransaction
+ _objc_msgSend$targetLookupResultsLoadedFromPersisted:targetLookupResultsKey:persistedEntryID:
+ _objc_msgSend$transactionMetrics
+ getSystemInformation.onceToken
+ getSystemInformation.systemInfoDict
+ sharedInstance.sharedInstanceDispatchOnce
- -[MADAnalyticsManager recordDownloadAttemptForAssetType:clientName:baseUrl:relativePath:purpose:result:analyticsFileType:isAutoDownload:isPallas:pallasAssetAudience:isUserPriority:bytesWritten:bytesTransferredEst:brainVersion:additionalData:]
- -[MADAutoAssetStager loadPersistedTargetLookupResults]
- -[MADAutoAssetStager newSetLookupResult:forSetCatalog:]
- -[MADAutoAssetStager storeSetLookupResultsToTargetLookupResults]
- -[MADAutoAssetStager targetLookupResultsLoadedFromPersisted:persistedEntryID:]
- GCC_except_table130
- GCC_except_table137
- GCC_except_table168
- GCC_except_table249
- GCC_except_table377
- GCC_except_table542
- GCC_except_table544
- GCC_except_table547
- GCC_except_table549
- GCC_except_table563
- GCC_except_table67
- GCC_except_table89
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1102
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1031
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1035
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1051
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1113
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1114
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1118
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1137
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1137.cold.1
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1147
- __27-[MABrainUpdater schedule:]_block_invoke_2.408
- __27-[MABrainUpdater schedule:]_block_invoke_3.409
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1061
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1108
- __46-[MABAACertManager issueAndCopyCertsInternal:]_block_invoke.350
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1157
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1157.cold.1
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1164
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1125
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1126
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1127
- __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.971
- __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.991
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.286
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1095
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1113
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1079
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1086
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1087
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2104
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2297
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2298
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2298.cold.1
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1064
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1065
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1066
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1100
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1101
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1101.cold.1
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1103
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1103.cold.1
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.2872
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.2873
- ___block_descriptor_187_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8s144l8s152l8s160l8s168l8
- __block_literal_global.1000
- __block_literal_global.1025
- __block_literal_global.1058
- __block_literal_global.1060
- __block_literal_global.1094
- __block_literal_global.1115
- __block_literal_global.1162
- __block_literal_global.1186
- __block_literal_global.1196
- __block_literal_global.1209
- __block_literal_global.1216
- __block_literal_global.1223
- __block_literal_global.1263
- __block_literal_global.1288
- __block_literal_global.1293
- __block_literal_global.1449
- __block_literal_global.1484
- __block_literal_global.1566
- __block_literal_global.1571
- __block_literal_global.1576
- __block_literal_global.1610
- __block_literal_global.1802
- __block_literal_global.2029
- __block_literal_global.2040
- __block_literal_global.2048
- __block_literal_global.2056
- __block_literal_global.2064
- __block_literal_global.2072
- __block_literal_global.2080
- __block_literal_global.2088
- __block_literal_global.2096
- __block_literal_global.2261
- __block_literal_global.2310
- __block_literal_global.269
- __block_literal_global.272
- __block_literal_global.275
- __block_literal_global.2843
- __block_literal_global.2861
- __block_literal_global.3180
- __block_literal_global.3250
- __block_literal_global.3252
- __block_literal_global.326
- __block_literal_global.3398
- __block_literal_global.341
- __block_literal_global.3454
- __block_literal_global.363
- __block_literal_global.411
- __block_literal_global.4185
- __block_literal_global.550
- __block_literal_global.571
- __block_literal_global.940
- __block_literal_global.954
- __block_literal_global.961
- __block_literal_global.970
- __block_literal_global.973
- __block_literal_global.977
- __block_literal_global.980
- __block_literal_global.983
- __block_literal_global.986
- __block_literal_global.989
- __block_literal_global.991
- __block_literal_global.993
- __block_literal_global.996
- _objc_msgSend$_targetNameLookupResults:
- _objc_msgSend$initWithDouble:
- _objc_msgSend$loadPersistedTargetLookupResults
- _objc_msgSend$newSetLookupResult:forSetCatalog:
- _objc_msgSend$recordDownloadAttemptForAssetType:clientName:baseUrl:relativePath:purpose:result:analyticsFileType:isAutoDownload:isPallas:pallasAssetAudience:isUserPriority:bytesWritten:bytesTransferredEst:brainVersion:additionalData:
- _objc_msgSend$storeSetLookupResultsToTargetLookupResults
- _objc_msgSend$targetLookupResultsLoadedFromPersisted:persistedEntryID:
CStrings:
+ "%@/%@.state"
+ "%@:_blendCandidateSetConfigurations"
+ "%@:_formCandidateSetLookupArray"
+ "%@:newSetLookupResult"
+ "%{public}@\n[%{public}@] {%{public}@} set-configuration (%ld of %ld) [OPTIONAL]:%{public}@"
+ "%{public}@\n[%{public}@] {%{public}@} set-configuration (%ld of %ld) [REQUIRED]:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} formed set-configurations (for determine lookups):%ld"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} ignoring empty entry | assetMetadata:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} set-configuration (%ld of %ld):%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} set-configuration already covered in REQUIRED so skipping for OPTIONAL | assetType:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} unable to load stager-set-configuration from by-asset-type dict (dropping from candidates) | assetType:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithSetConfigurations} [OPTIONAL] (from auto-control-manager provided)  | setConfiguration:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithSetConfigurations} [REQUIRED] (from auto-control-manager provided) | setConfiguration:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithSetConfigurations} nil set-configuration encountered on setConfgurations provided from auto-control-manager | setConfigurations\n:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithSetConfigurations} nil set-entry encountered on setConfiguration array | nextSetConfiguration:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithSetConfigurations} stage auto-asset (from auto-control-manager provided set-configuration) | nextSetEntry:%@ | lookupAssets(by-asset-type):%ld"
+ "%{public}@\n[AUTO-STAGER] {_updateLookupResultsJustStagedAllMode} unable to retrieve set-lookup-result | entryID:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_updateLookupResultsJustStagedByGroupMode} unable to load persisted set-lookup-result file | targetLookupResultsKey:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {loadPersistedTargetLookupResults} cache miss | lookupResultsKey:%{public}@ cachingEnabled:%@"
+ "%{public}@\n[AUTO-STAGER] {loadPersistedTargetLookupResults} multiple entries | lookupResultsKey:%{public}@"
+ "-[MADAnalyticsManager recordDownloadAttemptForAssetType:clientName:baseUrl:relativePath:purpose:result:analyticsFileType:isAutoDownload:isPallas:pallasAssetAudience:isUserPriority:bytesWritten:bytesTransferredEst:brainVersion:withTaskMetrics:withOptions:additionalData:]"
+ "2.4.1"
+ "372eb249-0e93-4789-85fb-7675dd1bfe73"
+ "?2"
+ "@\"NSObject<OS_os_transaction>\""
+ "@32@0:8d16d24"
+ "AUTO-CONTROL-MANAGER-PROVIDED-SET-CONFIGURATION"
+ "Carrier"
+ "CellularAccessRequest"
+ "CellularAccessResponse"
+ "Checked"
+ "ConstrainedNetworkAccessRequest"
+ "ConstrainedNetworkAccessResponse"
+ "DateOfFirstRunOnCurrentOS"
+ "Discovered"
+ "ExpensiveNetworkAccessRequest"
+ "ExpensiveNetworkAccessResponse"
+ "HealthReport"
+ "HealthReportIntervalSec"
+ "HealthReportLeewaySec"
+ "LastKnownBuildVersion"
+ "LastReportDate"
+ "Locked"
+ "MAHR"
+ "MAHealthReport"
+ "MobileAsset."
+ "MobileAssetHealthReport"
+ "MultipathRequest"
+ "MultipathResponse"
+ "O\x0f\x1f\b\x112Rd"
+ "SerialNumber"
+ "Starting built-in MobileAsset brain built Dec 16 2024 14:57:41"
+ "Starting downloaded MobileAsset brain (version: %@) built Dec 16 2024 14:57:41"
+ "T@\"NSCache\",&,N,V_targetLookupResults"
+ "T@\"NSDate\",&,N,V_dateOfFirstRunInCurrentOS"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_persistedStateDispatchQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_reportQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_reportTimer"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_startupTransaction"
+ "T@\"SUCorePersistedState\",&,N,V_state"
+ "Td,V_reportCadance"
+ "Td,V_reportLeeway"
+ "TimeSinceOTA"
+ "TimeoutIntervalForRequest"
+ "Vend"
+ "[%@] {%@} assetType in both REQUIRED and OPTIONAL set-configuration candidates | requiredConfiguration:%@ | optionalConfiguration:%@"
+ "[%@] {%@} unable to load optionalConfiguration | optionalIndex:%ld"
+ "[%{public}@] {ResumeJobs} ending startup transaction."
+ "[%{public}@] {_updateLookupResultsJustStagedAllMode} unable to load set-lookup-result | entryID:%{public}@"
+ "[MobileAssetHealthReport]: Collecting health report"
+ "[MobileAssetHealthReport]: Date of first run in %@ : %@"
+ "[MobileAssetHealthReport]: Failed to copy system info dict"
+ "[MobileAssetHealthReport]: Reporting interval is %lf seconds (leeway = %lf seconds)"
+ "[MobileAssetHealthReport]: Submitting health report %{public}@"
+ "[MobileAssetHealthReport]: Unable to determine currentOSVersion. Cannot determine date of first run"
+ "[MobileAssetHealthReport]: Unable to determine time interval since last update"
+ "[MobileAssetHealthReport]: Unable to determine time of last update. Assuming current time"
+ "[MobileAssetHealthReport]: failed to create persisted state directory, error: %{public}@"
+ "[MobileAssetHealthReport]: scheduleReport: Canceling previously scheduled report"
+ "[MobileAssetHealthReport]: scheduleReport: LastReportDate: [%{public}@]"
+ "[MobileAssetHealthReport]: scheduleReport: Next report delay: %lf seconds"
+ "_blendCandidateSetConfigurations:blendingIntoRequiredConfigurations:blendingFromOptionalConfigurations:"
+ "_collectAndSubmitReport"
+ "_dateOfFirstRunInCurrentOS"
+ "_getHealthReportForSets:"
+ "_incompleteTaskMetrics"
+ "_initializePeriodicHealthReport"
+ "_persistedStateDispatchQueue"
+ "_reportCadance"
+ "_reportLeeway"
+ "_reportQueue"
+ "_reportTimer"
+ "_startupTransaction"
+ "_state"
+ "_updateLookupResultsJustStagedAllMode"
+ "_updateLookupResultsJustStagedAllMode:"
+ "_updateLookupResultsJustStagedByGroupMode"
+ "_updateLookupResultsJustStagedByGroupMode:"
+ "allowsConstrained"
+ "allowsConstrainedAccess"
+ "com.apple."
+ "com.apple.MobileAsset.MobileAssetHealthReportPersistedStateQueue"
+ "com.apple.MobileAsset.MobileAssetHealthReportQueue"
+ "com.apple.MobileAsset.UAF.FM.Visual"
+ "com.apple.MobileAsset.startupTransaction"
+ "com.apple.if.planner"
+ "com.apple.if.planner.overrides"
+ "com.apple.modelcatalog"
+ "com.apple.siri.understanding"
+ "com.apple.siri.understanding.nl.overrides"
+ "dateOfFirstRunInCurrentOS"
+ "getHealthReport"
+ "getHealthReportForSets:"
+ "getLastReportDate"
+ "getSystemInformation"
+ "getTargetLookupResultsForKey:"
+ "https://gdmf-auth.apple.com/v2/assets"
+ "iOS Carrier"
+ "importantSetIdentifiers"
+ "indexForAssetType:representedInSetConfigurations:"
+ "initWithInterval:leeway:"
+ "isCellular"
+ "isConstrained"
+ "isExpensive"
+ "isMultipath"
+ "newSetLookupResult:forAssetType:forSetCatalog:"
+ "none"
+ "persistedStateDispatchQueue"
+ "recordDownloadAttemptForAssetType:clientName:baseUrl:relativePath:purpose:result:analyticsFileType:isAutoDownload:isPallas:pallasAssetAudience:isUserPriority:bytesWritten:bytesTransferredEst:brainVersion:withTaskMetrics:withOptions:additionalData:"
+ "replaceObjectAtIndex:withObject:"
+ "reportCadance"
+ "reportLeeway"
+ "reportQueue"
+ "reportTimer"
+ "scheduleReport:"
+ "setDateOfFirstRunInCurrentOS:"
+ "setLastRerpotDate:"
+ "setPersistedStateDispatchQueue:"
+ "setReportCadance:"
+ "setReportLeeway:"
+ "setReportQueue:"
+ "setReportTimer:"
+ "setStartupTransaction:"
+ "setState:"
+ "startupTransaction"
+ "targetLookupResultsLoadedFromPersisted:targetLookupResultsKey:persistedEntryID:"
+ "transactionMetrics"
+ "v140@0:8@16@24@32@40@48@56@64B72B76@80B88@92@100@108@116@124@132"
+ "yyyy-MM-dd HH:mm:ss"
+ "{%{public}@} [lookup #%ld] %{public}@"
- "\n[AUTO-STAGER] (%{public}@) | [%{public}@] [%{public}@] (target-lookup-results) targetLookupResults:%{public}@"
- "\n[AUTO-STAGER] (%{public}@) | [NO-TARGETS] [COMMON] (target-lookup-results) EMPTY targetLookupResults"
- "%{public}@\n[%{public}@] {%{public}@:_formCandidateSetLookupArray} set-configuration (%ld of %ld) [OPTIONAL]:%{public}@"
- "%{public}@\n[%{public}@] {%{public}@:_formCandidateSetLookupArray} set-configuration (%ld of %ld) [REQUIRED]:%{public}@"
- "%{public}@\n[AUTO-STAGER] {%{public}@:_formCandidateSetLookupArray} formed set-configurations (for determine lookups):%ld"
- "%{public}@\n[AUTO-STAGER] {%{public}@:_formCandidateSetLookupArray} set-configuration (%ld of %ld):%{public}@"
- "%{public}@\n[AUTO-STAGER] {%{public}@:_formCandidateSetLookupArray} unable to load stager-set-configuration from by-asset-type dict (dropping from candidates) | assetType:%{public}@"
- "%{public}@\n[AUTO-STAGER] {newSetLookupResult} ignoring empty entry | assetMetadata:%{public}@"
- "%{public}@\n[AUTO-STAGER] {updateLookupResultsJustStaged} unable to retrieve set-lookup-result | entryID:%{public}@"
- "-[MADAnalyticsManager recordDownloadAttemptForAssetType:clientName:baseUrl:relativePath:purpose:result:analyticsFileType:isAutoDownload:isPallas:pallasAssetAudience:isUserPriority:bytesWritten:bytesTransferredEst:brainVersion:additionalData:]"
- "2.2.22"
- "?1"
- "O\x0f\x1f\a\x112Rd"
- "Starting built-in MobileAsset brain built Dec  6 2024 22:00:31"
- "Starting downloaded MobileAsset brain (version: %@) built Dec  6 2024 22:00:31"
- "T@\"NSMutableDictionary\",&,N,V_targetLookupResults"
- "[%{public}@] {updateLookupResultsJustStaged} unable to load set-lookup-result | entryID:%{public}@"
- "initWithDouble:"
- "newSetLookupResult:forSetCatalog:"
- "recordDownloadAttemptForAssetType:clientName:baseUrl:relativePath:purpose:result:analyticsFileType:isAutoDownload:isPallas:pallasAssetAudience:isUserPriority:bytesWritten:bytesTransferredEst:brainVersion:additionalData:"
- "storeSetLookupResultsToTargetLookupResults"
- "targetLookupResultsLoadedFromPersisted:persistedEntryID:"
- "updateLookupResultsJustStaged"
- "v124@0:8@16@24@32@40@48@56@64B72B76@80B88@92@100@108@116"
- "{storeSetLookupResultsToTargetLookupResults} nil set-lookup-results"

```
