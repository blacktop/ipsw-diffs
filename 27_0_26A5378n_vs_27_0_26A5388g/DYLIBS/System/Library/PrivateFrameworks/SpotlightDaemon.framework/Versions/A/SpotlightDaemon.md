## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/Versions/A/SpotlightDaemon`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2451.1.401.0.0
-  __TEXT.__text: 0xbde30
-  __TEXT.__objc_methlist: 0x47fc
-  __TEXT.__const: 0x398
-  __TEXT.__cstring: 0x907c
-  __TEXT.__gcc_except_tab: 0x43ec
-  __TEXT.__oslogstring: 0xaf10
-  __TEXT.__unwind_info: 0x25b8
+2454.100.0.0.0
+  __TEXT.__text: 0xc23c8
+  __TEXT.__objc_methlist: 0x48fc
+  __TEXT.__const: 0x3c8
+  __TEXT.__cstring: 0x93d4
+  __TEXT.__gcc_except_tab: 0x4628
+  __TEXT.__oslogstring: 0xb6fb
+  __TEXT.__unwind_info: 0x2698
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x560
+  __DATA_CONST.__const: 0x5c0
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x39c0
+  __DATA_CONST.__objc_selrefs: 0x3a88
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x2e0
   __DATA_CONST.__got: 0xb70
-  __AUTH_CONST.__const: 0x5418
-  __AUTH_CONST.__cfstring: 0x7840
-  __AUTH_CONST.__objc_const: 0x5d70
+  __AUTH_CONST.__const: 0x56e8
+  __AUTH_CONST.__cfstring: 0x7ca0
+  __AUTH_CONST.__objc_const: 0x5df8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x348
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0xfe0
+  __AUTH_CONST.__auth_got: 0x1008
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x4d4
+  __DATA.__objc_ivar: 0x4e4
   __DATA.__data: 0x3f8
-  __DATA.__bss: 0xf0
+  __DATA.__bss: 0x140
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0x158

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3251
-  Symbols:   6587
-  CStrings:  2444
+  Functions: 3319
+  Symbols:   6706
+  CStrings:  2514
 
Symbols:
+ -[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer deleteUserActivitiesForBundleID:activityType:fromClient:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer issueNotesReindexIfNeeded:group:]
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
+ GCC_except_table100
+ GCC_except_table1004
+ GCC_except_table1005
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table1030
+ GCC_except_table1031
+ GCC_except_table104
+ GCC_except_table1079
+ GCC_except_table1084
+ GCC_except_table1148
+ GCC_except_table1189
+ GCC_except_table1195
+ GCC_except_table1196
+ GCC_except_table1202
+ GCC_except_table1203
+ GCC_except_table1204
+ GCC_except_table121
+ GCC_except_table1216
+ GCC_except_table1234
+ GCC_except_table1240
+ GCC_except_table1244
+ GCC_except_table1259
+ GCC_except_table1270
+ GCC_except_table1277
+ GCC_except_table1284
+ GCC_except_table1291
+ GCC_except_table1298
+ GCC_except_table1316
+ GCC_except_table1391
+ GCC_except_table1392
+ GCC_except_table1394
+ GCC_except_table1401
+ GCC_except_table1459
+ GCC_except_table1466
+ GCC_except_table204
+ GCC_except_table218
+ GCC_except_table227
+ GCC_except_table228
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table249
+ GCC_except_table258
+ GCC_except_table261
+ GCC_except_table266
+ GCC_except_table267
+ GCC_except_table277
+ GCC_except_table279
+ GCC_except_table280
+ GCC_except_table306
+ GCC_except_table311
+ GCC_except_table313
+ GCC_except_table327
+ GCC_except_table335
+ GCC_except_table341
+ GCC_except_table347
+ GCC_except_table375
+ GCC_except_table385
+ GCC_except_table400
+ GCC_except_table436
+ GCC_except_table440
+ GCC_except_table466
+ GCC_except_table495
+ GCC_except_table516
+ GCC_except_table517
+ GCC_except_table545
+ GCC_except_table572
+ GCC_except_table585
+ GCC_except_table588
+ GCC_except_table641
+ GCC_except_table655
+ GCC_except_table666
+ GCC_except_table692
+ GCC_except_table698
+ GCC_except_table713
+ GCC_except_table714
+ GCC_except_table726
+ GCC_except_table755
+ GCC_except_table781
+ GCC_except_table782
+ GCC_except_table783
+ GCC_except_table807
+ GCC_except_table81
+ GCC_except_table873
+ GCC_except_table894
+ GCC_except_table91
+ GCC_except_table915
+ GCC_except_table919
+ GCC_except_table923
+ GCC_except_table952
+ GCC_except_table96
+ GCC_except_table97
+ GCC_except_table975
+ GCC_except_table99
+ OBJC_IVAR_$_SPCoreSpotlightTask._foundItemCount
+ OBJC_IVAR_$_SPCoreSpotlightTask._longRunningQueryTimer
+ OBJC_IVAR_$_SPCoreSpotlightTask._trackFoundItemCount
+ OBJC_IVAR_$_SPHDBBundleRegistry._bundlesPendingRegistration
+ SPInitLongRunningQueryConfig.onceToken
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _SDDiagnosticGateIsInternal
+ _SIGetAccumulatedUACountResolved
+ _SIIndexMightContainBundleIDs
+ __159-[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:options:deleteAllReason:donationTimestamp:completionHandler:]_block_invoke
+ __62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke
+ __62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke_2
+ __74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke
+ __88-[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]_block_invoke_3
+ __OBJC_$_INSTANCE_METHODS_SPCoreSpotlightLiveQueryTask
+ ___108-[SPConcreteCoreSpotlightIndexer deleteUserActivitiesForBundleID:activityType:fromClient:completionHandler:]_block_invoke
+ ___159-[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:options:deleteAllReason:donationTimestamp:completionHandler:]_block_invoke_5
+ ___30-[SPCoreSpotlightTask addJob:]_block_invoke
+ ___59-[SPCoreSpotlightTask _terminateForLongRunningQueryTimeout]_block_invoke
+ ___62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke
+ ___62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke_2
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
+ ___88-[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]_block_invoke
+ ___88-[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]_block_invoke_2
+ ___88-[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]_block_invoke_3
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_16
+ ___SPInitLongRunningQueryConfig_block_invoke
+ ___SPSendLongRunningQueryAnalytics_block_invoke
+ ___block_descriptor_105_e8_32s40s48s_e26_"NSMutableDictionary"8?0l
+ ___block_descriptor_40_e8_32bs_e20_v24?0"NSError"8q16l
+ ___block_descriptor_48_e8_32bs40w_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40l
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40w_e17_v16?0"NSError"8l
+ ___block_descriptor_57_e8_32s40bs_e17_v16?0"NSError"8l
+ ___block_descriptor_65_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48r56r_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56r64r_e20_v24?0"NSError"8q16l
+ ___block_descriptor_72_e8_32s40s48w_e5_v8?0l
+ ___block_descriptor_73_e8_32s40s48s56s64r_e40_v16?0"SPConcreteCoreSpotlightIndexer"8l
+ ___block_descriptor_73_e8_32s40s48s56s64s_e40_v16?0"SPConcreteCoreSpotlightIndexer"8l
+ ___logForCSSignpostLongRunningQuery_block_invoke
+ ___logForCSSignpostQueryTelemetry_block_invoke
+ __os_log_fault_impl
+ _kSPUserActivityPurgeTargets
+ _logForCSSignpostLongRunningQuery
+ _logForCSSignpostQueryTelemetry
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
+ logForCSSignpostLongRunningQuery
+ logForCSSignpostLongRunningQuery.onceToken
+ logForCSSignpostLongRunningQuery.sLongRunningQueryLog
+ logForCSSignpostQueryTelemetry
+ logForCSSignpostQueryTelemetry.onceToken
+ logForCSSignpostQueryTelemetry.sQueryTelemetryLog
+ sLoginNotificatonQueue_block_invoke_8.sLoggedUACapKeys
+ sLoginNotificatonQueue_block_invoke_8.sLoggedUACapKeysLock
+ sLoginNotificatonQueue_block_invoke_8.sLoggedUACapOnce
- -[SPHDBBundleRegistry migratedBundles]
- GCC_except_table1013
- GCC_except_table1058
- GCC_except_table1122
- GCC_except_table1163
- GCC_except_table1169
- GCC_except_table1170
- GCC_except_table1176
- GCC_except_table1177
- GCC_except_table1178
- GCC_except_table118
- GCC_except_table1188
- GCC_except_table119
- GCC_except_table1190
- GCC_except_table1208
- GCC_except_table1218
- GCC_except_table1231
- GCC_except_table1241
- GCC_except_table1248
- GCC_except_table1255
- GCC_except_table1262
- GCC_except_table1269
- GCC_except_table1287
- GCC_except_table1361
- GCC_except_table1362
- GCC_except_table1364
- GCC_except_table1371
- GCC_except_table1429
- GCC_except_table1436
- GCC_except_table202
- GCC_except_table216
- GCC_except_table223
- GCC_except_table226
- GCC_except_table234
- GCC_except_table245
- GCC_except_table246
- GCC_except_table253
- GCC_except_table262
- GCC_except_table263
- GCC_except_table273
- GCC_except_table275
- GCC_except_table276
- GCC_except_table302
- GCC_except_table305
- GCC_except_table307
- GCC_except_table323
- GCC_except_table331
- GCC_except_table337
- GCC_except_table342
- GCC_except_table370
- GCC_except_table380
- GCC_except_table395
- GCC_except_table430
- GCC_except_table431
- GCC_except_table461
- GCC_except_table490
- GCC_except_table511
- GCC_except_table512
- GCC_except_table540
- GCC_except_table567
- GCC_except_table580
- GCC_except_table583
- GCC_except_table637
- GCC_except_table648
- GCC_except_table674
- GCC_except_table680
- GCC_except_table695
- GCC_except_table696
- GCC_except_table708
- GCC_except_table737
- GCC_except_table763
- GCC_except_table764
- GCC_except_table765
- GCC_except_table789
- GCC_except_table79
- GCC_except_table84
- GCC_except_table855
- GCC_except_table87
- GCC_except_table876
- GCC_except_table88
- GCC_except_table897
- GCC_except_table901
- GCC_except_table905
- GCC_except_table934
- GCC_except_table958
- GCC_except_table987
- GCC_except_table988
- GCC_except_table997
- __OBJC_$_PROP_LIST_SPHDBBundleRegistry
- ___block_descriptor_65_e8_32s40s48s56s_e40_v16?0"SPConcreteCoreSpotlightIndexer"8l
- _objc_msgSend$migratedBundles
CStrings:
+ "\"\\"
+ "%@\n%@"
+ "?"
+ "@\"NSMutableDictionary\"8@?0"
+ "HDB migration: bundle %{private}@ already migrated, skipping delete"
+ "HDB migration: markBundlePendingRegistration failed for %{private}@, aborting delete"
+ "LongRunningQuery"
+ "LongRunningQuerySetup"
+ "NOTES_REINDEX_VERSION_CHANGE"
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
+ "kSPUserActivityDelete"
+ "kSPUserActivityPurge"
+ "mode=%ld threshold=%.2f s"
+ "openIndex index delegate directory is NULL"
+ "protectionClassBitmask"
+ "thresholdSeconds"
+ "uapurge"
- "Throttling indexing reply for %@ by %g s (%g s) (%s) (%lu)"
```
