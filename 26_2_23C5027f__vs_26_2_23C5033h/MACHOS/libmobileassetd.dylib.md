## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1837.60.20.0.0
-  __TEXT.__text: 0x300d28
-  __TEXT.__auth_stubs: 0x2ca0
-  __TEXT.__objc_stubs: 0x24480
-  __TEXT.__objc_methlist: 0x1130c
+1837.60.34.0.0
+  __TEXT.__text: 0x301d08
+  __TEXT.__auth_stubs: 0x2cb0
+  __TEXT.__objc_stubs: 0x245a0
+  __TEXT.__objc_methlist: 0x1137c
   __TEXT.__const: 0x7bd18
-  __TEXT.__objc_methname: 0x41547
+  __TEXT.__objc_methname: 0x4171c
   __TEXT.__objc_classname: 0xf07
-  __TEXT.__objc_methtype: 0x41d1
-  __TEXT.__cstring: 0x3d88b
-  __TEXT.__oslogstring: 0x55d57
-  __TEXT.__gcc_except_tab: 0xd9a0
+  __TEXT.__objc_methtype: 0x41eb
+  __TEXT.__cstring: 0x3db0b
+  __TEXT.__oslogstring: 0x55fd7
+  __TEXT.__gcc_except_tab: 0xd9a4
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x14cc
   __TEXT.__constg_swiftt: 0x18a8

   __TEXT.__swift5_protos: 0x6c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x60d8
+  __TEXT.__unwind_info: 0x60e8
   __TEXT.__eh_frame: 0x346c
-  __DATA_CONST.__auth_got: 0x1660
+  __DATA_CONST.__auth_got: 0x1668
   __DATA_CONST.__got: 0x878
-  __DATA_CONST.__auth_ptr: 0xac8
+  __DATA_CONST.__auth_ptr: 0xaf8
   __DATA_CONST.__const: 0x9c50
-  __DATA_CONST.__cfstring: 0x2f6a0
+  __DATA_CONST.__cfstring: 0x2f8c0
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa090
+  __DATA_CONST.__objc_selrefs: 0xa0e0
   __DATA_CONST.__objc_arraydata: 0xb98
   __DATA_CONST.__objc_arrayobj: 0x2d0
   __DATA_CONST.__objc_intobj: 0x1278
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x166c8
+  __DATA.__objc_const: 0x16728
   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x890
   __DATA.__objc_superrefs: 0x310
-  __DATA.__objc_ivar: 0x152c
+  __DATA.__objc_ivar: 0x1534
   __DATA.__objc_data: 0x2d18
   __DATA.__data: 0x2cf0
   __DATA.__bss: 0x66a8

   - /System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/MobileAssetExclaveServices
   - /System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/Seeding.framework/Seeding

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 30196F88-E677-33EA-AEE2-FF2520F4C22B
-  Functions: 9440
-  Symbols:   17316
-  CStrings:  24552
+  UUID: CD4AE1F6-179A-351B-8612-9F628CC99D9D
+  Functions: 9450
+  Symbols:   17341
+  CStrings:  24609
 
Symbols:
+ +[DownloadManager isInPalletUpdateMode]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:forClientDomainName:forAssetSetIdentifier:withAddendumMessage:]
+ -[ASAssetMetadataUpdatePolicy isAppleInternalOverrideSetForAssetType:appleInternalPtr:]
+ -[ASAssetMetadataUpdatePolicy serverURLOverrideForAssetType:]
+ -[DownloadManager getInboxUpdaterServerURL]
+ -[MADAutoAssetControlManager _logPersistedSetTarget:operation:historyOperation:forPersistedEntryID:withSetTarget:message:]
+ -[MADAutoAssetControlManager removeSetTargetsForClientDomain:forSetIdentifier:fromLocation:forReason:]
+ -[MADAutoAssetControlManager setTargetPersistedMatchesClientSpecified:providingMismatchReason:]
+ -[MADAutoAssetSetHealthReport reportTime]
+ -[MADAutoAssetSetHealthReport setReportTime:]
+ -[MADAutoSetTarget detailedWithoutEntryID]
+ -[MobileAssetHealthReport _collectAndSubmitReportWithReports:]
+ -[MobileAssetHealthReport firstTimeInNewOS]
+ -[MobileAssetHealthReport scheduleReportWithReports:]
+ -[MobileAssetHealthReport setFirstTimeInNewOS:]
+ GCC_except_table257
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._reportTime
+ OBJC_IVAR_$_MobileAssetHealthReport._firstTimeInNewOS
+ _MSURetrievePreviousUpdateState
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_53
+ __104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1304
+ __104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1305
+ __104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1307
+ __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1299
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1800
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1807
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1808
+ __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2239
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1242
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1246
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1262
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1314
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1315
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1319
+ __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2395
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1350
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1360
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1215
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1216
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1224
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1225
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2329
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2341
+ __22-[ControlManager init]_block_invoke.1269
+ __24-[MABrainUpdater start:]_block_invoke.1150
+ __24-[MABrainUpdater start:]_block_invoke.1154
+ __27-[MABrainUpdater schedule:]_block_invoke.1161
+ __27-[MABrainUpdater schedule:]_block_invoke.1203
+ __27-[MABrainUpdater schedule:]_block_invoke.1208
+ __27-[MABrainUpdater schedule:]_block_invoke_2.1204
+ __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2376
+ __36-[MABrainUpdater update:completion:]_block_invoke.1272
+ __36-[MABrainUpdater update:completion:]_block_invoke.1273
+ __36-[MABrainUpdater update:completion:]_block_invoke.1280
+ __37-[DownloadManager startDownloadTimer]_block_invoke.1816
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1857
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1858
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1225
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1271
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2293
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2294
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1965
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1966
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1972
+ __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1256
+ __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1257
+ __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1926
+ __53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1547
+ __53-[MobileAssetHealthReport scheduleReportWithReports:]_block_invoke.1158
+ __53-[MobileAssetHealthReport scheduleReportWithReports:]_block_invoke.1161
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1340
+ __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2090
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1326
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1327
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1328
+ __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1618
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.391
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.409
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke_2.415
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1281
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1303
+ __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.2055
+ __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1270
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2399
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1137
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1138
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1139
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2598
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2599
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1275
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1276
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1277
+ __77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1262
+ __79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1236
+ __82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1292
+ __82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1299
+ __82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke_2.1300
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3493
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3494
+ __MABrainUtilityScheduleDeviceUnlockAction_block_invoke.416
+ ___53-[MobileAssetHealthReport scheduleReportWithReports:]_block_invoke
+ __block_literal_global.1126
+ __block_literal_global.1134
+ __block_literal_global.1140
+ __block_literal_global.1141
+ __block_literal_global.1154
+ __block_literal_global.1156
+ __block_literal_global.1168
+ __block_literal_global.1172
+ __block_literal_global.1175
+ __block_literal_global.1178
+ __block_literal_global.1180
+ __block_literal_global.1185
+ __block_literal_global.1190
+ __block_literal_global.1204
+ __block_literal_global.1206
+ __block_literal_global.1214
+ __block_literal_global.1222
+ __block_literal_global.1224
+ __block_literal_global.1255
+ __block_literal_global.1257
+ __block_literal_global.1265
+ __block_literal_global.1280
+ __block_literal_global.1282
+ __block_literal_global.1285
+ __block_literal_global.1305
+ __block_literal_global.1307
+ __block_literal_global.1387
+ __block_literal_global.1399
+ __block_literal_global.1404
+ __block_literal_global.1406
+ __block_literal_global.1432
+ __block_literal_global.1438
+ __block_literal_global.1443
+ __block_literal_global.1454
+ __block_literal_global.1459
+ __block_literal_global.1481
+ __block_literal_global.1668
+ __block_literal_global.1713
+ __block_literal_global.1732
+ __block_literal_global.1819
+ __block_literal_global.1824
+ __block_literal_global.1829
+ __block_literal_global.1832
+ __block_literal_global.1868
+ __block_literal_global.1894
+ __block_literal_global.2146
+ __block_literal_global.2168
+ __block_literal_global.2314
+ __block_literal_global.2318
+ __block_literal_global.2329
+ __block_literal_global.2337
+ __block_literal_global.2345
+ __block_literal_global.2353
+ __block_literal_global.2361
+ __block_literal_global.2369
+ __block_literal_global.2377
+ __block_literal_global.2385
+ __block_literal_global.2440
+ __block_literal_global.2442
+ __block_literal_global.2462
+ __block_literal_global.2553
+ __block_literal_global.2869
+ __block_literal_global.2873
+ __block_literal_global.4153
+ __block_literal_global.426
+ __block_literal_global.5223
+ __handleCacheDeletePurgeCallbackForVolume_block_invoke.1171
+ __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1167
+ _objc_msgSend$_collectAndSubmitReportWithReports:
+ _objc_msgSend$_logPersistedSetTarget:operation:historyOperation:forPersistedEntryID:withSetTarget:message:
+ _objc_msgSend$detailedWithoutEntryID
+ _objc_msgSend$firstTimeInNewOS
+ _objc_msgSend$getInboxUpdaterServerURL
+ _objc_msgSend$isAppleInternalOverrideSetForAssetType:appleInternalPtr:
+ _objc_msgSend$isInPalletUpdateMode
+ _objc_msgSend$loopbackServerURL:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:forClientDomainName:forAssetSetIdentifier:withAddendumMessage:
+ _objc_msgSend$removeSetTargetsForClientDomain:forSetIdentifier:fromLocation:forReason:
+ _objc_msgSend$reportTime
+ _objc_msgSend$scheduleReportWithReports:
+ _objc_msgSend$serverURLOverrideForAssetType:
+ _objc_msgSend$setFirstTimeInNewOS:
+ _objc_msgSend$setReportTime:
+ _objc_msgSend$setTargetPersistedMatchesClientSpecified:providingMismatchReason:
+ reg
- -[ASAssetMetadataUpdatePolicy checkPreferencesForOverride:]
- -[MADAutoAssetControlManager _logPersistedSetTarget:operation:forPersistedEntryID:withSetTarget:message:]
- -[MADAutoAssetControlManager removeSetTargetsForClientDomain:forSetIdentifier:fromLocation:]
- -[MADAutoAssetControlManager setTargetPersistedMatchesClientSpecified:]
- -[MobileAssetHealthReport _collectAndSubmitReport]
- -[MobileAssetHealthReport scheduleReport]
- GCC_except_table255
- _OUTLINED_FUNCTION_32
- _OUTLINED_FUNCTION_43
- __104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1295
- __104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1296
- __104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1298
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1290
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1791
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1798
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1799
- __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2224
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1233
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1237
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1253
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1305
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1306
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1310
- __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2381
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1341
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1351
- __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1206
- __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1207
- __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1215
- __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1216
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2314
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2326
- __22-[ControlManager init]_block_invoke.1260
- __24-[MABrainUpdater start:]_block_invoke.1136
- __24-[MABrainUpdater start:]_block_invoke.1141
- __27-[MABrainUpdater schedule:]_block_invoke.1152
- __27-[MABrainUpdater schedule:]_block_invoke.1194
- __27-[MABrainUpdater schedule:]_block_invoke.1199
- __27-[MABrainUpdater schedule:]_block_invoke_2.1195
- __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2362
- __36-[MABrainUpdater update:completion:]_block_invoke.1263
- __36-[MABrainUpdater update:completion:]_block_invoke.1264
- __36-[MABrainUpdater update:completion:]_block_invoke.1271
- __37-[DownloadManager startDownloadTimer]_block_invoke.1807
- __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1143
- __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1146
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1848
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1849
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1216
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1262
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2278
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2279
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1956
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1957
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1963
- __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1247
- __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1248
- __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1917
- __53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1538
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1331
- __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2081
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1317
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1318
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1319
- __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1609
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.382
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.400
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke_2.406
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1272
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1294
- __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.2046
- __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1261
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2390
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1128
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1129
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1130
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2589
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2590
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1266
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1267
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1268
- __77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1253
- __79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1221
- __82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1283
- __82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1290
- __82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke_2.1291
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3484
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3485
- __MABrainUtilityScheduleDeviceUnlockAction_block_invoke.407
- ___41-[MobileAssetHealthReport scheduleReport]_block_invoke
- __block_literal_global.1114
- __block_literal_global.1117
- __block_literal_global.1125
- __block_literal_global.1131
- __block_literal_global.1132
- __block_literal_global.1139
- __block_literal_global.1145
- __block_literal_global.1147
- __block_literal_global.1150
- __block_literal_global.1160
- __block_literal_global.1166
- __block_literal_global.1171
- __block_literal_global.1176
- __block_literal_global.1181
- __block_literal_global.1195
- __block_literal_global.1197
- __block_literal_global.1205
- __block_literal_global.1213
- __block_literal_global.1215
- __block_literal_global.1246
- __block_literal_global.1248
- __block_literal_global.1256
- __block_literal_global.1271
- __block_literal_global.1273
- __block_literal_global.1276
- __block_literal_global.1296
- __block_literal_global.1298
- __block_literal_global.1378
- __block_literal_global.1388
- __block_literal_global.1390
- __block_literal_global.1395
- __block_literal_global.1423
- __block_literal_global.1429
- __block_literal_global.1434
- __block_literal_global.1445
- __block_literal_global.1450
- __block_literal_global.1472
- __block_literal_global.1659
- __block_literal_global.1704
- __block_literal_global.1723
- __block_literal_global.1810
- __block_literal_global.1815
- __block_literal_global.1820
- __block_literal_global.1823
- __block_literal_global.1859
- __block_literal_global.1885
- __block_literal_global.2131
- __block_literal_global.2153
- __block_literal_global.2305
- __block_literal_global.2309
- __block_literal_global.2320
- __block_literal_global.2328
- __block_literal_global.2336
- __block_literal_global.2344
- __block_literal_global.2352
- __block_literal_global.2360
- __block_literal_global.2368
- __block_literal_global.2376
- __block_literal_global.2426
- __block_literal_global.2428
- __block_literal_global.2453
- __block_literal_global.2544
- __block_literal_global.2860
- __block_literal_global.2864
- __block_literal_global.4144
- __block_literal_global.417
- __block_literal_global.5199
- __handleCacheDeletePurgeCallbackForVolume_block_invoke.1162
- __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1158
- _objc_msgSend$_collectAndSubmitReport
- _objc_msgSend$_logPersistedSetTarget:operation:forPersistedEntryID:withSetTarget:message:
- _objc_msgSend$checkPreferencesForOverride:
- _objc_msgSend$controlAlteredSetConfiguration:
- _objc_msgSend$removeSetTargetsForClientDomain:forSetIdentifier:fromLocation:
- _objc_msgSend$scheduleReport
- _objc_msgSend$setTargetPersistedMatchesClientSpecified:
CStrings:
+ "AppleInternal"
+ "Asset-Type (%{public}@) is forcing server URL to %{public}@ server."
+ "Customer in box updater"
+ "Failed to determine URL for inboxUpdate server | error:%{public}@"
+ "Internal in box updater"
+ "MobileAssetForceInternalServerURL"
+ "NewOSReport"
+ "PrevUpdateState"
+ "RECLAIMED_ASSET            "
+ "ReportTime"
+ "SET_JOB_ASSET_DOWNLD_END   "
+ "SET_JOB_ASSET_DOWNLD_START "
+ "SET_TARGET_ADD             "
+ "SET_TARGET_REMOVE          "
+ "SET_TARGET_REPLACE         "
+ "Starting built-in MobileAsset brain built Nov  2 2025 23:32:10"
+ "Starting downloaded MobileAsset brain (version: %@) built Nov  2 2025 23:32:10"
+ "T@\"NSDate\",&,V_reportTime"
+ "TB,N,V_firstTimeInNewOS"
+ "[%{public}@] {loadPersistedSetTargets} no persisted set-targets to be resumed | bootedOSVersion:%{public}@ | bootedOSBuildVersion:%{public}@"
+ "[%{public}@] {loadPersistedSetTargets} set-targets preserved | bootedOSVersion:%{public}@ | bootedOSBuildVersion:%{public}@"
+ "[BaseURLOverride]: Failed to determine 'palletUpdate' mode: %{public}@"
+ "[BaseURLOverride]: Failed to obtain PalletUpdateMode URL for asset | Asset:%{public}@"
+ "[MobileAssetHealthReport]: Date of first run in %{public}@ : %{public}@"
+ "[MobileAssetHealthReport]: Failed to get the reports"
+ "[MobileAssetHealthReport]: First time in %{public}@"
+ "[MobileAssetHealthReport]: MSURetrievePreviousUpdateState is not available"
+ "_collectAndSubmitReportWithReports:"
+ "_firstTimeInNewOS"
+ "_logPersistedSetTarget:operation:historyOperation:forPersistedEntryID:withSetTarget:message:"
+ "_reportTime"
+ "cd060049-2465-43e3-bbb5-d769a66da2d7"
+ "detailedWithoutEntryID"
+ "ffc25f86-b83c-4139-b8ad-91131d0e5429"
+ "firstTimeInNewOS"
+ "getInboxUpdaterServerURL"
+ "https://gdmf-auth-stg.apple.com/v2/assets"
+ "isAppleInternalOverrideSetForAssetType:appleInternalPtr:"
+ "isInPalletUpdateMode"
+ "loopbackServerURL:"
+ "no persisted set-target entries"
+ "recordOperation:toHistoryType:fromLayer:forClientDomainName:forAssetSetIdentifier:withAddendumMessage:"
+ "removeSetTargetsForClientDomain:forSetIdentifier:fromLocation:forReason:"
+ "removed previously defined set-target | setTarget:%@ | removalReason:%@"
+ "reportTime"
+ "scheduleReportWithReports:"
+ "serverURLOverrideForAssetType:"
+ "set-configuration eliminate"
+ "set-target changed | clientDomainName:%@ | assetSetIdentifier:%@ | currentlyPersisted:%@ | clientProvided:%@ | minTargetOSMatch:%@ | maxTargetOSMatch:%@ | entriesMatch:%@"
+ "setFirstTimeInNewOS:"
+ "setReportTime:"
+ "setTargetPersistedMatchesClientSpecified:providingMismatchReason:"
+ "unable to decode persisted set-target"
+ "unable to load persisted set-target"
+ "v64@0:8@16@24q32@40@48@56"
+ "{%{public}@} | no set-target entry found | entryID:%{public}@"
+ "{%{public}@} | unable to determine previous set-target | entryID:%{public}@"
+ "{%{public}@} | unable to re-load set-target | entryID:%{public}@"
+ "{setTargetPersistedMatchesClientSpecified} | new set-target | setInfoInstance:%{public}@"
+ "{setTargetPersistedMatchesClientSpecified} | no persisted set-target entries | setInfoInstance:%{public}@"
+ "{setTargetPersistedMatchesClientSpecified} | set-target changed | mismatchReason:%{public}@ | setInfoInstance:%{public}@"
- "RECLAIMED_ASSET"
- "SET_JOB_ASSET_DOWNLOAD_END  "
- "SET_JOB_ASSET_DOWNLOAD_START"
- "Starting built-in MobileAsset brain built Oct 21 2025 17:00:04"
- "Starting downloaded MobileAsset brain (version: %@) built Oct 21 2025 17:00:04"
- "[%{public}@] {loadPersistedSetConfigurations} no persisted set-targets to be resumed | bootedOSVersion:%{public}@ | bootedOSBuildVersion:%{public}@"
- "[%{public}@] {loadPersistedSetConfigurations} set-targets preserved | bootedOSVersion:%{public}@ | bootedOSBuildVersion:%{public}@"
- "[BaseURLOverride]: Failed to determine if device in PalletUpdateMode: %{public}@"
- "[BaseURLOverride]: Unable to check if device in 'PalletUpdateMode'."
- "[MobileAssetHealthReport]: Date of first run in %@ : %@"
- "_collectAndSubmitReport"
- "_logPersistedSetTarget:operation:forPersistedEntryID:withSetTarget:message:"
- "checkPreferencesForOverride:"
- "http://localhost:8080"
- "removeSetTargetsForClientDomain:forSetIdentifier:fromLocation:"
- "removed previously defined set-target | setTarget:%@"
- "scheduleReport"
- "setTargetPersistedMatchesClientSpecified:"
- "{%{public}@} | no set-target entry found for entry:%{public}@"
- "{%{public}@} | unable to determine previous set-target for entry:%{public}@"
- "{%{public}@} | unable to re-load set-target for entry:%{public}@"

```
