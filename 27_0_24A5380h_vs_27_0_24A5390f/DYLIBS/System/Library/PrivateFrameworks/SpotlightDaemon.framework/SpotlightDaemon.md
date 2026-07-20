## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2451.1.101.0.0
-  __TEXT.__text: 0xbc484
-  __TEXT.__objc_methlist: 0x48b4
-  __TEXT.__const: 0x3c0
-  __TEXT.__cstring: 0x932b
-  __TEXT.__gcc_except_tab: 0x4710
-  __TEXT.__oslogstring: 0xc3d0
+2454.100.0.0.0
+  __TEXT.__text: 0xc06f8
+  __TEXT.__objc_methlist: 0x49cc
+  __TEXT.__const: 0x3d8
+  __TEXT.__cstring: 0x96b7
+  __TEXT.__gcc_except_tab: 0x4944
+  __TEXT.__oslogstring: 0xcb64
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x2720
+  __TEXT.__unwind_info: 0x2800
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x44f0
+  __DATA_CONST.__const: 0x4730
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b08
+  __DATA_CONST.__objc_selrefs: 0x3bd8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x138
-  __DATA_CONST.__objc_arraydata: 0x2f8
+  __DATA_CONST.__objc_arraydata: 0x300
   __DATA_CONST.__got: 0xbe8
-  __AUTH_CONST.__const: 0x1228
-  __AUTH_CONST.__cfstring: 0x7b40
-  __AUTH_CONST.__objc_const: 0x5ec0
+  __AUTH_CONST.__const: 0x1308
+  __AUTH_CONST.__cfstring: 0x7fe0
+  __AUTH_CONST.__objc_const: 0x5f48
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1110
+  __AUTH_CONST.__auth_got: 0x1130
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x4fc
+  __DATA.__objc_ivar: 0x50c
   __DATA.__data: 0x418
-  __DATA.__bss: 0xf0
+  __DATA.__bss: 0x150
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0x158
-  __DATA_DIRTY.__bss: 0x6f0
+  __DATA_DIRTY.__bss: 0x6e0
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3249
-  Symbols:   6524
-  CStrings:  2591
+  Functions: 3320
+  Symbols:   6646
+  CStrings:  2661
 
Symbols:
+ -[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer deleteUserActivitiesForBundleID:activityType:fromClient:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer issueNotesReindexIfNeeded:group:]
+ -[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupAppClips]
+ -[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]
+ -[SPConcreteCoreSpotlightIndexer resetUserActivityPurgeFixupVersion]
+ -[SPConcreteCoreSpotlightIndexer runUserActivityPurgeFixupWithGroup:]
+ -[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]
+ -[SPCoreSpotlightLiveQueryTask supportsLongRunningQueryTimer]
+ -[SPCoreSpotlightTask _armLongRunningQueryTimerWithMode:queryContext:]
+ -[SPCoreSpotlightTask _effectiveLongQueryMode]
+ -[SPCoreSpotlightTask _handleLongRunningQueryTimerFireWithMode:thresholdNSec:daemonName:bundleIDs:]
+ -[SPCoreSpotlightTask _prepareSIQueryWithQueryString:queryContext:]
+ -[SPCoreSpotlightTask _terminateForLongRunningQueryTimeout]
+ -[SPCoreSpotlightTask foundItemCount]
+ -[SPCoreSpotlightTask longRunningQueryTimer]
+ -[SPCoreSpotlightTask setLongRunningQueryTimer:]
+ -[SPCoreSpotlightTask supportsLongRunningQueryTimer]
+ -[SPHDBBundleRegistry allMigratedOrPendingBundles]
+ -[SPHDBBundleRegistry clearPendingRegistration:]
+ -[SPHDBBundleRegistry isBundlePendingRegistration:]
+ -[SPHDBBundleRegistry markBundlePendingRegistration:]
+ GCC_except_table1005
+ GCC_except_table1006
+ GCC_except_table1050
+ GCC_except_table1055
+ GCC_except_table109
+ GCC_except_table1106
+ GCC_except_table1140
+ GCC_except_table1146
+ GCC_except_table1147
+ GCC_except_table1153
+ GCC_except_table1155
+ GCC_except_table1156
+ GCC_except_table1165
+ GCC_except_table1167
+ GCC_except_table1182
+ GCC_except_table1188
+ GCC_except_table1192
+ GCC_except_table1206
+ GCC_except_table1217
+ GCC_except_table1224
+ GCC_except_table1238
+ GCC_except_table1245
+ GCC_except_table1262
+ GCC_except_table1340
+ GCC_except_table1341
+ GCC_except_table1343
+ GCC_except_table1350
+ GCC_except_table1408
+ GCC_except_table1415
+ GCC_except_table1541
+ GCC_except_table1542
+ GCC_except_table170
+ GCC_except_table183
+ GCC_except_table188
+ GCC_except_table201
+ GCC_except_table208
+ GCC_except_table210
+ GCC_except_table221
+ GCC_except_table224
+ GCC_except_table227
+ GCC_except_table228
+ GCC_except_table236
+ GCC_except_table237
+ GCC_except_table243
+ GCC_except_table245
+ GCC_except_table246
+ GCC_except_table263
+ GCC_except_table266
+ GCC_except_table269
+ GCC_except_table283
+ GCC_except_table291
+ GCC_except_table307
+ GCC_except_table331
+ GCC_except_table341
+ GCC_except_table355
+ GCC_except_table388
+ GCC_except_table389
+ GCC_except_table393
+ GCC_except_table416
+ GCC_except_table445
+ GCC_except_table446
+ GCC_except_table461
+ GCC_except_table462
+ GCC_except_table492
+ GCC_except_table516
+ GCC_except_table530
+ GCC_except_table533
+ GCC_except_table544
+ GCC_except_table545
+ GCC_except_table546
+ GCC_except_table584
+ GCC_except_table598
+ GCC_except_table628
+ GCC_except_table653
+ GCC_except_table654
+ GCC_except_table664
+ GCC_except_table692
+ GCC_except_table717
+ GCC_except_table718
+ GCC_except_table719
+ GCC_except_table743
+ GCC_except_table78
+ GCC_except_table809
+ GCC_except_table833
+ GCC_except_table854
+ GCC_except_table858
+ GCC_except_table86
+ GCC_except_table862
+ GCC_except_table89
+ GCC_except_table890
+ GCC_except_table90
+ GCC_except_table91
+ GCC_except_table919
+ GCC_except_table92
+ GCC_except_table93
+ GCC_except_table950
+ GCC_except_table96
+ GCC_except_table979
+ GCC_except_table980
+ GCC_except_table989
+ _NOTES_REINDEX_VERSION_CHANGE_block_invoke_2.onceToken
+ _NOTES_REINDEX_VERSION_CHANGE_block_invoke_2.sDASQueue
+ _OBJC_IVAR_$_SPCoreSpotlightTask._foundItemCount
+ _OBJC_IVAR_$_SPCoreSpotlightTask._longRunningQueryTimer
+ _OBJC_IVAR_$_SPCoreSpotlightTask._trackFoundItemCount
+ _OBJC_IVAR_$_SPHDBBundleRegistry._bundlesPendingRegistration
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _SDDiagnosticGateIsInternal
+ _SIGetAccumulatedUACountResolved
+ _SIIndexMightContainBundleIDs
+ _SPInitLongRunningQueryConfig.onceToken
+ __OBJC_$_INSTANCE_METHODS_SPCoreSpotlightLiveQueryTask
+ ___108-[SPConcreteCoreSpotlightIndexer deleteUserActivitiesForBundleID:activityType:fromClient:completionHandler:]_block_invoke
+ ___159-[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:options:deleteAllReason:donationTimestamp:completionHandler:]_block_invoke_5
+ ___159-[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:options:deleteAllReason:donationTimestamp:completionHandler:]_block_invoke_6
+ ___30-[SPCoreSpotlightTask addJob:]_block_invoke
+ ___59-[SPCoreSpotlightTask _terminateForLongRunningQueryTimeout]_block_invoke
+ ___62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke
+ ___62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke_2
+ ___62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke_3
+ ___62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke_4
+ ___66-[SPConcreteCoreSpotlightIndexer issueNotesReindexIfNeeded:group:]_block_invoke
+ ___69-[SPConcreteCoreSpotlightIndexer runUserActivityPurgeFixupWithGroup:]_block_invoke
+ ___70-[SPCoreSpotlightTask _armLongRunningQueryTimerWithMode:queryContext:]_block_invoke
+ ___74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke
+ ___74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke_2
+ ___74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke_3
+ ___74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke_4
+ ___74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke_5
+ ___74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke_6
+ ___74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke_7
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_6
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_7
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_8
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_9
+ ___88-[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]_block_invoke
+ ___88-[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]_block_invoke_2
+ ___88-[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]_block_invoke_3
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_20
+ ___SPInitLongRunningQueryConfig_block_invoke
+ ___SPSendLongRunningQueryAnalytics_block_invoke
+ ___block_descriptor_105_e8_32s40s48s_e26_"NSMutableDictionary"8?0ls32l8s40l8s48l8
+ ___block_descriptor_40_e8_32bs_e20_v24?0"NSError"8q16ls32l8
+ ___block_descriptor_48_e8_32bs40w_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40lw40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e42_v48?0^{__CFString=}8B16B20q24q32?<v?>40lr40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_57_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0lr48l8s40l8s32l8r56l8
+ ___block_descriptor_65_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r_e5_v8?0ls32l8r48l8r56l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e20_v24?0"NSError"8q16ls32l8s40l8r56l8r64l8s48l8
+ ___block_descriptor_72_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_73_e8_32s40s48s56s64r_e40_v16?0"SPConcreteCoreSpotlightIndexer"8ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56s64s_e40_v16?0"SPConcreteCoreSpotlightIndexer"8ls32l8s40l8s48l8s56l8s64l8
+ ___logForCSSignpostLongRunningQuery_block_invoke
+ ___logForCSSignpostQueryTelemetry_block_invoke
+ _gMediaStatusDomain_block_invoke_9.sLoggedUACapKeys
+ _gMediaStatusDomain_block_invoke_9.sLoggedUACapKeysLock
+ _gMediaStatusDomain_block_invoke_9.sLoggedUACapOnce
+ _isLowOnDiskSpace
+ _kSPUserActivityPurgeTargets
+ _logForCSSignpostLongRunningQuery
+ _logForCSSignpostLongRunningQuery.onceToken
+ _logForCSSignpostLongRunningQuery.sLongRunningQueryLog
+ _logForCSSignpostQueryTelemetry
+ _logForCSSignpostQueryTelemetry.onceToken
+ _logForCSSignpostQueryTelemetry.sQueryTelemetryLog
+ _objc_msgSend$_armLongRunningQueryTimerWithMode:queryContext:
+ _objc_msgSend$_effectiveLongQueryMode
+ _objc_msgSend$_finishUserActivityPurgeWithDeleted:completionHandler:
+ _objc_msgSend$_handleLongRunningQueryTimerFireWithMode:thresholdNSec:daemonName:bundleIDs:
+ _objc_msgSend$_prepareSIQueryWithQueryString:queryContext:
+ _objc_msgSend$_terminateForLongRunningQueryTimeout
+ _objc_msgSend$allMigratedOrPendingBundles
+ _objc_msgSend$clearPendingRegistration:
+ _objc_msgSend$contentTypeTree
+ _objc_msgSend$deleteUserActivitiesForBundleID:activityType:fromClient:completionHandler:
+ _objc_msgSend$doubleForKey:
+ _objc_msgSend$foundItemCount
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$isBundlePendingRegistration:
+ _objc_msgSend$issueNotesReindexIfNeeded:group:
+ _objc_msgSend$issuePriorityIndexFixupAppClips
+ _objc_msgSend$issueUserActivityPurgeCommand:completionHandler:
+ _objc_msgSend$issueUserActivityPurgeFixup:
+ _objc_msgSend$longQueryHandlingModeOverride
+ _objc_msgSend$longQueryTimeoutOverride
+ _objc_msgSend$longRunningQueryTimer
+ _objc_msgSend$markBundlePendingRegistration:
+ _objc_msgSend$resetUserActivityPurgeFixupVersion
+ _objc_msgSend$runUserActivityPurgeFixupWithGroup:
+ _objc_msgSend$setByAddingObjectsFromSet:
+ _objc_msgSend$setLongRunningQueryTimer:
+ _objc_msgSend$supportsLongRunningQueryTimer
+ _objc_setProperty_atomic_copy
+ _sSPLongRunningQueryMode
+ _sSPLongRunningQueryThresholdNSec
- -[SPHDBBundleRegistry migratedBundles]
- GCC_except_table1027
- GCC_except_table1078
- GCC_except_table1112
- GCC_except_table1118
- GCC_except_table1119
- GCC_except_table1125
- GCC_except_table1126
- GCC_except_table1127
- GCC_except_table1128
- GCC_except_table1137
- GCC_except_table1139
- GCC_except_table1160
- GCC_except_table1164
- GCC_except_table1176
- GCC_except_table1186
- GCC_except_table1193
- GCC_except_table1200
- GCC_except_table1207
- GCC_except_table1214
- GCC_except_table1308
- GCC_except_table1309
- GCC_except_table1311
- GCC_except_table1318
- GCC_except_table1376
- GCC_except_table1383
- GCC_except_table1509
- GCC_except_table1510
- GCC_except_table180
- GCC_except_table185
- GCC_except_table198
- GCC_except_table205
- GCC_except_table216
- GCC_except_table217
- GCC_except_table219
- GCC_except_table223
- GCC_except_table226
- GCC_except_table232
- GCC_except_table238
- GCC_except_table240
- GCC_except_table241
- GCC_except_table258
- GCC_except_table261
- GCC_except_table264
- GCC_except_table278
- GCC_except_table286
- GCC_except_table296
- GCC_except_table325
- GCC_except_table335
- GCC_except_table349
- GCC_except_table382
- GCC_except_table383
- GCC_except_table387
- GCC_except_table410
- GCC_except_table439
- GCC_except_table440
- GCC_except_table455
- GCC_except_table456
- GCC_except_table486
- GCC_except_table510
- GCC_except_table524
- GCC_except_table527
- GCC_except_table538
- GCC_except_table539
- GCC_except_table540
- GCC_except_table579
- GCC_except_table590
- GCC_except_table615
- GCC_except_table635
- GCC_except_table645
- GCC_except_table673
- GCC_except_table698
- GCC_except_table699
- GCC_except_table700
- GCC_except_table724
- GCC_except_table75
- GCC_except_table76
- GCC_except_table790
- GCC_except_table81
- GCC_except_table814
- GCC_except_table82
- GCC_except_table835
- GCC_except_table839
- GCC_except_table84
- GCC_except_table843
- GCC_except_table85
- GCC_except_table871
- GCC_except_table900
- GCC_except_table931
- GCC_except_table960
- GCC_except_table961
- GCC_except_table970
- GCC_except_table986
- GCC_except_table987
- _PHOTOS_INDEX_VERSION_CHANGE_block_invoke_2.onceToken
- _PHOTOS_INDEX_VERSION_CHANGE_block_invoke_2.sDASQueue
- __OBJC_$_PROP_LIST_SPHDBBundleRegistry
- ___block_descriptor_48_e8_32s40r_e42_v48?0^{__CFString=}8B16B20q24q32?<v?>40ls32l8r40l8
- ___block_descriptor_65_e8_32s40s48s56s_e40_v16?0"SPConcreteCoreSpotlightIndexer"8ls32l8s40l8s48l8s56l8
- _objc_msgSend$migratedBundles
CStrings:
+ "\"\\"
+ "%@\n%@"
+ "?"
+ "@\"NSMutableDictionary\"8@?0"
+ "Can't process VFS notification because indexDirectory is not set"
+ "HDB migration: bundle %{private}@ already migrated, skipping delete"
+ "HDB migration: markBundlePendingRegistration failed for %{private}@, aborting delete"
+ "LongRunningQuery"
+ "LongRunningQuerySetup"
+ "NOTES_REINDEX_VERSION_CHANGE"
+ "Need to perform priority migration ON for index %@ for app clips"
+ "Notes index version changed: %@ -> %ld"
+ "Notes re-index forced"
+ "QueryTelemetry"
+ "SPHDBBundleRegistry: clearPendingRegistration called with invalid bundleID"
+ "SPHDBBundleRegistry: cleared pending registration for %{private}@"
+ "SPHDBBundleRegistry: markBundlePendingRegistration called with invalid bundleID"
+ "SPHDBBundleRegistry: marked bundle %{private}@ pending migration"
+ "Throttling indexing reply for %@ by %g s (elapsed %g s) (%s) (%lu)"
+ "UA-CAP: dropping user activity for %{public}@ (dataclass %{public}@): count %u >= cap %u (shared:%d)"
+ "UA-PURGE uapurge: fixup error for %{public}@: %{public}@"
+ "UA-PURGE: delete error for %{public}@/%{public}@: %{public}@"
+ "UA-PURGE: deleted %ld for %{public}@/%{public}@"
+ "UA-PURGE: fixup aborted before vacuum (delete error), will retry next launch"
+ "UA-PURGE: fixup complete for %{public}@, version %ld -> %ld"
+ "UA-PURGE: fixup deferred for %{public}@, will retry next launch (version still %ld): %{public}@"
+ "UA-PURGE: no vacuum owed (delete state %ld), skipping vacuum"
+ "UA-PURGE: refusing delete with empty bundleID(%{public}@) or activityType(%{public}@)"
+ "UA-PURGE: refusing delete with unsafe characters in bundleID(%{public}@) or activityType(%{public}@)"
+ "UA-PURGE: skipped vacuum, insufficient free space (deleted %ld), will retry next launch"
+ "UA-PURGE: skipping fixup for %{public}@, stored version %ld %{public}s target %d"
+ "UA-PURGE: starting fixup for %{public}@ (version before: %ld, target: %d)"
+ "UA-PURGE: vacuum complete (size query unavailable)"
+ "UA-PURGE: vacuum complete, reclaimed %lld bytes (best-effort)"
+ "UA-PURGE: vacuum error: %{public}@ (version not stamped, will retry)"
+ "UA-PURGE: vacuum requested (deleted %ld)"
+ "[qid=%ld][client=%@] all indexers skipped, bundleIDs:[%@]"
+ "[qid=%ld][client=%@] skipped:[%{public}@], started:[%{public}@], bundleIDs:[%@]"
+ "_kMDItemBundleID=\"%@\" && _kMDItemUserActivityType=\"%@\""
+ "ahead of"
+ "already at"
+ "bundleIDCount"
+ "bundleID_0"
+ "bundleID_1"
+ "bundleID_2"
+ "clientBundleID"
+ "com.apple.Keynote"
+ "com.apple.Numbers"
+ "com.apple.Pages"
+ "com.apple.app-clips"
+ "com.apple.corespotlight.longQueryHandlingMode"
+ "com.apple.corespotlight.longQueryThresholdSeconds"
+ "com.apple.iWork.Keynote"
+ "com.apple.iWork.Numbers"
+ "com.apple.iWork.Pages"
+ "com.apple.keynote.documentEditing"
+ "com.apple.numbers.documentEditing"
+ "com.apple.pages.documentEditing"
+ "com.apple.spotlight.longrunningquery"
+ "daemonName"
+ "elapsed=%.2f threshold=%.2f bundle=%{public}@ private=1"
+ "elapsed=%.2f threshold=%.2f bundle=%{public}@ query=%{private}@"
+ "elapsedSeconds"
+ "filterQueryCount"
+ "foundItemCountAtFire"
+ "hasSearchInternalEntitlement"
+ "issueNotesReindex"
+ "kSPPriorityIndexVersionAppClips"
+ "kSPUserActivityDelete"
+ "kSPUserActivityPurge"
+ "mode=%ld threshold=%.2f s"
+ "openIndex index delegate directory is NULL"
+ "protectionClassBitmask"
+ "thresholdSeconds"
+ "uapurge"
- "Received empty update vfsevent; assuming not in low disk space state"
- "Received low disk space vfsevent; assuming very low disk ended"
- "Received very low disk space vfsevent"
- "Slowed down %s journal playback for %@ by %f s"
- "Throttling indexing reply for %@ by %g s (%g s) (%s) (%lu)"
```
