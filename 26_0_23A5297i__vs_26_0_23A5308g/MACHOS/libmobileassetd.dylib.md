## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1837.0.31.0.1
-  __TEXT.__text: 0x2e69ac
+1837.0.53.0.0
+  __TEXT.__text: 0x2eafc0
   __TEXT.__auth_stubs: 0x2be0
-  __TEXT.__objc_stubs: 0x22cc0
-  __TEXT.__objc_methlist: 0x10654
-  __TEXT.__const: 0x7ba08
-  __TEXT.__cstring: 0x3a10b
-  __TEXT.__objc_methname: 0x3e881
+  __TEXT.__objc_stubs: 0x22e60
+  __TEXT.__objc_methlist: 0x106ec
+  __TEXT.__const: 0x7ba88
+  __TEXT.__cstring: 0x3abdb
+  __TEXT.__objc_methname: 0x3eac8
   __TEXT.__objc_classname: 0xe66
-  __TEXT.__objc_methtype: 0x3f68
-  __TEXT.__oslogstring: 0x53dc7
-  __TEXT.__gcc_except_tab: 0xd21c
+  __TEXT.__objc_methtype: 0x403e
+  __TEXT.__oslogstring: 0x54347
+  __TEXT.__gcc_except_tab: 0xd23c
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__swift5_typeref: 0x1332
-  __TEXT.__constg_swiftt: 0x1788
-  __TEXT.__swift5_reflstr: 0x8c1
-  __TEXT.__swift5_fieldmd: 0x120c
-  __TEXT.__swift5_types: 0x1cc
-  __TEXT.__swift5_builtin: 0xf0
+  __TEXT.__swift5_typeref: 0x14cc
+  __TEXT.__constg_swiftt: 0x18a8
+  __TEXT.__swift5_reflstr: 0x951
+  __TEXT.__swift5_fieldmd: 0x13f8
+  __TEXT.__swift5_types: 0x1f0
+  __TEXT.__swift5_builtin: 0x1a4
   __TEXT.__swift5_assocty: 0x6a0
   __TEXT.__swift5_proto: 0x3cc
   __TEXT.__swift5_protos: 0x6c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x5e88
-  __TEXT.__eh_frame: 0x3464
+  __TEXT.__unwind_info: 0x5ee8
+  __TEXT.__eh_frame: 0x346c
   __DATA_CONST.__auth_got: 0x1600
-  __DATA_CONST.__got: 0x740
-  __DATA_CONST.__auth_ptr: 0xac0
-  __DATA_CONST.__const: 0x8580
-  __DATA_CONST.__cfstring: 0x2c940
+  __DATA_CONST.__got: 0x748
+  __DATA_CONST.__auth_ptr: 0xac8
+  __DATA_CONST.__const: 0x99a8
+  __DATA_CONST.__cfstring: 0x2d6e0
   __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a88
-  __DATA_CONST.__objc_arraydata: 0xbe8
+  __DATA_CONST.__objc_selrefs: 0x9af0
+  __DATA_CONST.__objc_arraydata: 0xbf0
   __DATA_CONST.__objc_arrayobj: 0x2d0
-  __DATA_CONST.__objc_intobj: 0x4b0
+  __DATA_CONST.__objc_intobj: 0x1020
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x154d8
+  __DATA.__objc_const: 0x154f8
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x850
+  __DATA.__objc_classrefs: 0x858
   __DATA.__objc_superrefs: 0x2f0
-  __DATA.__objc_ivar: 0x13f8
+  __DATA.__objc_ivar: 0x13fc
   __DATA.__objc_data: 0x2b88
-  __DATA.__data: 0x2ca8
+  __DATA.__data: 0x2cf0
   __DATA.__bss: 0x6668
   __DATA.__common: 0x98
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 81A06B36-B25B-398E-941E-564DA44F8972
-  Functions: 9079
-  Symbols:   16627
-  CStrings:  23430
+  UUID: 45092919-4604-393B-B322-764BFAFA0500
+  Functions: 9155
+  Symbols:   16697
+  CStrings:  23680
 
Symbols:
+ +[MADAutoAssetControlManager considerPerfomingCrosscheckTrim]
+ +[MADCacheDeleteManagerError mapCacheDeleteManagerErrorIndications]
+ +[MADCacheDeleteManagerError mapCacheDeleteManagerErrorIndications].cold.1
+ -[DownloadManager isValidUUID:]
+ -[DownloadManager pallasRequestedAssetSetID:]
+ -[MABAACertManager dealloc]
+ -[MADAnalyticsManager recordMobileAssetPurgeAttempt:withUrgency:withBytesPurged:withResult:withDir:withRetentionPolicy:withReason:]
+ -[MADAutoAssetControlManager _removeNextDownloadedDescriptorIfNewerDownloaded:]
+ -[MADAutoAssetControlManager initialHealthReportPerformedCrosscheck]
+ -[MADAutoAssetControlManager setInitialHealthReportPerformedCrosscheck:]
+ -[MADAutoAssetControlManager validateShortTermLockURL:normalizedClientDomainNameURL:normalizedAssetSetIdentifierURL:fileManager:isLatestLocker:isSpecificLocker:]
+ -[MADAutoAssetControlManager verifyLockerLatestSymlink]
+ -[MADAutoAssetJob setDescriptorDiscardRamped]
+ -[MADAutoAssetJob setSetDescriptorDiscardRamped:]
+ -[MADAutoAssetPersisted persistedEntryIDs:assetType:]
+ -[MADAutoAssetStager action_RemoveAllReplyCanceled:error:]
+ -[MAKeyManagerDownloadSessionDelegate dealloc]
+ -[SecureMobileAssetBundle initWithPath:].cold.1
+ -[SoftwareUpdateSSO _completionDeadline]
+ -[SoftwareUpdateSSO invalidate]
+ GCC_except_table152
+ GCC_except_table153
+ GCC_except_table173
+ GCC_except_table191
+ GCC_except_table196
+ GCC_except_table202
+ GCC_except_table256
+ GCC_except_table315
+ GCC_except_table328
+ GCC_except_table340
+ GCC_except_table346
+ GCC_except_table347
+ GCC_except_table351
+ GCC_except_table357
+ GCC_except_table358
+ GCC_except_table363
+ GCC_except_table364
+ GCC_except_table368
+ GCC_except_table376
+ GCC_except_table377
+ GCC_except_table423
+ GCC_except_table435
+ GCC_except_table436
+ GCC_except_table520
+ GCC_except_table580
+ GCC_except_table615
+ GCC_except_table623
+ GCC_except_table625
+ GCC_except_table639
+ GCC_except_table668
+ GCC_except_table774
+ GCC_except_table775
+ GCC_except_table776
+ GCC_except_table777
+ GCC_except_table780
+ OBJC_IVAR_$_MADAutoAssetControlManager._initialHealthReportPerformedCrosscheck
+ OBJC_IVAR_$_MADAutoAssetJob._setDescriptorDiscardRamped
+ OBJC_IVAR_$_SoftwareUpdateSSO.ssoControllerQueue
+ _NSURLIsSymbolicLinkKey
+ _OBJC_CLASS_$_SUCoreErrorInformation
+ __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1266
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1767
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1774
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1775
+ __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2203
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1191
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1195
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1211
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1273
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1274
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1278
+ __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2377
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1297
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1307
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1182
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1183
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1191
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1192
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2310
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2322
+ __22-[ControlManager init]_block_invoke.1236
+ __24-[MABrainUpdater start:]_block_invoke.1112
+ __24-[MABrainUpdater start:]_block_invoke.1117
+ __24-[MABrainUpdater start:]_block_invoke.1121
+ __27-[MABrainUpdater schedule:]_block_invoke.1128
+ __27-[MABrainUpdater schedule:]_block_invoke.1170
+ __27-[MABrainUpdater schedule:]_block_invoke.1175
+ __27-[MABrainUpdater schedule:]_block_invoke_2.1171
+ __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2358
+ __36-[MABrainUpdater update:completion:]_block_invoke.1239
+ __36-[MABrainUpdater update:completion:]_block_invoke.1240
+ __36-[MABrainUpdater update:completion:]_block_invoke.1247
+ __37-[DownloadManager startDownloadTimer]_block_invoke.1780
+ __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1119
+ __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1122
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1824
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1825
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1222
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1269
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2257
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2258
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1929
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1930
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1936
+ __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1223
+ __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1224
+ __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1890
+ __53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1514
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1321
+ __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2057
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1285
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1286
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1287
+ __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1585
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.379
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.397
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke_2.403
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1248
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1270
+ __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.2022
+ __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1214
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1239
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1246
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1247
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2371
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1104
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1105
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1106
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2570
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2571
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1224
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1225
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1226
+ __77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1229
+ __79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1190
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1260
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1261
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1263
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3438
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3439
+ __MABrainUtilityScheduleDeviceUnlockAction_block_invoke.404
+ ___40-[SecureMobileAssetBundle initWithPath:]_block_invoke
+ ___58-[MADAutoAssetControlManager firstSchedulerCrosscheckTrim]_block_invoke
+ ___58-[MADAutoAssetControlManager firstSchedulerCrosscheckTrim]_block_invoke_2
+ ___58-[MADAutoAssetControlManager firstSchedulerCrosscheckTrim]_block_invoke_3
+ ___61+[MADAutoAssetControlManager considerPerfomingCrosscheckTrim]_block_invoke
+ ___67+[MADCacheDeleteManagerError mapCacheDeleteManagerErrorIndications]_block_invoke
+ ___79-[MADAutoAssetControlManager _removeNextDownloadedDescriptorIfNewerDownloaded:]_block_invoke
+ ___block_descriptor_105_e8_32s40s48s56s64bs72r80r88r96r_e11_v16?0B8B12ls32l8r72l8s40l8s48l8r80l8r88l8r96l8s64l8s56l8
+ ___swift_assignWithCopy_strong
+ ___swift_assignWithTake_strong
+ ___swift_destroy_strong
+ ___swift_initWithCopy_strong
+ ___swift_memcpy0_1
+ ___swift_memcpy56_8
+ __block_literal_global.1093
+ __block_literal_global.1101
+ __block_literal_global.1107
+ __block_literal_global.1115
+ __block_literal_global.1123
+ __block_literal_global.1126
+ __block_literal_global.1135
+ __block_literal_global.1136
+ __block_literal_global.1142
+ __block_literal_global.1145
+ __block_literal_global.1147
+ __block_literal_global.1152
+ __block_literal_global.1157
+ __block_literal_global.1171
+ __block_literal_global.1173
+ __block_literal_global.1181
+ __block_literal_global.1201
+ __block_literal_global.1209
+ __block_literal_global.1219
+ __block_literal_global.1221
+ __block_literal_global.1224
+ __block_literal_global.1247
+ __block_literal_global.1249
+ __block_literal_global.1252
+ __block_literal_global.1272
+ __block_literal_global.1274
+ __block_literal_global.1358
+ __block_literal_global.1360
+ __block_literal_global.1365
+ __block_literal_global.1367
+ __block_literal_global.1371
+ __block_literal_global.1399
+ __block_literal_global.1405
+ __block_literal_global.1410
+ __block_literal_global.1415
+ __block_literal_global.1420
+ __block_literal_global.1442
+ __block_literal_global.1605
+ __block_literal_global.1632
+ __block_literal_global.1677
+ __block_literal_global.1729
+ __block_literal_global.1734
+ __block_literal_global.1739
+ __block_literal_global.1742
+ __block_literal_global.1773
+ __block_literal_global.1797
+ __block_literal_global.2065
+ __block_literal_global.2110
+ __block_literal_global.2132
+ __block_literal_global.2290
+ __block_literal_global.2301
+ __block_literal_global.2309
+ __block_literal_global.2317
+ __block_literal_global.2325
+ __block_literal_global.2333
+ __block_literal_global.2341
+ __block_literal_global.2349
+ __block_literal_global.2357
+ __block_literal_global.2422
+ __block_literal_global.2424
+ __block_literal_global.2427
+ __block_literal_global.2434
+ __block_literal_global.2830
+ __block_literal_global.2833
+ __block_literal_global.4068
+ __block_literal_global.414
+ __block_literal_global.5111
+ __handleCacheDeletePurgeCallbackForVolume_block_invoke.1138
+ __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1134
+ _assetPathDirectory
+ _isValidSymlink
+ _mapMABrainErrorIndications
+ _mapV2ErrorIndications
+ _objc_msgSend$_completionDeadline
+ _objc_msgSend$_removeNextDownloadedDescriptorIfNewerDownloaded:
+ _objc_msgSend$action_RemoveAllReplyCanceled:error:
+ _objc_msgSend$attributesOfErrorForDomain:withCode:codeName:
+ _objc_msgSend$considerPerfomingCrosscheckTrim
+ _objc_msgSend$initialHealthReportPerformedCrosscheck
+ _objc_msgSend$isValidUUID:
+ _objc_msgSend$mapAutoAssetErrorIndications
+ _objc_msgSend$mapCacheDeleteManagerErrorIndications
+ _objc_msgSend$pallasRequestedAssetSetID:
+ _objc_msgSend$pathWithComponents:
+ _objc_msgSend$persistedEntryIDs:assetType:
+ _objc_msgSend$recordMobileAssetPurgeAttempt:withUrgency:withBytesPurged:withResult:withDir:withRetentionPolicy:withReason:
+ _objc_msgSend$setDescriptorDiscardRamped
+ _objc_msgSend$setInitialHealthReportPerformedCrosscheck:
+ _objc_msgSend$setRefKey:
+ _objc_msgSend$setSetDescriptorDiscardRamped:
+ _objc_msgSend$validateShortTermLockURL:normalizedClientDomainNameURL:normalizedAssetSetIdentifierURL:fileManager:isLatestLocker:isSpecificLocker:
+ _objc_msgSend$verifyLockerLatestSymlink
+ _symbolic SPy_____GSg So10ccmode_ctrV
+ _symbolic SPy_____GSg So11ccdrbg_infoV
+ _symbolic SPy_____GSg So13ccdrbg_df_ctxV
+ _symbolic Sb_____SgXCSg s13OpaquePointerV
+ _symbolic _____ So10ccmode_ctrV
+ _symbolic _____ So11ccdrbg_infoV
+ _symbolic _____ So11ccrng_stateV
+ _symbolic _____ So13ccdrbg_df_ctxV
+ _symbolic _____ So16ccrng_drbg_stateV
+ _symbolic _____ So20ccrng_sequence_stateV
+ _symbolic _____ So21ccdrbg_nistctr_customV
+ _symbolic _____ So8cc_iovecV
+ _symbolic _____ So9ccctr_ctxa
+ _symbolic _____SPy_____GSg_SiSPy_____GSgSiSvSgtXCSg s5Int32V So13ccdrbg_df_ctxV So8cc_iovecV
+ _symbolic _____SPy_____GSg_Spy_____GSgSVSgtXCSg s5Int32V So10ccmode_ctrV So9ccctr_ctxa
+ _symbolic _____SPy_____GSg_Spy_____GSgSiSVSgAHtXCSg s5Int32V So10ccmode_ctrV So9ccctr_ctxa
+ _symbolic _____SPy_____GSg______SgSiSVSgSiAGSiAGtXCSg s5Int32V So11ccdrbg_infoV s13OpaquePointerV
+ _symbolic _____Spy_____GSg_SiSVSgSvSgtXCSg s5Int32V So9ccctr_ctxa
+ _symbolic _____Spy_____GSg_SiSvSgtXCSg s5Int32V So11ccrng_stateV
+ _symbolic __________Sg_SiSVSgSiADtXCSg s5Int32V s13OpaquePointerV
+ _symbolic __________Sg_SiSvSgSiSVSgtXCSg s5Int32V s13OpaquePointerV
+ _symbolic y_____SgXCSg s13OpaquePointerV
+ initWithPath:.secureAssetErrorInfoOnce
+ mapCacheDeleteManagerErrorIndications.errorInfoOnce
- -[MADAutoAssetControlManager schedulerTickPerformedCrossCheck]
- -[MADAutoAssetControlManager setSchedulerTickPerformedCrossCheck:]
- -[MADAutoAssetControlManager validateShortTermLockURL:normalizedClientDomainNameURL:normalizedAssetSetIdentifierURL:fileManager:]
- -[SoftwareUpdateExtensibleSSOAuthenticator authenticationController]
- -[SoftwareUpdateExtensibleSSOAuthenticator setAuthenticationController:]
- -[SoftwareUpdateSSO initWithOptions:].cold.1
- GCC_except_table155
- GCC_except_table175
- GCC_except_table200
- GCC_except_table254
- GCC_except_table313
- GCC_except_table322
- GCC_except_table329
- GCC_except_table330
- GCC_except_table342
- GCC_except_table349
- GCC_except_table353
- GCC_except_table354
- GCC_except_table361
- GCC_except_table362
- GCC_except_table365
- GCC_except_table366
- GCC_except_table370
- GCC_except_table421
- GCC_except_table427
- GCC_except_table428
- GCC_except_table516
- GCC_except_table574
- GCC_except_table609
- GCC_except_table611
- GCC_except_table619
- GCC_except_table633
- GCC_except_table660
- GCC_except_table766
- GCC_except_table767
- GCC_except_table768
- GCC_except_table769
- GCC_except_table772
- OBJC_IVAR_$_MADAutoAssetControlManager._schedulerTickPerformedCrossCheck
- OBJC_IVAR_$_SoftwareUpdateExtensibleSSOAuthenticator._authenticationController
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1248
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1745
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1752
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1753
- __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2182
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1169
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1173
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1189
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1251
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1252
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1256
- __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2356
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1275
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1285
- __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1164
- __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1165
- __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1173
- __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1174
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2289
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2301
- __22-[ControlManager init]_block_invoke.1218
- __24-[MABrainUpdater start:]_block_invoke.1094
- __24-[MABrainUpdater start:]_block_invoke.1099
- __24-[MABrainUpdater start:]_block_invoke.1103
- __27-[MABrainUpdater schedule:]_block_invoke.1110
- __27-[MABrainUpdater schedule:]_block_invoke.1152
- __27-[MABrainUpdater schedule:]_block_invoke.1157
- __27-[MABrainUpdater schedule:]_block_invoke_2.1153
- __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2337
- __36-[MABrainUpdater update:completion:]_block_invoke.1221
- __36-[MABrainUpdater update:completion:]_block_invoke.1222
- __36-[MABrainUpdater update:completion:]_block_invoke.1229
- __37-[DownloadManager startDownloadTimer]_block_invoke.1762
- __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1101
- __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1104
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1802
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1803
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1201
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1248
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2236
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2237
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1911
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1912
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1918
- __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1205
- __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1206
- __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1872
- __53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1496
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1300
- __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2035
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1263
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1264
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1265
- __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1567
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.376
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.394
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke_2.400
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1230
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1252
- __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.2000
- __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1190
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1217
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1224
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1225
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2350
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1086
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1087
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1088
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2550
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2551
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1202
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1203
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1204
- __77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1211
- __79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1172
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1238
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1239
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1241
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3346
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3347
- __MABrainUtilityScheduleDeviceUnlockAction_block_invoke.401
- ___37-[SoftwareUpdateSSO initWithOptions:]_block_invoke
- ___block_descriptor_104_e8_32s40s48s56s64bs72r80r88r96r_e11_v16?0B8B12ls32l8r72l8s40l8s48l8r80l8r88l8r96l8s64l8s56l8
- __block_literal_global.1072
- __block_literal_global.1075
- __block_literal_global.1083
- __block_literal_global.1085
- __block_literal_global.1097
- __block_literal_global.1105
- __block_literal_global.1106
- __block_literal_global.1117
- __block_literal_global.1118
- __block_literal_global.1121
- __block_literal_global.1127
- __block_literal_global.1129
- __block_literal_global.1134
- __block_literal_global.1153
- __block_literal_global.1155
- __block_literal_global.1163
- __block_literal_global.1185
- __block_literal_global.1198
- __block_literal_global.1200
- __block_literal_global.1206
- __block_literal_global.1229
- __block_literal_global.1231
- __block_literal_global.1234
- __block_literal_global.1254
- __block_literal_global.1256
- __block_literal_global.1340
- __block_literal_global.1342
- __block_literal_global.1347
- __block_literal_global.1349
- __block_literal_global.1350
- __block_literal_global.1381
- __block_literal_global.1387
- __block_literal_global.1392
- __block_literal_global.1397
- __block_literal_global.1402
- __block_literal_global.1424
- __block_literal_global.1584
- __block_literal_global.1614
- __block_literal_global.1659
- __block_literal_global.1708
- __block_literal_global.1713
- __block_literal_global.1718
- __block_literal_global.1721
- __block_literal_global.1752
- __block_literal_global.1776
- __block_literal_global.1798
- __block_literal_global.2092
- __block_literal_global.2114
- __block_literal_global.2269
- __block_literal_global.2280
- __block_literal_global.2288
- __block_literal_global.2296
- __block_literal_global.2304
- __block_literal_global.2312
- __block_literal_global.2320
- __block_literal_global.2328
- __block_literal_global.2336
- __block_literal_global.2401
- __block_literal_global.2403
- __block_literal_global.2406
- __block_literal_global.2413
- __block_literal_global.2805
- __block_literal_global.2808
- __block_literal_global.3976
- __block_literal_global.411
- __block_literal_global.5013
- __handleCacheDeletePurgeCallbackForVolume_block_invoke.1120
- __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1116
- _objc_msgSend$authenticationController
- _objc_msgSend$osTransactionNamePreviouslyInFlightJob:
- _objc_msgSend$schedulerTickPerformedCrossCheck
- _objc_msgSend$setAuthenticationController:
- _objc_msgSend$setSchedulerTickPerformedCrossCheck:
- _objc_msgSend$validateShortTermLockURL:normalizedClientDomainNameURL:normalizedAssetSetIdentifierURL:fileManager:
- _ssoControllerQueue
- _ssoControllerQueueOnce
CStrings:
+ "%@_%@.%@"
+ "%{public}@ | invalid asset-selector (no asset-type) | assetType:%{public}@"
+ "%{public}@ | {%{public}@} newer version found that is ramped (and have older atomic-instance) - discrarding newer set-descriptor | autoAssetSetDescriptor:%{public}@"
+ "1\""
+ "@68@0:8@16i24q28q36@44q52@60"
+ "Alloc"
+ "AppleConnect"
+ "AssetNotInstalled"
+ "AuthInstall"
+ "Canceled"
+ "ClientCommunication"
+ "CommitManifests"
+ "Depersonalize"
+ "DictionaryEnumerationFailure"
+ "Directory"
+ "DiskImageAttach"
+ "DiskImageEject"
+ "DownloadAssetFailed"
+ "ExclavesUnsupported"
+ "ExtensibleSSOAuthenticator: Authentication completed successfully\n"
+ "GetBrainInfo"
+ "Graft"
+ "GraftCommittedTicketDataNil"
+ "GraftInfo"
+ "GraftNotPersonalizedForExclaves"
+ "GraftPath"
+ "GraftPersonalizedBundleTicketDataNil"
+ "GraftTicketMismatch"
+ "InstallCreateBrainDirFailed"
+ "InstallFailed"
+ "InstallWriteBrainPlistFailed"
+ "InstallWriteStageFileFailed"
+ "Invalid RequestedAssetSetID for key: %{public}@"
+ "InvalidArgument"
+ "InvalidCommand"
+ "InvalidDictionaryType"
+ "MABAACertManager not supported with hactivation"
+ "MADStager:RemoveAllReplyCanceled"
+ "MapToExclaves"
+ "MapToExclavesActivateManifestFailed"
+ "MapToExclavesCommittedTicketDataNil"
+ "MapToExclavesDetermineState"
+ "MapToExclavesInfoPlistDataNil"
+ "MapToExclavesInfoPlistPathNil"
+ "MapToExclavesIntegrityCatalogDataNil"
+ "MapToExclavesIntegrityCatalogPathNil"
+ "MapToExclavesNotPersonalizedForExclaves"
+ "MapToExclavesPersonalizedBundleTicketDataNil"
+ "MapToExclavesStoreManifestFailed"
+ "MapToExclavesTicketDataNil"
+ "MapToExclavesTicketMismatch"
+ "MapToExclavesTicketPathNil"
+ "MapToExclavesUnregisterExisting"
+ "Mount"
+ "MountAttachDiskImage"
+ "MountCommittedTicketDataNil"
+ "MountFindAPFSVolume"
+ "MountFindDevNodes"
+ "MountFoundMultipleAPFSVolumes"
+ "MountNotPersonalizedForExclaves"
+ "MountPath"
+ "MountPersonalizedBundleTicketDataNil"
+ "MountRootHash"
+ "MountTicket"
+ "MountTicketMismatch"
+ "NO_JOB_FOUND|"
+ "Personalize"
+ "PrerollNonce"
+ "PurgeReason"
+ "RemoveAllReplyCanceled"
+ "RequestedAssetSetID"
+ "RequestedAssetSetID-%@"
+ "RetentionPolicy"
+ "RollNonce"
+ "SUSPEND_RESUME callbacks(%@)|"
+ "ScanCatalogDownloadFailed"
+ "ScanFailed"
+ "ScanNoUpdateFound"
+ "ShouldHactivate"
+ "Starting built-in MobileAsset brain built Jul 27 2025 18:37:18"
+ "Starting downloaded MobileAsset brain (version: %@) built Jul 27 2025 18:37:18"
+ "TB,N,V_initialHealthReportPerformedCrosscheck"
+ "TB,N,V_setDescriptorDiscardRamped"
+ "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_refKey"
+ "TotalBytesPurged"
+ "UnexpectedFailure"
+ "Ungraft"
+ "Unimplemented"
+ "UnmapFromExclaves"
+ "Unmount"
+ "Unsupported"
+ "Using RequestedAssetSetID %{public}@ for asset type %{public}@"
+ "[%{public}@]\n[CONSIDER-REMOVAL] {_removeNextDownloadedDescriptorIfNewerDownloaded} unable to decode asset-descriptor | entryID:%{public}@"
+ "[%{public}@]\n[CONSIDER-REMOVAL] {_removeNextDownloadedDescriptorIfNewerDownloaded} unable to load persisted-entry | entryID:%{public}@"
+ "[%{public}@]\n[REMOVAL] {_removeNextDownloadedDescriptorIfNewerDownloaded} crosscheck[BEGIN]"
+ "[%{public}@]\n[REMOVAL] {_removeNextDownloadedDescriptorIfNewerDownloaded} crosscheck[END]"
+ "[%{public}@]\n[REMOVAL] {_removeNextDownloadedDescriptorIfNewerDownloaded} removing | removeDescriptor:%{public}@"
+ "[%{public}@] {removeCurrentSetJob} | removalFlow:%{public}@"
+ "[KnoxServerAuth] Attempting to fetch DAW token with UI %{public}s, SSO %{public}s"
+ "[MORE_CLIENT_REQUESTS] {%{public}@:removeCurrentSetJob} set-job indicated removal but has more to do | removalFlow:%{public}@ | eventInfo:%{public}@"
+ "[overall]instance:%@,selector:%@,UUID:%@,tasks:%lu,requests:%ld,table:%@,FSM:%@,sched:%@,NWFail:%@|beingCancled:%@|[earlier]sched:%@,NWFail:%@|bonded:%@|[active]instance:%@,desire:%@(awaitDownload:%@,checkAwait:%@),found:%@,end:%@,listen:%@,jobInfo:%@|[aggregated]policy:%@,clientRequested:%@|firstClientName:%@,triggeringLayer:%@|onFilesystemByVersion:%ld|[check]Base:%@,UUID:%@,lookupGrant:%@,rampFG:%@,rampLatch:%@,options:%@|[asset]base:%@,patch:%@,full:%@,newer:%@,downloading:%@,scheduler:%@,lookupRsp:%@(forConfig:%@),user:%@,boosting:%@,checking:%@,determining:%@,locking:%@,patched:%@|[installed]:version:%@,build:%@|[status]current:%@,progress:%@,lastPatch:%@|[results]selector:%@,instance:%@,found:%@,end:%@,listen:%@,[set]aggregatedPolicy:%@,descriptor:%@,next:%ld,found:%@,discardRampled:%@"
+ "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}"
+ "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@0:8"
+ "_completionDeadline"
+ "_initialHealthReportPerformedCrosscheck"
+ "_removeNextDownloadedDescriptorIfNewerDownloaded"
+ "_removeNextDownloadedDescriptorIfNewerDownloaded:"
+ "_setDescriptorDiscardRamped"
+ "action_RemoveAllReplyCanceled:error:"
+ "action_SetCalculateDownloadSpace:NotEnoughSpaceForSetDownload(%lld)"
+ "alternate eventInfo.autoAssetUUID:%@|"
+ "attributesOfErrorForDomain:withCode:codeName:"
+ "autoJobByIdentifier:%@|"
+ "autoJobByUUID:%@|"
+ "byIdentifier autoSetJob from autoJobByIdentifier(%@)|"
+ "byIdentifier autoSetJob from cancelingSetJob(%@)|"
+ "byUUID autoSetJob(%@)|"
+ "cache-delete"
+ "cancelingSetJob:%@|"
+ "clientRequestCount(autoJobByUUID:%ld,autoJobByIdentifier:%ld,cancelingSetJob:%ld)|"
+ "com.apple.MobileAssetError.CancelDownload"
+ "com.apple.MobileAssetError.Query"
+ "com.apple.mobileassetd.Purge.Attempt"
+ "com_apple_MobileAsset"
+ "considerPerfomingCrosscheckTrim"
+ "eliminateTracker(%@)|"
+ "eliminatorTrackedJobUUID(%@) != autoAssetJobUUID(%@)|"
+ "eventInfo.autoAssetUUID:N|"
+ "from autoJobByUUID(setJobIdentifier:%@,autoJobByIdentifier:%@,cancelingSetJob:%@)|"
+ "getDawToken called in unsupported environment\n"
+ "initialHealthReportPerformedCrosscheck"
+ "isValidUUID:"
+ "jobFinished|"
+ "mapAutoAssetErrorIndications"
+ "mapCacheDeleteManagerErrorIndications"
+ "nil eliminatorTrackedJobUUID|"
+ "nil setJobKey|"
+ "overallInvolvedScheduler|"
+ "overallPotentialNetworkFailure|"
+ "pallasRequestedAssetSetID:"
+ "pathWithComponents:"
+ "persistedEntryIDs:assetType:"
+ "recordMobileAssetPurgeAttempt:withUrgency:withBytesPurged:withResult:withDir:withRetentionPolicy:withReason:"
+ "removed discovered(%@)|"
+ "removed eliminatorTrackedJobUUID(%@)|"
+ "removed from cancelingSetJobsByIdentifier(%@)|"
+ "removed from currentJobsByUUID(%@)|"
+ "removed from currentSetJobsByIdentifier(%@)|"
+ "removed latest(%@)|"
+ "schedulerInvolved|"
+ "setDescriptorDiscardRamped"
+ "setInitialHealthReportPerformedCrosscheck:"
+ "setSetDescriptorDiscardRamped:"
+ "specific"
+ "ssoControllerQueue"
+ "updateAutoAssetSetStatus|"
+ "v24@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16"
+ "v64@0:8@16@24@32@40^B48^B56"
+ "validateShortTermLockURL:normalizedClientDomainNameURL:normalizedAssetSetIdentifierURL:fileManager:isLatestLocker:isSpecificLocker:"
+ "verifyLatestLockerSymlink"
+ "verifyLockerLatestSymlink"
+ "{%@} | job finished that was not tracked by UUID or by set-identifier | removalFlow:%@ | eventInfo:%@"
+ "{_removeNextDownloadedDescriptorIfNewerDownloaded} recursion problem - abandoning crosscheck | remainingEntryIDCount:%ld | beginEntryIDCount:%ld"
+ "{shortTermLockFilesHealthCheck} %{public}@ is no longer used - will be removed"
+ "{shortTermLockFilesHealthCheck} Failed to remove invalid symlink %{public}@.  Error: %{public}@"
+ "{shortTermLockFilesHealthCheck} Latest symlink %{public}@ is not pointing to a valid target - will be removed"
+ "{shortTermLockFilesHealthCheck} Latest symlink %{public}@ points to a valid target"
+ "{validateShortTermLockURL} specific | clientDomainName:%{public}@ assetSetIdentifier:%{public}@ atomicInstanceUUID:%{public}@"
+ "{verifyLockerLatestSymlink} Successfully removed invalid symlink %{public}@"
+ "{verifyLockerLatestSymlink} Symlink %{public}@ confirmed to have valid target"
+ "{verifyLockerLatestSymlink} Symlink %{public}@ does not have a valid target, it will be removed"
+ "{verifyLockerLatestSymlink} Tried to remove invalid symlink %{public}@, but failed with error: %{public}@"
- " | byIdentifier"
- " | byUUID:%@"
- "\"\""
- "%@:_removeDownloadedDescriptorsWithNewerDownloaded"
- "@\"ASAuthorizationController\""
- "GenerateDawToken called in unsupported environment\n"
- "INFO: ExtensibleSSOAuthenticator: Authentication completed successfully\n"
- "Starting built-in MobileAsset brain built Jul 14 2025 23:40:39"
- "Starting downloaded MobileAsset brain (version: %@) built Jul 14 2025 23:40:39"
- "T@\"ASAuthorizationController\",&,N,V_authenticationController"
- "T@,&,V_refKey"
- "TB,N,V_schedulerTickPerformedCrossCheck"
- "Unable to allocate AuthenticationController object\n"
- "Unable to create request object\n"
- "[%{public}@]\n[CONSIDER-REMOVAL] {_removeDownloadedDescriptorsWithNewerDownloaded} unable to determine previous status | entryID:%{public}@"
- "[%{public}@]\n[REMOVAL] {_removeDownloadedDescriptorsWithNewerDownloaded} removing | removeDescriptor:%{public}@"
- "[%{public}@] {removeCurrentSetJob} %{public}@"
- "[KnoxServerAuth] Attempting to fetch DAW token with UI %s"
- "[MORE_CLIENT_REQUESTS] {%{public}@:removeCurrentSetJob} set-job indicated removal but has more to do | clientRequestCount(autoJobByUUID:%ld,autoJobByIdentifier:%ld) | eventInfo:%{public}@"
- "[NO_JOB_FOUND] {%{public}@:removeCurrentSetJob} set-job not found | eventInfo:%{public}@"
- "[overall]instance:%@,selector:%@,UUID:%@,tasks:%lu,requests:%ld,table:%@,FSM:%@,sched:%@,NWFail:%@|beingCancled:%@|[earlier]sched:%@,NWFail:%@|bonded:%@|[active]instance:%@,desire:%@(awaitDownload:%@,checkAwait:%@),found:%@,end:%@,listen:%@,jobInfo:%@|[aggregated]policy:%@,clientRequested:%@|firstClientName:%@,triggeringLayer:%@|onFilesystemByVersion:%ld|[check]Base:%@,UUID:%@,lookupGrant:%@,rampFG:%@,rampLatch:%@,options:%@|[asset]base:%@,patch:%@,full:%@,newer:%@,downloading:%@,scheduler:%@,lookupRsp:%@(forConfig:%@),user:%@,boosting:%@,checking:%@,determining:%@,locking:%@,patched:%@|[installed]:version:%@,build:%@|[status]current:%@,progress:%@,lastPatch:%@|[results]selector:%@,instance:%@,found:%@,end:%@,listen:%@,[set]aggregatedPolicy:%@,descriptor:%@,next:%ld,found:%@"
- "_authenticationController"
- "_schedulerTickPerformedCrossCheck"
- "action_SetCalculateDownloadSpace"
- "authenticationController"
- "schedulerTickPerformedCrossCheck"
- "setAuthenticationController:"
- "setSchedulerTickPerformedCrossCheck:"
- "validateShortTermLockURL:normalizedClientDomainNameURL:normalizedAssetSetIdentifierURL:fileManager:"
- "{%@} set-job being removed that is not an activeSetJob and not a cancelingSetJob | autoSetJob:%@"
- "{%@} | job finished that was not tracked by UUID or by set-identifier from eventInfo:%@"

```
