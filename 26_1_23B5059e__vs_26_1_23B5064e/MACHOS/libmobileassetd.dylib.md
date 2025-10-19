## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1837.40.63.0.0
-  __TEXT.__text: 0x2ff414
+1837.40.71.0.0
+  __TEXT.__text: 0x300668
   __TEXT.__auth_stubs: 0x2c90
-  __TEXT.__objc_stubs: 0x24320
-  __TEXT.__objc_methlist: 0x11224
+  __TEXT.__objc_stubs: 0x24480
+  __TEXT.__objc_methlist: 0x1130c
   __TEXT.__const: 0x7ba98
-  __TEXT.__objc_methname: 0x41432
-  __TEXT.__objc_classname: 0xeee
-  __TEXT.__objc_methtype: 0x41dd
-  __TEXT.__cstring: 0x3d45b
-  __TEXT.__oslogstring: 0x55e77
-  __TEXT.__gcc_except_tab: 0xd944
+  __TEXT.__objc_methname: 0x41547
+  __TEXT.__objc_classname: 0xf07
+  __TEXT.__objc_methtype: 0x41d1
+  __TEXT.__cstring: 0x3d87b
+  __TEXT.__oslogstring: 0x55d87
+  __TEXT.__gcc_except_tab: 0xd980
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x14cc
   __TEXT.__constg_swiftt: 0x18a8

   __TEXT.__swift5_protos: 0x6c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x6070
+  __TEXT.__unwind_info: 0x60d8
   __TEXT.__eh_frame: 0x346c
   __DATA_CONST.__auth_got: 0x1658
   __DATA_CONST.__got: 0x878
   __DATA_CONST.__auth_ptr: 0xac8
-  __DATA_CONST.__const: 0x9b98
-  __DATA_CONST.__cfstring: 0x2f400
-  __DATA_CONST.__objc_classlist: 0x460
+  __DATA_CONST.__const: 0x9c58
+  __DATA_CONST.__cfstring: 0x2f6a0
+  __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa028
+  __DATA_CONST.__objc_selrefs: 0xa090
   __DATA_CONST.__objc_arraydata: 0xb98
   __DATA_CONST.__objc_arrayobj: 0x2d0
-  __DATA_CONST.__objc_intobj: 0x12d8
+  __DATA_CONST.__objc_intobj: 0x1278
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x16568
+  __DATA.__objc_const: 0x166c8
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x888
-  __DATA.__objc_superrefs: 0x308
-  __DATA.__objc_ivar: 0x1520
-  __DATA.__objc_data: 0x2cc8
+  __DATA.__objc_classrefs: 0x890
+  __DATA.__objc_superrefs: 0x310
+  __DATA.__objc_ivar: 0x152c
+  __DATA.__objc_data: 0x2d18
   __DATA.__data: 0x2cf0
-  __DATA.__bss: 0x6688
+  __DATA.__bss: 0x66a8
   __DATA.__common: 0x98
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D372D5A7-43E3-3BAD-A572-3D802B7C7298
-  Functions: 9408
-  Symbols:   17251
-  CStrings:  24498
+  UUID: 787DD40D-9698-3CF9-BC90-402AAF0651C3
+  Functions: 9440
+  Symbols:   17317
+  CStrings:  24553
 
Symbols:
+ +[MAAssetTypeDescriptor _assetTypeDescriptors]
+ +[MAAssetTypeDescriptor _assetTypeDescriptors].cold.1
+ +[MAAssetTypeDescriptor _loadDescriptorsFromPath:intoDictionary:]
+ +[MAAssetTypeDescriptor _secureAssetTypeDescriptors]
+ +[MAAssetTypeDescriptor _secureAssetTypeDescriptors].cold.1
+ +[MAAssetTypeDescriptor _typeDescriptorDictionaryForAssetType:typeDescriptors:]
+ +[MAAssetTypeDescriptor _typeDescriptorsMatchingBooleanKey:]
+ +[MAAssetTypeDescriptor descriptorForAssetType:]
+ +[MAAssetTypeDescriptor typeDescriptorsToDataVault]
+ +[MAAssetTypeDescriptor typeDescriptorsToRemoveV1Assets]
+ +[MADAutoAssetSecure isCodeAsset:forDescriptor:]
+ -[DownloadManager checkSplunkStatus:failureReason:productVersion:sessionId:nonce:url:statusCode:assetAudience:version:baseUrl:discretionary:deviceCheck:]
+ -[DownloadManager massageXmlAndPersist:catalogInfo:descriptor:assets:transformations:to:postedDate:assetSetId:pallasUrl:considerCaching:]
+ -[DownloadManager newDefaultEventDictionary:sessionId:nonce:url:statusCode:assetAudience:uuid:assetType:version:baseUrl:discretionary:deviceCheck:]
+ -[MAAssetTypeDescriptor .cxx_destruct]
+ -[MAAssetTypeDescriptor assetProperties]
+ -[MAAssetTypeDescriptor assetSpecifiers]
+ -[MAAssetTypeDescriptor assetType]
+ -[MAAssetTypeDescriptor description]
+ -[MAAssetTypeDescriptor initWithAssetType:]
+ -[MAAssetTypeDescriptor isSecure]
+ -[MAAssetTypeDescriptor shouldMakeDataVault]
+ -[MAAssetTypeDescriptor shouldRemoveV1Assets]
+ -[MADAutoAssetControlManager doesSetDescriptorReferenceDropped:forSetDescriptor:]
+ -[MADAutoAssetControlManager getCorruptedEntryInfo:]
+ -[MADAutoAssetControlManager jobDescriptorOnFilesystemValidated:forOSBuild:]
+ -[MADAutoAssetDescriptor assetBuild]
+ -[MADAutoAssetDescriptor wasBuiltForOSBuild:]
+ -[SecureMobileAssetBundle bundleAccessPermitted:]
+ -[SecureMobileAssetBundle typeDescriptor]
+ GCC_except_table16
+ GCC_except_table255
+ GCC_except_table321
+ GCC_except_table330
+ GCC_except_table332
+ GCC_except_table334
+ GCC_except_table348
+ GCC_except_table355
+ GCC_except_table359
+ GCC_except_table366
+ GCC_except_table372
+ GCC_except_table377
+ GCC_except_table385
+ GCC_except_table4
+ GCC_except_table432
+ GCC_except_table445
+ GCC_except_table530
+ GCC_except_table532
+ GCC_except_table594
+ GCC_except_table631
+ GCC_except_table633
+ GCC_except_table639
+ GCC_except_table641
+ GCC_except_table658
+ GCC_except_table687
+ GCC_except_table795
+ GCC_except_table796
+ GCC_except_table800
+ OBJC_IVAR_$_MAAssetTypeDescriptor._assetType
+ OBJC_IVAR_$_MAAssetTypeDescriptor._isSecure
+ OBJC_IVAR_$_MAAssetTypeDescriptor._typeDescriptor
+ OBJC_IVAR_$_SecureMobileAssetBundle._typeDescriptor
+ _OBJC_CLASS_$_MAAssetTypeDescriptor
+ _OBJC_METACLASS_$_MAAssetTypeDescriptor
+ __104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1295
+ __104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1296
+ __104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1298
+ __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1290
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1791
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1798
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1799
+ __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2224
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1233
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1237
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1253
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1305
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1306
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1310
+ __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2381
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1341
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1351
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1206
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1207
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1215
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1216
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2314
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2326
+ __22-[ControlManager init]_block_invoke.1260
+ __24-[MABrainUpdater start:]_block_invoke.1136
+ __24-[MABrainUpdater start:]_block_invoke.1141
+ __27-[MABrainUpdater schedule:]_block_invoke.1152
+ __27-[MABrainUpdater schedule:]_block_invoke.1194
+ __27-[MABrainUpdater schedule:]_block_invoke.1199
+ __27-[MABrainUpdater schedule:]_block_invoke_2.1195
+ __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2362
+ __36-[MABrainUpdater update:completion:]_block_invoke.1263
+ __36-[MABrainUpdater update:completion:]_block_invoke.1264
+ __36-[MABrainUpdater update:completion:]_block_invoke.1271
+ __37-[DownloadManager startDownloadTimer]_block_invoke.1807
+ __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1143
+ __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1146
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1848
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1849
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1216
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1262
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2278
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2279
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1956
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1957
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1963
+ __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1247
+ __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1248
+ __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1917
+ __53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1538
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1331
+ __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2081
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1317
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1318
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1319
+ __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1609
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1272
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1294
+ __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.2046
+ __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1261
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2390
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1128
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1129
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1130
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2589
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2590
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1266
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1267
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1268
+ __77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1253
+ __79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1221
+ __82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1283
+ __82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1290
+ __82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke_2.1291
+ __OBJC_$_CLASS_METHODS_MAAssetTypeDescriptor
+ __OBJC_$_INSTANCE_METHODS_MAAssetTypeDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MAAssetTypeDescriptor
+ __OBJC_$_PROP_LIST_MAAssetTypeDescriptor
+ __OBJC_CLASS_RO_$_MAAssetTypeDescriptor
+ __OBJC_METACLASS_RO_$_MAAssetTypeDescriptor
+ ___137-[DownloadManager massageXmlAndPersist:catalogInfo:descriptor:assets:transformations:to:postedDate:assetSetId:pallasUrl:considerCaching:]_block_invoke
+ ___153-[DownloadManager checkSplunkStatus:failureReason:productVersion:sessionId:nonce:url:statusCode:assetAudience:version:baseUrl:discretionary:deviceCheck:]_block_invoke
+ ___46+[MAAssetTypeDescriptor _assetTypeDescriptors]_block_invoke
+ ___52+[MAAssetTypeDescriptor _secureAssetTypeDescriptors]_block_invoke
+ ___60+[MAAssetTypeDescriptor _typeDescriptorsMatchingBooleanKey:]_block_invoke
+ ___60+[MAAssetTypeDescriptor _typeDescriptorsMatchingBooleanKey:]_block_invoke_2
+ ___79+[MAAssetTypeDescriptor _typeDescriptorDictionaryForAssetType:typeDescriptors:]_block_invoke
+ ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96s104s112s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
+ ___block_descriptor_48_e8_32s40r_e29_v32?08"NSDictionary"16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e22_v16?0"NSDictionary"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8
+ __block_literal_global.1114
+ __block_literal_global.1117
+ __block_literal_global.1125
+ __block_literal_global.1131
+ __block_literal_global.1132
+ __block_literal_global.1139
+ __block_literal_global.1145
+ __block_literal_global.1147
+ __block_literal_global.1150
+ __block_literal_global.1160
+ __block_literal_global.1163
+ __block_literal_global.1166
+ __block_literal_global.1171
+ __block_literal_global.1176
+ __block_literal_global.1181
+ __block_literal_global.1195
+ __block_literal_global.1197
+ __block_literal_global.1205
+ __block_literal_global.1213
+ __block_literal_global.1215
+ __block_literal_global.1246
+ __block_literal_global.1248
+ __block_literal_global.1256
+ __block_literal_global.1271
+ __block_literal_global.1273
+ __block_literal_global.1276
+ __block_literal_global.1296
+ __block_literal_global.1298
+ __block_literal_global.1378
+ __block_literal_global.1388
+ __block_literal_global.1390
+ __block_literal_global.1395
+ __block_literal_global.1397
+ __block_literal_global.1423
+ __block_literal_global.1429
+ __block_literal_global.1434
+ __block_literal_global.1445
+ __block_literal_global.1450
+ __block_literal_global.1472
+ __block_literal_global.1659
+ __block_literal_global.1704
+ __block_literal_global.1723
+ __block_literal_global.1810
+ __block_literal_global.1815
+ __block_literal_global.1820
+ __block_literal_global.1823
+ __block_literal_global.1859
+ __block_literal_global.1885
+ __block_literal_global.2131
+ __block_literal_global.2153
+ __block_literal_global.2305
+ __block_literal_global.2309
+ __block_literal_global.2320
+ __block_literal_global.2328
+ __block_literal_global.2336
+ __block_literal_global.2344
+ __block_literal_global.2352
+ __block_literal_global.2360
+ __block_literal_global.2368
+ __block_literal_global.2376
+ __block_literal_global.2426
+ __block_literal_global.2428
+ __block_literal_global.2453
+ __block_literal_global.2544
+ __block_literal_global.2860
+ __block_literal_global.2864
+ __block_literal_global.5199
+ __handleCacheDeletePurgeCallbackForVolume_block_invoke.1159
+ __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1155
+ _assetTypeDescriptors.assetTypeDescriptors
+ _assetTypeDescriptors.onceToken
+ _deviceOSBuildVersion
+ _kMobileAssetPreferencesFakeDeviceOSBuildVersion
+ _objc_msgSend$assetBuild
+ _objc_msgSend$bundleAccessPermitted:
+ _objc_msgSend$checkSplunkStatus:failureReason:productVersion:sessionId:nonce:url:statusCode:assetAudience:version:baseUrl:discretionary:deviceCheck:
+ _objc_msgSend$descriptorForAssetType:
+ _objc_msgSend$doesSetDescriptorReferenceDropped:forSetDescriptor:
+ _objc_msgSend$getCorruptedEntryInfo:
+ _objc_msgSend$initWithAssetType:
+ _objc_msgSend$isCodeAsset:forDescriptor:
+ _objc_msgSend$isEqualSelector:
+ _objc_msgSend$isSecure
+ _objc_msgSend$jobDescriptorOnFilesystemValidated:forOSBuild:
+ _objc_msgSend$massageXmlAndPersist:catalogInfo:descriptor:assets:transformations:to:postedDate:assetSetId:pallasUrl:considerCaching:
+ _objc_msgSend$newDefaultEventDictionary:sessionId:nonce:url:statusCode:assetAudience:uuid:assetType:version:baseUrl:discretionary:deviceCheck:
+ _objc_msgSend$typeDescriptorsToDataVault
+ _objc_msgSend$typeDescriptorsToRemoveV1Assets
+ _objc_msgSend$verifyPlist:manifest:manifestType:result:error:
+ _objc_msgSend$wasBuiltForOSBuild:
+ _secureAssetTypeDescriptors.onceToken
+ _secureAssetTypeDescriptors.secureAssetTypeDescriptors
- -[ControlManager assetTypeDescriptors]
- -[ControlManager loadAssetTypeDescriptors]
- -[DownloadManager applyTransformsAndCheckReceipts:transformations:assetType:assets:receiptResults:]
- -[DownloadManager checkSplunkStatus:failureReason:productVersion:sessionId:nonce:url:statusCode:assetAudience:version:receiptResults:baseUrl:discretionary:deviceCheck:]
- -[DownloadManager massageXmlAndPersist:catalogInfo:descriptor:assets:transformations:to:postedDate:receiptResults:assetSetId:pallasUrl:considerCaching:]
- -[DownloadManager newDefaultEventDictionary:sessionId:nonce:url:statusCode:assetAudience:uuid:assetType:version:receiptResults:baseUrl:discretionary:deviceCheck:]
- GCC_except_table177
- GCC_except_table256
- GCC_except_table320
- GCC_except_table329
- GCC_except_table331
- GCC_except_table333
- GCC_except_table336
- GCC_except_table350
- GCC_except_table358
- GCC_except_table362
- GCC_except_table370
- GCC_except_table374
- GCC_except_table378
- GCC_except_table431
- GCC_except_table437
- GCC_except_table529
- GCC_except_table531
- GCC_except_table593
- GCC_except_table630
- GCC_except_table632
- GCC_except_table638
- GCC_except_table640
- GCC_except_table655
- GCC_except_table684
- GCC_except_table791
- GCC_except_table792
- GCC_except_table793
- OBJC_IVAR_$_ControlManager._assetTypeDescriptors
- __104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1301
- __104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1302
- __104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1304
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1299
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1800
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1807
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1808
- __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2239
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1239
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1243
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1259
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1311
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1312
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1316
- __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2413
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1347
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1357
- __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1215
- __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1216
- __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1224
- __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1225
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2346
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2358
- __22-[ControlManager init]_block_invoke.1269
- __24-[MABrainUpdater start:]_block_invoke.1150
- __24-[MABrainUpdater start:]_block_invoke.1154
- __27-[MABrainUpdater schedule:]_block_invoke.1161
- __27-[MABrainUpdater schedule:]_block_invoke.1203
- __27-[MABrainUpdater schedule:]_block_invoke.1208
- __27-[MABrainUpdater schedule:]_block_invoke_2.1204
- __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2394
- __36-[MABrainUpdater update:completion:]_block_invoke.1272
- __36-[MABrainUpdater update:completion:]_block_invoke.1273
- __36-[MABrainUpdater update:completion:]_block_invoke.1280
- __37-[DownloadManager startDownloadTimer]_block_invoke.1816
- __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1152
- __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1155
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1857
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1858
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1225
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1271
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2293
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2294
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1965
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1966
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1972
- __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1256
- __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1257
- __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1926
- __53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1547
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1340
- __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2090
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1323
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1324
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1325
- __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1618
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1281
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1303
- __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.2055
- __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1269
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2399
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1137
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1138
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1139
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2598
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2599
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1272
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1273
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1274
- __77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1262
- __79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1230
- __82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1289
- __82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1296
- __82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke_2.1297
- ___152-[DownloadManager massageXmlAndPersist:catalogInfo:descriptor:assets:transformations:to:postedDate:receiptResults:assetSetId:pallasUrl:considerCaching:]_block_invoke
- ___168-[DownloadManager checkSplunkStatus:failureReason:productVersion:sessionId:nonce:url:statusCode:assetAudience:version:receiptResults:baseUrl:discretionary:deviceCheck:]_block_invoke
- ___block_descriptor_137_e8_32s40s48s56s64s72s80s88s96s104s112s120s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
- __block_literal_global.1123
- __block_literal_global.1126
- __block_literal_global.1134
- __block_literal_global.1140
- __block_literal_global.1141
- __block_literal_global.1156
- __block_literal_global.1157
- __block_literal_global.1168
- __block_literal_global.1172
- __block_literal_global.1175
- __block_literal_global.1178
- __block_literal_global.1180
- __block_literal_global.1185
- __block_literal_global.1190
- __block_literal_global.1204
- __block_literal_global.1206
- __block_literal_global.1214
- __block_literal_global.1222
- __block_literal_global.1224
- __block_literal_global.1255
- __block_literal_global.1257
- __block_literal_global.1264
- __block_literal_global.1280
- __block_literal_global.1282
- __block_literal_global.1285
- __block_literal_global.1305
- __block_literal_global.1307
- __block_literal_global.1387
- __block_literal_global.1394
- __block_literal_global.1396
- __block_literal_global.1401
- __block_literal_global.1403
- __block_literal_global.1432
- __block_literal_global.1438
- __block_literal_global.1443
- __block_literal_global.1454
- __block_literal_global.1459
- __block_literal_global.1481
- __block_literal_global.1668
- __block_literal_global.1712
- __block_literal_global.1713
- __block_literal_global.1819
- __block_literal_global.1824
- __block_literal_global.1829
- __block_literal_global.1832
- __block_literal_global.1868
- __block_literal_global.1894
- __block_literal_global.2146
- __block_literal_global.2168
- __block_literal_global.2273
- __block_literal_global.2318
- __block_literal_global.2329
- __block_literal_global.2337
- __block_literal_global.2345
- __block_literal_global.2353
- __block_literal_global.2361
- __block_literal_global.2369
- __block_literal_global.2377
- __block_literal_global.2385
- __block_literal_global.2458
- __block_literal_global.2460
- __block_literal_global.2468
- __block_literal_global.2556
- __block_literal_global.2869
- __block_literal_global.2872
- __block_literal_global.5193
- __handleCacheDeletePurgeCallbackForVolume_block_invoke.1171
- __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1167
- _objc_msgSend$applyTransformsAndCheckReceipts:transformations:assetType:assets:receiptResults:
- _objc_msgSend$checkSplunkStatus:failureReason:productVersion:sessionId:nonce:url:statusCode:assetAudience:version:receiptResults:baseUrl:discretionary:deviceCheck:
- _objc_msgSend$loadAssetTypeDescriptors
- _objc_msgSend$massageXmlAndPersist:catalogInfo:descriptor:assets:transformations:to:postedDate:receiptResults:assetSetId:pallasUrl:considerCaching:
- _objc_msgSend$newDefaultEventDictionary:sessionId:nonce:url:statusCode:assetAudience:uuid:assetType:version:receiptResults:baseUrl:discretionary:deviceCheck:
- _objc_msgSend$verifyReceipt:withSignature:
CStrings:
+ "\n[AUTO-SECURE][AUTO-DETERMINE] {%{public}@} determined secure attribute | secureAssetBundle:%{public}@ | autoAssetDescriptor:%{public}@"
+ "\n[STARTUP-CROSSCHECK] {loadPersistedCrosscheckStaleForceUnlock} dropping atomic-instance (referenced asset dropped) | setAtomicInstance:%{public}@"
+ "%@:isCodeAsset"
+ "%@:secureCheckUngraftAll"
+ "(isSecureMobileAsset:%@ | isPersonalized:%@ | isPersonalizedManifestStaged:%@ | manifest:%@ | isAccessible:%@ | assetBundlePath:%@ | accessPath:%@ | secureInfoPlist:%@)"
+ "/System/Library/SecureAssetTypeDescriptors/"
+ "<MAAssetTypeDescriptor: %p>: (AssetType: %@, Secure: %d)"
+ "@\"MAAssetTypeDescriptor\""
+ "@108@0:8@16@24@32@40q48@56@64@72@80@88B96@100"
+ "AccessNotPermitted"
+ "Asset Specifiers"
+ "Classic"
+ "Code"
+ "CompatibilityVersionMismatch"
+ "CryptexInfo plist is missing its asset-type defined in: %@"
+ "DEL_AI_ELIMINATED          "
+ "DEL_ASSET_INCOMPLETE       "
+ "DEL_ASSET_SMAC_DIFF_OS_BLD "
+ "DEL_SD_ELIMINATED          "
+ "Failed to load asset descriptors from path %{public}@. %@"
+ "Failed to parse CryptexInfo as a plist."
+ "Failed to validate cryptex info plist with manifest from disk."
+ "FakeDeviceOSBuildVersion"
+ "MAAssetTypeDescriptor"
+ "Secure cryptex info plist (%@) is missing on the bundle."
+ "Starting built-in MobileAsset brain built Oct  6 2025 01:50:07"
+ "Starting downloaded MobileAsset brain (version: %@) built Oct  6 2025 01:50:07"
+ "Stored personalized manifest ticket (%@) could not be read"
+ "T@\"MAAssetTypeDescriptor\",R,V_typeDescriptor"
+ "T@\"NSArray\",R,D,N"
+ "T@\"NSDictionary\",R,D,N"
+ "TB,R,D,N"
+ "TB,R,N,V_isSecure"
+ "UNKNOWN_MANIFEST_TYPE"
+ "Unable to read cryptex info path %@"
+ "[%{public}@] {jobDescriptorOnFilesystemValidated} SMAC for different OS-build | osBuild:%{public}@ | assetBuild:%{public}@ | jobDescriptor:%{public}@ | localURLForDescriptor:%{public}@"
+ "[BaseURLOverride]: Using PalletUpdateMode URL for asset | Asset:%{public}@."
+ "[SMA] Cannot create an MAAssetTypeDescriptor because assetType is nil for bundle: %{public}@"
+ "[SMA] [SecureMAHelper]: Successfully recorded graft entry | assetType:%@ | grafted:%@"
+ "_isSecure"
+ "_typeDescriptor"
+ "assetBuild"
+ "assetProperties"
+ "assetSpecifiers"
+ "bundleAccessPermitted:"
+ "checkSplunkStatus:failureReason:productVersion:sessionId:nonce:url:statusCode:assetAudience:version:baseUrl:discretionary:deviceCheck:"
+ "descriptorForAssetType:"
+ "doesSetDescriptorReferenceDropped"
+ "doesSetDescriptorReferenceDropped:forSetDescriptor:"
+ "forcing atomic-instance unlocked due to incomplete set-descriptor | setDescriptor:%@"
+ "forcing atomic-instance unlocked due to set-eliminate | setDescriptor:%@"
+ "getCorruptedEntryInfo:"
+ "isCodeAsset:forDescriptor:"
+ "isSecure"
+ "jobDescriptorOnFilesystemValidated:forOSBuild:"
+ "massageXmlAndPersist called with no assets"
+ "massageXmlAndPersist:catalogInfo:descriptor:assets:transformations:to:postedDate:assetSetId:pallasUrl:considerCaching:"
+ "newDefaultEventDictionary:sessionId:nonce:url:statusCode:assetAudience:uuid:assetType:version:baseUrl:discretionary:deviceCheck:"
+ "q92@0:8@16@24@32@40@48@56@64@72@80B88"
+ "setDescriptor.latestDowloadedAtomicInstanceEntries"
+ "setLockUsageMapForSetDescriptor"
+ "shouldMakeDataVault"
+ "shouldRemoveV1Assets"
+ "typeDescriptor"
+ "typeDescriptorsToDataVault"
+ "typeDescriptorsToRemoveV1Assets"
+ "v108@0:8@16@24@32@40@48@56q64@72@80@88B96@100"
+ "v16@?0@\"NSDictionary\"8"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "v32@?0@8@\"NSDictionary\"16^B24"
+ "wasBuiltForOSBuild:"
+ "{%@:doesSetDescriptorReferenceDropped:} downloaded set-descriptor missing asset-descriptor | setDescriptor:%@ | nextDownloadedEntry:%@"
- "(isSecureMobileAsset:%@ | isPersonalized:%@ | isPersonalizedManifestStaged:%@ | isAccessible:%@ | assetBundlePath:%@ | accessPath:%@ | secureInfoPlist:%@)"
- "@116@0:8@16@24@32@40q48@56@64@72@80@88@96B104@108"
- "Asset failed receipt check with error %ld: %{public}@"
- "Asset failed receipt due to nil receiptFieldData"
- "Asset failed receipt due to nil receiptFields"
- "Asset failed receipt due to nil receiptMeasurement"
- "Asset failed receipt sha1 check as measurements are not equal"
- "Asset failed receipt sha256 check as measurements are not equal"
- "AssetReceipt"
- "AssetSignature"
- "Measurement"
- "MeasurementSHA256"
- "MobileAsset receipt results: Total: %d With Receipt: %d Valid: %d Valid But Expired: %d"
- "Skipping: %{public}@ not making it a datavault"
- "Skipping: %{public}@ not making it a datavault as assetType is nil in descriptor"
- "Starting built-in MobileAsset brain built Sep 29 2025 20:41:39"
- "Starting downloaded MobileAsset brain (version: %@) built Sep 29 2025 20:41:39"
- "T@\"NSMutableDictionary\",R,N,V_assetTypeDescriptors"
- "The content or signature is null, skipping"
- "The receipt is not a dictionary"
- "Total: %d (Missing: %d Valid: %d Expired: %d Errors: %d) ErrorCodes: %@"
- "Wrong number of receipt results %ld vs %ld"
- "[BaseURLOverride]: Not using PalletUpdateMode URL for asset(%{public}@)."
- "[BaseURLOverride]: Using PalletUpdateMode URL for asset(%{public}@)."
- "[SMA] [SecureMAHelper]: Successfully recorded graft entry for asset of type %@"
- "_assetTypeDescriptors"
- "applyTransformsAndCheckReceipts:transformations:assetType:assets:receiptResults:"
- "assetReceiptData"
- "assetTypeDescriptors"
- "checkSplunkStatus:failureReason:productVersion:sessionId:nonce:url:statusCode:assetAudience:version:receiptResults:baseUrl:discretionary:deviceCheck:"
- "loadAssetTypeDescriptors"
- "massageXmlAndPersist:catalogInfo:descriptor:assets:transformations:to:postedDate:receiptResults:assetSetId:pallasUrl:considerCaching:"
- "newDefaultEventDictionary:sessionId:nonce:url:statusCode:assetAudience:uuid:assetType:version:receiptResults:baseUrl:discretionary:deviceCheck:"
- "q100@0:8@16@24@32@40@48@56@64^@72@80@88B96"
- "removeAllObsoletedV1Assets Skipping: %{public}@ not removing its V1 assets"
- "removeAllObsoletedV1Assets Skipping: %{public}@ not removing its V1 assets as assetType is nil in descriptor"
- "v116@0:8@16@24@32@40@48@56q64@72@80@88@96B104@108"
- "v56@0:8@16@24@32@40^@48"
- "verifySetDescriptorIsLockable"

```
