## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2465.1.9.0.0
-  __TEXT.__text: 0xc87f0
-  __TEXT.__objc_methlist: 0x4e04
-  __TEXT.__const: 0x410
-  __TEXT.__cstring: 0x9f53
-  __TEXT.__gcc_except_tab: 0x4a80
-  __TEXT.__oslogstring: 0xd788
+2465.2.7.101.0
+  __TEXT.__text: 0xca134
+  __TEXT.__objc_methlist: 0x4ef4
+  __TEXT.__const: 0x430
+  __TEXT.__cstring: 0xa040
+  __TEXT.__gcc_except_tab: 0x4aac
+  __TEXT.__oslogstring: 0xd7ed
   __TEXT.__dlopen_cstrs: 0xf4
-  __TEXT.__unwind_info: 0x3630
+  __TEXT.__unwind_info: 0x36b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4980
-  __DATA_CONST.__objc_classlist: 0x1d0
+  __DATA_CONST.__const: 0x4a20
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f00
+  __DATA_CONST.__objc_selrefs: 0x3fc8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x150
-  __DATA_CONST.__objc_arraydata: 0x318
-  __DATA_CONST.__got: 0xc38
-  __AUTH_CONST.__const: 0x1428
-  __AUTH_CONST.__cfstring: 0x8320
-  __AUTH_CONST.__objc_const: 0x6540
+  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_arraydata: 0x320
+  __DATA_CONST.__got: 0xc40
+  __AUTH_CONST.__const: 0x1448
+  __AUTH_CONST.__cfstring: 0x8440
+  __AUTH_CONST.__objc_const: 0x6678
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1140
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x56c
+  __AUTH_CONST.__auth_got: 0x1158
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x580
   __DATA.__data: 0x410
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0x160
-  __DATA_DIRTY.__bss: 0x750
+  __DATA_DIRTY.__bss: 0x700
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3477
-  Symbols:   5216
-  CStrings:  2773
+  Functions: 3513
+  Symbols:   5273
+  CStrings:  2783
 
Symbols:
+ -[MDSearchableIndexService _evaluateFileProviderContainerGroups:excludedBundleIDs:allowedBundleIDs:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer _closeIndexOnLockSuspendQueue]
+ -[SPConcreteCoreSpotlightIndexer _commitUpdatesUnlessSuspended:]
+ -[SPConcreteCoreSpotlightIndexer _fileProviderItemVerdictForAttributes:visibility:]
+ -[SPConcreteCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:allowedBundleIDs:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:allowedBundleIDs:visibility:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer _oidPathIsHidden:visibility:]
+ -[SPConcreteCoreSpotlightIndexer _openIndexOnLockSuspendQueue:shouldReindexAll:readOnly:forcePC:]
+ -[SPConcreteCoreSpotlightIndexer _resumeIndexOnLockSuspendQueue]
+ -[SPConcreteCoreSpotlightIndexer _test_isSuspending]
+ -[SPConcreteCoreSpotlightIndexer dispatchDeviceLockSuspendToGroup:]
+ -[SPConcreteCoreSpotlightIndexer lockSuspendQueue]
+ -[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:outstandingMaintenance:]
+ -[SPCoreSpotlightIndexer _finishLocalizedStringUsageTask:identifier:reporter:]
+ -[SPCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:allowedBundleIDs:completionHandler:]
+ -[SPCoreSpotlightIndexer _sampleLocalizedStringUsageWithReporter:completion:]
+ -[SPLocalizedStringUsageReporter addCensus:]
+ -[SPLocalizedStringUsageReporter cancelFlag]
+ -[SPLocalizedStringUsageReporter cancel]
+ -[SPLocalizedStringUsageReporter censusCount]
+ -[SPLocalizedStringUsageReporter init]
+ -[SPLocalizedStringUsageReporter isCanceled]
+ -[SPLocalizedStringUsageReporter payload]
+ GCC_except_table1030
+ GCC_except_table1060
+ GCC_except_table1069
+ GCC_except_table1085
+ GCC_except_table1126
+ GCC_except_table1131
+ GCC_except_table1182
+ GCC_except_table1216
+ GCC_except_table1222
+ GCC_except_table1223
+ GCC_except_table1229
+ GCC_except_table1230
+ GCC_except_table1231
+ GCC_except_table1241
+ GCC_except_table1243
+ GCC_except_table1258
+ GCC_except_table1264
+ GCC_except_table1268
+ GCC_except_table1282
+ GCC_except_table1298
+ GCC_except_table1305
+ GCC_except_table1312
+ GCC_except_table1319
+ GCC_except_table1326
+ GCC_except_table1343
+ GCC_except_table1421
+ GCC_except_table1422
+ GCC_except_table1424
+ GCC_except_table1431
+ GCC_except_table1494
+ GCC_except_table1501
+ GCC_except_table1628
+ GCC_except_table1629
+ GCC_except_table334
+ GCC_except_table344
+ GCC_except_table350
+ GCC_except_table374
+ GCC_except_table384
+ GCC_except_table398
+ GCC_except_table432
+ GCC_except_table433
+ GCC_except_table437
+ GCC_except_table460
+ GCC_except_table497
+ GCC_except_table498
+ GCC_except_table513
+ GCC_except_table514
+ GCC_except_table544
+ GCC_except_table568
+ GCC_except_table582
+ GCC_except_table596
+ GCC_except_table597
+ GCC_except_table598
+ GCC_except_table636
+ GCC_except_table650
+ GCC_except_table662
+ GCC_except_table685
+ GCC_except_table691
+ GCC_except_table711
+ GCC_except_table721
+ GCC_except_table757
+ GCC_except_table782
+ GCC_except_table783
+ GCC_except_table784
+ GCC_except_table811
+ GCC_except_table877
+ GCC_except_table901
+ GCC_except_table923
+ GCC_except_table927
+ GCC_except_table931
+ GCC_except_table962
+ GCC_except_table991
+ _OBJC_CLASS_$_SPLocalizedStringUsageReporter
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._lockSuspendQueue
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._suspendsPending
+ _OBJC_IVAR_$_SPLocalizedStringUsageReporter._canceled
+ _OBJC_IVAR_$_SPLocalizedStringUsageReporter._censusCount
+ _OBJC_IVAR_$_SPLocalizedStringUsageReporter._lock
+ _OBJC_IVAR_$_SPLocalizedStringUsageReporter._totals
+ _OBJC_METACLASS_$_SPLocalizedStringUsageReporter
+ _SPLocalizedStringUsageEventName
+ _SPLocalizedStringUsageLocalizedFieldCountKey
+ _SPLocalizedStringUsageLocalizedVariantCountKey
+ _SPLocalizedStringUsagePagesPerIndex
+ _SPLocalizedStringUsagePayload
+ _SPLocalizedStringUsageRegularFieldCountKey
+ _SPLocalizedStringUsageRoundedEstimate
+ _SPLocalizedStringUsageSampledPagesKey
+ _SPLocalizedStringUsageTotalsAddCensus
+ __OBJC_$_INSTANCE_METHODS_SPLocalizedStringUsageReporter
+ __OBJC_$_INSTANCE_VARIABLES_SPLocalizedStringUsageReporter
+ __OBJC_CLASS_RO_$_SPLocalizedStringUsageReporter
+ __OBJC_METACLASS_RO_$_SPLocalizedStringUsageReporter
+ __SISampleStringFieldCensus
+ ___118-[MDSearchableIndexService _evaluateFileProviderContainerGroups:excludedBundleIDs:allowedBundleIDs:completionHandler:]_block_invoke
+ ___118-[MDSearchableIndexService _evaluateFileProviderContainerGroups:excludedBundleIDs:allowedBundleIDs:completionHandler:]_block_invoke_2
+ ___154-[SPCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:allowedBundleIDs:completionHandler:]_block_invoke
+ ___154-[SPCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:allowedBundleIDs:completionHandler:]_block_invoke_2
+ ___173-[SPConcreteCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:allowedBundleIDs:visibility:completionHandler:]_block_invoke
+ ___173-[SPConcreteCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:allowedBundleIDs:visibility:completionHandler:]_block_invoke_2
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_7
+ ___31-[SPCoreSpotlightIndexer start]_block_invoke_5
+ ___31-[SPCoreSpotlightIndexer start]_block_invoke_6
+ ___31-[SPCoreSpotlightIndexer start]_block_invoke_7
+ ___44-[SPConcreteCoreSpotlightIndexer closeIndex]_block_invoke
+ ___64-[SPConcreteCoreSpotlightIndexer _resumeIndexOnLockSuspendQueue]_block_invoke
+ ___64-[SPConcreteCoreSpotlightIndexer _resumeIndexOnLockSuspendQueue]_block_invoke_2
+ ___67-[SPConcreteCoreSpotlightIndexer dispatchDeviceLockSuspendToGroup:]_block_invoke
+ ___77-[SPCoreSpotlightIndexer _sampleLocalizedStringUsageWithReporter:completion:]_block_invoke
+ ___77-[SPCoreSpotlightIndexer _sampleLocalizedStringUsageWithReporter:completion:]_block_invoke_2
+ ___78-[SPCoreSpotlightIndexer _finishLocalizedStringUsageTask:identifier:reporter:]_block_invoke
+ ___83-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:outstandingMaintenance:]_block_invoke
+ ___83-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:outstandingMaintenance:]_block_invoke_2
+ ___83-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:outstandingMaintenance:]_block_invoke_3
+ ___97-[SPConcreteCoreSpotlightIndexer _openIndexOnLockSuspendQueue:shouldReindexAll:readOnly:forcePC:]_block_invoke
+ ___97-[SPConcreteCoreSpotlightIndexer _openIndexOnLockSuspendQueue:shouldReindexAll:readOnly:forcePC:]_block_invoke_2
+ ___97-[SPConcreteCoreSpotlightIndexer _openIndexOnLockSuspendQueue:shouldReindexAll:readOnly:forcePC:]_block_invoke_3
+ ___97-[SPConcreteCoreSpotlightIndexer _openIndexOnLockSuspendQueue:shouldReindexAll:readOnly:forcePC:]_block_invoke_4
+ ___97-[SPConcreteCoreSpotlightIndexer _openIndexOnLockSuspendQueue:shouldReindexAll:readOnly:forcePC:]_block_invoke_5
+ ___97-[SPConcreteCoreSpotlightIndexer _openIndexOnLockSuspendQueue:shouldReindexAll:readOnly:forcePC:]_block_invoke_6
+ ___97-[SPConcreteCoreSpotlightIndexer _openIndexOnLockSuspendQueue:shouldReindexAll:readOnly:forcePC:]_block_invoke_7
+ ___97-[SPConcreteCoreSpotlightIndexer _openIndexOnLockSuspendQueue:shouldReindexAll:readOnly:forcePC:]_block_invoke_8
+ ___97-[SPConcreteCoreSpotlightIndexer _openIndexOnLockSuspendQueue:shouldReindexAll:readOnly:forcePC:]_block_invoke_9
+ ___block_descriptor_48_e8_32s40s_e38_v16?0r^{SIStringFieldCensus=QQQQQQQ}8ls32l8s40l8
+ ___block_descriptor_59_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ __openIndexOnLockSuspendQueue:shouldReindexAll:readOnly:forcePC:.lastReport
+ __openIndexOnLockSuspendQueue:shouldReindexAll:readOnly:forcePC:.lastTime
+ __openIndexOnLockSuspendQueue:shouldReindexAll:readOnly:forcePC:.onceToken
+ __openIndexOnLockSuspendQueue:shouldReindexAll:readOnly:forcePC:.totalCost
+ _objc_retain_x7
+ _strchr
- -[MDSearchableIndexService _evaluateFileProviderContainerGroups:excludedBundleIDs:completionHandler:]
- -[SPConcreteCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:completionHandler:]
- -[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]
- -[SPCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:completionHandler:]
- GCC_except_table1004
- GCC_except_table1033
- GCC_except_table1034
- GCC_except_table1043
- GCC_except_table1100
- GCC_except_table1105
- GCC_except_table1156
- GCC_except_table1190
- GCC_except_table1196
- GCC_except_table1197
- GCC_except_table1203
- GCC_except_table1204
- GCC_except_table1205
- GCC_except_table1206
- GCC_except_table1215
- GCC_except_table1217
- GCC_except_table1238
- GCC_except_table1242
- GCC_except_table1256
- GCC_except_table1272
- GCC_except_table1279
- GCC_except_table1286
- GCC_except_table1293
- GCC_except_table1300
- GCC_except_table1317
- GCC_except_table1395
- GCC_except_table1396
- GCC_except_table1398
- GCC_except_table1405
- GCC_except_table1468
- GCC_except_table1475
- GCC_except_table1602
- GCC_except_table1603
- GCC_except_table342
- GCC_except_table348
- GCC_except_table372
- GCC_except_table382
- GCC_except_table396
- GCC_except_table429
- GCC_except_table430
- GCC_except_table434
- GCC_except_table457
- GCC_except_table486
- GCC_except_table487
- GCC_except_table502
- GCC_except_table503
- GCC_except_table533
- GCC_except_table557
- GCC_except_table571
- GCC_except_table574
- GCC_except_table586
- GCC_except_table587
- GCC_except_table625
- GCC_except_table639
- GCC_except_table651
- GCC_except_table674
- GCC_except_table680
- GCC_except_table699
- GCC_except_table700
- GCC_except_table743
- GCC_except_table768
- GCC_except_table769
- GCC_except_table770
- GCC_except_table796
- GCC_except_table862
- GCC_except_table886
- GCC_except_table908
- GCC_except_table912
- GCC_except_table916
- GCC_except_table944
- GCC_except_table973
- _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._suspending
- ___101-[MDSearchableIndexService _evaluateFileProviderContainerGroups:excludedBundleIDs:completionHandler:]_block_invoke
- ___101-[MDSearchableIndexService _evaluateFileProviderContainerGroups:excludedBundleIDs:completionHandler:]_block_invoke_2
- ___137-[SPCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:completionHandler:]_block_invoke
- ___137-[SPCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:completionHandler:]_block_invoke_2
- ___145-[SPConcreteCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:completionHandler:]_block_invoke
- ___145-[SPConcreteCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:completionHandler:]_block_invoke_2
- ___45-[SPConcreteCoreSpotlightIndexer resumeIndex]_block_invoke_2
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_5
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_6
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_7
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_8
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_9
- _openIndex:shouldReindexAll:readOnly:forcePC:.lastReport
- _openIndex:shouldReindexAll:readOnly:forcePC:.lastTime
- _openIndex:shouldReindexAll:readOnly:forcePC:.onceToken
- _openIndex:shouldReindexAll:readOnly:forcePC:.totalCost
CStrings:
+ "23F"
+ "Task %@ sampled %lu indexes, payload:%@"
+ "[ProtectedApps] container item donated: owner:%@ provider:%@"
+ "com.apple.searchd.reportLocalizedStringUsage"
+ "com.apple.spotlight.index.LocalizedStringUsage"
+ "com.apple.spotlight.lockSuspendQueue.%@"
+ "localizedFieldCount"
+ "localizedVariantCount"
+ "regularFieldCount"
+ "sampledPages"
+ "v16@?0r^{SIStringFieldCensus=QQQQQQQ}8"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf1"
- "_kMDItemOID"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xc1"
```
