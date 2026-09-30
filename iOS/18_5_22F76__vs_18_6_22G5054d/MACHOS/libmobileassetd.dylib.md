## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1487.122.1.0.0
-  __TEXT.__text: 0x27a750
-  __TEXT.__auth_stubs: 0x2480
-  __TEXT.__objc_stubs: 0x228c0
-  __TEXT.__objc_methlist: 0x105ac
-  __TEXT.__const: 0x488e
-  __TEXT.__cstring: 0x37fdc
-  __TEXT.__objc_methname: 0x3de49
-  __TEXT.__objc_classname: 0xe6b
-  __TEXT.__objc_methtype: 0x3b54
-  __TEXT.__oslogstring: 0x4dae5
-  __TEXT.__gcc_except_tab: 0x3118
+1487.140.25.0.0
+  __TEXT.__text: 0x27ad90
+  __TEXT.__auth_stubs: 0x2490
+  __TEXT.__objc_stubs: 0x22a20
+  __TEXT.__objc_methlist: 0x105e4
+  __TEXT.__const: 0x479e
+  __TEXT.__cstring: 0x382fc
+  __TEXT.__objc_methname: 0x3e02b
+  __TEXT.__objc_classname: 0xe8b
+  __TEXT.__objc_methtype: 0x3b57
+  __TEXT.__oslogstring: 0x4de35
+  __TEXT.__gcc_except_tab: 0x30f8
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x1093
   __TEXT.__constg_swiftt: 0x14fc

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4870
+  __TEXT.__unwind_info: 0x4878
   __TEXT.__eh_frame: 0x3284
-  __DATA_CONST.__auth_got: 0x1250
+  __DATA_CONST.__auth_got: 0x1258
   __DATA_CONST.__got: 0x690
   __DATA_CONST.__auth_ptr: 0xa20
-  __DATA_CONST.__const: 0x6850
-  __DATA_CONST.__cfstring: 0x2bcc0
-  __DATA_CONST.__objc_classlist: 0x3f0
+  __DATA_CONST.__const: 0x6898
+  __DATA_CONST.__cfstring: 0x2bf20
+  __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9940
-  __DATA_CONST.__objc_arraydata: 0xb70
+  __DATA_CONST.__objc_selrefs: 0x9970
+  __DATA_CONST.__objc_arraydata: 0xbb8
   __DATA_CONST.__objc_arrayobj: 0x270
   __DATA_CONST.__objc_intobj: 0x570
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x15160
+  __DATA.__objc_const: 0x15280
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x808
+  __DATA.__objc_classrefs: 0x818
   __DATA.__objc_superrefs: 0x2f0
-  __DATA.__objc_ivar: 0x13f4
-  __DATA.__objc_data: 0xdb0
+  __DATA.__objc_ivar: 0x1400
+  __DATA.__objc_data: 0xe00
   __DATA.__data: 0x26c8
   __DATA.__bss: 0x51b0
   __DATA.__common: 0x90

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3C913CC7-8CF6-3BC1-AD87-23761AD814DD
-  Functions: 8370
-  Symbols:   15468
-  CStrings:  22423
+  UUID: 7C2D94FB-6799-3D73-BCDF-C54A96D0556E
+  Functions: 8376
+  Symbols:   15498
+  CStrings:  22484
 
Symbols:
+ +[DownloadManager addNWActivityToDownloadInfo:andTask:andLabel:withOptions:]
+ +[MADAutoAssetControlManager preferenceForceStartupHealthReport]
+ +[MADAutoAssetControlManager preferenceHealthReportAdditionalSetNames]
+ +[MADAutoAssetPersisted isConsideredMatchWithoutVersion:ofEntryFullEntryIDName:toSelectorPersistedEntryID:]
+ +[MAThirdPartyCompatibilityDaemon _sanitizedURLPathComponentFor:]
+ +[MAThirdPartyCompatibilityDaemon isThirdPartyAssetType:]
+ +[MAThirdPartyCompatibilityDaemon thirdPartyServerURLForAssetType:]
+ -[MADAutoAssetControlManager locatePersistedKnownDescriptorEntryIDs:forAssetType:]
+ -[MADAutoAssetControlManager preferenceForceStartupHealthReport]
+ -[MADAutoAssetControlManager preferenceHealthReportAdditionalSetNames]
+ -[MADAutoAssetControlManager setPreferenceForceStartupHealthReport:]
+ -[MADAutoAssetSetHealthReport latestInstanceFromPreSUStaging]
+ -[MADAutoAssetSetHealthReport setLatestInstanceFromPreSUStaging:]
+ GCC_except_table28
+ GCC_except_table607
+ GCC_except_table615
+ GCC_except_table631
+ GCC_except_table770
+ GCC_except_table99
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceForceStartupHealthReport
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceHealthReportAdditionalSetNames
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._latestInstanceFromPreSUStaging
+ _Constants
+ _InvShiftRows_RotWord
+ _OBJC_CLASS_$_MAThirdPartyCompatibilityDaemon
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_METACLASS_$_MAThirdPartyCompatibilityDaemon
+ _S_Box_Inverse_Zero
+ __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1209
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1632
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1639
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1640
+ __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2138
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1139
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1143
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1159
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1221
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1222
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1226
+ __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2316
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1245
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1255
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1127
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1128
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1136
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1137
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2246
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2258
+ __22-[ControlManager init]_block_invoke.1185
+ __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2297
+ __37-[DownloadManager startDownloadTimer]_block_invoke.1722
+ __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1074
+ __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1077
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1690
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1691
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1175
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1222
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2193
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2194
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1877
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1878
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1884
+ __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1838
+ __53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1463
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1271
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1278
+ __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.1922
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1233
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1234
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1235
+ __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1532
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1208
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1229
+ __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.1887
+ __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1163
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1187
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1194
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1195
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2325
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1059
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1060
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1061
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2522
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2523
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1172
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1173
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1174
+ __77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1178
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1209
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1211
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3316
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3317
+ __MAPreferencesCopyArrayOfStrings
+ __MAPreferencesCopyNSArrayOfStringsValue
+ __OBJC_$_CLASS_METHODS_MAThirdPartyCompatibilityDaemon
+ __OBJC_CLASS_RO_$_MAThirdPartyCompatibilityDaemon
+ __OBJC_METACLASS_RO_$_MAThirdPartyCompatibilityDaemon
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80r88r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8r80l8r88l8
+ __block_literal_global.1048
+ __block_literal_global.1062
+ __block_literal_global.1063
+ __block_literal_global.1075
+ __block_literal_global.1076
+ __block_literal_global.1079
+ __block_literal_global.1084
+ __block_literal_global.1094
+ __block_literal_global.1099
+ __block_literal_global.1104
+ __block_literal_global.1109
+ __block_literal_global.1126
+ __block_literal_global.1133
+ __block_literal_global.1158
+ __block_literal_global.1162
+ __block_literal_global.1172
+ __block_literal_global.1173
+ __block_literal_global.1174
+ __block_literal_global.1207
+ __block_literal_global.1221
+ __block_literal_global.1231
+ __block_literal_global.1297
+ __block_literal_global.1302
+ __block_literal_global.1304
+ __block_literal_global.1323
+ __block_literal_global.1346
+ __block_literal_global.1353
+ __block_literal_global.1361
+ __block_literal_global.1383
+ __block_literal_global.1542
+ __block_literal_global.1581
+ __block_literal_global.1620
+ __block_literal_global.1688
+ __block_literal_global.1693
+ __block_literal_global.1698
+ __block_literal_global.1732
+ __block_literal_global.1756
+ __block_literal_global.2050
+ __block_literal_global.2072
+ __block_literal_global.2244
+ __block_literal_global.2255
+ __block_literal_global.2263
+ __block_literal_global.2271
+ __block_literal_global.2277
+ __block_literal_global.2279
+ __block_literal_global.2287
+ __block_literal_global.2295
+ __block_literal_global.2303
+ __block_literal_global.2311
+ __block_literal_global.2321
+ __block_literal_global.2369
+ __block_literal_global.2371
+ __block_literal_global.2380
+ __block_literal_global.3976
+ __block_literal_global.5005
+ __handleCacheDeletePurgeCallbackForVolume_block_invoke.1090
+ __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1086
+ _downloadTypeForTaskDescriptor
+ _isDisallowedFromContentCaching
+ _kMobileAssetPreferencesAutoHealthReportSetNames
+ _kMobileAssetPreferencesAutoStartupHealthReport
+ _kMobileAssetPreferencesThirdPartyStagingBucketPathComponent
+ _kMobileAssetPreferencesThirdPartyStagingPathComponent
+ _kSecAttrAccessibleAlwaysThisDeviceOnlyPrivate
+ _nw_activity_submit_metrics
+ _objc_msgSend$_sanitizedURLPathComponentFor:
+ _objc_msgSend$addCharactersInString:
+ _objc_msgSend$addNWActivityToDownloadInfo:andTask:andLabel:withOptions:
+ _objc_msgSend$alphanumericCharacterSet
+ _objc_msgSend$compatibilityVersionStringForAssetType:
+ _objc_msgSend$isBootedOSSecureInternal
+ _objc_msgSend$isConsideredMatchWithoutVersion:ofEntryFullEntryIDName:toSelectorPersistedEntryID:
+ _objc_msgSend$latestInstanceFromPreSUStaging
+ _objc_msgSend$locatePersistedKnownDescriptorEntryIDs:forAssetType:
+ _objc_msgSend$precomposedStringWithCanonicalMapping
+ _objc_msgSend$preferenceForceStartupHealthReport
+ _objc_msgSend$preferenceHealthReportAdditionalSetNames
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$setLatestInstanceFromPreSUStaging:
+ _objc_msgSend$stringByReplacingMatchesInString:options:range:withTemplate:
+ _objc_msgSend$thirdPartyServerURLForAssetType:
+ _simplifySetIdentifier
+ ccaes_arm_encrypt_key128
+ ccaes_arm_encrypt_key192
+ ccaes_arm_encrypt_key256
- +[DownloadManager addNWActivityToDownloadInfo:andTask:andLabel:]
- +[MADAutoAssetStager controlForcePurge:]
- +[MADAutoAssetStager persistedStagedCount]
- -[MADAutoAssetControlManager newSetDescriptorLimitedToLockInformation:forSetConfiguration:]
- -[MADAutoAssetControlManager verifySetLookupResultPreferringDownloaded:]
- -[MADAutoAssetStager _setConfigurationHasEntriesWhenTargeting:]
- -[MADAutoAssetStager _targetNameLookupResults:]
- -[MADAutoAssetStager action_EliminateDoneDecideMoreCandidates:error:]
- -[MADAutoAssetStager action_ResumingNextAvailableBeginDownload:error:]
- -[MADAutoAssetStager newTargetLookupResultsForTargetTrainName:forTargetRestoreVersion:]
- GCC_except_table18
- GCC_except_table611
- GCC_except_table619
- GCC_except_table633
- GCC_except_table769
- GCC_except_table97
- _AESSubBytesWordTable
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1206
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1629
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1636
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1637
- __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2135
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1136
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1140
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1156
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1218
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1219
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1223
- __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2312
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1242
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1252
- __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1124
- __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1125
- __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1133
- __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1134
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2241
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2253
- __22-[ControlManager init]_block_invoke.1182
- __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2293
- __37-[DownloadManager startDownloadTimer]_block_invoke.1719
- __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1071
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1687
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1688
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1148
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1195
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2190
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2191
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1874
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1875
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1881
- __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1835
- __53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1460
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1244
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1251
- __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.1919
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1230
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1231
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1232
- __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1529
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1205
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1226
- __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.1884
- __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1160
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1184
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1191
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1192
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2322
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1056
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1057
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1058
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2519
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2520
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1169
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1170
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1171
- __77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1175
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1205
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1206
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3313
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3314
- ___42+[MADAutoAssetStager persistedStagedCount]_block_invoke
- __block_literal_global.1042
- __block_literal_global.1057
- __block_literal_global.1059
- __block_literal_global.1069
- __block_literal_global.1073
- __block_literal_global.1074
- __block_literal_global.1081
- __block_literal_global.1085
- __block_literal_global.1096
- __block_literal_global.1101
- __block_literal_global.1106
- __block_literal_global.1123
- __block_literal_global.1130
- __block_literal_global.1145
- __block_literal_global.1147
- __block_literal_global.1155
- __block_literal_global.1159
- __block_literal_global.1170
- __block_literal_global.1204
- __block_literal_global.1218
- __block_literal_global.1228
- __block_literal_global.1286
- __block_literal_global.1288
- __block_literal_global.1293
- __block_literal_global.1296
- __block_literal_global.1343
- __block_literal_global.1350
- __block_literal_global.1358
- __block_literal_global.1380
- __block_literal_global.1539
- __block_literal_global.1578
- __block_literal_global.1617
- __block_literal_global.1691
- __block_literal_global.1696
- __block_literal_global.1704
- __block_literal_global.1735
- __block_literal_global.1753
- __block_literal_global.1759
- __block_literal_global.2047
- __block_literal_global.2069
- __block_literal_global.2241
- __block_literal_global.2252
- __block_literal_global.2260
- __block_literal_global.2268
- __block_literal_global.2273
- __block_literal_global.2276
- __block_literal_global.2284
- __block_literal_global.2292
- __block_literal_global.2300
- __block_literal_global.2308
- __block_literal_global.2318
- __block_literal_global.2365
- __block_literal_global.2367
- __block_literal_global.2386
- __block_literal_global.3973
- __block_literal_global.4996
- __handleCacheDeletePurgeCallbackForVolume_block_invoke.1087
- __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1083
- _ccaes_arm_decrypt_key128
- _ccaes_arm_decrypt_key192
- _ccaes_arm_decrypt_key256
- _ccaes_arm_encrypt_key128
- _ccaes_arm_encrypt_key192
- _ccaes_arm_encrypt_key256
- _kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly
- _objc_msgSend$action_EliminateDoneDecideMoreCandidates:error:
- _objc_msgSend$action_ResumingNextAvailableBeginDownload:error:
- _objc_msgSend$addNWActivityToDownloadInfo:andTask:andLabel:
- _objc_msgSend$defaultThirdPartyServerURLForAssetType:
- _objc_msgSend$initWithAssetType:
- aes_dkey_expansion
- aes_key_expansion
CStrings:
+ "%@:locatePersistedKnownDescriptorEntryIDs"
+ "%@:newAtomicInstanceAndSetDescriptorFromStaged"
+ "%{public}@\n[AUTO-STAGER] {AddToStagedDecideMoreAvailable} asset-descriptor ALREADY-DOWNLOADED | self.activeJobDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {AddToStaged} [BY-GROUP-MODE] asset-descriptor ALREADY-DOWNLOADED | self.activeJobDescriptor:%{public}@"
+ "%{public}@ | MISSING asset-version | entryName:%{public}@"
+ "%{public}@ | MISSING param | entryName:%{public}@ | selectorPersistedEntryID:%{public}@"
+ "%{public}@ | corrupted current-entry-IDs | %{public}@"
+ "%{public}@ | invalid asset-selector (no asset-specifier) | assetSelector:%{public}@"
+ "%{public}@ | invalid asset-selector (no asset-type) | assetSelector:%{public}@"
+ "%{public}@ | invalid regex | regexError:%{public}@"
+ "%{public}@ | nil regex (no regexError)"
+ "%{public}@ | unable to form persisted-entry-ID | assetSelector:%{public}@"
+ "-_"
+ "2.5.1"
+ "2.6.2"
+ "AutoHealthReportSets"
+ "AutoStartupHealthReport"
+ "CrystalGSeed"
+ "MAThirdPartyCompatibility: %@ override (%@) provided, with illegal characters."
+ "MAThirdPartyCompatibilityDaemon"
+ "Metrics"
+ "PSUS"
+ "Replacing"
+ "Setting"
+ "Starting built-in MobileAsset brain built Jun  3 2025 12:01:55"
+ "Starting downloaded MobileAsset brain (version: %@) built Jun  3 2025 12:01:55"
+ "T@\"NSArray\",R,&,N,V_preferenceHealthReportAdditionalSetNames"
+ "TB,N,V_preferenceForceStartupHealthReport"
+ "TB,V_latestInstanceFromPreSUStaging"
+ "ThirdPartyStagingBucketPathComponent"
+ "ThirdPartyStagingPathComponent"
+ "[%{public}@] {%{public}@} responding to client with error | responseMessage:%{public}@, responseError:%{public}@"
+ "[AUTO-SHORT-TERM][LATEST]{trackShortTermLockedSetDescriptor} %{public}@ latest supporting SHORT-TERM locking | atomicInstance:%{public}@ | setDescriptor:%{public}@"
+ "[MA_PREFS] {_MAPreferencesCopyArrayOfStrings} invalid entry for key:%{public}@ | value:%{public}@ | index:%d | not a string"
+ "[MA_PREFS] {_MAPreferencesCopyNSArrayOfStringsValue} invalid type for key:%{public}@ | expecting array of strings"
+ "_[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+_[0-9]+$"
+ "_latestInstanceFromPreSUStaging"
+ "_preferenceForceStartupHealthReport"
+ "_preferenceHealthReportAdditionalSetNames"
+ "_sanitizedURLPathComponentFor:"
+ "addCharactersInString:"
+ "addNWActivityToDownloadInfo:andTask:andLabel:withOptions:"
+ "alphanumericCharacterSet"
+ "com.apple.MobileAsset.UAF.FM.CodeLM"
+ "com.apple.MobileAsset.UAF.FM.GenerativeModels"
+ "com.apple.MobileAsset.UAF.Handwriting.Synthesis"
+ "com.apple.MobileAsset.UAF.IF.Planner"
+ "com.apple.MobileAsset.UAF.Search.ODLA"
+ "com.apple.MobileAsset.UAF.Speech.AutomaticSpeechRecognition"
+ "com.apple.MobileAsset.UAF.VoiceAssistant"
+ "compatibilityVersionStringForAssetType:"
+ "https://mesu.apple.com/3p/%@/%@/assets/%@/%@/"
+ "https://mesu.apple.com/3p/%@/assets/%@/%@/"
+ "https://mesu.apple.com/3p/assets/%@/%@/"
+ "https://mesu.apple.com/3p/staging/assets/%@/%@/"
+ "ios"
+ "isBootedOSSecureInternal"
+ "isConsideredMatchWithoutVersion:ofEntryFullEntryIDName:toSelectorPersistedEntryID:"
+ "latestInstanceFromPreSUStaging"
+ "locatePersistedKnownDescriptorEntryIDs:forAssetType:"
+ "precomposedStringWithCanonicalMapping"
+ "preferenceForceStartupHealthReport"
+ "preferenceHealthReportAdditionalSetNames"
+ "rampForeground:%@, discretionary:%@, timeout:%@, allowSame:%@, allowContentCaching:%@ | [installed] build:%@, version:%@ | analyticsData:%@"
+ "regularExpressionWithPattern:options:error:"
+ "set-identifier (for given client-domain-name) is not currently defined | clientDomainName:%@ | assetSetIdentifier:%@"
+ "setLatestInstanceFromPreSUStaging:"
+ "setPreferenceForceStartupHealthReport:"
+ "stringByReplacingMatchesInString:options:range:withTemplate:"
+ "thirdPartyServerURLForAssetType:"
+ "v44@0:8@16@24I32@36"
+ "{%@:newAtomicInstanceAndSetDescriptorFromStaged} unable to allocate already-downloaded-atomic-entry | alreadyDownloadedDescriptor:%@"
+ "{%@} unable to determine localContentURL of already-downloaded-descriptor | alreadyDownloadedDescriptor:%@"
+ "{%{public}@} [%{public}@] | fromLookupResultSetDescriptor:%{public}@ | reportedDiscoveredEntries:\n%{public}@"
+ "{%{public}@} [DROP-SET-DESCRIPTOR] set-descriptor with downloaded entry missing from filesystem | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@ | localContentURL:%{public}@ | setDescriptor:%{public}@"
+ "{%{public}@} [DROP-SET-DESCRIPTOR] set-descriptor with downloaded entry missing localContentURL | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@ | setDescriptor:%{public}@"
+ "{%{public}@} [DROP-SET-DESCRIPTOR] set-descriptor with downloaded entry that is not a directory | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@ | localContentURL:%{public}@ | setDescriptor:%{public}@"
+ "{%{public}@} [KEEP-SET-DESCRIPTOR] set-descriptor with downloaded entry on filesystem | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@ | localContentURL:%{public}@ | setDescriptor:%{public}@"
+ "{%{public}@} no auto-asset-descriptor entry found | entry:%{public}@"
+ "{%{public}@} no persisted-entry found | assetSelector:%{public}@"
+ "{%{public}@} no persisted-entry found | entry:%{public}@"
+ "{%{public}@} unable to load known descriptor | entry:%{public}@"
+ "{%{public}@} unable to load persisted-state entry | entry:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | by-set-configuration lookup-cache disabled | set-configuration:%{public}@ | assetAudience:%{public}@ | setAssetType:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | cached entry config mismatch | removed entry | set-configuration:%{public}@ | assetAudience:%{public}@ | setAssetType:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | cached secs(%ld) <= max-valid secs(%ld) | using entry | set-configuration:%{public}@ | assetAudience:%{public}@ | setAssetType:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | cached secs(%ld) > max-valid secs(%ld) | removed entry | set-configuration:%{public}@ | assetAudience:%{public}@ | setAssetType:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | current time before cached entry time - removed future entry | set-configuration:%{public}@ | assetAudience:%{public}@ | setAssetType:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | no cached entry | set-configuration:%{public}@ | assetAudience:%{public}@ | setAssetType:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | unable to determine by-set-configuration lookup-cache key (no asset-type from set-configuration) | setConfiguration:%{public}@ | setAssetType:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | unable to determine by-set-configuration lookup-cache key | setConfiguration:%{public}@ | setAssetType:%{public}@ | assetAudience:%{public}@ | setAssetType:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | unable to determine timestamp(s) | removed entry | set-configuration:%{public}@ | assetAudience:%{public}@ | setAssetType:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | unable to locate auto-asset-lookup-cache | set-configuration:%{public}@ | setAssetType:%{public}@"
- "%{public}@\n[AUTO-STAGER] {newTargetLookupResultsForTargetTrainName} unable to retrieve target-lookup-results | entryID:%{public}@"
- "2.5.0"
- "2.6.1"
- "CrystalF"
- "EliminateDoneDecideMoreCandidates"
- "LOOKUP_RESULTS"
- "ResumingNextAvailableBeginDownload"
- "Starting built-in MobileAsset brain built Apr 20 2025 21:21:32"
- "Starting downloaded MobileAsset brain (version: %@) built Apr 20 2025 21:21:32"
- "[%{public}@]\n{verifySetLookupResultPreferringDownloaded} replaced stager set-lookup-result | staged-assetID:%{public}@ | downloaded-assetID:%{public}@"
- "[%{public}@]\n{verifySetLookupResultPreferringDownloaded} stager set-lookup-result with no downloaded descriptor (dropped) | nextDiscoveredEntry:%{public}@"
- "[%{public}@]\n{verifySetLookupResultPreferringDownloaded} unable to allocate replacement entry | staged-assetID:%{public}@ | downloaded-assetID:%{public}@"
- "[%{public}@] {newTargetLookupResultsForTargetTrainName} unable to load target-lookup-results | entryID:%{public}@"
- "[AUTO-ASSET] [LOCAL-CONTENT-URL] {verifySetLookupResultPreferringDownloaded} not adopting set-lookup-result - %{public}@"
- "[AUTO-SHORT-TERM][LATEST]{trackShortTermLockedSetDescriptor} latest supporting SHORT-TERM locking | atomicInstance:%{public}@ | setDescriptor:%{public}@"
- "_setConfigurationHasEntriesWhenTargeting:"
- "_targetNameLookupResults:"
- "action_EliminateDoneDecideMoreCandidates:error:"
- "action_ResumingNextAvailableBeginDownload:error:"
- "addNWActivityToDownloadInfo:andTask:andLabel:"
- "controlForcePurge:"
- "defaultThirdPartyServerURLForAssetType:"
- "newSetDescriptorLimitedToLockInformation:forSetConfiguration:"
- "newTargetLookupResultsForTargetTrainName"
- "newTargetLookupResultsForTargetTrainName:forTargetRestoreVersion:"
- "persistedStagedCount"
- "rampForeground:%@, discretionary:%@, timeout:%@, allowSame:%@ | [installed] build:%@, version:%@ | analyticsData:%@"
- "set-identifier (for given client-domain-name) is not currently defined"
- "unable to get local content URL | downloadedDescriptor:%@"
- "v36@0:8@16@24I32"
- "verifySetLookupResultPreferringDownloaded"
- "verifySetLookupResultPreferringDownloaded:"
- "{%@} no auto-asset-descriptor entry found | entry:%{public}@"
- "{%@} no persisted-entry found | assetSelector:%{public}@"
- "{%@} no persisted-entry found | entry:%{public}@"
- "{%{public}@} [DROP-SET-DESCRIPTOR] set-descriptor with downloaded entry missing from filesystem | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@ | localContentURL:%{public}@"
- "{%{public}@} [DROP-SET-DESCRIPTOR] set-descriptor with downloaded entry missing localContentURL | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@"
- "{%{public}@} [DROP-SET-DESCRIPTOR] set-descriptor with downloaded entry that is not a directory | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@ | localContentURL:%{public}@"
- "{%{public}@} [KEEP-SET-DESCRIPTOR] set-descriptor with downloaded entry on filesystem | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@ | localContentURL:%{public}@"
- "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | by-set-configuration lookup-cache disabled | set-configuration:%{public}@ | assetAudience:%{public}@"
- "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | cached entry config mismatch | removed entry | set-configuration:%{public}@ | assetAudience:%{public}@"
- "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | cached secs(%ld) <= max-valid secs(%ld) | using entry | set-configuration:%{public}@ | assetAudience:%{public}@"
- "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | cached secs(%ld) > max-valid secs(%ld) | removed entry | set-configuration:%{public}@ | assetAudience:%{public}@"
- "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | current time before cached entry time - removed future entry | set-configuration:%{public}@ | assetAudience:%{public}@"
- "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | no cached entry | set-configuration:%{public}@ | assetAudience:%{public}@"
- "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | unable to determine by-set-configuration lookup-cache key (no asset-type from set-configuration) | setConfiguration:%{public}@"
- "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | unable to determine by-set-configuration lookup-cache key | setConfiguration:%{public}@ | setAssetType:%{public}@ | assetAudience:%{public}@"
- "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | unable to determine timestamp(s) | removed entry | set-configuration:%{public}@ | assetAudience:%{public}@"
- "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | unable to locate auto-asset-lookup-cache | set-configuration:%{public}@"
- "{AUTO-STAGER:persistedStagedCount} | unable to determine previous staging information from persisted-state (no auto-asset-stager)"
- "{_setConfigurationHasEntriesWhenTargeting} no auto-asset-entries for set-configuration:%@"
- "{controlForcePurge} failed to locate shared AutoAssetStager"

```
